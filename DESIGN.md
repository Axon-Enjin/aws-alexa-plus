---
name: CareSync
description: A calm conversation-led family care workspace.
colors:
  plum: "#342449"
  action: "#512779"
  action-hover: "#3e1c60"
  lavender: "#eee9f6"
  canvas: "#efebf7"
  sidebar: "#f8f8fc"
  white: "#fff"
  ink: "#20192e"
  muted: "#665c7d"
  line: "#dfd9e9"
  green: "#24684e"
  green-bg: "#e5f1eb"
  red: "#a82d4a"
  red-bg: "#fae8ee"
  amber: "#8c5816"
  amber-bg: "#faf0dd"
  user-message: "#dfd2f2"
  nav-selected: "#e8ddf5"
  nav-hover: "#4b395f"
  avatar: "#dfd3f1"
  focus: "#9575bb"
  confirmation-border: "#8253a6"
  secondary-border: "#b9a7ce"
  chip-bg: "#f8f5fc"
  chip-border: "#dbd1e7"
  chip-text: "#5b3e73"
  chip-hover: "#e6dcf1"
  status-bg: "#eeedf4"
  status-text: "#59506d"
typography:
  headline:
    fontFamily: '"Segoe UI Variable", "Segoe UI", ui-sans-serif, system-ui, sans-serif'
    fontSize: "1.5rem"
    fontWeight: 650
    letterSpacing: "-0.03em"
  title:
    fontFamily: '"Segoe UI Variable", "Segoe UI", ui-sans-serif, system-ui, sans-serif'
    fontSize: "0.9375rem"
    fontWeight: 650
  body:
    fontFamily: '"Segoe UI Variable", "Segoe UI", ui-sans-serif, system-ui, sans-serif'
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.65
  supporting:
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontSize: "0.8125rem"
    fontWeight: 600
  label:
    fontSize: "0.75rem"
    fontWeight: 600
  status:
    fontSize: "0.6875rem"
    fontWeight: 600
rounded:
  control: "8px"
  navigation: "10px"
  surface: "12px"
  status: "20px"
  circle: "50%"
spacing:
  compact: "7px"
  control-gap: "10px"
  small: "12px"
  message-gap: "15px"
  card: "18px"
  confirmation: "19px"
  section: "22px"
  conversation-gap: "25px"
  context-inline: "26px"
  workspace-inline: "28px"
components:
  button-primary:
    backgroundColor: "{colors.action}"
    textColor: "{colors.white}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "10px 17px"
  button-primary-hover:
    backgroundColor: "{colors.action-hover}"
  button-secondary:
    backgroundColor: "{colors.white}"
    textColor: "{colors.action}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "10px 17px"
  button-secondary-hover:
    backgroundColor: "{colors.lavender}"
  composer:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.surface}"
    padding: "9px 12px 9px 18px"
  navigation-selected:
    backgroundColor: "{colors.nav-selected}"
    textColor: "{colors.plum}"
    rounded: "{rounded.navigation}"
    padding: "13px 2px"
  suggestion:
    backgroundColor: "{colors.chip-bg}"
    textColor: "{colors.chip-text}"
    rounded: "{rounded.control}"
    padding: "7px 11px"
  status:
    backgroundColor: "{colors.status-bg}"
    textColor: "{colors.status-text}"
    typography: "{typography.status}"
    rounded: "{rounded.status}"
    padding: "4px 8px"
  summary:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.surface}"
  confirmation:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.surface}"
    padding: "19px"
  assistant-message:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "14px 18px"
  user-message:
    backgroundColor: "{colors.user-message}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "14px 18px"
---

# Design System: CareSync

## Overview

**Creative North Star: "Community health wayfinding"**

CareSync is a calm, conversational family care workspace. Deep plum establishes a stable navigation landmark; cool white care context and a pale lavender conversation field make household information easy to locate without competing with the current task.

The visual language is practical and approachable: readable Segoe-like task typography, precise line icons, linked-ring identity, white message surfaces, and outlined confirmation slips. Care status remains explicit in text and small semantic badges. Simulation labels and confirmation language are part of the interface's clarity.

**Key Characteristics:**

- Plum landmarks and lavender conversation surfaces.
- Readable task typography with restrained size contrast.
- Flat tonal layering, thin dividers, and softly rounded controls.
- Clearly authored messages and explicit action confirmation.

## Colors

The palette combines a plum identity with cool lavender neutrals and restrained semantic status colors. Frontmatter is normative; these roles describe the implemented values in caresync/web/app.css.

### Primary

- **Deep Plum** (plum): the navigation rail and light-surface identity.
- **Action Plum** (action, action-hover): confirmation buttons, send control, links, and assistant identity.
- **Conversation Lavender** (user-message): the caregiver's message surface.
- **Selected Lavender** (nav-selected): selected navigation tile; nav-hover provides the darker rail hover.

### Secondary

- **Care Green** (green, green-bg): taken/done medication states and online device status.
- **Attention Rose** (red, red-bg): missed medication status and low supply runway.
- **Due Amber** (amber, amber-bg): due/skipped medication states.

### Neutral

- **Lavender Canvas** (canvas): the conversation workspace.
- **Cool Context** (sidebar): the care sidebar.
- **White** (white): header, assistant messages, summaries, confirmation slips, and composer.
- **Deep Ink** (ink): main text; **Muted Plum** (muted): supporting text and timestamps.
- **Soft Divider** (line): section, panel, composer, and resolved-confirmation borders.
- **Hover Lavender** (lavender): secondary and icon control hover.
- **Avatar Lavender** (avatar): caregiver and resident initials.
- **Quiet Status** (status-bg, status-text): upcoming/running and other neutral status labels.
- **Suggestion Lavender** (chip-bg, chip-border, chip-text, chip-hover): suggested question controls.
- **Focus Lavender** (focus), **Confirmation Plum** (confirmation-border), and **Secondary Outline** (secondary-border): keyboard focus and distinct action boundaries.

**The Text-With-Status Rule.** Communicate state with a readable label alongside its color; use an icon where the implemented status pattern supplies one.

## Typography

**Display and body font:** Segoe UI Variable, Segoe UI, ui-sans-serif, system-ui, sans-serif. There is no separate display face or external font dependency.

The typography supports repeated reading and care tasks. It uses modest size contrast, medium-weight labels, and generous conversation leading. Root text size is (18px), changing to (16px) at the phone breakpoint.

- **Headline:** workspace heading uses the headline token; care-context heading is (1.375rem) with the same weight and tracking. The workspace heading changes to (1.1875rem) at (900px) and (1.0625rem) at (600px).
- **Title:** section and confirmation headings use the title token; resident name is (1.0625rem).
- **Body:** message text uses the body token and a maximum bubble width of (74ch). On phones it becomes (0.875rem) with line height (1.6).
- **Supporting:** summary details and task output use compact supporting text; task output has line height (1.65).
- **Label:** author labels, suggestions, and action descriptions use the compact label scale. Timestamps and status labels use (0.6875rem); technical details use (0.625rem).
- **Numbers:** appointment times, date dividers, and message timestamps use tabular numerals.

## Layout

The app is a viewport-height workspace (100dvh) with a minimum desktop height of (580px). The navigation rail, independently scrolling care context, and conversation form three columns. The header and composer remain outside the scrolling conversation; the message column is centered with a maximum width of (1000px). Summary containers stop at (680px).

| Viewport        | Implemented layout                                                                                                                                                                  |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| At least 1500px | Columns: 94px rail, 340px context, remaining conversation; context inline padding 29px.                                                                                             |
| 1201–1499px     | Columns: 88px rail, 320px context, remaining conversation; workspace inline padding 28px. Confirmation actions sit beside the proposal.                                             |
| 901–1200px      | Columns: 78px rail, 280px context, remaining conversation; workspace inline padding 22px. Confirmation actions wrap below the proposal.                                             |
| 601–900px       | 72px rail plus conversation. Context becomes a 320px drawer, inset after the rail and capped at the available width. Header inline padding 16px.                                    |
| At most 600px   | Single conversation column; rail is hidden. Context drawer begins at the left edge, width 330px capped at 88%. Conversation inline padding 14px; composer dock inline padding 12px. |

Care sections use thin separators and vertical breathing room rather than nested cards. Message groups are separated by (25px), reducing to (23px) on phones. User messages align right and occupy up to (75%) of their row, increasing to (88%) on phones.

The phone composer reserves the bottom safe area. Suggested questions form a horizontally scrolling row on phones. The context drawer has a backdrop, focus containment, Escape dismissal, and focus restoration; background controls are inert while it is open.

Home retains this conversation layout. Category views replace the main content area with an independently scrolling care record, using (32px) padding on desktop and (25px 18px) on phones. At widths of at least (1300px), the shared assistant opens beside the category in a (380px) panel and can be hidden. Below (1300px), it opens in place of the category; “Back to view” restores the category. Category navigation resets this assistant visibility according to the current breakpoint. At widths up to (600px), a horizontally scrolling navigation row below the header keeps all five views accessible when the rail is hidden.

## Elevation & Depth

The implemented system has no box shadows. Depth comes from the dark rail, cool context panel, lavender conversation field, and white foreground surfaces. Thin borders identify boundaries and the pending confirmation. The drawer uses a translucent plum backdrop (#22153066), not a shadow.

**The Tonal Depth Rule.** Preserve tonal separation and thin borders instead of introducing decorative drop shadows.

## Shapes

Containers use the surface radius; action buttons, suggestions, thumbnails, and icon controls use the control radius. Navigation tiles use the navigation radius. Status badges are short pills, while avatars, the send control, and confirmation thumbnails are circular.

Assistant bubbles have a square upper-left corner; caregiver bubbles have a square upper-right corner. This directional silhouette complements alignment and author labels. The linked-ring mark repeats two offset circular outlines. Standard icons are unfilled, rounded line drawings (24px canvas, 1.7px stroke); smaller component variants retain that vocabulary.

## Components

### Buttons

Confident, compact action controls. Primary and secondary buttons use the frontmatter padding, a minimum height of (42px), and the button type token. Primary actions darken on hover; secondary actions use a lavender hover fill and thin secondary outline. On phones horizontal padding is (13px). Disabled controls use opacity (0.55) and a not-allowed cursor.

Keyboard focus is a (3px) Focus Lavender outline offset by (4px). Button color, background, and border changes transition over (160ms ease). Text actions use Action Plum with an underline on hover.

### Navigation

A persistent deep-plum rail uses icon-over-label tiles. Selection uses a pale lavender tile and plum text; hover uses the darker rail tone. Labels and selected state remain explicit. At the phone breakpoint the rail disappears, with care context available through the header control and category links available in the horizontal navigation row. Both navigation variants identify the current view with `aria-current="page"`.

Home, Medications, Calendar, Supplies, and Memory use `#/home`, `#/medications`, `#/calendar`, `#/supplies`, and `#/memory`. Direct links and browser Back/Forward select the same views; an empty or unknown route resolves to Home. Navigation updates the header and document title without replacing the shared conversation, unsent composer text, pending confirmation, or asynchronous visit task. Medication filtering and appointment form drafts also survive view changes within the loaded page.

### Category records and assistant access

Category content extends the same flat surfaces, thin dividers, semantic status labels, and compact controls. Category headings use (1.625rem) type with weight (650), tracking (-0.03em), and line height (1.25), reducing to (1.5rem) on phones.

- **Home:** the household greeting, care summary, suggestions, and full conversation.
- **Medications:** a filterable recorded-dose table, daily routine, and reminder review action; reminder delivery does not mark a dose taken.
- **Calendar:** the next appointment, clinician/location/ride details, visit packet action, and weekday/time rescheduling form.
- **Supplies:** item names, brand, runway, simulated price/delivery, and an item-specific reorder review; low-runway items use the primary action treatment.
- **Memory:** household notes with recorded source and time.

Category actions reveal the shared assistant and run the existing conversational flow; reorder review requires explicit confirmation before a simulated order. Revealing a hidden assistant through a category action focuses its heading so the new conversation state is announced. The header toggle opens the assistant with focus in the composer; returning to the category focuses the care-view region. Suggestions remain hidden in the compact category assistant, while messages and pending confirmation remain available.

### Chips and status

Suggested questions are softly outlined rounded rectangles. They disappear while confirmation is pending. Status badges use the compact pill style, semantic foreground/background pairs, text labels, and small icons where applicable. A reminder outcome must not visually imply that a medication was taken.

### Cards and summary rows

White summary containers group related care facts. Individual rows pair a line icon with a title, supporting text, and an optional status or chevron. Rows use (15px 19px) padding, changing to (13px 12px) on phones. Clickable rows receive a pale hover fill. Async task cards use the same surface radius with (18px) padding, an inline status, expandable packet content, and a text download action.

### Composer

A white bordered surface combines the text field, microphone, and circular plum submit button. The field uses body-scale text on desktop and (1rem) on phones. Focus is represented by the container border (#a38abe), replacing an individual input outline. The submit control is (42px) square on desktop and (38px) on phones. Listening adds a lavender microphone background. Notices appear immediately above the composer.

### Messages

Assistant messages use white directional bubbles, a plum linked-ring avatar, an author label, and a timestamp. Caregiver messages use lavender directional bubbles, initials, and right-aligned time. Text wraps within its container and preserves intentional line breaks. Connection errors use a lightly rose-tinted message surface with an explicit recovery control.

### Confirmation slips

Pending actions use a white outlined slip with a compact object thumbnail, clear question, explanatory text, primary confirmation, secondary deferral, and a textual pending state. The pending outline becomes the ordinary divider color once resolved; resolved controls are disabled and the state text becomes muted. Confirmation stays attached to the conversation that produced it.

### Motion and updates

Motion explains state: button transitions use (160ms ease), the drawer uses (220ms cubic-bezier(0.16, 1, 0.3, 1)), and the checking icon fades on a (1.6s ease-in-out) loop. Conversation scrolling is smooth. Reduced-motion preference disables transitions, animation, and smooth scrolling. Async packet completion follows the latest content only when the reader was already within (80px) of the conversation bottom.

## Do's and Don'ts

### Do:

- Do use plum landmarks, lavender conversation surfaces, and white foreground content.
- Do keep care status legible in text alongside semantic color.
- Do retain the linked-ring identity and precise rounded line icons.
- Do keep confirmation decisions and their eventual outcomes visible in the conversation.
- Do preserve the accessible context drawer and reduced-motion behavior.

### Don't:

- Don't add decorative shadows to the flat tonal surface system.
- Don't substitute a display or editorial font for the approved Segoe-like task typography.
- Don't use color alone to communicate medication or action state.
- Don't visually present a delivered reminder as a taken medication.
