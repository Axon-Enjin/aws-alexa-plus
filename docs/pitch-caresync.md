# Pitch and Demo (PITCH)

**Project:** CareSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Gerald
**Status:** Draft
**Last reconciled:** N/A (not yet reconciled with reality)
**IDEA:** [idea-caresync.md](idea-caresync.md)

---

## 1. Narrative Spine

**Hook (first 10 seconds):** Alex is late for work and still does not know if Mom took the morning dose, if the cardiologist is still Thursday, or if the pads will last the week.

**Problem (15 seconds):** Those three facts live in three places. Every visit starts by asking for the medication list again.

**Solution (20 seconds):** Ask what is going on with Mom today. One reply joins the dose, the visit, and the supply, and a card shows the same facts. Memory holds the plan across sessions.

**Proof (demo tease):** First Alex moves the cardiologist to Thursday at 2. Later, a new session already knows. Then a reorder waits for a yes. Then a visit packet finishes in the background.

**Differentiation (10 seconds):** This is not a single question and a single answer. It keeps the plan, it will not buy without a yes, and it does the pre-visit list as a task.

**Ask / close:** We are submitting this to the Alexa+ track: a self-hosted server, a simulated web app, and a synthetic household.

---

## 2. Slide / Scene Outline

| # | Scene | On screen | Speaker says | Duration |
|---|-------|-----------|--------------|----------|
| 1 | The morning | Alex, three lists | "Thursday morning, three places to check." | 15s |
| 2 | The product | One card, three facts | "One question. Dose, visit, supply." | 20s |
| 3 | Demo | Simulator | The four beats below | 90s |
| 4 | The rule | Confirmation card | "It does not buy until you say yes. The household is synthetic." | 15s |
| 5 | Close | Track line | "Self-hosted server, simulated app, memory across two sessions." | 15s |

**Total time:** about 2 minutes 35 seconds, under the 3 minute video limit.

---

## 3. Live Demo Script

**Pre-flight:** Fixture household loaded. Two sessions available. No real person's data on screen.

**Demo path (happy path only):**

1. Session 1: "Mom's cardiologist moved to Thursday at 2." The reply repeats Thursday at 2.
2. Session 2: "What's going on with Mom today?" The reply and the card join the missed morning dose, Thursday at 2, and a four-day supply.
3. "Reorder the pads." The confirmation card appears. The user says yes. The reply says the simulated order was placed.
4. "Get me ready for Thursday." Progress shows. The packet card lists meds, adherence, notes, and questions.

**Fallback if live fails:** Play the recorded capture of the same four beats.

**Do not demo:** A second household, an error state, settings, or any screen that implies a real purchase or a real clinic.

---

## 4. Judging Criteria Map

Stage 2 criteria from the track rules, equal weight.

| Official criterion | Where we address it | Evidence |
|--------------------|---------------------|----------|
| Tech Implementation | Scene 5 and demo steps 1 to 4 | Self-hosted server called from the simulator. Memory across two sessions. A task with progress. Bedrock agent. |
| Design | Scene 2 and the confirmation card | One question, one card, one yes. |
| Potential Impact | Scene 1 | A specific weekday-morning caregiver. Synthetic data, so the claim stays inside the demo. |
| Quality of the Idea | Scene 4 | Orchestration across the plan, a purchase that waits, and a pre-visit list. Not a single-turn bot. |

Pass/fail viability: the project uses the track's server path and shows it in the video. Friction worth naming in the log: new spec surface, tasks, cards, and memory setup. Bonus wording is up to the judges.

---

## 5. Production Readiness Gate (pre-demo)

**Gate status:** Not run. The recording has not been made.

**Blockers and N/A items:** Visual tokens [FILL]. Latency number [FILL]. Card host [FILL]. No production host, so production rollout is n/a. User-protection bars for a real subject are out of the demo (see the posture note). Synthetic data and the confirmation rule are the demo bars.

---

## 6. Anticipated Q&A

| Likely question | Short answer |
|-----------------|--------------|
| Is this a real clinic or a real order? | No. One synthetic household. The reorder is simulated and waits for a yes. |
| Why not a single question bot? | The second session has to remember Thursday at 2 without being told again. |
| Where do the cards come from? | The server returns the facts. Whether the simulator hosts rich cards or plain cards is still open. |

---

## Self-Check

- [x] Spine names the person and the pain
- [x] Demo path matches the direction note
- [x] Every stage 2 criterion has a scene
- [x] No internal ids, no engine name, no unfilled template braces
