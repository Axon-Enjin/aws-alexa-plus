"""Exercise the Vercel Starlette app, including the cookie that carries an order."""

import tempfile
from pathlib import Path

from starlette.testclient import TestClient

import caresync.store as store

store.DB_PATH = Path(tempfile.mkdtemp()) / "care.db"

from caresync.web_app import app  # noqa: E402

client = TestClient(app)
status = client.post("/api/turn", json={"utterance": "What's going on with Mom today?", "session_id": "web"})
print(status.status_code, status.json()["transport"])
print(status.json()["speech"][:180])
order = client.post("/api/turn", json={"utterance": "Order the usual briefs", "session_id": "web"})
print("order", order.status_code, order.json()["speech"][:160])
yes = client.post("/api/turn", json={"utterance": "Yes, place the order", "session_id": "web"})
print("yes", yes.status_code, yes.json()["speech"][:180])
board = client.get("/api/board").json()
briefs = next(item for item in board["supplies"] if item["id"] == "briefs")
print("days", briefs["days_left"])
