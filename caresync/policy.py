"""In-process enforcement of policies/caresync.cedar.

The Cedar file is the contract. These three rules are the same ones written
there: a caregiver with consent may read and propose; nobody may execute a
reminder or a payment unless that caregiver has confirmed the staged action.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

POLICY_PATH = Path(__file__).resolve().parent / "policies" / "caresync.cedar"

CAREGIVER_ID = "maya-reyes"


@dataclass(frozen=True)
class Decision:
    allowed: bool
    action: str
    reason: str


def policy_text() -> str:
    return POLICY_PATH.read_text(encoding="utf-8")


def decide(action: str, actor_id: str, *, confirmed: bool, consent: bool) -> Decision:
    role = "caregiver" if actor_id == CAREGIVER_ID else "other"
    if action in {"read", "propose"}:
        if role == "caregiver" and consent:
            return Decision(True, action, "permit: caregiver with consent")
        return Decision(False, action, "permit requires a caregiver with consent on file")
    if action == "execute":
        if role == "caregiver" and consent and confirmed:
            return Decision(True, action, "forbid lifted: caregiver confirmed this action")
        if not confirmed:
            return Decision(False, action, "forbid: execution requires an explicit confirmation")
        return Decision(False, action, "forbid: only the designated caregiver can execute")
    return Decision(False, action, f"unknown action {action}")
