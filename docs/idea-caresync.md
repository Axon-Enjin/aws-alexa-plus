# Idea Brief (IDEA)

**Project:** CareSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Gerald
**Status:** Draft
**Last reconciled:** N/A (not yet reconciled with reality)
**Event / context:** Amazon Developer Hackathon, Alexa+ track. Internal demo 2026-10-15. Submission 2026-10-23 12:00 PM PT.

---

## 1. The Spark

**One-line pitch:** Ask what is going on with Mom today and get one answer that joins her meds, her next appointment, and what is about to run out.

**Problem:** Adults who already have a job and children also track an aging parent's medications, appointments, and supplies across paper planners and shared notes.

**Insight (why us, why now):** The Alexa+ track allows a simulated web app and a self-hosted MCP server, so a cross-session care plan can be demoed without insurer or pharmacy APIs. The visit-prep paperwork becomes a long-running task instead of a separate product.

**Riskiest assumption:** A judge can see memory across two sessions, a confirmed reorder, and a finished visit packet in a simulated web app before the submission deadline.

---

## 2. Who It's For

**Primary user (named, specific):** Alex Rivera, 41, a working parent who coordinates weekday care for their mother and keeps the plan in notes and texts.

**Their moment of pain:** Thursday morning, before work, Alex asks what is going on with Mom today and has to open the pill list, the calendar, and the supply note separately.

**Success in their words:** "I asked once and it already knew about Thursday at 2 and the pads running out."

---

## 3. Scope & Cut Line

| # | Capability | Core to the one thing? |
|---|------------|------------------------|
| 1 | Cross-session care brief with an on-screen card | YES |
| 2 | Spoken plan update, such as moving the cardiologist to Thursday at 2 | YES |
| 3 | Supply runway and a reorder that waits for an explicit confirmation | YES |
| 4 | Visit Prep Packet as a long-running task with progress | YES |
| 5 | Policy rules that keep the agent inside the caregiver's scope | NO |
| 6 | A second surface besides the MCP server | NO |

**Explicitly out of scope (v0):** Real payments, real insurer or health-record integrations, insurance appeal letters, and any non-synthetic household.

**If we only ship one thing:** Session 2 answers "What's going on with Mom today?" from memory of session 1, with one card on screen.

---

## 4. Success & Judging Criteria

**How we know it worked:** A recorded simulator session shows the four demo beats in IDEA.md without real health data.

| Criterion | How we hit it |
|-----------|---------------|
| Tech Implementation | Self-hosted MCP tools called from the simulator, plus Bedrock and cross-session memory |
| Design | One spoken question, one card, one confirmation |
| Potential Impact | A named caregiver moment, synthetic data only |
| Quality of the Idea | Orchestration across the plan, not a single-turn question bot |

---

## 5. Concept Visuals

No frames exist yet. Do not describe images that are not in the repo.

| Screen / section | Asset path | Decision |
|------------------|------------|----------|
| Care brief card | [FILL] | Not drawn |

---

## 6. Open Questions

| Question | Owner | Resolve by |
|----------|-------|------------|
| Locked voice-latency number | Gerald | [FILL] |
| MCP Apps host in the simulator, or plain cards | Gerald | [FILL] |
| Agent Skill as a second surface | Gerald | [FILL] |
| License file | Gerald | [FILL] |

**Spike plan (optional):** None this cycle. The cheapest test is the demo itself, and this cycle is docs-only.

---

## Self-Check

- [x] Lock bar fields are real, specific, and not placeholders
- [x] Riskiest assumption named; a spike is planned if code is the cheapest test
- [x] Cut line explicit; "If we only ship one thing" named
