import tempfile
import unittest
from pathlib import Path

import caresync.store as store
from caresync.browser_state import current, decode, empty, encode, install, uninstall
from caresync.orchestrator import compose, plan
from caresync.policy import decide, policy_text
from caresync.tools import confirm_action, get_task, propose_action, read_calendar, read_telemetry, start_visit_packet, update_appointment


class PolicyTests(unittest.TestCase):
    def test_cedar_file_forbids_unconfirmed_execution(self):
        text = policy_text().lower()
        self.assertIn("forbid", text)
        self.assertIn("context.confirmed == true", text)

    def test_read_requires_caregiver_consent(self):
        self.assertTrue(decide("read", "maya-reyes", confirmed=False, consent=True).allowed)
        self.assertFalse(decide("read", "stranger", confirmed=False, consent=False).allowed)

    def test_execute_requires_confirmation(self):
        self.assertFalse(decide("execute", "maya-reyes", confirmed=False, consent=True).allowed)
        self.assertTrue(decide("execute", "maya-reyes", confirmed=True, consent=True).allowed)
        self.assertFalse(decide("execute", "stranger", confirmed=True, consent=False).allowed)


class PlanTests(unittest.TestCase):
    def test_hero_questions(self):
        self.assertEqual(plan("What's going on with Mom today?"), "status")
        self.assertEqual(plan("How is Elena today?"), "status")
        self.assertEqual(plan("Did she take her pills?"), "meds")
        self.assertEqual(plan("Remind her on the kitchen Show"), "remind")
        self.assertEqual(plan("Yes, send it"), "confirm")
        self.assertEqual(plan("Order the usual briefs"), "order")
        self.assertEqual(plan("Yes, place the order"), "confirm")
        self.assertEqual(plan("No, leave it"), "cancel")
        self.assertEqual(plan("When is cardiology?"), "calendar")
        self.assertEqual(plan("Mom's cardiologist moved to Thursday at 2"), "update_visit")
        self.assertEqual(plan("Get me ready for Thursday"), "packet")
        self.assertEqual(plan("What did we decide yesterday?"), "memory")

    def test_yes_inside_a_real_question_is_not_confirmation(self):
        self.assertEqual(plan("Yes we should check on Mom"), "status")
        self.assertEqual(plan("Yes we should check on Mom", has_token=True), "status")
        self.assertEqual(plan("Yes, when is cardiology?", has_token=True), "calendar")


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        store.DB_PATH = Path(self.tmp.name) / "care.db"

    def tearDown(self):
        self.tmp.cleanup()

    def test_seed_has_a_missed_morning_dose_and_a_visit(self):
        from datetime import datetime

        evening = datetime(2026, 10, 18, 20, 11)
        self.assertEqual(store.med_status(8, 0, False, evening), "missed")
        self.assertEqual(store.med_status(8, 0, True, evening), "taken")
        self.assertEqual(store.med_status(20, 0, False, evening), "due")
        home = store.household()
        by_id = {med["id"]: med for med in home["meds"]}
        self.assertEqual(by_id["lisinopril"]["status"], store.med_status(8, 0, False))
        self.assertIn("Patel", home["appointment"]["clinician"])
        self.assertEqual(home["supplies"][0]["days_left"], 4)

    def test_unconfirmed_execute_is_denied_and_confirm_changes_the_board(self):
        denied = confirm_action("session-a", "", "maya-reyes")
        self.assertIn("denied", denied)
        staged = propose_action("order_supply", "session-a")
        self.assertIn("input_required", staged)
        done = confirm_action("session-a", "", "maya-reyes")
        self.assertIn("executed", done)
        home = store.household()
        briefs = next(item for item in home["supplies"] if item["id"] == "briefs")
        self.assertGreater(briefs["days_left"], 4)

    def test_stranger_cannot_confirm_a_staged_order(self):
        propose_action("remind_show", "session-b")
        denied = confirm_action("session-b", "", "someone-else")
        self.assertIn("denied", denied)
        self.assertNotIn("executed", denied)

    def test_cookie_overlay_keeps_an_order_without_the_database(self):
        token = install(empty())
        try:
            staged = propose_action("order_supply", "session-web")
            self.assertIn("input_required", staged)
            store.DB_PATH = Path(self.tmp.name) / "other.db"
            done = confirm_action("session-web", "", "maya-reyes")
            self.assertIn("executed", done)
            home = store.household()
            briefs = next(item for item in home["supplies"] if item["id"] == "briefs")
            self.assertEqual(briefs["days_left"], 34)
            roundtrip = decode(encode(current()))
            self.assertEqual(roundtrip["supply_days"]["briefs"], 30)
        finally:
            uninstall(token)

    def test_spoken_move_is_what_the_next_session_reads(self):
        import json

        saved = json.loads(update_appointment(3, 14, 0))
        self.assertIn("Thursday", saved["appointment"]["when_label"])
        later = json.loads(read_calendar())
        self.assertIn("Thursday", later["appointment"]["when_label"])
        self.assertIn("2:00 PM", later["appointment"]["when_label"])

    def test_other_household_is_refused(self):
        denied = read_calendar(resident_id="hh_other")
        self.assertIn("denied", denied)
        self.assertNotIn("Patel", denied)

    def test_visit_packet_finishes_with_meds_and_questions(self):
        import json
        import time

        update_appointment(3, 14, 0)
        started = json.loads(start_visit_packet())
        self.assertEqual(started["status"], "running")
        time.sleep(1.6)
        finished = json.loads(get_task(started["task_id"]))
        self.assertEqual(finished["status"], "completed")
        self.assertIn("Lisinopril", finished["result"])
        self.assertIn("Questions", finished["result"])
        self.assertIn("Thursday", finished["result"])

    def test_telemetry_is_specific(self):
        payload = read_telemetry()
        self.assertIn("Lisinopril", payload)
        self.assertIn("Kitchen", payload)


class ComposeTests(unittest.TestCase):
    def test_status_speech_names_the_miss_and_the_visit(self):
        speech, cards = compose(
            "status",
            {
                "read_telemetry": {
                    "ok": True,
                    "meds": [{"name": "Lisinopril", "dose": "10 mg", "time": "8:00 AM", "status": "missed"}],
                    "missed": [{"name": "Lisinopril", "dose": "10 mg"}],
                    "due": [],
                    "telemetry": {"echo_show": {"name": "Kitchen", "online": True}},
                },
                "read_calendar": {
                    "ok": True,
                    "appointment": {
                        "specialty": "Cardiology",
                        "clinician": "Dr. Anita Patel",
                        "when_label": "Tomorrow, 2:00 PM",
                        "place": "Austin Heart Clinic",
                        "ride": "Maya",
                        "note": "Pre-visit form is still open",
                    },
                },
                "check_inventory": {
                    "ok": True,
                    "items": [{"id": "briefs", "brand": "Northstar Overnight", "name": "Protective underwear", "days_left": 4, "price": "$42.18", "arrives": "Tomorrow"}],
                },
                "recall_memory": {"ok": True, "memories": [{"body": "Luis is the backup ride."}]},
            },
            "What's going on with Mom today?",
        )
        self.assertIn("Lisinopril", speech)
        self.assertIn("Patel", speech)
        self.assertTrue(any(card["kind"] == "confirm" or card.get("action") for card in cards))


if __name__ == "__main__":
    unittest.main()
