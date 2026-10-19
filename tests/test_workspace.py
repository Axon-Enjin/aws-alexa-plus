"""HTTP contracts that keep the chat and household context in sync."""

import tempfile
import unittest
from pathlib import Path

from starlette.testclient import TestClient

import caresync.store as store
from caresync.web_app import build_web_app


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.previous_db = store.DB_PATH
        store.DB_PATH = Path(self.tmp.name) / "workspace.db"
        self.client = TestClient(build_web_app())

    def tearDown(self):
        self.client.close()
        store.DB_PATH = self.previous_db
        self.tmp.cleanup()

    def turn(self, utterance, token="", session="workspace"):
        response = self.client.post("/api/turn", json={
            "utterance": utterance,
            "session_id": session,
            "confirmation_token": token,
        })
        self.assertEqual(response.status_code, 200)
        return response.json()

    def test_pending_action_survives_question_and_is_cleared_after_cancel(self):
        proposal = self.turn("Remind her on the kitchen Show")
        token = proposal["pending_action"]["token"]
        self.assertEqual(proposal["pending_action"]["kind"], "remind_show")
        question = self.turn("When is cardiology?", token)
        self.assertEqual(question["pending_action"]["token"], token)
        unrelated_yes = self.turn("Yes, when is cardiology?", token)
        self.assertEqual(unrelated_yes["intent"], "calendar")
        self.assertEqual(unrelated_yes["pending_action"]["token"], token)
        other_session = self.turn("How is Elena today?", session="another-tab")
        self.assertIsNone(other_session["pending_action"])
        cancelled = self.turn("No, leave it", token)
        self.assertIsNone(cancelled["pending_action"])
        self.assertEqual(cancelled["household"]["meds"], proposal["household"]["meds"])

    def test_confirm_returns_updated_household_and_cannot_repeat_order(self):
        proposal = self.turn("Order the usual briefs")
        token = proposal["pending_action"]["token"]
        before = next(x for x in proposal["household"]["supplies"] if x["id"] == "briefs")["days_left"]
        confirmed = self.turn("Yes, place the order", token)
        after = next(x for x in confirmed["household"]["supplies"] if x["id"] == "briefs")["days_left"]
        self.assertEqual(after, before + 30)
        self.assertIsNone(confirmed["pending_action"])
        repeat = self.turn("Yes, place the order", token)
        self.assertEqual(next(x for x in repeat["household"]["supplies"] if x["id"] == "briefs")["days_left"], after)
        moved = self.turn("Mom's cardiologist moved to Thursday at 2")
        self.assertEqual(moved["household"]["appointment"]["when_label"], "Thursday, 2:00 PM")

    def test_thumbnails_are_served_without_exposing_arbitrary_files(self):
        for name in ("supply-brief.png", "kitchen-display.png"):
            response = self.client.get("/assets/" + name)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["content-type"], "image/png")
            self.assertTrue(response.content.startswith(b"\x89PNG"))
        self.assertEqual(self.client.get("/assets/asset-provenance.json").status_code, 404)

    def test_reordering_strips_confirms_the_selected_item_only(self):
        proposal = self.turn("Order Glucose test strips")
        self.assertIn("$18.99", proposal["speech"])
        self.assertNotIn("$42.18", proposal["speech"])
        before = {item["id"]: item["days_left"] for item in proposal["household"]["supplies"]}
        self.assertEqual(before, {"briefs": 4, "strips": 18})
        confirmed = self.turn("Yes, place the order", proposal["pending_action"]["token"])
        after = {item["id"]: item["days_left"] for item in confirmed["household"]["supplies"]}
        self.assertEqual(after, {"briefs": 4, "strips": 48})
        self.assertIn("glucose test strips", confirmed["speech"].lower())

    def test_unknown_supply_does_not_stage_a_different_product(self):
        reply = self.turn("Order mystery gloves")
        self.assertIsNone(reply["pending_action"])
        self.assertFalse(any(card.get("confirm") for card in reply["cards"]))
        self.assertIn("Choose one supply", reply["speech"])

    def test_invalid_appointment_time_keeps_existing_visit(self):
        before = self.client.get("/api/board").json()["appointment"]
        reply = self.turn("Move cardiology to Thursday at 25:99")
        self.assertEqual(reply["household"]["appointment"], before)


if __name__ == "__main__":
    unittest.main()
