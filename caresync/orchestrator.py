"""Turn a caregiver utterance into MCP tool calls and a spoken reply."""

from __future__ import annotations

import json
import re
import time
from collections.abc import Awaitable, Callable
from typing import Any

from caresync.policy import CAREGIVER_ID
from caresync.store import RESIDENT_ID

ToolCaller = Callable[[str, dict[str, Any]], Awaitable[dict[str, Any]]]

_AFFIRM_REST = {
    "",
    "send it",
    "place the order",
    "place it",
    "do it",
    "please",
    "buy it",
    "confirm",
    "go ahead",
}
_AFFIRM = re.compile(
    r"^(yes|yeah|yep|yup|ok|okay|confirm|do it|go ahead|send it|place the order|place it|buy it)\b",
    re.I,
)
_CANCEL = re.compile(r"^(no|nope|cancel|never mind|not now|leave it|don't|stop)\b", re.I)


def plan(utterance: str, *, has_token: bool = False) -> str:
    text = " ".join(utterance.lower().strip().split())
    if not text:
        return "help"
    if _CANCEL.match(text) and (has_token or len(text.split()) <= 6):
        rest = _CANCEL.sub("", text).strip(" ,.!")
        if rest in {"", "leave it", "send it", "thanks"}:
            return "cancel"
    if _AFFIRM.match(text):
        rest = _AFFIRM.sub("", text).strip(" ,.!")
        if rest in _AFFIRM_REST:
            return "confirm"
    if re.search(r"\b(get me ready|visit packet|prep packet|ready for)\b", text):
        return "packet"
    if re.search(r"\b(moved|move|reschedule|changed|change)\b", text) and re.search(
        r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b", text
    ):
        return "update_visit"
    if re.search(r"\b(order|reorder|buy)\b", text):
        return "order"
    if re.search(r"\b(brief|briefs|pads|underwear|supplies|supply|stock|inventory)\b", text):
        return "inventory"
    if re.search(r"\b(pill|pills|meds|medication|medications|dose|doses|dispenser)\b", text):
        return "meds"
    if re.search(r"\b(remind|echo|show)\b", text):
        return "remind"
    if re.search(r"\b(yesterday|remember|memory|decide|decided|last time)\b", text):
        return "memory"
    if re.search(r"\b(appointment|cardiology|cardiologist|doctor|calendar|patel|clinic)\b", text):
        return "calendar"
    if re.search(r"\b(hi|hello|hey|help)\b", text) or "what can you" in text:
        return "help"
    return "status"


async def handle_turn(
    utterance: str,
    session_id: str,
    call_tool: ToolCaller,
    *,
    confirmation_token: str = "",
    actor_id: str = CAREGIVER_ID,
) -> dict[str, Any]:
    intent = plan(utterance, has_token=bool(confirmation_token))
    calls = _calls(intent, session_id, confirmation_token, actor_id, utterance)
    trace: list[dict[str, Any]] = []
    results: dict[str, Any] = {}
    started = time.perf_counter()
    for name, args in calls:
        t0 = time.perf_counter()
        try:
            payload = await call_tool(name, args)
            ok = bool(payload.get("ok", True))
            error = ""
        except Exception as exc:  # noqa: BLE001 — surface transport failures in the reply
            payload = {"ok": False, "status": "error", "reason": str(exc)}
            ok = False
            error = str(exc)
        ms = int((time.perf_counter() - t0) * 1000)
        trace.append({"tool": name, "ms": ms, "ok": ok, "error": error})
        results[name] = payload
        if not ok and name not in {"get_task"}:
            break
    speech, cards = compose(intent, results, utterance)
    return {
        "speech": speech,
        "cards": cards,
        "intent": intent,
        "trace": trace,
        "elapsed_ms": int((time.perf_counter() - started) * 1000),
        "session_id": session_id,
    }


def _calls(
    intent: str,
    session_id: str,
    token: str,
    actor_id: str,
    utterance: str,
) -> list[tuple[str, dict[str, Any]]]:
    base = {"actor_id": actor_id, "resident_id": RESIDENT_ID}
    if intent == "confirm":
        return [
            (
                "confirm_action",
                {"session_id": session_id, "confirmation_token": token, "actor_id": actor_id},
            )
        ]
    if intent == "cancel":
        return [
            (
                "dismiss_action",
                {"session_id": session_id, "confirmation_token": token, "actor_id": actor_id},
            )
        ]
    if intent == "order":
        return [
            ("check_inventory", {**base, "item_query": utterance}),
            ("propose_action", {**base, "kind": "order_supply", "session_id": session_id}),
        ]
    if intent == "inventory":
        return [("check_inventory", {**base, "item_query": utterance})]
    if intent == "update_visit":
        parsed = _parse_move(utterance)
        if parsed is None:
            return [("read_calendar", base)]
        weekday, hour, minute = parsed
        return [("update_appointment", {**base, "weekday": weekday, "hour": hour, "minute": minute})]
    if intent == "packet":
        return [("start_visit_packet", base)]
    if intent == "remind":
        return [("propose_action", {**base, "kind": "remind_show", "session_id": session_id})]
    if intent == "memory":
        return [("recall_memory", base)]
    if intent == "calendar":
        return [("read_calendar", base), ("recall_memory", base)]
    if intent == "meds":
        return [("read_telemetry", base)]
    if intent == "help":
        return [("read_telemetry", base)]
    return [
        ("recall_memory", base),
        ("read_telemetry", base),
        ("read_calendar", base),
        ("read_routines", base),
        ("check_inventory", {**base, "item_query": ""}),
    ]


def _parse_move(utterance: str) -> tuple[int, int, int] | None:
    text = utterance.lower()
    day = re.search(r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b", text)
    clock_match = re.search(r"\bat\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\b", text)
    if day is None or clock_match is None:
        return None
    hour = int(clock_match.group(1))
    minute = int(clock_match.group(2) or 0)
    meridian = clock_match.group(3)
    if meridian == "pm" and hour < 12:
        hour += 12
    elif meridian == "am" and hour == 12:
        hour = 0
    elif meridian is None and 1 <= hour <= 7:
        hour += 12
    weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"].index(day.group(1))
    return weekday, hour, minute


def compose(intent: str, results: dict[str, Any], utterance: str) -> tuple[str, list[dict[str, Any]]]:
    if any(item.get("ok") is False and item.get("status") == "error" for item in results.values()):
        reason = next(item.get("reason", "the care server did not answer") for item in results.values() if not item.get("ok"))
        return (
            f"I couldn't reach the care record. {reason}",
            [],
        )

    if intent == "help":
        name = ((results.get("read_telemetry") or {}).get("resident") or "this household").split()[0]
        return (
            f"I can read {name}'s medicines, the next visit, and what is running low. "
            "I will not send a reminder or place an order until you confirm it.",
            [],
        )

    if intent == "meds":
        tele = results.get("read_telemetry") or {}
        meds = tele.get("meds") or []
        if not meds:
            return ("I don't have a medication list for this household.", [])
        speech = ". ".join(f"{med['name']} {med['dose']} is {med['status']}" for med in meds) + "."
        return speech, [_meds_card(meds)]

    if intent == "confirm":
        payload = results.get("confirm_action", {})
        if payload.get("status") == "denied" or not payload.get("ok", False):
            reason = payload.get("reason", "There is nothing waiting for a yes.")
            return (f"I didn't send it. {reason}", [])
        if payload.get("status") != "executed":
            return ("Nothing is waiting on a yes. Ask me about Elena's day first.", [])
        kind = payload.get("kind")
        if kind == "order_supply":
            speech = f"Placed. {payload.get('result')} The charge is simulated. No wallet was billed."
            title = "Order placed"
        else:
            speech = f"Done. {payload.get('result')} I'll keep the morning dose on the board until the dispenser opens."
            title = "On the kitchen Show"
        return (
            speech,
            [
                {
                    "kind": "done",
                    "title": title,
                    "body": payload.get("summary", ""),
                    "tone": "ok",
                    "task_id": payload.get("task_id"),
                }
            ],
        )

    if intent == "cancel":
        payload = results.get("dismiss_action", {})
        if payload.get("status") == "nothing_pending":
            return ("Nothing was waiting. Elena's board is unchanged.", [])
        return ("Left it. I won't send that unless you ask again.", [{"kind": "done", "title": "Cancelled", "body": payload.get("summary", ""), "tone": "info"}])

    if intent == "remind":
        proposal = results.get("propose_action", {})
        if not proposal.get("ok"):
            return (proposal.get("reason", "I can't stage that reminder."), [])
        return (
            f"I can put this on the kitchen Show: {proposal['summary']} Send it?",
            [_confirm_card("Send to the Show", proposal)],
        )

    if intent == "order":
        inventory = results.get("check_inventory", {})
        proposal = results.get("propose_action", {})
        items = inventory.get("items") or []
        item = items[0] if items else None
        if not proposal.get("ok") or item is None:
            return ("I couldn't stage an order.", [])
        speech = (
            f"She has {item['days_left']} days of {item['brand']} left. "
            f"The usual box is {item['price']} and arrives {item['arrives'].lower()}. "
            "I will not place it until you confirm."
        )
        return speech, [_supply_card(item), _confirm_card("Place the order", proposal, tone="warn")]

    if intent == "inventory":
        inventory = results.get("check_inventory", {})
        items = inventory.get("items") or []
        if not items:
            return ("I don't have a supply by that name on Elena's list.", [])
        item = items[0]
        speech = (
            f"{item['brand']} {item['name'].lower()}: {item['days_left']} days left, "
            f"{item['price']}, arrives {item['arrives'].lower()} if you reorder the usual box."
        )
        return speech, [
            _supply_card(item),
            {
                "kind": "prompt",
                "title": "Reorder",
                "body": "I will ask before anything is placed.",
                "tone": "info",
                "action": {"label": "Order the usual", "utterance": "Order the usual briefs"},
            },
        ]

    if intent == "memory":
        memory = results.get("recall_memory", {})
        notes = memory.get("memories") or []
        if not notes:
            return ("I don't have notes from earlier yet.", [])
        speech = "From earlier: " + " ".join(note["body"] for note in notes[:2])
        cards = [
            {"kind": "memory", "title": "Already on file", "body": note["body"], "tone": "info"}
            for note in notes[:3]
        ]
        return speech, cards

    if intent == "update_visit":
        saved = (results.get("update_appointment") or {}).get("appointment") or {}
        if not saved:
            return ("I didn't catch a weekday and a time. Try Thursday at 2.", [])
        speech = (
            f"Saved. Cardiology with {saved.get('clinician', 'the clinic')} "
            f"is now {saved.get('when_label', 'the new time')}."
        )
        return speech, [_visit_card(saved)]

    if intent == "packet":
        started = results.get("start_visit_packet") or {}
        if not started.get("ok"):
            return (started.get("reason", "I couldn't start the visit packet."), [])
        when = started.get("when_label", "the visit")
        return (
            f"I'm putting the packet together for {when}. It will list the medications, how today went, and what to ask.",
            [
                {
                    "kind": "packet",
                    "title": "Visit packet",
                    "body": "Gathering medications, adherence, notes, and questions.",
                    "tone": "info",
                    "task_id": started.get("task_id"),
                }
            ],
        )

    if intent == "calendar":
        appointment = (results.get("read_calendar") or {}).get("appointment") or {}
        notes = (results.get("recall_memory") or {}).get("memories") or []
        backup = next((n["body"] for n in notes if "Luis" in n["body"]), "")
        speech = (
            f"{appointment.get('specialty', 'The visit')} with {appointment.get('clinician', 'the clinic')} "
            f"is {appointment.get('when_label', 'soon')} at {appointment.get('place', 'the clinic')}. "
            f"{appointment.get('ride', 'Maya')} is the ride. {appointment.get('note', '')}"
        ).strip()
        if backup:
            speech += " " + backup
        return speech, [_visit_card(appointment)]

    return _status_reply(results)


def _status_reply(results: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    tele = results.get("read_telemetry") or {}
    appointment = (results.get("read_calendar") or {}).get("appointment") or {}
    inventory = results.get("check_inventory") or {}
    notes = (results.get("recall_memory") or {}).get("memories") or []
    meds = tele.get("meds") or []
    missed = tele.get("missed") or []
    due = tele.get("due") or []
    items = inventory.get("items") or []
    briefs = next((item for item in items if item["id"] == "briefs"), items[0] if items else None)
    show = (tele.get("telemetry") or {}).get("echo_show") or {}

    parts: list[str] = []
    if missed:
        names = ", ".join(f"{m['name']} {m['dose']}" for m in missed)
        parts.append(f"{names} never left the dispenser this morning.")
    if due:
        names = ", ".join(m["name"] for m in due)
        parts.append(f"{names} is due now.")
    if appointment:
        when = (
            appointment["when_label"]
            .replace("Tomorrow, ", "tomorrow at ")
            .replace("Today, ", "today at ")
        )
        parts.append(f"{appointment['specialty']} with {appointment['clinician']} is {when}, and you're the ride.")
    if briefs and briefs["days_left"] <= 7:
        parts.append(f"{briefs['brand']} has {briefs['days_left']} days left.")
    if notes:
        parts.append(notes[0]["body"])
    if show.get("online"):
        parts.append("Want me to put that on the kitchen Show?")
    speech = " ".join(parts) if parts else "I don't have a change on Elena's board right now."

    cards: list[dict[str, Any]] = []
    if meds:
        cards.append(_meds_card(meds))
    if appointment:
        cards.append(_visit_card(appointment))
    if briefs:
        cards.append(_supply_card(briefs))
    cards.append(
        {
            "kind": "prompt",
            "title": "Kitchen Show",
            "body": "Ask before anything is sent.",
            "tone": "info",
            "action": {"label": "Remind her", "utterance": "Remind her on the kitchen Show"},
        }
    )
    return speech, cards


def _meds_card(meds: list[dict[str, Any]]) -> dict[str, Any]:
    lines = [f"{m['name']} {m['dose']}\n{m['status']} at {m['time']}" for m in meds]
    missed = any(m["status"] == "missed" for m in meds)
    return {
        "kind": "meds",
        "title": "Medicines",
        "body": "\n".join(lines),
        "tone": "warn" if missed else "ok",
    }


def _visit_card(appointment: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "visit",
        "title": appointment.get("specialty", "Visit"),
        "body": (
            f"{appointment.get('when_label', '')}\n"
            f"{appointment.get('clinician', '')}\n"
            f"{appointment.get('place', '')}\n"
            f"Ride: {appointment.get('ride', '')}"
        ),
        "tone": "info",
    }


def _supply_card(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "supply",
        "title": item["brand"],
        "body": f"{item['name']}\n{item['days_left']} days left · {item['price']}\nArrives {item['arrives'].lower()}",
        "tone": "warn" if item["days_left"] <= 7 else "ok",
    }


def _confirm_card(title: str, proposal: dict[str, Any], tone: str = "info") -> dict[str, Any]:
    token = proposal.get("confirmation_token", "")
    yes = "Yes, place the order" if proposal.get("kind") == "order_supply" else "Yes, send it"
    no = "No, leave it"
    return {
        "kind": "confirm",
        "title": title,
        "body": proposal.get("summary", ""),
        "tone": tone,
        "confirm": {"token": token, "yes": yes, "no": no},
    }


def parse_tool_result(content_text: str) -> dict[str, Any]:
    try:
        parsed = json.loads(content_text)
    except json.JSONDecodeError:
        return {"ok": False, "status": "error", "reason": content_text}
    if isinstance(parsed, dict):
        return parsed
    return {"ok": True, "value": parsed}
