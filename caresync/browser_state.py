"""Signed cookie that carries care-record changes across Vercel instances.

The household seed is rebuilt on each instance. Pending confirmations, orders,
reminders, and notes live in this cookie so a yes on one instance still
matches the question asked on another.
"""

from __future__ import annotations

import base64
import contextvars
import hashlib
import hmac
import json
import os

_state: contextvars.ContextVar[dict | None] = contextvars.ContextVar("caresync_overlay", default=None)
_SECRET = os.environ.get("CARESYNC_SECRET", "caresync-demo-secret").encode()


def empty() -> dict:
    return {"pending": [], "memories": [], "supply_days": {}, "routines": {}, "tasks": []}


def active() -> bool:
    return _state.get() is not None


def current() -> dict | None:
    return _state.get()


def install(data: dict):
    return _state.set(data)


def uninstall(token) -> None:
    _state.reset(token)


def decode(raw: str | None) -> dict:
    base = empty()
    if not raw or "." not in raw:
        return base
    body, sig = raw.rsplit(".", 1)
    expected = hmac.new(_SECRET, body.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig):
        return base
    try:
        padded = body + "=" * (-len(body) % 4)
        parsed = json.loads(base64.urlsafe_b64decode(padded))
    except (json.JSONDecodeError, ValueError):
        return base
    if isinstance(parsed, dict):
        for key in base:
            if key in parsed:
                base[key] = parsed[key]
    return base


def encode(data: dict) -> str:
    raw = base64.urlsafe_b64encode(json.dumps(data, separators=(",", ":")).encode()).decode().rstrip("=")
    sig = hmac.new(_SECRET, raw.encode(), hashlib.sha256).hexdigest()
    return f"{raw}.{sig}"


def cookie_header(data: dict, *, secure: bool) -> str:
    parts = [
        f"caresync={encode(data)}",
        "Path=/",
        "HttpOnly",
        "SameSite=Lax",
        "Max-Age=86400",
    ]
    if secure:
        parts.append("Secure")
    return "; ".join(parts)
