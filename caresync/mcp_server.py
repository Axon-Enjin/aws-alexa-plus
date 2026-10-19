"""Streamable HTTP MCP server and the simulated Alexa+ routes."""

from __future__ import annotations

import json
from pathlib import Path

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from starlette.requests import Request
from starlette.responses import FileResponse, JSONResponse

from caresync import tools
from caresync.orchestrator import handle_turn, parse_tool_result
from caresync.store import find_pending, household, init_db, reset_db

WEB = Path(__file__).resolve().parent / "web"
READ_ONLY = ToolAnnotations(readOnlyHint=True, destructiveHint=False, openWorldHint=False)
STAGED = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=False)

INSTRUCTIONS = (
    "CareSync Orchestrator keeps one household care plan: medicines, the next visit, "
    "routines, supplies, and the kitchen Echo Show. Read tools are safe. "
    "propose_action only stages a reminder or an order. confirm_action is the only "
    "tool that sends a reminder or places an order, and it refuses without a matching "
    "confirmation token from the designated caregiver."
)


def build_mcp(port: int) -> FastMCP:
    mcp = FastMCP(
        "CareSync Orchestrator",
        instructions=INSTRUCTIONS,
        host="127.0.0.1",
        port=port,
        streamable_http_path="/mcp",
        stateless_http=False,
        json_response=False,
    )

    @mcp.tool(annotations=READ_ONLY)
    def recall_memory(actor_id: str = "maya-reyes", resident_id: str = "elena-reyes") -> str:
        """Cross-session notes CareSync already has about this household."""
        return tools.recall_memory(actor_id, resident_id)

    @mcp.tool(annotations=READ_ONLY)
    def read_telemetry(actor_id: str = "maya-reyes", resident_id: str = "elena-reyes") -> str:
        """Pill dispenser, motion, fall quiet-period, and whether the kitchen Show is online."""
        return tools.read_telemetry(actor_id, resident_id)

    @mcp.tool(annotations=READ_ONLY)
    def read_calendar(actor_id: str = "maya-reyes", resident_id: str = "elena-reyes") -> str:
        """The next appointment, who is driving, and what is still unfinished."""
        return tools.read_calendar(actor_id, resident_id)

    @mcp.tool(annotations=READ_ONLY)
    def read_routines(actor_id: str = "maya-reyes", resident_id: str = "elena-reyes") -> str:
        """Today's care routine and which steps are still open."""
        return tools.read_routines(actor_id, resident_id)

    @mcp.tool(annotations=READ_ONLY)
    def check_inventory(
        item_query: str = "",
        actor_id: str = "maya-reyes",
        resident_id: str = "elena-reyes",
    ) -> str:
        """Days of each supply left, and the usual listing a caregiver would reorder."""
        return tools.check_inventory(item_query, actor_id, resident_id)

    @mcp.tool(annotations=STAGED)
    def update_appointment(
        weekday: int,
        hour: int,
        minute: int,
        actor_id: str = "maya-reyes",
        resident_id: str = "elena-reyes",
    ) -> str:
        """Save a spoken visit change and read the new time back."""
        return tools.update_appointment(weekday, hour, minute, actor_id, resident_id)

    @mcp.tool(annotations=READ_ONLY)
    def start_visit_packet(actor_id: str = "maya-reyes", resident_id: str = "elena-reyes") -> str:
        """Start a visit-prep packet. Poll get_task until it finishes."""
        return tools.start_visit_packet(actor_id, resident_id)

    @mcp.tool(annotations=STAGED)
    def propose_action(
        kind: str,
        session_id: str,
        actor_id: str = "maya-reyes",
        resident_id: str = "elena-reyes",
    ) -> str:
        """Stage a reminder or an order. Does not execute it. Returns a confirmation token."""
        return tools.propose_action(kind, session_id, actor_id, resident_id)

    @mcp.tool(annotations=STAGED)
    def confirm_action(
        session_id: str,
        confirmation_token: str = "",
        actor_id: str = "maya-reyes",
    ) -> str:
        """Execute a staged action. Refuses unless the token matches and policy allows it."""
        return tools.confirm_action(session_id, confirmation_token, actor_id)

    @mcp.tool(annotations=STAGED)
    def dismiss_action(
        session_id: str,
        confirmation_token: str = "",
        actor_id: str = "maya-reyes",
    ) -> str:
        """Drop a staged action without executing it."""
        return tools.dismiss_action(session_id, confirmation_token, actor_id)

    @mcp.tool(annotations=READ_ONLY)
    def get_task(task_id: str, actor_id: str = "maya-reyes") -> str:
        """Poll a reminder or order task. Running tasks complete after a short delay."""
        return tools.get_task(task_id, actor_id)

    @mcp.resource("care://household/reyes", mime_type="application/json")
    def household_resource() -> str:
        """The Reyes care record the simulator and the tools share."""
        return json.dumps(household())

    @mcp.prompt(name="caresync_brief")
    def caresync_brief(utterance: str = "What's going on with Mom today?") -> str:
        """Instructions for an Alexa+ client driving CareSync."""
        return (
            "You are CareSync on Alexa+, speaking to Maya Reyes about her mother Elena. "
            "Use the CareSync tools. Never invent a dose, a time, or a price. "
            "To remind the kitchen Echo Show or to place an order, call propose_action, "
            "read the confirmation token back, and wait. Call confirm_action only after "
            f"Maya agrees. Her latest utterance: {utterance}"
        )

    mcp_url = f"http://127.0.0.1:{port}/mcp"

    @mcp.custom_route("/", methods=["GET"])
    async def index(_: Request) -> FileResponse:
        return FileResponse(WEB / "index.html")

    @mcp.custom_route("/assets/app.css", methods=["GET"])
    async def css(_: Request) -> FileResponse:
        return FileResponse(WEB / "app.css", media_type="text/css")

    @mcp.custom_route("/assets/app.js", methods=["GET"])
    async def js(_: Request) -> FileResponse:
        return FileResponse(WEB / "app.js", media_type="text/javascript")

    @mcp.custom_route("/assets/supply-brief.png", methods=["GET"])
    @mcp.custom_route("/assets/kitchen-display.png", methods=["GET"])
    async def image(request: Request) -> FileResponse:
        return FileResponse(WEB / request.url.path.rsplit("/", 1)[-1], media_type="image/png")

    @mcp.custom_route("/api/health", methods=["GET"])
    async def health(_: Request) -> JSONResponse:
        return JSONResponse({"ok": True, "mcp": mcp_url, "service": "caresync"})

    @mcp.custom_route("/api/board", methods=["GET"])
    async def board(_: Request) -> JSONResponse:
        return JSONResponse(household())

    @mcp.custom_route("/api/reset", methods=["POST"])
    async def reset(_: Request) -> JSONResponse:
        reset_db()
        return JSONResponse(household())

    @mcp.custom_route("/api/turn", methods=["POST"])
    async def turn(request: Request) -> JSONResponse:
        body = await request.json()
        utterance = str(body.get("utterance") or "").strip()
        session_id = str(body.get("session_id") or "maya")
        token = str(body.get("confirmation_token") or "")
        if not utterance:
            return JSONResponse({"speech": "Say that again? I missed it.", "cards": [], "trace": []})

        async with streamable_http_client(mcp_url) as (read, write, _session_id):
            async with ClientSession(read, write) as session:
                init = await session.initialize()

                async def call_tool(name: str, args: dict) -> dict:
                    result = await session.call_tool(name, args)
                    text = _content_text(result)
                    if result.isError:
                        raise RuntimeError(text or f"{name} failed")
                    return parse_tool_result(text)

                payload = await handle_turn(
                    utterance,
                    session_id,
                    call_tool,
                    confirmation_token=token,
                )
        payload["protocol"] = str(init.protocolVersion)
        payload["transport"] = "streamable-http"
        payload["household"] = household()
        pending = find_pending(session_id)
        payload["pending_action"] = {"token": pending["token"], "kind": pending["kind"]} if pending else None
        return JSONResponse(payload)

    @mcp.custom_route("/api/task/{task_id}", methods=["GET"])
    async def task(request: Request) -> JSONResponse:
        task_id = request.path_params["task_id"]

        async with streamable_http_client(mcp_url) as (read, write, _session_id):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("get_task", {"task_id": task_id})
                text = _content_text(result)
        return JSONResponse(parse_tool_result(text))

    return mcp


def build_app(port: int = 8080):
    init_db()
    return build_mcp(port).streamable_http_app()


def _content_text(result) -> str:
    parts: list[str] = []
    for block in result.content or []:
        text = getattr(block, "text", None)
        if text:
            parts.append(text)
    return "\n".join(parts)
