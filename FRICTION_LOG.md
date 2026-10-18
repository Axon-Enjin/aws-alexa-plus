# Friction log

Entries from building CareSync against the Alexa+ rules. Each one is a task, what we expected, what happened, and what would have unblocked it.

## 1. Streamable HTTP on the same process as the demo UI

- Task: one command that serves the MCP endpoint and the simulator.
- Steps: construct `FastMCP`, add HTTP routes, return `streamable_http_app()`, have the turn handler open `streamable_http_client` against itself.
- Expected: a documented way to mount Streamable HTTP inside an existing app, and a client call that does not deadlock the worker serving it.
- Actual: the session manager has to be created via `streamable_http_app()` and kept alive with its lifespan. A turn that calls back into the same server only works because the client await yields the event loop. That is easy to get wrong and easy to deadlock.
- Severity: High
- Workaround: keep tools as plain functions, register them on FastMCP, and call them through the official client from the request handler.
- Suggestion: a one-page “Streamable HTTP plus your own routes” sample that shows the lifespan and a same-process client.

## 2. Protocol version the research assumed vs the SDK that ships

- Task: implement the stateless 2026-07-28 behaviors called out in the track research (no session affinity, confirmation payload, external state).
- Steps: install `mcp`, read `LATEST_PROTOCOL_VERSION`.
- Expected: the SDK would negotiate the revision the research described.
- Actual: the installed SDK’s latest version is `2025-11-25`. Care state is external (SQLite) and confirmation is an explicit tool result, which is the behavior we needed, but it is not the later spec’s wire format.
- Severity: Medium
- Workaround: target 2025-11-25, which is the floor the hackathon rules name, and keep confirmation in tool results.
- Suggestion: publish which protocol versions the Alexa+ simulator will send, in one table, next to the rules.

## 3. Installing the MCP SDK next to an older FastAPI

- Task: `pip install mcp` on a machine that already had FastAPI 0.115.
- Expected: a clean install.
- Actual: pip reported that the MCP SDK’s Starlette does not satisfy FastAPI 0.115 (`starlette<0.47`). The CareSync app does not import FastAPI, so the demo still runs, but the resolver warning looks like a broken environment.
- Severity: Low
- Workaround: run CareSync from its own requirements file. Do not import the old FastAPI app.
- Suggestion: state the Starlette range in the MCP server quickstart so it doesn’t look like an accident.

## 4. DNS rebinding defaults on localhost

- Task: point a client at `http://127.0.0.1:8080/mcp`.
- Expected: localhost would be allowed without extra security settings.
- Actual: FastMCP turns on DNS-rebinding protection for localhost and only allows specific host and origin patterns. A client that sends a different Host fails closed.
- Severity: Medium
- Workaround: bind `127.0.0.1` and call that exact host.
- Suggestion: when the check fails, name the header and the allow-list in the response body.

## 5. No Alexa+ add-on toolkit for participants

- Task: demo an Echo Show card and a confirmation on something a judge recognizes as Alexa+.
- Expected: the Category SDK, MCP toolkit, or web simulator mentioned around Alexa+ would be usable.
- Actual: the hackathon rules say those tools are gated and not available. Teams build their own front end.
- Severity: High
- Workaround: a local simulator that still drives a real MCP server, with cards for the visit, the missed dose, and the confirm step.
- Suggestion: ship a minimal public simulator that attaches to a participant MCP URL, even if the rest of the add-on SDK stays gated.
