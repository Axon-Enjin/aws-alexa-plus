"""SQLite care record. MCP sessions do not hold this state."""

from __future__ import annotations

import json
import os
import sqlite3
import threading
from datetime import datetime, timedelta
from pathlib import Path

from caresync.browser_state import current
from caresync.policy import CAREGIVER_ID

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = Path("/tmp/caresync.db") if os.environ.get("VERCEL") else ROOT / "data" / "caresync.db"

RESIDENT_ID = "elena-reyes"

_lock = threading.RLock()


def _connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def _now() -> datetime:
    return datetime.now().replace(microsecond=0)


def _iso(dt: datetime) -> str:
    return dt.isoformat(timespec="minutes")


def clock(dt: datetime) -> str:
    return dt.strftime("%I:%M %p").lstrip("0")


def med_status(hour: int, minute: int, taken: bool, now: datetime | None = None) -> str:
    now = now or _now()
    due = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if taken:
        return "taken"
    delta_min = (now - due).total_seconds() / 60
    if delta_min > 90:
        return "missed"
    if -90 <= delta_min <= 90:
        return "due"
    return "upcoming"


def init_db(conn: sqlite3.Connection | None = None) -> None:
    own = conn is None
    conn = conn or _connect()
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE IF NOT EXISTS meds (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                dose TEXT NOT NULL,
                hour INTEGER NOT NULL,
                minute INTEGER NOT NULL,
                taken INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS appointment (
                id TEXT PRIMARY KEY,
                clinician TEXT NOT NULL,
                specialty TEXT NOT NULL,
                place TEXT NOT NULL,
                hour INTEGER NOT NULL,
                minute INTEGER NOT NULL,
                day_offset INTEGER NOT NULL,
                ride TEXT NOT NULL,
                note TEXT NOT NULL,
                weekday INTEGER
            );
            CREATE TABLE IF NOT EXISTS routines (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                when_label TEXT NOT NULL,
                status TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS supplies (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                brand TEXT NOT NULL,
                days_left INTEGER NOT NULL,
                price_cents INTEGER NOT NULL,
                arrives TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS telemetry (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                show_name TEXT NOT NULL,
                show_online INTEGER NOT NULL,
                falls_clear_days INTEGER NOT NULL,
                motion_room TEXT NOT NULL,
                motion_minutes_ago INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                body TEXT NOT NULL,
                created_at TEXT NOT NULL,
                source TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS pending (
                token TEXT PRIMARY KEY,
                session_id TEXT NOT NULL,
                kind TEXT NOT NULL,
                summary TEXT NOT NULL,
                payload TEXT NOT NULL,
                created_at TEXT NOT NULL,
                status TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                status TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TEXT NOT NULL,
                kind TEXT NOT NULL DEFAULT 'note'
            );
            """
        )
        conn.commit()
        _migrate(conn)
        row = conn.execute("SELECT value FROM meta WHERE key = 'seeded'").fetchone()
        if row is None:
            _seed(conn)
    finally:
        if own:
            conn.close()


def reset_db() -> None:
    overlay = current()
    if overlay is not None:
        overlay.clear()
        overlay.update(
            {"pending": [], "memories": [], "supply_days": {}, "routines": {}, "tasks": [], "appointment": None}
        )
        return
    with _lock:
        conn = _connect()
        try:
            conn.executescript(
                """
                DELETE FROM meta;
                DELETE FROM meds;
                DELETE FROM appointment;
                DELETE FROM routines;
                DELETE FROM supplies;
                DELETE FROM telemetry;
                DELETE FROM memories;
                DELETE FROM pending;
                DELETE FROM tasks;
                """
            )
            _seed(conn)
        finally:
            conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    appointment_cols = {row[1] for row in conn.execute("PRAGMA table_info(appointment)")}
    if "weekday" not in appointment_cols:
        conn.execute("ALTER TABLE appointment ADD COLUMN weekday INTEGER")
    task_cols = {row[1] for row in conn.execute("PRAGMA table_info(tasks)")}
    if "kind" not in task_cols:
        conn.execute("ALTER TABLE tasks ADD COLUMN kind TEXT NOT NULL DEFAULT 'note'")
    conn.commit()


WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def _when_label(weekday: int, hour: int, minute: int, now: datetime) -> str:
    stamp = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    return f"{WEEKDAY_NAMES[weekday]}, {clock(stamp)}"


def _seed(conn: sqlite3.Connection) -> None:
    conn.executemany(
        "INSERT INTO meds (id, name, dose, hour, minute, taken) VALUES (?, ?, ?, ?, ?, ?)",
        [
            ("lisinopril", "Lisinopril", "10 mg", 8, 0, 0),
            ("aspirin", "Aspirin", "81 mg", 8, 0, 1),
            ("metformin", "Metformin", "500 mg", 20, 0, 0),
        ],
    )
    conn.execute(
        """
        INSERT INTO appointment
            (id, clinician, specialty, place, hour, minute, day_offset, ride, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "cardio",
            "Dr. Anita Patel",
            "Cardiology",
            "Austin Heart Clinic, 4th floor",
            14,
            0,
            1,
            "Maya",
            "Pre-visit form is still open",
        ),
    )
    conn.executemany(
        "INSERT INTO routines (id, label, when_label, status) VALUES (?, ?, ?, ?)",
        [
            ("morning-meds", "Morning medicines", "8:00 AM", "open"),
            ("lunch", "Lunch check-in", "12:30 PM", "done"),
            ("walk", "Afternoon walk", "4:00 PM", "skipped"),
            ("evening-meds", "Evening medicines", "8:00 PM", "open"),
        ],
    )
    conn.executemany(
        """
        INSERT INTO supplies (id, name, brand, days_left, price_cents, arrives)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            ("briefs", "Protective underwear", "Northstar Overnight", 4, 4218, "Tomorrow"),
            ("strips", "Glucose test strips", "Northstar", 18, 1899, "Thursday"),
        ],
    )
    conn.execute(
        """
        INSERT INTO telemetry
            (id, show_name, show_online, falls_clear_days, motion_room, motion_minutes_ago)
        VALUES (1, 'Kitchen', 1, 14, 'kitchen', 40)
        """
    )
    yesterday = _iso(_now() - timedelta(days=1))
    conn.executemany(
        "INSERT INTO memories (body, created_at, source) VALUES (?, ?, ?)",
        [
            (
                "Maya asked CareSync to watch the morning lisinopril after Sunday's miss.",
                yesterday,
                "seed",
            ),
            (
                "Luis is the backup ride if Maya's shift runs late.",
                yesterday,
                "seed",
            ),
        ],
    )
    conn.execute("INSERT INTO meta (key, value) VALUES ('seeded', '1')")
    conn.commit()


def _med_rows(conn: sqlite3.Connection, now: datetime) -> list[dict]:
    rows = []
    for row in conn.execute("SELECT * FROM meds ORDER BY hour, name"):
        status = med_status(row["hour"], row["minute"], bool(row["taken"]), now)
        due = now.replace(hour=row["hour"], minute=row["minute"], second=0, microsecond=0)
        rows.append(
            {
                "id": row["id"],
                "name": row["name"],
                "dose": row["dose"],
                "time": clock(due),
                "status": status,
            }
        )
    return rows


def _appointment(conn: sqlite3.Connection, now: datetime) -> dict:
    row = conn.execute("SELECT * FROM appointment LIMIT 1").fetchone()
    if row["weekday"] is not None:
        when_label = _when_label(row["weekday"], row["hour"], row["minute"], now)
    else:
        when = (now + timedelta(days=row["day_offset"])).replace(
            hour=row["hour"], minute=row["minute"], second=0, microsecond=0
        )
        day = "Today" if row["day_offset"] == 0 else "Tomorrow" if row["day_offset"] == 1 else when.strftime("%A")
        when_label = f"{day}, {clock(when)}"
    return {
        "id": row["id"],
        "clinician": row["clinician"],
        "specialty": row["specialty"],
        "place": row["place"],
        "when_label": when_label,
        "ride": row["ride"],
        "note": row["note"],
    }


def household(now: datetime | None = None) -> dict:
    now = now or _now()
    init_db()
    with _lock:
        conn = _connect()
        try:
            meds = _med_rows(conn, now)
            appointment = _appointment(conn, now)
            routines = [dict(r) for r in conn.execute("SELECT id, label, when_label, status FROM routines")]
            supplies = []
            for row in conn.execute("SELECT * FROM supplies"):
                supplies.append(
                    {
                        "id": row["id"],
                        "name": row["name"],
                        "brand": row["brand"],
                        "days_left": row["days_left"],
                        "price": f"${row['price_cents'] / 100:.2f}",
                        "price_cents": row["price_cents"],
                        "arrives": row["arrives"],
                    }
                )
            tele = conn.execute("SELECT * FROM telemetry WHERE id = 1").fetchone()
            seen = now - timedelta(minutes=tele["motion_minutes_ago"])
            memories = [
                {"body": r["body"], "created_at": r["created_at"], "source": r["source"]}
                for r in conn.execute("SELECT body, created_at, source FROM memories ORDER BY id DESC LIMIT 6")
            ]
            built = {
                "resident": {
                    "id": RESIDENT_ID,
                    "name": "Elena Reyes",
                    "age": 78,
                    "city": "Austin",
                    "conditions": "Heart failure, type 2 diabetes",
                },
                "caregiver": {
                    "id": CAREGIVER_ID,
                    "name": "Maya Reyes",
                    "relationship": "Daughter, power of attorney",
                    "consent": True,
                },
                "meds": meds,
                "appointment": appointment,
                "routines": routines,
                "supplies": supplies,
                "telemetry": {
                    "echo_show": {"name": tele["show_name"], "online": bool(tele["show_online"])},
                    "falls_clear_days": tele["falls_clear_days"],
                    "motion": {"room": tele["motion_room"], "last_seen": clock(seen), "home": True},
                    "dispenser_opened_morning": any(
                        m["id"] == "lisinopril" and m["status"] == "taken" for m in meds
                    ),
                },
                "memories": memories,
            }
            return _with_overlay(built)
        finally:
            conn.close()


def _with_overlay(home: dict) -> dict:
    overlay = current()
    if not overlay:
        return home
    for item in home["supplies"]:
        extra = int(overlay.get("supply_days", {}).get(item["id"], 0))
        if extra:
            item["days_left"] += extra
    for routine in home["routines"]:
        replacement = overlay.get("routines", {}).get(routine["id"])
        if replacement:
            routine["status"] = replacement
    extra = list(reversed(overlay.get("memories") or []))
    home["memories"] = (extra + home["memories"])[:6]
    saved = overlay.get("appointment")
    if saved:
        home["appointment"]["when_label"] = saved["when_label"]
    return home


def remember(body: str, source: str) -> None:
    overlay = current()
    if overlay is not None:
        overlay.setdefault("memories", []).append({"body": body, "created_at": _iso(_now()), "source": source})
        overlay["memories"] = overlay["memories"][-6:]
        return
    init_db()
    with _lock:
        conn = _connect()
        try:
            conn.execute(
                "INSERT INTO memories (body, created_at, source) VALUES (?, ?, ?)",
                (body, _iso(_now()), source),
            )
            conn.commit()
        finally:
            conn.close()


def stage(token: str, session_id: str, kind: str, summary: str, payload: dict) -> None:
    overlay = current()
    if overlay is not None:
        for item in overlay.setdefault("pending", []):
            if item["session_id"] == session_id and item["status"] == "open":
                item["status"] = "replaced"
        overlay["pending"].append(
            {
                "token": token,
                "session_id": session_id,
                "kind": kind,
                "summary": summary,
                "payload": payload,
                "created_at": _iso(_now()),
                "status": "open",
            }
        )
        overlay["pending"] = overlay["pending"][-8:]
        return
    init_db()
    with _lock:
        conn = _connect()
        try:
            conn.execute(
                "UPDATE pending SET status = 'replaced' WHERE session_id = ? AND status = 'open'",
                (session_id,),
            )
            conn.execute(
                """
                INSERT INTO pending (token, session_id, kind, summary, payload, created_at, status)
                VALUES (?, ?, ?, ?, ?, ?, 'open')
                """,
                (token, session_id, kind, summary, json.dumps(payload), _iso(_now())),
            )
            conn.commit()
        finally:
            conn.close()


def find_pending(session_id: str, token: str = "") -> dict | None:
    overlay = current()
    if overlay is not None:
        items = [
            item
            for item in overlay.get("pending", [])
            if item["session_id"] == session_id and item["status"] == "open" and (not token or item["token"] == token)
        ]
        if not items:
            return None
        item = items[-1]
        return {
            "token": item["token"],
            "session_id": item["session_id"],
            "kind": item["kind"],
            "summary": item["summary"],
            "payload": item["payload"],
        }
    init_db()
    with _lock:
        conn = _connect()
        try:
            if token:
                row = conn.execute(
                    "SELECT * FROM pending WHERE token = ? AND session_id = ? AND status = 'open'",
                    (token, session_id),
                ).fetchone()
            else:
                row = conn.execute(
                    """
                    SELECT * FROM pending
                    WHERE session_id = ? AND status = 'open'
                    ORDER BY created_at DESC LIMIT 1
                    """,
                    (session_id,),
                ).fetchone()
            if row is None:
                return None
            return {
                "token": row["token"],
                "session_id": row["session_id"],
                "kind": row["kind"],
                "summary": row["summary"],
                "payload": json.loads(row["payload"]),
            }
        finally:
            conn.close()


def close_pending(token: str, status: str) -> None:
    overlay = current()
    if overlay is not None:
        for item in overlay.get("pending", []):
            if item["token"] == token:
                item["status"] = status
        return
    with _lock:
        conn = _connect()
        try:
            conn.execute("UPDATE pending SET status = ? WHERE token = ?", (status, token))
            conn.commit()
        finally:
            conn.close()


def update_appointment(weekday: int, hour: int, minute: int) -> dict:
    """Store a spoken visit change. Weekday is Monday=0."""
    init_db()
    label = _when_label(weekday, hour, minute, _now())
    overlay = current()
    if overlay is not None:
        overlay["appointment"] = {"weekday": weekday, "hour": hour, "minute": minute, "when_label": label}
        home = household()
        return home["appointment"]
    with _lock:
        conn = _connect()
        try:
            conn.execute(
                "UPDATE appointment SET weekday = ?, hour = ?, minute = ? WHERE id = 'cardio'",
                (weekday, hour, minute),
            )
            conn.commit()
        finally:
            conn.close()
    return household()["appointment"]


def _finished_result(kind: str, label: str) -> str:
    if kind == "visit_packet":
        return visit_packet_text()
    return label


def visit_packet_text() -> str:
    home = household()
    meds = "\n".join(f"{med['name']} {med['dose']} - {med['status']}" for med in home["meds"])
    notes = "\n".join(note["body"] for note in home["memories"][:2]) or "No earlier notes."
    visit = home["appointment"]
    missed = [med["name"] for med in home["meds"] if med["status"] == "missed"]
    if missed:
        question = f"Ask about the missed {missed[0]} dose, and confirm the visit time still works."
    else:
        question = "Confirm the visit time still works, and ask if the morning doses should stay as scheduled."
    return (
        f"Medications\n{meds}\n\n"
        f"Visit\n{visit['when_label']} · {visit['clinician']}\n{visit['place']}\n\n"
        f"Notes\n{notes}\n\n"
        f"Questions\n{question}"
    )


def create_task(task_id: str, label: str, kind: str = "note") -> None:
    overlay = current()
    if overlay is not None:
        overlay.setdefault("tasks", []).append(
            {
                "id": task_id,
                "label": label,
                "status": "running",
                "result": "",
                "created_at": _iso(_now()),
                "kind": kind,
            }
        )
        overlay["tasks"] = overlay["tasks"][-8:]
        return
    init_db()
    with _lock:
        conn = _connect()
        try:
            conn.execute(
                "INSERT INTO tasks (id, label, status, result, created_at, kind) VALUES (?, ?, 'running', '', ?, ?)",
                (task_id, label, _iso(_now()), kind),
            )
            conn.commit()
        finally:
            conn.close()


def read_task(task_id: str) -> dict | None:
    overlay = current()
    if overlay is not None:
        row = next((item for item in overlay.get("tasks", []) if item["id"] == task_id), None)
        if row is None:
            return None
        created = datetime.fromisoformat(row["created_at"])
        if row["status"] == "running" and (_now() - created).total_seconds() >= 1.5:
            row["status"] = "completed"
            row["result"] = _finished_result(row.get("kind", "note"), row["label"])
        return {
            "task_id": row["id"],
            "label": row["label"],
            "kind": row.get("kind", "note"),
            "status": row["status"],
            "result": row["result"],
        }
    init_db()
    with _lock:
        conn = _connect()
        try:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
            if row is None:
                return None
            created = datetime.fromisoformat(row["created_at"])
            status = row["status"]
            result = row["result"]
            kind = row["kind"] if "kind" in row.keys() else "note"
            if status == "running" and (_now() - created).total_seconds() >= 1.5:
                status = "completed"
                result = _finished_result(kind, row["label"])
                conn.execute(
                    "UPDATE tasks SET status = ?, result = ? WHERE id = ?",
                    (status, result, task_id),
                )
                conn.commit()
            return {"task_id": row["id"], "label": row["label"], "kind": kind, "status": status, "result": result}
        finally:
            conn.close()


def apply_effect(kind: str, payload: dict) -> str:
    """Mutate the care record after a confirmed action. Returns a short result."""
    overlay = current()
    if overlay is not None:
        if kind == "remind_show":
            overlay.setdefault("routines", {})["morning-meds"] = "reminded"
            return "Reminder is on the kitchen Echo Show."
        if kind == "order_supply":
            supply_id = payload.get("supply_id", "briefs")
            days = overlay.setdefault("supply_days", {})
            days[supply_id] = int(days.get(supply_id, 0)) + 30
            row = next(item for item in household()["supplies"] if item["id"] == supply_id)
            return (
                f"Order placed for {row['brand']} {row['name'].lower()}. "
                f"About {row['days_left']} days on hand once it arrives."
            )
        return "Nothing to apply."
    init_db()
    with _lock:
        conn = _connect()
        try:
            if kind == "remind_show":
                conn.execute(
                    "UPDATE routines SET status = 'reminded' WHERE id = 'morning-meds'"
                )
                conn.commit()
                return "Reminder is on the kitchen Echo Show."
            if kind == "order_supply":
                supply_id = payload.get("supply_id", "briefs")
                conn.execute(
                    "UPDATE supplies SET days_left = days_left + 30 WHERE id = ?",
                    (supply_id,),
                )
                conn.commit()
                row = conn.execute("SELECT days_left, brand, name FROM supplies WHERE id = ?", (supply_id,)).fetchone()
                return (
                    f"Order placed for {row['brand']} {row['name'].lower()}. "
                    f"About {row['days_left']} days on hand once it arrives."
                )
            return "Nothing to apply."
        finally:
            conn.close()
