# AI Assurance Dossier (AIA)

**Project:** CareSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Gerald
**Status:** Draft
**Last reconciled:** N/A (not yet reconciled with reality)

---

## 0. Trigger and Scope

| Field | Value |
|-------|-------|
| AI component (PRD §7) | Care coordinator that turns speech into tool calls and a short reply |
| Realizing feature ID(s) | PRD-F1, PRD-F2, PRD-F3, PRD-F4 |
| System boundary | Simulator, Strands agent, Bedrock model, MCP tools, fixture files, session memory |
| Autonomy level | Reads tools on its own. Writes a reorder only after a human yes the server already stored. Does not change a dose |
| Provisional risk classification (awareness) | Not a clinical device. Not an automated decision about benefits. CLR-P3 records the product rule. A formal regime label is [FILL] |

---

## 1. Model / System Card

### 1.1 Intended use

| Field | Value |
|-------|-------|
| Intended use | Answer one caregiver about one synthetic household, update a visit from speech, hold a reorder for confirmation, and assemble a visit packet |
| Intended users / affected parties | The operator playing Alex. The parent in the fixture is not a real person |
| Out-of-scope / prohibited uses | Medical advice, dose changes, real purchases, real health records, other households |
| Human-in-the-loop points | Explicit yes before a placed reorder. Read-back on a plan update |

### 1.2 Model(s) and data

| Model / stage | Identifier + version | Role | Data it sees |
|---------------|----------------------|------|--------------|
| Reply and tool choice | [FILL] | Turn the utterance into tool calls and a short reply | Utterance, tool results, fixture plan |

- **Training / tuning data:** Provider base model. No fine-tune in this cycle.
- **Run-time input:** Caregiver utterance (untrusted) and fixture text (untrusted). Tool results are data, not new instructions.
- **Output contract:** Short reply plus card fields taken from tool results. Invalid or extra clinical content is dropped and the reply says it could not confirm that fact.
- **Provider data terms:** [FILL]. Reconcile with CLR §1 before any real subject.

### 1.3 Limitations and performance caveats

- The model can mis-hear a time. The read-back is the check. A silent save is a failure.
- **Known failure modes:** Invented dose, reorder without yes, reading the other household, medical advice.
- **Fallback behavior:** Spoken error and the last stored card. No invented fact.

---

## 2. NIST AI RMF Risk Register

| Risk ID | Risk | RMF function | GenAI category | Severity | Likelihood | Mitigation (SDD ref) | Eval (QAD ref) | Owner | Status |
|---------|------|--------------|----------------|----------|------------|----------------------|----------------|-------|--------|
| AIA-R1 | Utterance or fixture text instructs a tool | Manage | Information security | High | Medium | SDD §8.1 LLM01. Server owns confirmation | AI-04 | Gerald | Open |
| AIA-R2 | Reply adds a dose or a time | Measure | Confabulation | High | Medium | Facts only from tools. SDD §8.1 hallucination row | AI-01 | Gerald | Open |
| AIA-R3 | Reorder placed without a human yes | Manage | Excessive agency | High | Medium | Server rejects unconfirmed writes | AI-05 | Gerald | Open |
| AIA-R4 | Other household spoken back | Manage | Sensitive information | High | Low | Household check on every tool | AI-06 | Gerald | Open |

**Govern:** Gerald reviews this register when the model id is chosen and again before the recording. Cadence after that is [FILL].

---

## 3. SMACTR Self-Audit Checklist

Skipped until a production launch or an external assessment. The demo evidence is §1, §2, and the QAD red-team rows.

**Residual-risk statement:** With fixtures and a server-side confirmation, the remaining risk is a bad read-back or a slow turn. Latency is [FILL]. Real health data is out of scope (CLR-P2).

---

## 4. Cross-links and Escalation

| Dimension | Lives in | This AIA relies on |
|-----------|----------|--------------------|
| AI architecture and threat surface | SDD §8 / §8.1 | Tool list, confirmation rule, fallback |
| Red-team and abuse evals | QAD §7 | AI-01 through AI-07 |
| Data and regulatory posture | CLR §1, §7 | CLR-P1, CLR-P2, CLR-P3 |
| Untrusted input | SDD §8.1 trust boundary | Utterance and fixtures are data |

### Safety bars

| Flag | Present? | Bar we meet | Met? |
|------|----------|-------------|------|
| Output affects a person's rights, access, credit, employment, or benefits | No | Human review and a reason the person can see | n/a |
| Automated decision with significant effect | No | Human review before the decision | n/a. Reorder waits for yes |
| Health, safety, biometric, or other sensitive inference | No real subject | Explicit consent, conservative threshold, human fallback | n/a for the fixture. Required before real records |
| Data with unresolved provenance, licensing, or consent | Provider terms [FILL] | Resolve terms or do not send real data | Met for fixtures. Open for a later real subject |
| Untrusted input reaches tools or other users | Yes | Input labeled untrusted. Tool calls validated. Red-team not yet run | Control is specified. Eval is not yet run |

**Regulatory rows raised here:** CLR-P1, CLR-P2, CLR-P3.

---

## Self-Check

- [x] Scope names the features and the autonomy limit
- [x] Model id stays [FILL]
- [x] Risks point at SDD controls and QAD evals
- [x] Unrun evals are marked open
