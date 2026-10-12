# Design System (DSD)

**Project:** CareSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Gerald
**Status:** Draft
**Last reconciled:** N/A (not yet reconciled with reality)

---

## 0. Brand Stance

### The Three Rules

- **Make it relatable:** A card that could sit on a generic assistant home screen fails. The card names the parent, the visit, and the supply.
- **Make it human:** The reply reads the time back in the caregiver's words, including "Thursday at 2".
- **Make them part of the branding:** Written for Alex on a weekday morning, not for every smart-speaker user.

### Mode

**Selected mode:** `Product (task-first). The card is the brand.`

### Aesthetic Provenance

**Cultural or aesthetic reference:** `[FILL]`

**Line AI slop would never write:** `Thursday at 2. Pads run out Friday.`

**Archetypical user:** `Alex Rivera, 41, Thursday morning, one parent, three lists.`

**Category slop default:** `A purple assistant orb, a gradient hero, and a slogan about peace of mind.`

**How users appear in the brand:** `By the parent's first name on the card and the caregiver's own phrase in the confirmation.`

### Anti-References

Must not resemble: `a hospital portal` · `a shopping app home` · `a meditation app`

---

## 0.5 Concept Visuals (from IDEA)

**IDEA link:** [idea-caresync.md](idea-caresync.md). **Frames:** none on disk. **Shape pass:** [FILL]

---

## 1. Design Philosophy & Vision

**Core aesthetic:** [FILL]. Until tokens exist, the product rule is one card, three facts, one next action.

**Emotional intent:** Calm and specific. **References:** [FILL]. **Explicitly avoids:** Clinical dashboards, cart grids, and stock assistant chrome.

---

## 2. Brand Primitives

### 2.0 Token Architecture

Three tiers when code exists: primitive, semantic, component. Values below are not chosen.

### 2.1 Colors

Exact hex is [FILL]. Do not invent a palette in this doc.

| Token | Value |
|-------|-------|
| `--color-bg` | `[FILL]` |
| `--color-surface` | `[FILL]` |
| `--color-border` | `[FILL]` |
| `--color-primary` | `[FILL]` |
| `--color-primary-hover` | `[FILL]` |
| `--color-text` | `[FILL]` |
| `--color-text-muted` | `[FILL]` |
| `--color-success` | `[FILL]` |
| `--color-warning` | `[FILL]` |
| `--color-error` | `[FILL]` |

### 2.2 Logo System

**Variants:** primary `[FILL]`, secondary `[FILL]`, icon `[FILL]`.

**Clear space:** [FILL]. **Minimum size:** [FILL]. **Backgrounds:** [FILL]. **Don'ts:** Do not draw a medical cross as the mark.

### 2.3 Typography

| Role | Font | Weight / size / line height |
|------|------|-----------------------------|
| Headings | [FILL] | [FILL] |
| Body | [FILL] | [FILL] |
| Small / Caption | [FILL] | [FILL] |
| Mono / Code | [FILL] | [FILL] |

**Loading / license / fallback:** [FILL]

### 2.4 Imagery & Illustration

**Style:** No photography of real patients. **AI prompts:** [FILL]. **References:** none.

### 2.5 Elevation & Depth

Shadow tokens: [FILL]. The confirmation card must be visually distinct from the brief card. How is [FILL].

---

## 3. Layout & Spatial System

**Base unit:** `[FILL]`

**Scale:** [FILL]

**Grid:** One column for the spoken reply, one card under it. **Breakpoints:** [FILL]. The demo is a desktop browser recording unless Gerald decides otherwise.

---

## Self-Check

- [x] Stance filled before tokens
- [x] Unchosen colors, type, and logo stay [FILL]
- [x] No image is described that is not in the repo
