"""Hit a running CareSync server and print the hero conversation."""

import json
import urllib.request

BASE = "http://127.0.0.1:8080"


def post(path: str, body: dict) -> dict:
    req = urllib.request.Request(
        BASE + path,
        data=json.dumps(body).encode(),
        headers={"content-type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)


def main() -> None:
    with urllib.request.urlopen(BASE + "/api/board", timeout=10) as response:
        board = json.load(response)
    print("BOARD", board["resident"]["name"], [f"{m['name']}:{m['status']}" for m in board["meds"]])
    session_id = "demo-session"
    lines = [
        "What's going on with Mom today?",
        "Remind her on the kitchen Show",
        "Yes, send it",
        "Order the usual briefs",
        "Yes, place the order",
        "What did we decide yesterday?",
    ]
    for utter in lines:
        payload = post("/api/turn", {"utterance": utter, "session_id": session_id})
        print("---", utter)
        print(payload.get("intent"), payload.get("protocol"), payload.get("elapsed_ms"))
        print(payload.get("speech", "")[:500])
        print("tools", [(item["tool"], item["ok"], item["ms"]) for item in payload.get("trace", [])])
        print("cards", [card.get("kind") for card in payload.get("cards", [])])


if __name__ == "__main__":
    main()
