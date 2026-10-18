# Alexa+

**CareSync Orchestrator** is the build. It is a self-hosted MCP server (protocol 2025-11-25, Streamable HTTP) and a simulated Alexa+ screen for one household: Maya Reyes looking after her mother Elena.

The screen is the demo. Every spoken turn opens an MCP session against `http://127.0.0.1:8080/mcp` and calls tools there. Care state lives in SQLite, not in the MCP session. A reminder or an order is only staged by `propose_action`. `confirm_action` runs it, and refuses when there is no matching confirmation. The rules are in [`caresync/policies/caresync.cedar`](caresync/policies/caresync.cedar).

## Run

```powershell
pip install -r requirements.txt
python -m caresync
```

Open http://127.0.0.1:8080

The hosted simulator is the Vercel app (`app.py`). It runs the same care turns in-process and keeps a yes or an order in a signed cookie, because a Vercel function has no localhost MCP port. `python -m caresync` is the Streamable HTTP server.

Ask “What’s going on with Mom today?”, then “Remind her on the kitchen Show”, then “Yes, send it”. The order path is “Order the usual briefs”, then “Yes, place the order”. Reset puts the household back.

MCP endpoint for any other client: `http://127.0.0.1:8080/mcp`

```powershell
python -m unittest discover -s tests
```

Nothing here calls a paid API. Orders are simulated. This is not a medical device.

## What the agent can do

| Tool | Effect |
|---|---|
| `recall_memory` | Notes from earlier sessions |
| `read_telemetry` | Dispenser, motion, kitchen Show |
| `read_calendar` | Next visit and who is driving |
| `read_routines` | Today’s care steps |
| `check_inventory` | Days left and the usual listing |
| `propose_action` | Stages a Show reminder or an order and returns a confirmation token |
| `confirm_action` | Executes that staged action, or denies it |
| `dismiss_action` | Drops a staged action |
| `get_task` | Polls the reminder or order after a yes |

## Hackathon

Build, Ship, Shape: Amazon Developer Hackathon. Deadline 23 Oct 2026, 12:00 PM PT. Alexa+ track: a self-hosted MCP server (spec 2025-11-25 or later, Streamable HTTP) or an Agent Skill. A simulated Alexa+ web app is the allowed alternative.

The research picked CareSync over CareCart and ClaimFighter. The report’s transaction SOM is about $47.5M. A separate subscription view is about $9M ARR. Those are different claims.

| File | What it is |
|---|---|
| [HACKATHON.md](HACKATHON.md) | Rules and dates |
| [ORG.md](ORG.md) | Amazon, AWS, and device-team context |
| [PROMPT.md](PROMPT.md) | Research prompt for this track |
| [Alexa-Hackathon-Research-Plan.md](Alexa-Hackathon-Research-Plan.md) | Research report and the three pitches |
| [SUBMISSION.md](SUBMISSION.md) | Draft Devpost answers |
| [FRICTION_LOG.md](FRICTION_LOG.md) | Friction log for the judging bonus |

# Alexa+

Track repo for the Amazon Developer Hackathon. This folder is the whole project: rules, sponsor context, the research prompt, and the research report. It does not depend on any other local folder.

- **Hackathon:** Build, Ship, Shape: Amazon Developer Hackathon
- **Deadline:** 23 Oct 2026, 12:00 PM PT
- **Track:** A self-hosted MCP server (spec 2025-11-25 or later, Streamable HTTP) or an Agent Skill. A simulated Alexa+ web app is the allowed alternative.

## Recommended build

**CareSync Orchestrator:** a voice agent that remembers a family care plan and acts on appointments, routines, and the home. Rubric total 33, ahead of ClaimFighter (26) and CareCart (25).

The report's transaction SOM is about $47.5M. A separate subscription view is about $9M ARR. Those are different claims. ClaimFighter becomes the better build only if insurers expose a claims API. The main risks are protected health information and fragmented calendars and devices.

## Docs

| File | What it is |
|---|---|
| [HACKATHON.md](HACKATHON.md) | Full hackathon rules and dates, copied so this repo stands alone |
| [ORG.md](ORG.md) | Amazon, AWS, and device-team goals, copied so this repo stands alone |
| [PROMPT.md](PROMPT.md) | Deep-research prompt for this track |
| [Alexa-Hackathon-Research-Plan.md](Alexa-Hackathon-Research-Plan.md) | Research report and the three pitches |
