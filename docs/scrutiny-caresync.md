# IDEA Scrutiny Gate (SCRUTINY)

**Project:** CareSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Gerald
**Status:** Draft
**Last reconciled:** N/A (not yet reconciled)
**IDEA:** [idea-caresync.md](idea-caresync.md). Direction note: [IDEA.md](../IDEA.md).

---

## 1. Verdict

**Decision:** PROCEED WITH FIXES

**One-line rationale:** The lock bar names a person, a Thursday-morning scene, and one shippable card. Nothing load-bearing is contradicted. The open product choices stay [FILL] and do not block the docs.

**If PROCEED WITH FIXES, items carried into the build:**

- PRD §7 and SDD §7: voice latency number is [FILL]. The "about 2.5 seconds" line in the direction note is an unverified target, not a lock.
- DSD and SDD §4: MCP Apps versus plain cards is [FILL]. Do not pick a host.
- PRD §3: Agent Skill second surface is Could-Have and [FILL].
- CLR §7: founder sign-off date is [FILL]. Posture is recorded anyway.
- Effort on every plan row is UNCALIBRATED.
- VALIDATION is deferred. No new caregiver interviews this cycle. Market figures in the research file stay Unverified.

---

## 2. Claim & Reference Audit

**Coverage:** Claims extracted: 6; load-bearing: 4; verified: 2; unverified: 4; contradicted: 0.

| # | Category | Claim (from IDEA) | Finding | Source (required if Verified) | Severity if wrong |
|---|----------|-------------------|---------|-------------------------------|-------------------|
| FC-1 | Problem | A working parent tracking a parent's meds, visits, and supplies is the user | Unverified; needs check | Research file is an input, not a checked study | Significant |
| FC-2 | Solution | A simulated Alexa+ web app is an allowed demo path | Verified | https://amazonappdev2026.devpost.com/ and HACKATHON.md §4 (2026) | Fatal |
| FC-3 | Technical | The track accepts a self-hosted MCP server on Streamable HTTP, spec 2025-11-25 or later | Verified | https://amazonappdev2026.devpost.com/ and HACKATHON.md §4 (2026) | Fatal |
| FC-4 | Market/Competitor | Research rubric totals and market-size figures | Unverified; needs check | Pasted research. Not re-checked. Figures are not copied here | Minor |
| FC-5 | Technical/Feasibility | Cross-session memory plus a minutes-long visit packet can be shown by the internal demo date | Unverified; needs check | No spike this cycle | Significant |
| FC-6 | Insight | Folding reorder and visit prep into one coordinator is a better demo than three products | Unverified; needs check | Direction note only | Minor |

### 2.1 References Integrity

| # | Reference | Backs claim | Resolves? | Supports it? | Finding |
|---|-----------|-------------|-----------|--------------|---------|
| R-1 | HACKATHON.md and https://amazonappdev2026.devpost.com/ | FC-2, FC-3 | Yes | Yes | Verified |
| R-2 | Alexa-Hackathon-Research-Plan.md | FC-1, FC-4 | Yes, file is in the repo | Partly | Unverified |
| R-3 | IDEA.md demo script | FC-5, FC-6 | Yes | Partly | Unverified |
| R-4 | PROMPT.md, ORG.md | none load-bearing | Yes | No | Unverified |

---

## 3. Gap Analysis

| # | Missing input | Needed by (doc) | Blocker or TBD |
|---|---------------|-----------------|----------------|
| G-1 | Locked voice latency number | PRD §7, SDD §7 | TBD [FILL] |
| G-2 | MCP Apps host versus plain cards | DSD, SDD §4 | TBD [FILL] |
| G-3 | Agent Skill in or out | PRD §3 | TBD [FILL] |
| G-4 | Founder sign-off date | CLR §7 | TBD [FILL] |
| G-5 | Direct caregiver interviews | VALIDATION, not generated | TBD |
| G-6 | License file | repo root | TBD [FILL] |
| G-7 | Measured effort rate | PRD §9 | UNCALIBRATED |
| G-8 | Exact color, type, and logo tokens | DSD §2 | TBD [FILL] |

---

## 4. Assumption Stress-Test

**Load-bearing assumption:** A judge can see cross-session memory, a confirmed reorder, and a finished visit packet in a simulated web app before submission.

**Strongest argument against it:** The new MCP Tasks and Apps surfaces, plus memory setup, may not fit before 2026-10-15, and a simulated front end may look unofficial next to a device demo.

**Does it hold?** Holds with caveat. The rules allow the simulated path (FC-2). The schedule risk is real and unverified (FC-5). It is not contradicted.

**Cheapest test:** The internal demo on 2026-10-15. No spike this cycle because the cycle is docs-only.

### 4.1 Audience / 10-second stress

| Check | Finding |
|-------|---------|
| Stranger hook: who hurts and why, in 10 seconds, without slides | Pass. A working parent, Thursday morning, three lists for one parent. |
| Named user and pain present in IDEA §2 | Pass. Alex Rivera, Thursday morning. |
| One-liner repeatable (not generic SaaS) | Pass. One question, meds plus visit plus supplies. |
| Why not keep coping with the status quo? | Pass. The status quo is the three lists. The product joins them and waits for confirmation before it buys. |

**Audience verdict:** Holds. The scene is specific enough to demo.

---

## 5. Feasibility & Scope

| Check | Finding |
|-------|---------|
| "If we ship only one thing" is shippable in the window | The one card is smaller than the four-beat demo. The four-beat script is the goal. Schedule is unverified. |
| Production-grade reachable (security, data, rollback) | Not this cycle. Demo fixtures, simulated checkout, no production host. |
| Cut line honest, not hiding work | Real payments, records integrations, and appeal letters are out. Card host and Agent Skill are [FILL], not silent scope. |

---

## 6. Risk & Regulatory Pre-flight

| Flag | Present? | Pulls in |
|------|----------|----------|
| Collects user data / PII | Y | CLR §1, §3. Operator voice and a synthetic household. |
| Children, health, payment, biometric, or precise-location data | Y | CLR §3. Health-shaped fixtures. No real payments. No precise location. |
| Regulated activity (license, franchise, permit, sector rule) | Y | CLR §7. Health-adjacent records. Posture recorded. Not a block. |
| AI component with untrusted input or tools | Y | SDD §8.1, QAD red-team, AIA |
| Security-critical paths (auth, money, deletes) | Y | SDD §5, QAD abuse paths. Confirmation gate. No real money. |
| Public deploy | N | The repo will be public. The demo is not a production host. OPS stays out. |

---

## 7. Blocking Questions

None. Verdict is not DO NOT BUILD YET.

---

## Self-Check

- [x] Verdict matches the findings; DO NOT BUILD YET names a fatal flaw (1, 2, or 3)
- [x] Coverage line filled; every load-bearing claim has a row
- [x] No Verified row without a source
- [x] §2.1 audits every reference cited in the IDEA (or states there are none)
- [x] §4.1 filled, even in Quick Mode
- [x] §6 flags name the docs they pull in; regulatory flags route to CLR §7, not to §7 here
- [x] On PROCEED WITH FIXES, every fix names the doc it lands in
