"""Care tools. Every one of these is registered on the MCP server."""

from __future__ import annotations

import json
import re
import secrets

from caresync import policy
from caresync.store import (
    RESIDENT_ID,
    apply_effect,
    close_pending,
    create_task,
    find_pending,
    household,
    read_task,
    remember,
    stage,
    update_appointment as save_appointment,
)

ALLOWED_HOUSEHOLDS = {RESIDENT_ID, "hh_demo"}


def _dump(payload: dict) -> str:
    return json.dumps(payload)


def _denied(action: str, reason: str) -> str:
    return _dump({"ok": False, "status": "denied", "action": action, "reason": reason})


def _scope(resident_id: str) -> str | None:
    if resident_id not in ALLOWED_HOUSEHOLDS:
        return _denied("read", "That household is not on this plan.")
    return None


def _guard(action: str, actor_id: str, *, confirmed: bool = False) -> str | None:
    consent = actor_id == policy.CAREGIVER_ID
    decision = policy.decide(action, actor_id, confirmed=confirmed, consent=consent)
    if decision.allowed:
        return None
    return _denied(action, decision.reason)


def recall_memory(actor_id: str = policy.CAREGIVER_ID, resident_id: str = RESIDENT_ID) -> str:
    """Cross-session notes CareSync already has about this household."""
    blocked = _scope(resident_id) or _guard("read", actor_id)
    if blocked:
        return blocked
    home = household()
    return _dump(
        {
            "ok": True,
            "resident_id": resident_id,
            "resident": home["resident"]["name"],
            "memories": home["memories"],
        }
    )


def read_telemetry(actor_id: str = policy.CAREGIVER_ID, resident_id: str = RESIDENT_ID) -> str:
    """Pill dispenser, motion, fall quiet-period, and whether the kitchen Show is online."""
    blocked = _scope(resident_id) or _guard("read", actor_id)
    if blocked:
        return blocked
    home = household()
    missed = [m for m in home["meds"] if m["status"] == "missed"]
    due = [m for m in home["meds"] if m["status"] == "due"]
    return _dump(
        {
            "ok": True,
            "resident_id": resident_id,
            "resident": home["resident"]["name"],
            "meds": home["meds"],
            "missed": missed,
            "due": due,
            "telemetry": home["telemetry"],
        }
    )


def read_calendar(actor_id: str = policy.CAREGIVER_ID, resident_id: str = RESIDENT_ID) -> str:
    """The next appointment, who is driving, and what is still unfinished."""
    blocked = _scope(resident_id) or _guard("read", actor_id)
    if blocked:
        return blocked
    home = household()
    return _dump({"ok": True, "resident_id": resident_id, "appointment": home["appointment"]})


def read_routines(actor_id: str = policy.CAREGIVER_ID, resident_id: str = RESIDENT_ID) -> str:
    """Today's care routine and which steps are still open."""
    blocked = _scope(resident_id) or _guard("read", actor_id)
    if blocked:
        return blocked
    home = household()
    return _dump({"ok": True, "resident_id": resident_id, "routines": home["routines"]})


def _inventory_matches(items: list[dict], query: str) -> list[dict]:
    """Resolve catalogue IDs/names before shared brand words. Never guess an unknown product."""
    query = query.lower().strip()
    generic = {"check", "the", "usual", "supplies", "supply", "order", "reorder", "buy", "please", "show", "me", "her", "mom", "elena", "inventory", "stock", "what", "is", "left", "view", "s", "are", "low", "running", "days", "how", "many", "we", "have", "any", "do", "on", "hand", "my", "our"}
    if not query or not (set(re.findall(r"[a-z]+", query)) - generic):
        return items
    aliases = {"briefs": {"brief", "briefs", "pads", "underwear"}, "strips": {"strips", "strip", "glucose"}}
    words = set(re.findall(r"[a-z]+", query))
    specific = [item for item in items if item["name"].lower() in query or item["id"] in words or words & aliases.get(item["id"], set())]
    if specific:
        return specific
    branded = [item for item in items if item["brand"].lower() in query]
    if not branded:
        return []
    longest = max(len(item["brand"]) for item in branded)
    return [item for item in branded if len(item["brand"]) == longest]


def check_inventory(
    item_query: str = "",
    actor_id: str = policy.CAREGIVER_ID,
    resident_id: str = RESIDENT_ID,
) -> str:
    """Days of each supply left, and the usual listing a caregiver would reorder."""
    blocked = _scope(resident_id) or _guard("read", actor_id)
    if blocked:
        return blocked
    home = household()
    items = _inventory_matches(home["supplies"], item_query)
    return _dump({"ok": True, "resident_id": resident_id, "items": items})


def propose_action(
    kind: str,
    session_id: str,
    actor_id: str = policy.CAREGIVER_ID,
    resident_id: str = RESIDENT_ID,
    item_query: str = "",
) -> str:
    """Stage a reminder or an order. Does not execute it. Returns a confirmation token."""
    blocked = _scope(resident_id) or _guard("propose", actor_id)
    if blocked:
        return blocked
    home = household()
    if kind == "remind_show":
        missed = [m for m in home["meds"] if m["status"] == "missed"]
        med = missed[0]["name"] if missed else "evening medicine"
        summary = (
            f"{med} was missed, and {home['appointment']['specialty'].lower()} "
            f"is {home['appointment']['when_label']}."
        )
        payload = {"supply_id": None, "show": home["telemetry"]["echo_show"]["name"]}
    elif kind == "order_supply":
        matches = _inventory_matches(home["supplies"], item_query)
        generic_order = not item_query or not (set(re.findall(r"[a-z]+", item_query.lower())) - {"order", "reorder", "buy", "the", "usual", "supplies", "supply", "please"})
        if generic_order:
            matches = [item for item in home["supplies"] if item["id"] == "briefs"]
        if len(matches) != 1:
            return _dump({"ok": False, "status": "denied", "reason": "Choose one supply from the household list before ordering."})
        item = matches[0]
        summary = (
            f"{item['brand']} {item['name'].lower()}, {item['price']}, arrives {item['arrives'].lower()}."
        )
        payload = {"supply_id": item["id"], "price": item["price"]}
    else:
        return _dump({"ok": False, "status": "denied", "reason": f"unknown action kind {kind}"})

    token = "cs_" + secrets.token_hex(4)
    stage(token, session_id, kind, summary, payload)
    return _dump(
        {
            "ok": True,
            "status": "input_required",
            "confirmation_token": token,
            "kind": kind,
            "summary": summary,
            "resident_id": resident_id,
            "policy": "execute is forbidden until the caregiver confirms this token",
        }
    )


def confirm_action(
    session_id: str,
    confirmation_token: str = "",
    actor_id: str = policy.CAREGIVER_ID,
) -> str:
    """Execute a staged action. Refuses unless the token matches and policy allows it."""
    pending = find_pending(session_id, confirmation_token)
    confirmed = pending is not None
    blocked = _guard("execute", actor_id, confirmed=confirmed)
    if blocked:
        return blocked
    assert pending is not None
    close_pending(pending["token"], "confirmed")
    result = apply_effect(pending["kind"], pending["payload"])
    remember(f"Maya confirmed: {pending['summary']} {result}", "confirm")
    task_id = "task_" + secrets.token_hex(3)
    label = result
    create_task(task_id, label)
    return _dump(
        {
            "ok": True,
            "status": "executed",
            "kind": pending["kind"],
            "summary": pending["summary"],
            "result": result,
            "task_id": task_id,
            "confirmation_token": pending["token"],
        }
    )


def update_appointment(
    weekday: int,
    hour: int,
    minute: int,
    actor_id: str = policy.CAREGIVER_ID,
    resident_id: str = RESIDENT_ID,
) -> str:
    """Save a spoken visit change and read the new time back."""
    blocked = _scope(resident_id) or _guard("propose", actor_id)
    if blocked:
        return blocked
    if not (0 <= weekday <= 6 and 0 <= hour <= 23 and 0 <= minute <= 59):
        return _denied("propose", "Choose a valid weekday and time for the visit.")
    saved = save_appointment(weekday, hour, minute)
    remember(f"Maya moved cardiology to {saved['when_label']}.", "update")
    return _dump({"ok": True, "appointment": saved})


def start_visit_packet(
    actor_id: str = policy.CAREGIVER_ID,
    resident_id: str = RESIDENT_ID,
) -> str:
    """Start a visit-prep packet. Poll get_task until it finishes."""
    blocked = _scope(resident_id) or _guard("read", actor_id)
    if blocked:
        return blocked
    visit = household()["appointment"]["when_label"]
    task_id = "task_" + secrets.token_hex(3)
    create_task(task_id, visit, kind="visit_packet")
    return _dump({"ok": True, "status": "running", "task_id": task_id, "when_label": visit})


def dismiss_action(session_id: str, confirmation_token: str = "", actor_id: str = policy.CAREGIVER_ID) -> str:
    """Drop a staged action without executing it."""
    blocked = _guard("propose", actor_id)
    if blocked:
        return blocked
    pending = find_pending(session_id, confirmation_token)
    if pending is None:
        return _dump({"ok": True, "status": "nothing_pending"})
    close_pending(pending["token"], "dismissed")
    return _dump({"ok": True, "status": "dismissed", "kind": pending["kind"], "summary": pending["summary"]})


def get_task(task_id: str, actor_id: str = policy.CAREGIVER_ID) -> str:
    """Poll a reminder or order task. Running tasks complete after a short delay."""
    blocked = _guard("read", actor_id)
    if blocked:
        return blocked
    task = read_task(task_id)
    if task is None:
        return _dump({"ok": False, "status": "missing", "task_id": task_id})
    return _dump({"ok": True, **task})
