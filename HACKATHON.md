# Build, Ship, Shape: Amazon Developer Hackathon

> *Build across Amazon Devices and shape what's next.*

- **URL:** https://amazonappdev2026.devpost.com/
- **Sponsor:** Amazon Developer, 410 Terry Avenue North, Seattle, WA 98109
- **Administrator:** Devpost, Inc., 250 Broadway, Floor 24, New York, NY 10007
- **Hackathon manager:** janet@devpost.com · General questions: support@devpost.com
- **Format:** Online, public · Themes: Machine Learning/AI, Open Ended, Productivity
- **Participants (as of 2026-09-28):** 17,081
- **Source retrieved:** 2026-09-28 (overview, rules, resources, schedule, FAQs, updates pages)

First hackathon where **Fire TV, Alexa+, Ring, and Bee** are all open to outside developers at once. Build for one product or combine several (living room + front door + cloud).

---

## 1. Key Dates

| Period | Pacific Time | Philippine Time (GMT+8) |
|---|---|---|
| Submissions open | Mon Aug 31, 2026, 10:15 AM PDT | Tue Sep 1, 2026, 1:15 AM |
| AWS credit request deadline | Wed Oct 21, 2026, 12:00 PM PT | Thu Oct 22, 2026, 3:00 AM |
| **Submission deadline** | **Fri Oct 23, 2026, 12:00 PM PDT** | **Sat Oct 24, 2026, 3:00 AM** |
| Judging | Mon Nov 9 – Fri Nov 20, 2026, 12:00 PM PT (per Official Rules) | Nov 10 – Nov 21, 4:00 AM |
| Winners announced | ~Thu Dec 3, 2026, 12:00 PM PST | Fri Dec 4, 2026, 4:00 AM |

> ⚠️ **Discrepancy:** the `/details/dates` schedule page lists Judging as **Oct 26 – Nov 20**; the Official Rules (and FAQ) say **Nov 9 – Nov 20**. The Official Rules prevail on conflicts (Rules §11).

---

## 2. Eligibility

**Open to:**
- Individuals at or above the age of majority in their place of residence
- Teams of eligible individuals (no max team size — appoint one **Representative** to submit)
- Organizations (corporations, nonprofits, LLCs, partnerships, etc.) existing at time of entry
- An individual may join multiple teams/orgs *and* also enter individually

**Not open to:**
- Residents of places where US or local law prohibits participation — explicitly **Brazil, Quebec, Russia, Crimea, Cuba, Iran, North Korea**, and any OFAC comprehensively sanctioned country
- Sponsor, Administrator, and other Promotion Entities; their employees, agents, and immediate family/household
- Judges and their employers; affiliates/subsidiaries of the above
- Anyone with a real or apparent conflict of interest
- Projects developed with financial or preferential support (funding, contracts, commercial license) from Sponsor or Devpost

> Philippines is **eligible**.

---

## 3. How to Enter

1. Click **Join Hackathon** on the site (free Devpost account).
2. Pick a track and set up the environment:
   - **Fire TV:** developer account + docs at developer.amazon.com/apps-and-games/
   - **Alexa+:** MCP open-source docs at modelcontextprotocol.io/docs/latest/getting-started/intro
   - **Bee:** docs.bee.computer
   - **Ring:** developer.ring.com
   - **AWS:** builder.aws.com
3. Build (new, or a significant update to an existing project during the Submission Period).
4. Complete all required fields on "Enter a Submission" before the deadline. Drafts can be saved; no changes after the deadline.

**Multiple submissions** allowed if each is unique and substantially different.

---

## 4. Primary Tracks

Pick a primary track. Each project can win **one track prize + one mini challenge prize** max. Sponsor may reassign projects between categories.

### 📺 Fire TV
- Launch a **demo-ready app on Fire OS or Vega OS**.
- Any framework: React Native, web technologies, Android (Kotlin/Java).
- **Priority categories:** AI-enhanced viewing, sports, fitness, family entertainment, multi-modal UX, computer vision.
- **Proof:** demo video must show it running on a real Fire TV device **or** the Fire TV/Vega simulator (Android TV Emulator also OK per FAQ). No physical device required.
- Exempt from the "runtime tech hook" repo requirement.

### 🗣️ Alexa+
- Build a **self-hosted MCP server** (spec **2025-11-25 or later**, **Streamable HTTP** transport) **or** an **Agent Skill**.
- **Alternative path:** a **simulated Alexa+ experience** in a web app using any AI/agentic tool — no specific framework required; exempt from the runtime-hook rule, but repo must include simulation source and the video must clearly show it.
- The gated Alexa+ Add-on tools (Category SDK, MCP Toolkit, CLI, Web Simulator) are **not available** to participants — build self-hosted and demo via your own front end.
- Hosting not required: a locally runnable repo + demo video is enough.
- "Significant update" example: a new conversational feature on an existing app — show a clear before/after.

### ⌚ Bee (Wearable AI)
- Connect to **real data recorded and processed through a Bee device or an Apple Watch running Bee software**, via Bee's **CLI, MCP, or Agent Skills**.
- Demo + code must show the project **actually using live Bee data** to do something useful for a person. Mentioning Bee isn't enough.
- No public-facing integration required (others don't need to connect their Bee).
- **Priority use cases:** education, developer experience, personal productivity.
- Notes: CLI requires a Bee account (not necessarily a device). Developer Mode in the Bee Android app only appears after pairing a Bee device.

### 🔔 Ring
- Build a new app or extend an existing one using **Ring APIs, SDKs, simulators, or devices**. No physical device required (free Ring developer account gives Ring / Amazon Vision API access).
- **Priority categories:** access control, business systems, IoT home automation, accessibility, caretaking.
- **Proof:** demo through a simulator (e.g. Ring Developer Playground) or a real device.

### Runtime tech requirement (Alexa+, Bee, Ring)
Repo must **import and actually call** the track's required tech at runtime — a library import, an app/backend entry point, or a loaded agent/flow/MCP config. A README mention does not count.

---

## 5. Mini Challenges (layered on your primary-track project)

Not separate projects — add to the one you already built.

### AWS Builder
- Use AWS services with **documented integrations**: Amazon Bedrock, AgentCore, Strands SDK, Kiro Crew, SageMaker, etc.
- **Kiro Crew qualifies on its own** (as a dev tool) — no separate AWS runtime service required.
- Describe which AWS services you used and how **in your Product Feedback answer**.
- AWS free tier is enough to start.

### Open Source
- Ship a **new open-source project** (with OSS license) **or** a **contribution** (branch, fork, or PR — merge not required) to a public repo **during the hackathon window**.
- **Required fields:** contribution URL, project repo URL, GitHub username, description of what you did / how it works / why it matters.
- Tip: October = Hacktoberfest (MLH, DEV, DigitalOcean). **Not affiliated**; 2026 format no longer counts PRs — check their rules.

---

## 6. Submission Requirements

| # | Item | Notes |
|---|---|---|
| 1 | **Text description** | Features, functionality, how it works |
| 2 | **GitHub repo URL** | GitHub only (no GitLab). All source, assets, and clear setup/run instructions |
| 3 | **Demo video** | < 3 min, **YouTube or Vimeo, public, English**. Show it running on the intended device/platform. No third-party trademarks or copyrighted music/footage without permission. Judges needn't watch past 3:00 — lead with the best |
| 4 | **Product Feedback** for *each* tool/API/SDK | What you used and for what; what worked; what needs work; onboarding (zero → hello world); would you build again (Yes/No + why). AWS Builder: describe AWS services here |
| 5 | **Track(s) and mini challenge(s)** entered | |
| 6 | Mini challenge extra fields | Open Source: contribution URL, repo URL, GitHub username, description |
| 7 | Pre-existing project explanation | What was built/changed during the Submission Period |
| 8 | *Optional:* **Feature requests** | Description, why it matters, priority: Critical / Important / Nice-to-have |
| 9 | *Optional:* **Friction log entries** | Task attempted, steps, expected vs actual, severity, workaround, actionable suggestion. **Up to 10% judging bonus** |

### Repository access
- **Public:** must include an OSS license file, detectable in the repo's About section.
- **Private** (allowed since Sep 16, 2026 update): add as collaborators (Settings → Collaborators → Add people) **before the deadline**:
  - Devpost: `testing@devpost.com`
  - Amazon DevRel: `chris-trag` (Chris Traganos), `knmeiss` (Kourtney Meiss), `giolaq` (Giovanni Laquidara), `anishamalde` (Anisha Malde), `mosesroth` (Moses Roth), `emersonsklar` (Emerson Sklar)
  - ⚠️ GitHub invites **expire after 7 days** and must be accepted — add them at submission time; re-send if lapsed.

### Testing & other conditions
- Project must be accessible to judges free of charge until judging ends; private sites need login credentials in testing instructions.
- Judges may judge solely on description, images, and video.
- For non-mainstream hardware (wearables, etc.), Sponsor may request physical access.
- All materials in English (or with English translations).
- Third-party SDKs/APIs/data must be used within their license terms; open source allowed if you build on top of it and comply with licenses.

---

## 7. Prizes

**$138,000 cash + $52,000 AWS credits ≈ $190K total value.**

| Prize | Cash | AWS Credits | Extras |
|---|---|---|---|
| Fire TV – 1st | $25,000 | $15,000 | Meeting w/ Amazon Developer team; featured on Amazon Developer channels |
| Fire TV – 2nd | $15,000 | $5,000 | Featured |
| Fire TV – 3rd | $4,000 | $1,000 | Featured |
| Alexa+ – 1st | $25,000 | $15,000 | Meeting; featured |
| Alexa+ – 2nd | $15,000 | $5,000 | Featured |
| Alexa+ – 3rd | $4,000 | $1,000 | Featured |
| Bee – 1st | $12,000 | — | Meeting; featured |
| Bee – 2nd | $8,000 | — | Featured |
| Ring – 1st | $12,000 | — | Meeting; featured |
| Ring – 2nd | $8,000 | — | Featured |
| AWS Builder (mini) | $5,000 | $5,000 | Meeting; featured |
| Open Source (mini) | $5,000 | $5,000 | Meeting; featured |

- Max per project: 1 track prize + 1 mini challenge prize.
- Prizes non-transferable; subject to identity/role verification and winner affidavits (return within 10 business days). Paid within 60 days of receiving forms.
- Winners pay own taxes/fees (non-US residents may need **W-8BEN**); Sponsor may withhold tax.

### Build credits
- **$150 AWS Promotional Credits per individual** (each teammate can request their own), while supplies last, via form by **Oct 21, 12 PM PT**.
  - Rules link: https://forms.gle/5hyhr1u6x3fuV2aW7
  - Resources page link: https://forms.gle/GaHFxSbBQNG9Kti6A ⚠️ *(two different form URLs are published — confirm which is current)*
- Not redeemable for cash; overage charges are yours. FAQ tip: mock/stub Bedrock during dev, spin resources up only to test, tear down with CDK/CloudFormation/Terraform.

---

## 8. Judging

**Stage 1 — Pass/fail viability:** fits the theme and reasonably applies the required APIs/SDKs. Amazon's internal team also reviews friction logs here and recommends a bonus (up to 10%).

**Stage 2 — Four equally weighted criteria, each scored 1–5:**

| Criterion | Question |
|---|---|
| **Tech Implementation** | How well built? How effectively does it use the required APIs/SDKs/device capabilities for the track or mini challenge? |
| **Design** | Complete, coherent product experience? Intuitive interaction model for the target device/platform? |
| **Potential Impact** | Credible, specific case for solving customer needs? Could it serve an audience beyond the hackathon (e.g. Fire TV Appstore, Ring Appstore)? |
| **Quality of the Idea** | Creative, imaginative use of the tools? Genuine understanding of the developer ecosystem and end-user needs? |

Friction-log bonus (up to 10%) is applied to the final spreadsheet score. Judging may use expert panels, peer review, and/or **automated AI-driven analysis**. Judges TBA.

**Tie-break:** highest score on the first criterion (Tech Implementation), then next criterion, etc.; then judges vote.

### Obvious vs. creative (from the Official Rules)

| Track | Obvious (avoid) | Creative (aim here) |
|---|---|---|
| Fire TV | Basic streaming UI, simple video player, remote-controlled game | AI viewing that adapts to household patterns; CV fitness app using the TV camera; multi-modal voice + D-pad + visual in one flow |
| Alexa+ | Single-turn Q&A bot; basic MCP wrapper around an existing API | Agentic workflow orchestrating across services; context-aware add-on with state across sessions; purchasing; media support (cards, carousels); MCP Apps; Agent Skills |
| Bee | Notification relay; basic wearable → phone logging | Cross-device orchestration (Bee + Echo + Fire TV); ambient context driving a productivity workflow; on-wrist education coaching via Agent Skills; advanced use of facts/insights; real-time; self-improvement workflows; synced meeting insights across teams |
| Ring | Motion alert; basic doorbell live view | Non-security use cases (accessibility, caretaking, package/delivery management); business access control; multi-camera pipelines; event-based triggers |
| AWS Builder | Single Bedrock call; S3 storage | Multi-service pipeline (Bedrock + AgentCore + Strands); agentic architecture with Claude/Kiro for dev workflow; agent orchestration patterns |
| Open Source | README update, typo fix, formatting | Meaningful feature with tests; bug fix that unblocks others; new integration pattern (e.g. Vega support in a popular React Native library) |

---

## 9. Resources

### Start here (all tracks)
- **Amazon Devices Builder Tools** (MCP server + Agent Skills for your AI coding assistant — crash analysis, perf profiling, doc search, guided workflows): https://developer.amazon.com/docs/vega/latest/mcp-server.html
- Amazon Developer docs: https://developer.amazon.com/docs/apps-and-games/documentation.html
- Sample code: https://github.com/amazonappdev
- Developer Community forum: https://community.amazondeveloper.com/
- YouTube (AmazonAppDev): https://www.youtube.com/channel/UCT9ApARFgQJOeqD-ygmxnJQ
- dev.to: https://dev.to/amazonappdev
- Newsletter: https://m.amazonappservices.com/hackathon-subscribe
- LinkedIn showcase: https://www.linkedin.com/showcase/amazon-appstore-developers/

### Fire TV starters
| Repo | What it is |
|---|---|
| [react-native-multi-tv-app-sample](https://github.com/AmazonAppDev/react-native-multi-tv-app-sample) | Most complete starter; one codebase for Vega, Android TV, Apple TV, web (drawer nav, grid, hero, video player) |
| [react-native-multi-tv-helloworld](https://github.com/AmazonAppDev/react-native-multi-tv-helloworld) | Minimal multi-platform starter |
| [hello-world-fire-tv-react-native](https://github.com/AmazonAppDev/hello-world-fire-tv-react-native) | 5-minute RN Hello World |
| [vega-video-sample](https://github.com/AmazonAppDev/vega-video-sample) | Richest Vega reference: W3C media player, focus mgmt, live TV, IAP, content launcher |
| [vega-sports-app](https://github.com/AmazonAppDev/vega-sports-app) | Themeable content app with catalog/service integration |
| [vega-audio-sample](https://github.com/AmazonAppDev/vega-audio-sample) | Music player |
| [vega-tv-interfaces-sample](https://github.com/AmazonAppDev/vega-tv-interfaces-sample) | TV UI patterns: focus, i18n, navigation, scrolling |
| [hello-world-fire-tv](https://github.com/AmazonAppDev/hello-world-fire-tv) | Native Kotlin + Jetpack Compose |

- Callstack e-book: [The Ultimate Guide to React Native TV Development](https://www.callstack.com/ebooks/the-ultimate-guide-to-react-native-tv-development)
- Forums: [Vega](https://community.amazondeveloper.com/c/vega/6) · [Fire Devices & Appstore](https://community.amazondeveloper.com/c/fire-apps/17)

### Alexa+
- MCP getting started: https://modelcontextprotocol.io/docs/latest/getting-started/intro
- Build with Agent Skills: https://apps.extensions.modelcontextprotocol.io/api/#build-with-agent-skills

### Bee
- Docs (CLI, MCP server, Bee Skill, API): https://docs.bee.computer/
- [bee-cli](https://github.com/bee-computer/bee-cli) · [bee-skill](https://github.com/bee-computer/bee-skill)

### Ring
- Developer portal: https://developer.ring.com · Get started: https://developer.amazon.com/docs/ring/get-started.html
- API reference: https://developer.amazon.com/docs/ring/api-documentation.html
- UX design guide: https://developer.amazon.com/docs/ring/ux-design-guide.html
- Ring Appstore (live apps): https://ring.com/appstore
- Community: https://community.amazondeveloper.com/c/ring/53
- Starter: [ring-api-helloworld](https://github.com/AmazonAppDev/ring-api-helloworld)

### AWS
- AWS Builder Center: https://builder.aws.com/ · Learn: https://builder.aws.com/learn

### Help
- Devpost Discord: https://discord.gg/devpost — check in at `#amazon-developer-checkin` for the hackathon space (Chris & Moses active there)
- Live office hours: schedule/join link posted on the landing page
- Discussion forum: https://amazonappdev2026.devpost.com/forum_topics

---

## 10. Updates Timeline

| Date (approx.) | Update |
|---|---|
| ~Sep 1 | Live Build Session announced — Chris Traganos (Head of Dev Evangelism) & Moses Roth (Dev Advocate) |
| Sep 3, 2 PM ET | Build Session: AI builder tools for Fire TV, MCP for Alexa+ add-ons, Bee dev tools, Ring Appstore & computer vision APIs. Recording on YouTube |
| ~Sep 14 | "Let's get you building" — track links, Discord; product feedback goes straight to Amazon Developer team |
| Sep 16 | **Rules update:** code repository may now be private (with reviewer collaborators) |
| ~Sep 18 | "Got an idea?" — push past the obvious; scoring 1–5 per criterion; private-repo instructions |

---

## 11. IP, Publicity & Legal (summary)

- You keep IP. Sponsor gets a non-exclusive license to use the entry for judging.
- Sponsor and Devpost may promote the submission and use entrants' name, likeness, voice, image during the hackathon and **3 years after**.
- Submission must be original, solely owned, non-infringing; contracted technical help allowed if the work product is yours.
- Disputes: individual binding arbitration (AAA), Federal Arbitration Act; **New York law** governs. No class actions.
- Devpost Terms of Service and Privacy Policy incorporated by reference.

---

## 12. Quick Checklist

- [ ] Registered on Devpost
- [ ] Track chosen; env set up; AWS $150 credits requested by Oct 21 (PH: Oct 22, 3 AM)
- [ ] Required tech is imported *and called* at runtime (Alexa+/Bee/Ring)
- [ ] Repo on GitHub with setup/run instructions; OSS license (public) or reviewers invited ≤7 days before submit (private)
- [ ] Demo video < 3 min, public YouTube/Vimeo, English, shows device/simulator
- [ ] Product feedback for every tool/API/SDK (+ AWS services if AWS Builder)
- [ ] Open Source fields (if entering)
- [ ] Friction log entries (up to +10%)
- [ ] Feature requests (optional)
- [ ] Pre-existing project changes explained (if applicable)
- [ ] Submitted before **Sat Oct 24, 2026, 3:00 AM PHT**
