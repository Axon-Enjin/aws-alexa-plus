# IDEA: CareSync

## The idea
CareSync is a voice-first care coordinator for the "sandwich generation": adults managing an aging parent's medications, appointments, and supplies on top of their own job and kids. It is a self-hosted MCP server plus an agent that remembers the family's care plan across sessions and acts on it. The user asks "What's going on with Mom today?" and gets one answer that joins pill-dispenser adherence, tomorrow's cardiology appointment, and low supplies, with an Echo Show style card on screen and a suggested next action.

The core is cross-session care orchestration (the CareSync pitch). Two other pitches are folded in as features that make it formidable:
- **Supply runway and reorder (from CareCart).** CareSync tracks supply usage, warns "four days of pads left", and prepares a reorder. Nothing is bought without an explicit spoken or tapped confirmation through an MCP elicitation step. Checkout is simulated in the demo.
- **Long-running paperwork tasks (from ClaimFighter).** Using the MCP Tasks extension, CareSync runs background jobs that take minutes, starting with a **Visit Prep Packet**: current medication list, adherence summary, recent symptoms, and questions for the doctor, ready before the appointment. Caregivers in the research say every appointment asks for the medication list. Insurance appeal drafting reuses the same task pattern later.

## Why this direction won
- **Highest rubric score.** Research matrix: CareSync 33, ClaimFighter 26, CareCart 25. It leads on Design and Strategic fit and ties on Tech Implementation.
- **Hits the CREATIVE list directly.** The rules reward "agentic workflow orchestrating across services", "context-aware add-on with state across sessions", "purchasing", "media support (cards, carousels)", and "MCP Apps". CareSync with the folded features touches all of them. CareCart alone is called OBVIOUS (a wrapper around a shopping API).
- **ClaimFighter is better as a feature than a product.** Standalone, it carries legal and medical advice liability and depends on insurer APIs that do not exist. Its strongest technical idea, the async MCP task, is kept and pointed at a safer job first.
- **Demo-able by Oct 15.** Every external system (pill dispenser, calendar, catalog) is simulated with JSON fixtures, which the Alexa+ track explicitly allows through the simulated Alexa+ web app path.

## Ideas dropped or deferred
- Real Amazon Wallet payments and real insurer or EHR integrations: simulated only.
- Insurance appeal letters: deferred until after the hackathon (liability, citation hallucination risk).
- Philippine nurse human-in-the-loop fallback: business model note, not in the demo.
- Subscription-management pivot: kept only as the research's contingency if health-adjacent agents are blocked.

## Problem
63M US family caregivers spend about 27 hours a week on care work and about $7,200 a year out of pocket, tracking meds and appointments in paper planners and shared Google Docs. Source: Alexa-Hackathon-Research-Plan.md, sections 1 to 2.

## Suggested stack
- **MCP server:** self-hosted, Streamable HTTP, on the 2026-07-28 MCP spec (stateless core, Tasks and MCP Apps extensions; Tier 1 TypeScript and Python SDKs support it). The track minimum is 2025-11-25, so fall back to it if an SDK feature is missing. Tools such as `get_care_brief`, `get_adherence`, `list_appointments`, `get_supply_runway`, `prepare_reorder` (needs confirmation), `start_visit_packet` (task).
- **Agent:** Strands Agents SDK on Amazon Bedrock (Claude or Nova), with Bedrock AgentCore Memory for cross-session state. Stretch: AgentCore Policy (Cedar) rules so the agent cannot read or act outside the caregiver's scope.
- **Front end:** a simulated Alexa+ web app with voice in and out (browser speech or Amazon Polly and Transcribe) and Echo Show style cards and carousels, ideally rendered as MCP Apps UI.
- **Data:** synthetic household only (one parent, five meds, two appointments, three supplies). No real PHI anywhere.

## Demo (target by Oct 15, 2026)
A recorded web-simulator session across two conversations:
1. Session 1: "Mom's cardiologist moved to Thursday at 2." CareSync updates the plan and confirms.
2. Session 2, later (new session, memory proves continuity): "What's going on with Mom today?" Answer joins the missed morning dose, Thursday's appointment, and a four-day supply runway, with a card on screen.
3. "Reorder the pads." The confirmation card appears; the user says yes; simulated order placed.
4. "Get me ready for Thursday." A Visit Prep Packet task starts, shows progress, and the finished packet appears as a card.

## Hackathon fit
- **Track:** Alexa+ (self-hosted MCP server, demoed through our own front end; the repo must import and call MCP at runtime).
- **Mini challenges:** AWS Builder (Bedrock, AgentCore Memory, Strands, optionally Cedar policy). Open Source (release the caregiver MCP server or the Tasks plus confirmation pattern as a template).
- **Friction log:** building on a brand-new spec revision, Tasks and MCP Apps extensions, AgentCore Memory setup.

## Business context
- **Owner:** Axon Enjin. Track main: Gerald.
- **Hackathon:** Build, Ship, Shape: Amazon Developer Hackathon (see HACKATHON.md). Submission closes Oct 23, 2026, 12:00 PM PT (Oct 24, 3:00 AM PHT). Internal demo deadline: Oct 15, 2026.
- **Go-to-market after the hackathon:** US family caregivers on Alexa devices at about $9.99/month, plus a B2B2C path through home-care agencies. The research quotes two different sizes (about $9M ARR subscription view, about $47.5M transaction view); they are separate claims and both are estimates.
- **Constraints:** health-adjacent data means HIPAA awareness from day one: synthetic data only in the hackathon, no medical advice, human confirmation before any purchase or plan change.
- **Source research:** [Alexa-Hackathon-Research-Plan.md](Alexa-Hackathon-Research-Plan.md), [PROMPT.md](PROMPT.md), [HACKATHON.md](HACKATHON.md), [ORG.md](ORG.md).

## Open questions
- Voice latency: keep end-to-end turns under about 2.5 s; pick the Bedrock model accordingly.
- MCP Apps rendering in our own simulator: build the host side ourselves or render plain cards if time runs short?
- Do we add an Agent Skill as a second surface, or keep the scope to one MCP server?
