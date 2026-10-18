# CareSync submission notes

Draft for the Devpost form. Replace the video URL before submitting.

## Text description

CareSync is an Alexa+ add-on for a family caregiver. Maya Reyes asks, in one breath, what is going on with her mother today. The agent reads the pill dispenser, tomorrow’s cardiology visit, the kitchen Echo Show, and notes from the day before, then answers in a sentence and puts the same facts on screen as cards.

It does not send a reminder or place an order on its own. Those actions are staged by an MCP tool and executed only after Maya confirms. The boundary is a Cedar policy: execution is forbidden unless the designated caregiver has confirmed that specific action.

## How it works

- MCP server, Streamable HTTP, protocol 2025-11-25, at `/mcp`.
- The simulator at `/` is the Alexa+ stand-in. Each turn is an MCP client session that calls the tools. The repo imports the official MCP SDK and calls it at runtime.
- Household state is SQLite, keyed outside the protocol session, so a later question still knows what Maya confirmed.
- Wallet checkout and the Echo Show are simulated. No charge is made.

## Product feedback

### Model Context Protocol (Python SDK, Streamable HTTP)

- Used for: the whole tool surface (care record, staged actions, task poll).
- What worked: `FastMCP` served Streamable HTTP, and `streamable_http_client` plus `ClientSession` completed initialize and `tools/call` from the simulator.
- What needs work: the SDK that negotiates 2025-11-25 is a different shape from write-ups of a later stateless revision. Session handling and DNS-rebinding defaults take a day to learn, and they fail closed with little explanation.
- Onboarding, zero to hello world: the docs get a stdio server up quickly. Streamable HTTP plus a second app on the same port is where the time went.
- Build again: yes. The tool boundary is the right place to keep a confirmation gate.

### Alexa+ simulated client

- Used for: the judge-facing demo, because the gated Alexa+ add-on toolkit is not available to participants.
- What worked: a web screen can show the multi-step confirm path clearly.
- What needs work: a public, local simulator profile that already speaks Streamable HTTP the way the real Alexa+ client will, so teams stop guessing headers.
- Build again: yes, as the demo surface. The product itself wants a real Echo Show.

## Tracks

- Primary: Alexa+
- Mini-challenge fit: Open Source (this repo, MIT). AWS Builder is not claimed — the demo does not call Bedrock or AgentCore at runtime. The Cedar file is the policy those services would load later.

## Testing instructions

See the Run section in README.md. No login. Reset the household from the page if a previous order is still on the board.
