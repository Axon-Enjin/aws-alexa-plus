# Project State: CareSync

**Project slug:** `caresync`
**Owner:** Gerald
**Last updated:** 2026-10-12

---

## 1. Position

| Field | Value |
|-------|-------|
| **Current milestone** | Specify |
| **Entered on** | 2026-10-12 |
| **Exit condition** | Triggered docs exist, Scrutiny is PROCEED WITH FIXES, and the open owner decisions below are either resolved or still marked [FILL] |
| **Next milestone** | Implement |
| **Current blocker** | Docs-only this cycle. Card rendering, a second surface, and the voice latency number are [FILL] |
| **Owner of the next step** | Gerald |

**What we are building, in one line:** A voice care coordinator that remembers one synthetic household's plan across sessions and acts only after the caregiver confirms.

**Engagement type:** product-led (hackathon submission)

**Vault status:** none

---

## 2. Active signals

| Signal | True? | Evidence | Requires |
|--------|-------|----------|----------|
| S1 UI | yes | Simulated Alexa+ web app with on-screen cards (IDEA.md) | DSD |
| S2 Backend and integrations | yes | Self-hosted MCP server, Streamable HTTP, tool list in IDEA.md | SDD |
| S4 Non-trivial behavior | yes | Cross-session brief, plan update, confirmed reorder, visit-prep task | PRD |
| S7 Demo for judges | yes | Recorded simulator session is the submission proof | QAD, PITCH |
| S9 / S10 Health-adjacent data | yes | Medication, appointment, and supply plan, synthetic only | CLR |
| S11 Public repo that will be judged | yes | This repo is the submission tree. Root README.md already exists and stays the track readme | Use README.md; do not replace it |
| S12 Shipping an AI agent | yes | Strands on Bedrock with tools | AIA, PRD §7, SDD §8, QAD, CLR |
| S22 Judges | yes | Alexa+ track stage 2 criteria in HACKATHON.md | PITCH |
| S27 Hackathon time box | yes | Internal demo 2026-10-15; submission 2026-10-23 12:00 PM PT | Minimum template sections |
| S29 Health regulation | yes | Health-shaped records even when synthetic | CLR §7 |

**Deliberate absences** (checked and false):

- S3 / RFC: MCP Apps versus plain cards, and an Agent Skill second surface, are open. Do not pick a path. Both stay [FILL].
- S5 / BUILD: docs-only work with no implementation this cycle.
- S6 / SAD: no multi-agent roster.
- S8 / OPS: no production host this cycle.
- S13 / UES: checkout is simulated. No pricing sheet in this suite.
- S14 / OPP / PROP: no named buyer.
- S15 / BRD: hackathon slice, not a business-requirements cycle.
- S21 / GTM: no distribution this cycle.
- S23 / CHANGE: no code yet.
- WRAP: the event has not ended.
- VALIDATION: deferred. No new caregiver interviews this cycle. The research file is an input, not a validation brief.
- VOICE: not requested. Hard voice bans still apply.

---

## 3. Operating frameworks

| Dimension | Choice | Why |
|-----------|--------|-----|
| **Project management** | milestones | One hackathon slice with a demo date and a submission date |
| **Engineering maturity** | L0 | No application code in the repo |
| **Subagents** | none | One track owner |

---

## 4. Open assumptions

| ID | Assumption | Risk if wrong | Reversible? | Owner | Resolve by |
|----|-----------|---------------|-------------|-------|------------|
| A1 | A simulated Alexa+ web app is an accepted demo path | The submission fails the track rule | no | Gerald | Scrutiny (checked) |
| A2 | Synthetic fixtures are enough for the demo | Judges ask for a live device or live data we do not have | yes | Gerald | Implement |
| A3 | Plain cards are an acceptable fallback if MCP Apps hosting slips | The media-support beat is weaker | yes | Gerald | [FILL] |
| A4 | One MCP server is enough; an Agent Skill is optional | Scope grows past the demo | yes | Gerald | [FILL] |
| A5 | End-to-end voice turn target stays under about 2.5 seconds | The locked number is [FILL]; the demo feels slow | yes | Gerald | [FILL] |
| A6 | Effort has no measured rate | Any hour estimate would be invented | n/a | Gerald | UNCALIBRATED |

**Open questions for the user:**

1. Voice latency locked number: [FILL]
2. Simulator hosts MCP Apps UI, or plain cards: [FILL]
3. Agent Skill as a second surface: [FILL]
4. CLR founder sign-off date: [FILL]
5. License file: [FILL] (not added in this change)

---

## 5. Decisions

| ID | Question | Decision | Evidence class | Review when |
|----|----------|----------|----------------|-------------|
| D1 | What data is in the hackathon build? | Synthetic household only. No real health records. | Project Canonical | Before any non-synthetic data |
| D2 | When may a reorder happen? | Only after an explicit spoken or tapped confirmation. Checkout is simulated. | Project Canonical | Before any real payment |
| D3 | Does the agent give medical advice? | No. It reads the plan and prepares a visit packet. | Human Decision | Before any clinical claim |
| D4 | Which idea doc is canonical for the suite? | `docs/idea-caresync.md`. Root `IDEA.md` stays as the direction note and is not duplicated. | Project Canonical | On the next pivot |

---

## 6. Context exclusions

| Excluded | Reason | Where it lives now |
|----------|--------|--------------------|
| Engine tree | Never commit the engine | Outside this repo |
| Pricing and market-size figures | Leave them in the existing direction and research files. Do not copy them into this suite. | `IDEA.md`, `README.md`, `Alexa-Hackathon-Research-Plan.md` |
| Sponsor financials and public executive names | Existing org note. Not an input to the build. | `ORG.md` |

---

## 7. Next actions

1. Gerald resolves card rendering, the Agent Skill question, and the latency number, or leaves them [FILL] through the demo.
2. Implement only after those decisions. This cycle does not add application code.
3. Record the CLR founder sign-off date. It is [FILL].

**Artifact plan for this slice:**

| Artifact | Why it is justified now | Status |
|----------|-------------------------|--------|
| state.md | Operating position | done |
| idea-caresync.md | Frame. Root IDEA.md remains the direction note | done |
| scrutiny-caresync.md | Gate before the suite | done |
| prd-caresync.md | S4 behavior | done |
| dsd-caresync.md | S1 UI. Exact tokens [FILL] | done |
| sdd-caresync.md | S2 MCP server and tools | done |
| qad-caresync.md | S7 demo proof | done |
| clr-caresync.md | S9, S10, S29 | done |
| aia-caresync.md | S12 agent | done |
| pitch-caresync.md | S22 judges | done |
| VALIDATION | Deferred. No new interviews | not generated |
| RFC, BUILD, OPS, BRD, UES, GTM, WRAP, SAD | Triggers false or do-not-trigger | not generated |

---

## 8. Self-Check

| Check | Done |
|-------|------|
| Milestone and exit condition are current | [x] |
| Every listed signal has real evidence | [x] |
| Every assumption made this session is in §4 | [x] |
| Artifact plan contains no untriggered artifact | [x] |
| Context exclusions updated after any pivot | [x] |
