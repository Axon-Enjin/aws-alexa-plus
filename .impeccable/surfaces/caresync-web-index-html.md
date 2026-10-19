---
version: 1
slug: "caresync-web-index-html"
primary_target: "caresync/web/index.html"
related_targets: ["caresync/web/app.css","caresync/web/app.js"]
---

# Care assistant workspace

Scope: /, caresync/web/index.html with app.css and app.js. Mode: Operate.

The user approved mock C, .impeccable/mocks/c-conversation.png, on 2026-10-19 and authorized supporting backend changes. Keep every working demo flow and synthetic household truth. The initial state is a real household greeting, not a fabricated conversation or pre-staged reminder. Confirmation state from the comp appears after the user requests a reminder.

## Direction contract

THESIS: A conversation-led caregiver workspace with the household record always beside the task.

OWN-WORLD: Deep plum rail, cool white care sidebar, pale lavender conversation field. Linked rings, precise line icons, readable sans, white message surfaces and outlined confirmation slips.

STORY: Read Elena's care context, ask a question, inspect a proposal, explicitly confirm or cancel, then see its outcome and updated context.

FIRST VIEWPORT: 80px plum rail, roughly 320px care sidebar, remaining width conversation. Header at top, chronological chat through the middle, composer anchored below. On phones the care context opens as an accessible drawer.

FORM: Community health wayfinding, grounded candidate 5; composition C explicitly approved. Original seed 700610dd from the prior skill session; seed: none (unavailable).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Approved composition inventory

| Ingredient | Medium | Commitment |
| --- | --- | --- |
| Plum rail and navigation | HTML/CSS, small stroke SVG icons | Narrow persistent desktop rail; selected lavender tile |
| Care context sidebar | HTML/CSS | Resident, medications, visit, supplies, device; real board data |
| Linked-ring identity | SVG geometry | White on plum and plum on light surfaces |
| Conversation and summary rows | Semantic HTML/CSS | Chronological messages; white assistant, lavender user |
| Confirmation | HTML buttons and live state | Outlined white slip; yes/no inline; pending/executed/cancelled/superseded |
| Composer | HTML form | Full-width white input; microphone and plum submit; anchored bottom |
| Product/device thumbnails | Asset producer review | Neutral illustrative objects only; no invented brand evidence |
| Text | Segoe UI Variable system stack | Approved comp calls for Segoe-like task UI; fixed rem scale |

No appointment calendar date or health outcome may be copied from an image hallucination. Use the actual weekday/time from the backend. The app starts with a useful greeting and suggestions. The comp's two-turn reminder sequence is a verification state, not fabricated chat history.

## Approved category extension

The user approved real Home, Medications, Calendar, Supplies, and Memory views as an extension of composition C. Retain the incumbent palette, Segoe-like typography, linked rings, flat tonal surfaces, and confirmation language.

| View | Route | Purpose |
| --- | --- | --- |
| Home | `#/home` | Household greeting, summary, suggestions, and full conversation |
| Medications | `#/medications` | Filtered recorded doses, medication status, daily routine, reminder review |
| Calendar | `#/calendar` | Next visit and care logistics, visit packet, weekday/time rescheduling |
| Supplies | `#/supplies` | Item runway, simulated price/delivery, item-specific reorder review |
| Memory | `#/memory` | Household notes with recorded source and time |

Direct hash links and browser Back/Forward restore the selected view. Empty or unknown routes resolve to Home. Rail controls, sidebar section links, and phone navigation select these views; header and document title reflect the selected category. Navigation preserves the shared conversation, unsent composer text, pending confirmation, asynchronous visit tasks, medication filter, and appointment form drafts within the loaded page.

Home retains the full conversation composition. Category records scroll independently on the cool context surface. At widths of at least 1300px, the shared assistant is initially visible in a 380px panel beside the category and may be hidden. Below 1300px, categories initially fill the content area; opening the assistant replaces the category until “Back to view.” Changing category resets assistant visibility for the current breakpoint. At widths up to 600px, a horizontally scrolling row below the header exposes all five destinations while the plum rail is hidden. The existing care-context drawer remains available.

Category actions reveal the shared assistant and use the existing conversation flow. Reorder review targets the selected supply item and requires explicit confirmation before a simulated order. Revealing a hidden assistant through an action transfers focus to its heading; the header toggle focuses the composer when opening and the care-view region when returning. Compact category assistant suggestions are hidden, while conversation and pending decisions remain available.

Extension evidence: `.impeccable/review/views-medications-desktop.png` shows the category and assistant side by side; `.impeccable/review/views-supplies-mobile.png` shows phone navigation and item-specific reorder controls. The extension preserves the incumbent token frontmatter and `.impeccable/design.json`; responsive category behavior is recorded here and in DESIGN.md.
