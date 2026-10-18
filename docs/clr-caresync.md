# User Protection and Regulatory Posture (CLR)

**Project:** CareSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Gerald
**Status:** Draft
**Last reconciled:** N/A (not yet reconciled with reality)

---

## 0. Target Markets

The hackathon demo is a recording, not a launched service. Markets below are the ones the team would hit if the demo later became a product. Nothing here is a launch decision.

| Region | In scope? | Notes |
|--------|-----------|-------|
| Philippines (Data Privacy Act 2012, RA 10173) | No for the demo | Team context only. No Philippine users in the demo |
| European Union / UK (GDPR / UK GDPR) | No for the demo | No EU or UK users |
| California, USA (CCPA / CPRA) | No for the demo | The story is a US caregiver. No California resident data is collected |
| Other: United States, synthetic demo | Yes | One fixture household. No real data subject |

**Geo-blocking:** None, because the demo is not a public service. A later public host is [FILL].

---

## 1. Data Inventory / Record of Processing

| Activity | Purpose | Data categories | Data subjects | Recipients / sub-processors | Cross-border transfer | Retention | Legal basis |
|----------|---------|-----------------|---------------|-----------------------------|-----------------------|-----------|-------------|
| Fixture plan | Drive the demo | Synthetic meds, visits, supplies | None. The household is fictional | Model provider sees the fixture text | [FILL] region | Until the fixture file changes | Not personal data |
| Caregiver utterance | Run the turn | Speech or typed text of the operator | The person running the demo | Model provider | [FILL] | Not stored beyond the demo session, except a local debug log [FILL] | Demo operation |
| Cross-session memory | Remember the plan | Fixture facts and the spoken update | None real | AgentCore Memory | [FILL] | Demo lifetime | Not personal data while fixtures stay synthetic |
| Simulated reorder | Show confirmation | Supply id and held or placed | None real | None. No payment processor | None | Fixture file | Not a sale |

**Sensitivity flags:**

| Data type | Collected? |
|-----------|-----------|
| Basic PII (name, email) | No real name or email. Display labels are synthetic |
| Special-category (health, biometric, genetic, race, religion, sexuality, politics, union) | No real health data. The fixture is shaped like a medication list |
| Children's data | No |
| Precise location | No |
| Photos / camera / microphone | Yes, microphone, if the operator uses voice. Storage [FILL] |
| Device or advertising IDs | No |
| Analytics / telemetry | Demo events only. Tool [FILL] |
| Payment / card data | No. Checkout is simulated |

---

## 2. Multi-Jurisdiction Obligations Matrix (awareness)

Not filled. No region in §0 is in scope for a real data subject. If that changes, add posture rows before any real user.

**Sector rules:** Health-adjacent demo. No medical license is claimed. HIPAA program for real records is CLR-P2, deferred.

---

## 3. User-Protection Bars (non-negotiable)

| Flag | Present? | Bar we meet | Met? | Evidence |
|------|----------|-------------|------|----------|
| Any personal data | No real subject | Minimized collection; access and delete path; secrets never in code; least privilege | Yes for the demo | Fixture-only inventory in §1 |
| Any personal data | No real subject | Breach runbook | Not required while no real subject exists | Revisit with CLR-P2 |
| Children's data | No | Age gate and no profiling of minors | n/a | Out of scope |
| Health / biometric / other special category | Shape only, no real subject | Explicit opt-in; encrypted at rest and in transit; access logged; deletion path | Yes for the demo, because there is no real subject. No for a later real record | IDEA data rule: synthetic only |
| Payments / card data | No | No card numbers stored | Yes | PRD-F7 is Won't-Have. Reorder is simulated |
| Precise location | No | Opt-in if it ever appears | n/a | Not collected |
| Automated decisions with significant effect | No | Human yes before a reorder | Yes | PRD-F3. The agent does not change a dose |
| Tracking / ad-tech / profiling | No | Opt-out if it ever appears | n/a | Not collected |

A later build that stores a real medication list fails the health bar until encryption, access logs, deletion, and an explicit opt-in exist. That build is out of this cycle.

---

## 4. Terms of Use / EULA Readiness

Not this cycle. No public user account.

---

## 5. IP Infringement & Protection Readiness

| Item | Status | Counsel before |
|------|--------|----------------|
| Name and brand search | [FILL] | Before any brand spend |
| Open-source license file | [FILL]. Not added in this change | Before a public release that needs a license |
| Third-party fonts and audio | [FILL] with the design tokens | Before shipping assets |
| Model output ownership | [FILL] with the provider terms | Before any real user |

---

## 6. App Store / Platform Compliance

Not shipping to an app store in this cycle.

| Item | Status |
|------|--------|
| Apple privacy label | n/a |
| Google Play data safety | n/a |
| Third-party SDK disclosure | Bedrock and the MCP server. A store form is n/a |

---

## 7. Regulatory Posture Register

The founder owns every posture. The sign-off date is [FILL]. Recording the row is not the signature.

| ID | Obligation | Applies because | Exposure | Enforcement reality | Posture | Rationale | Revisit when | Kill switch / fallback | Owner | Counsel before |
|----|-----------|-----------------|----------|---------------------|---------|-----------|--------------|------------------------|-------|----------------|
| CLR-P1 | Do not collect real health data in the hackathon | The demo uses medication-shaped records | A real record would be a health-data event | Hackathon rule and user-protection bar | COMPLY | Synthetic fixtures are cheap and protect people | Before any non-synthetic health data | Delete the non-synthetic payload and stop the demo | Gerald, date [FILL] | Before any real record |
| CLR-P2 | HIPAA-style program if real US health records appear | Only if the product leaves the fixture | Civil and contractual exposure if real records are held without a program | Not in force for a fictional household | DEFER | No real subject exists. A program for nobody is not the demo | The day a real medication, appointment, or voice identified to a patient is stored | Stop intake. Refuse the payload. Keep the fixture path | Gerald, date [FILL] | Before that day |
| CLR-P3 | No medical advice and no purchase without a human yes | The agent speaks about meds and can prepare a reorder | Harm from a dose change or an unwanted order | Product rule, independent of a regulator | COMPLY | The bar is a server check plus a refusal | If a clinical claim is ever added | Disable the write tools | Gerald, date [FILL] | Before any clinical claim |

**Postures:** COMPLY is the default on CLR-P1 and CLR-P3 because both are cheap and protect the person in the demo. DEFER on CLR-P2 has a revisit trigger. §3 bars are not deferred. CLR-P2 is the paperwork and program around real records, which the demo does not have.

---

## Self-Check

- [x] Markets in §0 match the demo
- [x] §1 has retention on each row
- [x] Present bars are met or marked n/a with a reason
- [x] §7 rows have a posture, an owner, and a revisit or kill switch
- [x] Sign-off dates stay [FILL]
