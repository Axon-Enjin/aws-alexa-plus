"""Starlette app Vercel runs. Tool calls stay in-process.

Vercel does not give this function a localhost port, so the simulator cannot
open a Streamable HTTP session against itself. The local command
`python -m caresync` still does that.
"""

from __future__ import annotations

import json
from pathlib import Path

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse, JSONResponse
from starlette.routing import Route

from caresync import tools
from caresync.browser_state import cookie_header, current, decode, install, uninstall
from caresync.orchestrator import handle_turn
from caresync.store import household, reset_db

WEB = Path(__file__).resolve().parent / "web"


async def index(_: Request) -> FileResponse:
    return FileResponse(WEB / "index.html")


async def css(_: Request) -> FileResponse:
    return FileResponse(WEB / "app.css", media_type="text/css")


async def js(_: Request) -> FileResponse:
    return FileResponse(WEB / "app.js", media_type="text/javascript")


async def health(_: Request) -> JSONResponse:
    return JSONResponse({"ok": True, "service": "caresync", "transport": "vercel"})


async def board(_: Request) -> JSONResponse:
    return JSONResponse(household())


async def reset(_: Request) -> JSONResponse:
    reset_db()
    return JSONResponse(household())


async def _call_tool(name: str, args: dict) -> dict:
    raw = getattr(tools, name)(**args)
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        return {"ok": True, "value": parsed}
    return parsed


async def turn(request: Request) -> JSONResponse:
    body = await request.json()
    utterance = str(body.get("utterance") or "").strip()
    session_id = str(body.get("session_id") or "maya")
    token = str(body.get("confirmation_token") or "")
    if not utterance:
        return JSONResponse({"speech": "Say that again? I missed it.", "cards": [], "trace": []})
    payload = await handle_turn(
        utterance,
        session_id,
        _call_tool,
        confirmation_token=token,
    )
    payload["protocol"] = "in-process"
    payload["transport"] = "vercel"
    return JSONResponse(payload)


async def task(request: Request) -> JSONResponse:
    task_id = request.path_params["task_id"]
    return JSONResponse(await _call_tool("get_task", {"task_id": task_id}))


class OverlayCookie:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        request = Request(scope, receive)
        token = install(decode(request.cookies.get("caresync")))

        async def send_with_cookie(message):
            if message["type"] == "http.response.start":
                data = current() or decode(None)
                header = cookie_header(data, secure=request.url.scheme == "https")
                headers = list(message.get("headers") or [])
                headers.append((b"set-cookie", header.encode()))
                message["headers"] = headers
            await send(message)

        try:
            await self.app(scope, receive, send_with_cookie)
        finally:
            uninstall(token)


def build_web_app() -> Starlette:
    application = Starlette(
        routes=[
            Route("/", index),
            Route("/assets/app.css", css),
            Route("/assets/app.js", js),
            Route("/api/health", health),
            Route("/api/board", board),
            Route("/api/reset", reset, methods=["POST"]),
            Route("/api/turn", turn, methods=["POST"]),
            Route("/api/task/{task_id}", task),
        ]
    )
    application.add_middleware(OverlayCookie)
    return application


app = build_web_app()
