# FMD pointer

This project uses **Foundational Matrix Documents (FMD)** via a zero-footprint pointer. Do not duplicate FMD rules here; fetch the canonical engine at session start and follow it.

**Pinned engine:** FMD 2.0.1
**Source repo:** FMD framework
**Tag:** v2.0.1

## How to operate FMD in this repo

1. **Session start:** Fetch and read the canonical operating guide from:
   `FMD framework`
   Follow that file for routing, trigger phrases, file naming, and workflow. This pointer defers to it entirely.

2. **Routing surface:** Fetch the canonical trigger matrix when you need to map a request to an artifact:
   `FMD framework`
   It holds the signal register and every artifact's trigger and non-trigger conditions.

3. **Templates on demand:** When a trigger fires, fetch the template from:
   `FMD framework`
   Example: `PRD_Template.md` for a PRD request. Read the `> **Agent Instructions**` blockquote first.

4. **Guides on demand:** Detailed reference (orchestrator, milestones, context, knowledge, agents, frameworks, business development, engineering ladder, public surfaces, workflows) lives at:
   `FMD framework`
   Fetch only the guide the current task needs. Do not preload the folder.

5. **Offline fallback:** If GitHub is unreachable, or the source repo is private and you lack credentials, read the same paths from the local FMD clone:
   `<local path>`
   (relative paths: `AGENTS.md`, `templates/_triggers.md`, `templates/<NAME>_Template.md`, `guides/<NAME>.md`).

6. **Validation:** After generating docs, run the validator from the local clone:
   `python <local path> docs/`
   Add `--strict` for CI-grade checks. If offline and no clone is available, fetch `FMD framework` once and run it against `docs/`.

7. **Cockpit (visual progress):** Regenerate only on cockpit trigger or explicit request from the local clone:
   `python <local path> .`
   This writes `cockpit.html` at the project root (add it to `.gitignore`; it is a generated artifact).

8. **Generated output:** Save filled artifacts to `docs/{{type}}-{{slug}}.md` per the canonical AGENTS.md. Keep the operating position in `docs/state.md` by hand. The inventory and session log are mechanical: after each artifact write or gate run
   `python <local path> docs/ --action "<what happened>"`
   regenerates `docs/index.md` (stamped "Built on FMD 2.0.1") and appends to `docs/log-{{slug}}.md`.

## Reference-only (never auto-load into build context)

`examples/`, `Playbook.md`, `CHANGELOG.md`, and `benchmarks/` live only in the source repo.