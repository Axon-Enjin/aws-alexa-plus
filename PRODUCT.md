# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Family caregivers coordinating care for an aging parent. The working demo follows Maya Reyes caring for her mother Elena Reyes in Austin. The user confirmed that the redesign should prioritize a polished caregiver workspace and retain every current demo flow.

## Product Purpose

CareSync joins household care information into one conversational brief and supports follow-through on reminders, supplies, appointments, and visit preparation.

## Positioning

The agent connects persistent family memory, dispenser and household telemetry, medication schedules, calendar, routines, and supply runway. Explicit confirmation gates simulated orders and reminders.

## Operating Context

An Alexa+ hackathon simulator served by Python with a vanilla HTML/CSS/JavaScript frontend. Local turns use the self-hosted MCP server over Streamable HTTP; hosted Vercel turns execute the same tools in process. SQLite holds local household state; hosted browser state uses signed cookies.

## Capabilities and Constraints

Preserve the daily care brief, medication and supply questions, Echo Show reminder proposal and confirmation/cancellation, supply reorder proposal and confirmation/cancellation, appointment updates, persistent memory recall, asynchronous visit packet completion, optional browser speech input/output, and household reset. All household information and purchases are simulated. Nothing charges a wallet. This is not a medical device. Do not present telemetry as a clinical conclusion or mark medication taken on reminder delivery.

## Brand Commitments

Keep the CareSync name and Alexa+ simulator identity. The user requested a full visual redesign using the impeccable skill. No binding visual references have been supplied.

## Evidence on Hand

README.md and IDEA.md describe the product. caresync/store.py and /api/board supply the actual demo household; caresync/orchestrator.py defines available turns. Existing web source is in caresync/web/. No real resident photography, production integrations, customer proof, or clinical validation is provided.

## Product Principles

- Surface actionable care needs before secondary details.
- Keep remembered information grounded in the household record.
- Require a clear yes before executing a staged action.
- Keep the current care context available during a conversation.
- Make simulation status and action outcomes understandable.
