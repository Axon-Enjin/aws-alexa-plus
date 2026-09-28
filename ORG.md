# ORG.md — Organizations Behind "Build, Ship, Shape: Amazon Developer Hackathon"

> Scope: stated mission, goals, and current strategic priorities of every organization tied to
> `amazonappdev2026.devpost.com`, and what each one implies for a hackathon entrant.
> **Retrieval date for all sources: 2026-09-28.** agent mode report: sourced facts are tagged `[Sn]`
> (see Source List). Anything tagged **[Inference]** is my own reading, not a sourced claim.
>
> **Source tiers:** P = Primary (official Amazon/AWS/org pages, rules, blogs, filings) ·
> E = Expert (standards bodies, Wikipedia with follow-through) · J = Journalistic (TechCrunch,
> CNBC, InfoQ, SiliconANGLE) · W = Web (analyst blogs, secondary aggregators).
>
> **Caveat on extraction:** pages were read through an automated fetch/summarize step. Numbers
> are copied as the page stated them; any number listed under "Verification notes" (end of file)
> should be spot-checked against the live page before it is quoted in a submission.

---

## 0. The Hackathon Itself (baseline facts)

| Item | Fact | Src |
|---|---|---|
| Name | Build, Ship, Shape: Amazon Developer Hackathon | [S1] P |
| Tagline | "Build across Amazon Devices and shape what's next." | [S1][S2] P |
| Sponsor (legal) | Amazon Developer, 410 Terry Avenue North, Seattle, WA 98109 | [S2] P |
| Administrator | Devpost, Inc., 250 Broadway, Floor 24, New York, NY 10007 | [S2] P |
| Submission period | 2026-08-31 10:15 PT → 2026-10-23 12:00 PT | [S2] P |
| Judging / winners | Judging 2026-11-09 → 11-20; winners announced 2026-12-03 | [S2] P |
| Positioning | First time Fire TV, Alexa+, Ring and Bee are open to external developers in one global competition | [S1][S4] P |
| Primary tracks | Fire TV · Alexa+ · Bee (Wearable AI) · Ring | [S1] P |
| Mini challenges | AWS Builder (Bedrock, AgentCore, Strands SDK, Kiro Crew, SageMaker, etc.; Kiro Crew use qualifies on its own) · Open Source (new repo or contribution during window) | [S1] P |
| Prize pool | $138,000 total (cash + AWS credits + team meetings + promotion) | [S1] P |
| Judging criteria | Technical Implementation, Design, Potential Impact, Quality of the Idea — **equally weighted** in Stage Two | [S2] P |
| Friction-log bonus | Up to 10% bonus on final score; entries should include task attempted, steps, expected vs. actual, severity, workaround, actionable suggestion | [S1][S2][S4] P |
| Why feedback matters | Resources page: product feedback and feature requests "go straight to the teams building Fire TV, Alexa+, Bee, Ring, and the AWS tools" | [S3] P |
| Registration snapshot | 17,081 participants registered at time of retrieval | [S1] P |

### Track requirements (condensed)

| Track | Build surface | Priority themes named by sponsor | Src |
|---|---|---|---|
| Fire TV | Demo-ready app on Fire OS or Vega OS — React Native, web, or Android (Kotlin/Java) | AI-enhanced viewing, sports, fitness, family entertainment, multi-modal UX, computer vision | [S1] P |
| Alexa+ | Self-hosted MCP server (spec **2025-11-25 or later**, Streamable HTTP) or an Agent Skill; alt: simulated Alexa+ experience in a web app | (agentic services / smart home implied by docs) | [S1][S2] P |
| Bee | Must use real data from a Bee device or Apple Watch running Bee, via Bee CLI, MCP, or Agent Skills | Education, developer experience, personal productivity | [S1] P |
| Ring | New or extended app using Ring APIs, SDKs, simulators or devices (hardware optional) | Access control, business systems, IoT home automation, accessibility, caretaking | [S1] P |

---

## 1. Amazon (Parent)

### 1.1 Mission / positioning

| Statement | Src |
|---|---|
| Leadership Principles page: mission is "being Earth's most customer-centric company, best employer, and safest place to work." | [S5] P |
| About Us page: mission "to make customers' lives better and easier every day by relentlessly inventing on their behalf." | [S6] P |

**[Inference]** Amazon currently publishes two phrasings; the "customer-centric" framing is the long-standing one, the "better and easier every day" framing is the consumer-facing summary. Both anchor on customers + invention.

### 1.2 Leadership Principles most relevant to builders

Full list has 16 principles [S5] P. The ones that map directly onto hackathon judging:

| Principle | Paraphrase (from [S5]) | Hackathon relevance **[Inference]** |
|---|---|---|
| Customer Obsession | Start with the customer and work backward | Frame the demo around a real user problem (maps to *Potential Impact*) |
| Invent and Simplify | Innovate, seek ideas anywhere, accept being misunderstood | Novel but simple idea (maps to *Quality of the Idea*) |
| Insist on the Highest Standards | Relentlessly high quality, stop defects cascading | Polish, reliability (maps to *Design*, *Tech Implementation*) |
| Think Big | Bold direction, unconventional thinking | Cross-device / platform-level ideas |
| Bias for Action | Speed; reversible decisions don't need exhaustive study | Ship a working demo, not a deck |
| Frugality | More with less | Lean architecture, low cost-to-serve |
| Dive Deep | Stay connected to details, question anomalies | Friction logs are literally a Dive Deep artifact |
| Earn Trust | Listen, speak candidly | Privacy-respecting design (esp. Ring, Bee) |
| Success and Scale Bring Broad Responsibility | Consider second-order effects | Surveillance/privacy guardrails |

### 1.3 CEO Andy Jassy — stated priorities (2025–2026)

| Priority | Sourced claim | Src |
|---|---|---|
| AI as the multiplier | Letter to shareholders (covering FY2025): AI "is not a standalone initiative—it's a multiplier." | [S7] P |
| Agent-building stack | Letter lists Strands (agent building), AgentCore (secure, scalable agent environments), and turnkey agents Kiro (coding), Transform (migrations), Quick (knowledge work) | [S7] P, [S8] J |
| Infrastructure spend | Letter: approx. $200B capex planned for 2026, primarily AI infrastructure | [S7] P |
| Alexa+ | Letter reports customers talking to Alexa roughly twice as much after Alexa+ (see Verification notes) | [S7] P |
| Customer focus | "We will continue to focus relentlessly on our customers." | [S7] P |
| Q2 2026 results (2026-07-30) | Net sales $200.6B (+20% YoY); AWS +36.7% YoY, "fastest in 18 quarters"; AI and Chips businesses each >$25B run rate | [S9][S10] P |
| Agentic commerce | "Alexa for Shopping" — agentic shopping assistant; >350M customers used it in trailing 12 months (reported) | [S9] P, [S11] J |

**[Inference]** Jassy's through-line for 2026 is: (1) agents everywhere, (2) the AWS agent stack (Strands → AgentCore → Kiro/Quick) as the enterprise platform, (3) Alexa+ / Alexa for Shopping as the consumer agent. A hackathon entry that sits at the seam of consumer agent + AWS agent stack is on-strategy at the parent level.

### 1.4 What this means for a hackathon entrant (Amazon parent)

- **[Inference]** Work backward from a named customer and a measurable outcome; judges are Amazon employees steeped in PR/FAQ-style customer framing.
- **[Inference]** "Agentic" is the dominant corporate theme — an entry where the device *acts* (books, orders, alerts, automates) aligns better than one that only displays.
- **[Inference]** Frugality + Highest Standards: small, reliable, well-instrumented beats sprawling.

---

## 2. AWS (Amazon Web Services)

### 2.1 Mission / positioning

| Statement | Src |
|---|---|
| "the world's most comprehensive and broadly adopted cloud, is guided by customer obsession, a rapid pace of innovation, commitment to operational excellence, and long-term thinking." | [S12] P |
| "We democratize technology and make AI and cloud computing accessible to any organization." | [S12] P |
| Agentic goal (Swami Sivasubramanian, 2025-07-16): AWS aims to be "the best place to build the world's most useful AI agents." | [S13] P |

### 2.2 Gen-AI / agentic strategy — product map

| Product | What it is (sourced) | Latest status / dates | Src |
|---|---|---|---|
| Amazon Bedrock | Managed access to foundation models with governance/security controls; Jassy: "best selection of leading models" | Q2 2026: 10+ new models added; Web Search on Bedrock (Aug 2026); OpenAI models (GPT-5.5/5.4) in limited preview via Bedrock (Apr 2026) | [S10][S9][S14][S15] P |
| Bedrock AgentCore | Serverless runtime + Identity, Memory, Browser, Code Interpreter, Gateway, Observability for production agents | GA in 2025; re:Invent 2025 added Policy (Cedar-based, intercepts Gateway tool calls) and Evaluations; Q2 2026 added Payments and Web Search; Aug 2026 open-sourced "Dogwood" temporal policy language for AgentCore | [S13] P, [S16] J, [S14][S10] P |
| Strands Agents SDK | Open-source (Apache 2.0) agent SDK, Python + TypeScript; MCP and A2A support | Strands 1.0 (Python) added multi-agent primitives + A2A; TypeScript SDK 1.0 runs in Node.js and browser | [S17][S18] P |
| Kiro | Spec-driven agentic IDE / coding agent | Q2 2026: available on iOS; usage tripled QoQ; positioned as ~50% more cost-effective | [S9][S10] P |
| **Kiro Crew** — **VERIFIED, exists** | Open-source (Apache 2.0) persistent multi-agent workspace: shared memory, reusable skills, cron/webhook triggers, concurrent agents; runs on Kiro CLI and reads `.kiro` config | Announced/open-sourced **2026-08-04**; originated internally (reported codename MeshClaw); >39,000 internal Amazon builders, ~500 contributors in <6 months; repo `github.com/kirodotdev/kirocrew`; macOS/Linux/Windows; Slack/Telegram/Discord/WeCom integrations | [S19][S14] P, [S20][S21] J |
| Amazon SageMaker AI | Jassy: lets companies "build their own foundation models" on proprietary data | Q2 2026 call | [S10] P |
| Amazon Nova 2 / Nova Forge | Nova 2 model family; Nova Forge for custom training ("Novellas") | re:Invent 2025 | [S22] J |
| Amazon Quick | Agentic "work companion" | Apr 2026: desktop app, free/plus tiers; Q2 2026: background autonomous agents | [S15][S9] P |
| AWS MCP Server / Agent Toolkit for AWS | Managed remote MCP server giving agents authenticated access to AWS services; toolkit = MCP server + skills + plugins | GA 2026-05-06 | [S23] P |

### 2.3 Current strategic priorities (stated)

| # | Priority | Src |
|---|---|---|
| 1 | AI inference close to customers' existing apps and data, with strongest security | [S10] P |
| 2 | Custom silicon (Trainium, Graviton) for price-performance; Chips business >$25B run rate | [S10] P, [S22] J |
| 3 | Agents as the inflection point — Garman re:Invent 2025: "billions of agents all working together" | [S22] J |
| 4 | Trust/governance to unblock agents — Garman: most customers feel "blocked" from deploying agents to critical use cases (hence Policy + Evaluations) | [S16] J |
| 5 | Turnkey agents: Kiro (dev), Transform (migration), Quick (knowledge work), Connect (CX) | [S7][S15] P |
| 6 | Open standards: MCP + A2A in Strands; AWS is a supporting member of the Agentic AI Foundation | [S13][S27] P |

### 2.4 Developer-ecosystem goals

| Program | Fact | Src |
|---|---|---|
| AWS Builder Center (`builder.aws.com`) | Launched July 2025; consolidates legacy AWS Developer Center and community.aws; workshops, AI playgrounds, Heroes/Community Builders content, User Group directory; sign-in via AWS Builder ID | [S24] P |
| Hackathon framing | Resources page: "AWS's hub for developers: learning, community, tutorials, and Q&A in one place" | [S3] P |
| Free Tier | Since 2025-07-15: new accounts get $100 credits at sign-up + up to $100 more by using services (e.g., EC2, Bedrock); free plan lasts 6 months or until credits exhausted; 30+ always-free services | [S25] P |
| Hackathon credits | Track winners receive $1,000–$15,000 AWS credits; mini-challenge winners $5,000 credits | [S1] P |
| Community | AWS Heroes Summit (Aug 2026) positioned around feedback with product teams | [S14] P |

### 2.5 What this means for a hackathon entrant (AWS)

- **[Inference]** The AWS Builder mini-challenge rewards *using the agent stack*, not generic EC2 hosting. Strongest signal: Strands agent → deployed on AgentCore Runtime → exposing/consuming MCP → optionally orchestrated with Kiro Crew.
- **[Inference]** Kiro Crew is only ~7 weeks old at submission deadline; early real-world usage + a friction log on it is likely high-value feedback to AWS.
- **[Inference]** AgentCore Policy/Evaluations directly address Garman's stated blocker (trust). A consumer-device agent with explicit guardrails and evals demonstrates the exact thing AWS is selling.
- **[Inference]** Frugality: the $200 Free Tier credit model means a lean Bedrock + Lambda/AgentCore build is feasible without spend.

---

## 3. Amazon Developer / Amazon Devices & Services (the Sponsor)

### 3.1 Mission / positioning

| Item | Fact | Src |
|---|---|---|
| Leader | Panos Panay leads Amazon Devices & Services (joined 2023 from Microsoft, where he led Surface/Windows) | [S26] J |
| Strategic frame | Panay (July 2026): Amazon views AI devices as an ambient system following users across home, on the go, and eventually the car; moving "beyond screens and apps" | [S28] J, [S29] W |
| Custom silicon | CNBC (2026-07-02): Amazon is designing its own AI chips for Echo, Fire TV and future devices (article 403'd on fetch; headline + secondary summaries only) | [S28] J |
| Product tiers | Panay teased "entry, core, signature" quality tiers for future Alexa gadgets | [S30] W |
| CES 2026 posture | Analyst: Amazon prioritized "faster interfaces, broader integrations, and expanded availability" over flagship hardware; Sidewalk, Alexa+, Fire TV act as connective tissue | [S31] W |

### 3.2 Stated goals & developer-relations changes

| Change / goal | Fact | Src |
|---|---|---|
| Appstore consolidation | Amazon Appstore for Android phones discontinued 2025-08-20 (no new Android-phone submissions after 2025-02-20); Appstore **continues** on Fire TV, Fire Tablet, Fire TV built-in; Amazon Coins discontinued | [S32] P |
| Multi-OS | "We've always been a multi-OS company" — Fire OS continues alongside Vega OS | [S33] P |
| AI-assisted dev tooling | Amazon Devices Builder Tools (MCP server + Agent Skills) launched 2026-05-20 to make coding agents "aware of specialized Fire TV knowledge" | [S34] P |
| Consolidated developer front door | Single hackathon spanning four device platforms + AWS; resources hub on developer.amazon.com, GitHub `amazonappdev`, dev.to `amazonappdev`, community forum | [S3] P |
| Feedback loop | Friction logs + feedback routed to product teams (hackathon's explicit "Shape" goal) | [S1][S3] P |

### 3.3 What this means for a hackathon entrant (Sponsor)

- **[Inference]** The name is the thesis: **Build** (working demo) → **Ship** (demo-ready, store-grade) → **Shape** (feedback). The friction log is not optional garnish; it is the sponsor's primary data-collection objective, and it is worth up to 10%.
- **[Inference]** Panay's "ambient, follows you across contexts" framing rewards entries that span devices (e.g., Bee outside the home → Alexa+ inside → Fire TV/Ring surfaces), even though submissions are filed under one primary track.
- **[Inference]** Using Amazon Devices Builder Tools with an AI coding agent — and logging its friction — hits two sponsor goals at once.

---

## 4. Fire TV (Fire OS + Vega OS)

### 4.1 Mission / positioning

| Item | Fact | Src |
|---|---|---|
| Problem statement | Amazon cites research: U.S. customers spend ~12 minutes searching for content (up from 10.5 in 2023); redesign aims to cut discovery friction | [S35] P |
| Scale | aboutamazon: >300M Fire TV devices sold globally; Amazon Ads page: >200M devices sold (older figure — see Verification notes) | [S35] P, [S36] P |
| New UI | Began rollout Feb 2026; worldwide on current-gen Sticks, Cube, Ember TVs by 2026-06-22; up to ~30% faster; organized by movies/TV/sports; app pinning 6 → 20 | [S35] P, [S31] W |
| Hardware | Amazon Ember Artline lifestyle TV (CES 2026): matte 4K QLED, Omnisense presence detection, AI art recommendations | [S35] P |

### 4.2 Vega OS

| Item | Fact | Src |
|---|---|---|
| Launch | Announced 2025-09-30 with Fire TV Stick 4K Select; Vega Developer Tools in open beta | [S33] P |
| Design goals | Built specifically for Amazon devices; responsive, efficient; scales from Sticks to Echo Show with on-device AI | [S33] P |
| Framework | React Native for Vega (RN 0.72) and Vega WebView; common RN/web libraries preloaded in OS → smaller apps, consistent performance | [S33] P |
| Roadmap signal | Amazon Developer (X): Vega OS will power all future streaming media players | [S37] P |
| Constraint | Vega cannot run Android APKs; consumer sideloading blocked (developers can sideload to registered devices) | [S38] W |
| Docs version | Vega SDK docs at v0.24 as of retrieval | [S34][S39] P |

### 4.3 Current strategic priorities

| Priority | Fact | Src |
|---|---|---|
| AI-enhanced viewing via Alexa+ | Alexa+ free on compatible Fire TV for all U.S. customers; conversational search by mood/genre/actor; jump-to-scene on Prime Video; smart-home + Ring camera panel | [S40][S35] P |
| Engagement | Nearly 2x conversations vs. original Alexa on Fire TV; top recommendation chosen "over 40% more" often | [S40] P |
| Advertising | Fire TV sponsored tiles / Feature Rotator placements; interactive ads across Prime Video and Fire TV; Prime Video ads expanding to new countries in 2026; Prime Video avg monthly ad-supported reach >315M | [S36][S41] P |
| Developer tooling | Amazon Devices Builder Tools: MCP server (npm `@amazon-devices/amazon-devices-buildertools-mcp`) + Agent Skills; full Vega support, limited Fire OS; covers onboarding, IAP integration, perf/crash debugging, doc retrieval; works with Claude Code, Cursor, Kiro, Cline, Copilot, Amazon Q | [S34][S39] P |
| Early-adopter proof | Builder Tools blog quotes Paramount (days → hours for log analysis) and Sony LIV (IAP weeks → ~3 hours) | [S34] P |

### 4.4 What this means for a hackathon entrant (Fire TV)

- **[Inference]** Vega OS + React Native is the strategic path (all future sticks); Fire OS Android is supported but is the legacy lane. A Vega app signals alignment and yields higher-value friction data (young SDK, v0.24).
- **[Inference]** Sponsor-named categories (AI-enhanced viewing, sports, fitness, family, multi-modal, computer vision) + the 12-minute discovery problem → strong fits: agentic content discovery, second-screen/multi-modal control, Ring camera tie-ins on TV, CV-driven fitness.
- **[Inference]** 10-foot UX, focus management, and remote navigation are *Design* criteria traps — the Callstack e-book exists on the resource list for this reason.
- **[Inference]** Build with Amazon Devices Builder Tools inside an AI coding agent and log where it helps/fails.

---

## 5. Alexa+

### 5.1 Mission / positioning

| Item | Fact | Src |
|---|---|---|
| Positioning | "smarter, more conversational, more capable"; less like technology, more like "an insightful friend" | [S42] P |
| Architecture | "Experts" — groups of systems, capabilities, APIs, instructions — orchestrating "tens of thousands of services and devices"; LLMs on Amazon Bedrock | [S42] P |
| Agentic example | Navigates the web, uses Thumbtack to find a provider, books repair, reports back | [S42] P |
| Availability | Available to all U.S. customers; free for Prime (from Feb 2026); $19.99/mo non-Prime; free limited tier on Alexa.com + app | [S43] P |
| Expansion | CES 2026: Alexa.com (web) with cross-device context; Samsung TVs, BMW (Alexa Custom Assistant), Bosch, Oura integrations | [S31] W, [S44] P |
| Engagement | Customers interact >2x vs. previous Alexa; Alexa+ users 2–3x engagement, ~50% more smart-home engagement in first month | [S43][S45] P |

### 5.2 Developer / partner platform

| Path | Fact | Src |
|---|---|---|
| Alexa+ for Builders | Three paths: **Category SDK** (reservations, food ordering, home services — "in weeks"), **MCP Toolkit** (bring existing MCP server), **Smart Home AI Toolkit** (generate integrations from device docs / NL) | [S46] P |
| Access status | "currently available to select partners working directly with our team" (i.e., partner/brand preview) | [S46] P |
| July 2026 launch | 2026-07-23 blog: smart-home AI toolkit, MCP adoption, Amazon Wallet payments; integrations in Preview; partners incl. Bosch, iRobot, Whirlpool, Yale; services incl. Canva, Headspace, Lyft, Priceline, Taskrabbit, Viator | [S45] P |
| MCP Toolkit mechanics | Alexa+ acts as MCP client; you return standard MCP responses, Alexa+ handles NLU, response generation, UI rendering | [S47] P |
| Spec requirement | Supports MCP **2025-11-25**; server **must** support Streamable HTTP | [S47] P |
| Onboarding | Add-on Agent Skill (agentic onboarding for Claude Code, Kiro, Codex, Cursor) or Alexa AI CLI | [S47] P |
| Vision line | Customers "book, order, pay, and confirm through natural conversation"; discovery based on customer context, not brand recognition | [S46] P |

### 5.3 What this means for a hackathon entrant (Alexa+)

- **[Inference]** The hackathon is effectively a wide-open preview of a partner-gated platform. A clean, spec-compliant MCP server is directly reusable by Amazon's team — high *Potential Impact*.
- **[Inference]** Amazon's stated vision (book/order/pay/confirm in conversation; context-based discovery) favors **transactional, multi-step tools** with good elicitation over read-only Q&A tools.
- **[Inference]** Tool descriptions and metadata matter: Alexa+ picks your tools by context, not brand — clear tool naming/descriptions/icons (icons are a 2025-11-25 feature) are part of *Design*.
- **[Inference]** Note MCP 2026-07-28 is now final (stateless, Tasks moved to an extension). Rules say "2025-11-25 or later" — building on 2025-11-25 is the safest match with Alexa+'s documented support; if you target 2026-07-28 features, log any compatibility friction.

---

## 6. Ring

### 6.1 Mission / positioning

| Item | Fact | Src |
|---|---|---|
| Mission | Siminoff restoring Ring's original mission to "make neighborhoods safer," using AI to supercharge it | [S48] J |
| Leadership | Jamie Siminoff (founder) returned as CEO in April 2025 after stepping away in 2023 | [S48] J |
| AI vision | Turn Ring from a video doorbell company into an AI-powered "intelligent assistant" for the home and beyond; features incl. fire alerts, unusual-event alerts, conversational AI | [S48][S49] J |
| Ambition | Siminoff has claimed AI + camera coverage could get "very close to zero out crime" in 12–24 months | [S48] J |

### 6.2 Developer platform (launched 2026)

| Item | Fact | Src |
|---|---|---|
| Launch | Ring Appstore + opened APIs to third parties, 2026-03-31; ~15 apps at launch; initially U.S.-only | [S50] J |
| Goal | Siminoff: "hundreds of apps in tens of verticals" by year end; AI unlocks "an incredible amount of long tail use cases" | [S50] J |
| APIs | Live video (WebRTC, RTSP), motion events, doorbell presses, device status, event history; REST + OAuth 2.0 account linking + HMAC-signed webhooks | [S51][S52] P |
| Vision APIs | Computer vision: object detection, anomaly detection, predictive alerting | [S51] P |
| Ring MCP Server | MCP for AI-assisted coding with live API docs/examples; supports Kiro, Claude, Cursor, Lovable, Replit, v0, Windsurf, Copilot | [S51] P |
| Business model | Ring takes 10% commission on partner sales; subscriptions, one-time or ad-supported apps allowed | [S50] J |
| Publishing path | Draft → Testing → Certification → Beta Rollout → Production; privacy & security questionnaire | [S51] P |
| Categories | Business intelligence/operations, elder care, pet wellness, home analytics | [S51] P |
| Privacy constraints | Ring prohibits Appstore apps with facial recognition or license-plate reading | [S50] J |

### 6.3 Context / risk

| Event | Fact | Src |
|---|---|---|
| Super Bowl 2026 backlash | "Search Party" AI pet-finding ad drew criticism (EFF, Sen. Markey); Ring cancelled planned Flock Safety integration (announced Oct 2025, never launched) on 2026-02-12 | [S53] J |
| Analyst read | Recommended Ring re-emphasize user privacy and controls | [S31] W |

### 6.4 What this means for a hackathon entrant (Ring)

- **[Inference]** Ring's growth thesis is now software/long-tail verticals; sponsor-listed categories (caretaking, accessibility, access control, business systems, IoT automation) are exactly the gaps "hundreds of apps" must fill.
- **[Inference]** Privacy is a first-order design constraint, not a footnote. Avoid anything resembling facial recognition, plate reading, or neighbor surveillance; showcase consent, data minimization, and customer control — this aligns with *Earn Trust* and the post-Flock posture.
- **[Inference]** Vision APIs + event webhooks + an agent (e.g., Strands on AgentCore) that *acts* on events is a natural double-dip with the AWS Builder mini-challenge.

---

## 7. Bee (Wearable AI)

### 7.1 Mission / positioning

| Item | Fact | Src |
|---|---|---|
| Acquisition | Amazon agreed to acquire Bee, July 2025 (announced by co-founder Maria de Lourdes Zollo; Amazon confirmed) | [S54] J |
| Product | Clip-on pin or bracelet ($49.99 at acquisition time) and Apple Watch app; listens (unless muted) to create summaries, reminders, to-dos | [S54][S55] J |
| Why Amazon bought it | To extend Amazon AI beyond the home; Zollo: Bee understands "outside the house," Alexa "inside the house" — "complementary friends"; Daniel Rausch: they will eventually integrate | [S55] J |
| Amazon vision | Personal AI companion across home, on the go, daily moments; "ambient AI" | [S56] P |
| Zollo quote | "The goal has always been bigger than a single device." | [S56] P |
| Features | Voice Notes, Actions (email/calendar), Daily Insights, Templates; audio processed then discarded | [S56] P, [S55] J |
| Privacy claim | Only the user can access their data; Amazon/Bee cannot access transcripts/summaries unless explicitly shared | [S56] P |

### 7.2 Developer platform (`docs.bee.computer`)

| Interface | Fact | Src |
|---|---|---|
| CLI (`bee-cli`) | Access/export conversations, facts, todos, journals to local Markdown; real-time streaming; local HTTP proxy | [S57] P |
| MCP server | Works with Claude, Claude Code, Codex; data stays local | [S57] P |
| Bee Skill | Agent Skill connecting agents to personal context; real-time awareness; end-to-end encryption | [S57] P |
| Tagline | "Your AI, your memory." | [S57] P |

### 7.3 What this means for a hackathon entrant (Bee)

- **[Inference]** Bee is the least mature, most exploratory platform — Amazon is still evaluating whether personal-memory devices go mainstream. Entries that **prove a daily-use value loop** (education, dev experience, productivity — the sponsor's named priorities) are directly answering Amazon's open question.
- **[Inference]** "Outside the home" + Alexa "inside the home" is Amazon's stated complementarity → Bee-context-to-Alexa+/Fire TV handoffs are strategically on-thesis.
- **[Inference]** Requirement to use *real* Bee/Apple Watch data means demo credibility depends on showing actual captured context; privacy-first local processing matches Bee's own positioning.

---

## 8. Devpost (Administrator)

| Item | Fact | Src |
|---|---|---|
| Mission | "Devpost's mission is to inspire developers to build great software." | [S58] P |
| Goals | Deadlines create urgency; learning by building; prizes without claiming developer IP; personal achievement | [S58] P |
| Customers | Corporations, non-profits, government agencies, universities | [S58] P |
| Role here | Legal administrator; runs submission, eligibility, judging logistics | [S2] P |

**[Inference]** Devpost's interests are submission completeness and clean judging. Practical implication: meet every submission requirement (video, repo, description, track selection) exactly as written — incomplete entries are the most common self-inflicted loss.

---

## 9. Adjacent / Referenced Organizations

### 9.1 Model Context Protocol (MCP) and the Agentic AI Foundation

| Item | Fact | Src |
|---|---|---|
| Stewardship | 2025-12-09: Anthropic donated MCP to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation; co-founded by Anthropic, Block, OpenAI; supported by Google, Microsoft, AWS, Cloudflare, Bloomberg | [S27][S59] P |
| Governance | Existing MCP governance and maintainers unchanged; decisions via SEP process | [S27] P |
| Adoption (Dec 2025) | 97M+ monthly SDK downloads; 10,000 active servers | [S27] P |
| Spec 2025-11-25 | Largest release since launch: tasks (experimental), elicitation/sampling improvements, extensions, OIDC discovery, icon metadata, incremental scope consent; Streamable HTTP as the remote transport | [S60] P, [S61] W |
| Spec 2026-07-28 | Final 2026-07-28: stateless protocol (no `initialize` handshake / session header), Tasks moved to an extension, MCP Apps (server-rendered UI), formal 12-month deprecation policy | [S62] P |

**What this means for an entrant [Inference]:** Alexa+ and Bee both lean on MCP. Target 2025-11-25 + Streamable HTTP for Alexa+ (documented support); treat 2026-07-28 as "later is allowed by the rules" but unverified against Alexa+'s client — a prime friction-log candidate.

### 9.2 Callstack

| Item | Fact | Src |
|---|---|---|
| Role | Referenced resource: *The Ultimate Guide to React Native TV Development* | [S3] P |
| Content | 10-foot UI, remote navigation, focus management, video playback, accessibility, testing, CI/CD; covers tvOS, Android TV, Tizen, webOS (Vega not explicitly named in page summary) | [S63] P |
| Self-description | React Native core contributors; founded 2016; open-source commitment | [S63] P |

**[Inference]** Callstack is a React Native consultancy, not a sponsor. Useful for Fire TV *Design* criterion (focus/navigation).

### 9.3 Hacktoberfest — **NOT affiliated**

| Item | Fact | Src |
|---|---|---|
| Affiliation | Amazon Developer states it is **not affiliated** with Hacktoberfest; open-source work during the hackathon may also count there | [S3][S4] P |
| Organizers | Major League Hacking (MLH) and DEV, in partnership with DigitalOcean | [S64] P |
| 2026 format | No longer counts pull requests; 300+ community events focused on open-source AI; change driven by AI-generated low-effort PR spam | [S64] P |

**[Inference]** Don't plan an Open Source mini-challenge entry around Hacktoberfest PR counts — that mechanic no longer exists.

---

## 10. Cross-Org Alignment Map

### 10.1 Org goals × judging criteria

Judging criteria are equally weighted [S2]; friction log adds up to +10% [S2]. Cells are **[Inference]** mappings grounded in the sourced goals above.

| Org | Tech Implementation | Design | Potential Impact | Quality of the Idea | Friction-log bonus (≤10%) |
|---|---|---|---|---|---|
| Amazon (parent) | Agentic, actually works (Bias for Action, Highest Standards) | Customer-first, simple (Invent & Simplify) | Measurable customer outcome (Customer Obsession) | Think Big, not a clone | Dive Deep evidence |
| AWS | Strands / AgentCore / Kiro Crew / Bedrock used meaningfully; Policy + Evals for trust | Clean agent architecture | Reusable pattern for devices + cloud agents | Agents that act, with guardrails | Kiro Crew (new, Aug 2026), AgentCore, AWS MCP Server |
| Sponsor (Devices & Services) | Cross-device, ambient | Cohesive multi-surface UX | Feeds platform adoption | Ambient "follows you" concept | **Primary objective** of the event ("Shape") |
| Fire TV | Vega OS + React Native; Builder Tools MCP | 10-foot UI, focus nav, speed | Cuts content-discovery time; sports/fitness/family | AI-enhanced viewing, multi-modal, CV | Vega SDK v0.24, Builder Tools |
| Alexa+ | Spec-compliant MCP 2025-11-25, Streamable HTTP; or Agent Skill | Tool naming/descriptions/elicitation; voice + visual | Transactional services ("book, order, pay, confirm") | Context-based discovery, multi-step tasks | MCP Toolkit, Alexa AI CLI, add-on Agent Skill |
| Ring | Ring APIs + Vision APIs + webhooks | Privacy-forward, consented | Long-tail verticals (caretaking, accessibility, SMB) | New vertical beyond security | Developer portal, simulator, certification flow |
| Bee | Real Bee/Apple Watch data via CLI/MCP/Skill | Local-first, private | Daily-use loop (education, dev-ex, productivity) | Outside-home context → action | Young platform; CLI/MCP/Skill |
| Devpost | Complete, reproducible submission | Clear demo video | — | — | — |
| MCP / AAIF | Correct spec version, transport, auth | Tool metadata, icons | Interop across hosts | — | Version-compat gaps (2025-11-25 vs 2026-07-28) |

### 10.2 Strongest overlapping themes

| # | Theme | Orgs aligned | Evidence |
|---|---|---|---|
| 1 | **Agentic AI that acts, via MCP** | Amazon, AWS, Alexa+, Ring, Bee, Fire TV (Builder Tools), MCP/AAIF | Jassy agent stack [S7]; Alexa+ MCP Toolkit [S47]; Ring MCP server [S51]; Bee MCP [S57]; ADBT MCP [S34]; AWS MCP Server [S23] |
| 2 | **Agent Skills as a distribution unit** | Alexa+, Bee, Fire TV, AWS | Alexa+ add-on Agent Skill [S47]; Bee Skill [S57]; ADBT Agent Skills [S34]; AWS Agent Toolkit skills [S23] |
| 3 | **Ambient, multi-device orchestration** | Devices & Services, Alexa+, Bee, Fire TV, Ring | Panay ambient framing [S28]; Bee "outside"/Alexa "inside" [S55]; Ring cameras on Fire TV panel [S35] |
| 4 | **Developer feedback shaping products** | Sponsor, all device teams, AWS | Friction-log bonus [S2]; feedback "go straight to the teams" [S3]; Heroes Summit feedback focus [S14] |
| 5 | **AI coding agents as the dev workflow** | AWS (Kiro, Kiro Crew), Fire TV, Ring, Alexa+ | ADBT supports Claude Code/Cursor/Kiro [S34]; Ring lists Kiro/Claude/Cursor [S51]; Alexa+ onboarding skill for coding agents [S47] |
| 6 | **Trust, privacy, governance** | Amazon (Earn Trust), AWS (AgentCore Policy/Evals), Ring (no face/plate), Bee (user-only data) | [S5][S16][S50][S56] |
| 7 | **Open standards & open source** | AWS (Strands, Kiro Crew, Dogwood Apache 2.0), MCP/AAIF, Open Source mini-challenge | [S17][S19][S14][S27][S1] |

### 10.3 Highest-alignment project archetypes **[Inference]**

1. Alexa+ MCP server (2025-11-25, Streamable HTTP) for a transactional service, backed by a Strands agent on AgentCore with Policy guardrails → Alexa+ track + AWS Builder mini-challenge + friction log on MCP Toolkit.
2. Vega OS (React Native) Fire TV app for AI-enhanced viewing / sports / fitness, built with Amazon Devices Builder Tools in a coding agent → Fire TV track + friction log on Vega SDK v0.24 and ADBT.
3. Ring caretaking/accessibility app using Vision APIs + event webhooks, privacy-by-design, agent acts on events → Ring track + AWS Builder.
4. Bee productivity/education loop using real captured context via Bee MCP/Skill, handing off to Alexa+ or Fire TV → Bee track, strongest on Amazon's "ambient" thesis.
5. Any of the above released open-source during the window → Open Source mini-challenge (independent of Hacktoberfest).

---

## 11. Verification Notes (claims to spot-check or that could not be fully verified)

| Claim | Issue |
|---|---|
| Jassy letter Alexa+ stats ("talking twice as much", +25% music, +50% smart home) and FY2025 financials ($717B revenue etc.) | Extracted via automated summary of [S7]; re-read the letter before quoting |
| Fire TV devices sold: 300M+ [S35] vs 200M+ [S36] | Two official pages disagree; the Amazon Ads page is likely older |
| Kiro Crew internal codename "MeshClaw" | Journalistic only [S20]; not seen on kiro.dev |
| Panay "Leo is the invisible thread" / late-2027 Echo+Ring integration | Web-tier aggregator only [S29]; CNBC primary article returned 403 |
| Panay "entry, core, signature" tiers | Web-tier only [S30] |
| "Vega OS will power all future SMPs" | From Amazon Developer X post (search snippet) [S37]; not fetched directly |
| Consumer sideloading blocked on Vega | Web-tier only [S38] |
| Ring 10% commission; face/plate prohibition | Journalistic [S50]; not confirmed on developer.ring.com |
| Ring "simulators" | Named in hackathon rules [S1] but not described in the Ring get-started doc [S52] |
| Whether Alexa+ accepts MCP 2026-07-28 servers | Alexa+ docs state 2025-11-25 support only [S47]; rules allow "or later" [S1]; unresolved |
| Hackathon judging-criteria weights | Rules say equally weighted [S2]; overview page gave no weights — RESOLVED in favor of rules |
| Hacktoberfest disclaimer | Found on resources page / community posts [S3][S4], not in official rules [S2] |
| "Alexa for Shopping" 350M customers | Reported via earnings summary [S9]/[S11]; verify against release PDF |
| Specific Kiro GA date, SageMaker 2026 roadmap | Not researched to primary depth; omitted |

---

## 12. Source List (all retrieved 2026-09-28)

| ID | Tier | Title / description | URL |
|---|---|---|---|
| S1 | P | Build, Ship, Shape — Devpost overview | https://amazonappdev2026.devpost.com/ |
| S2 | P | Official Rules | https://amazonappdev2026.devpost.com/rules |
| S3 | P | Resources page | https://amazonappdev2026.devpost.com/resources |
| S4 | P | Amazon Developer Community announcement | https://community.amazondeveloper.com/t/build-ship-shape-amazon-developer-hackathon/29097 |
| S5 | P | Amazon Leadership Principles | https://www.aboutamazon.com/about-us/leadership-principles |
| S6 | P | About Amazon — Who we are | https://www.aboutamazon.com/about-us |
| S7 | P | Andy Jassy's 2025 Letter to Shareholders | https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2025-letter-to-shareholders |
| S8 | J | CNBC — Jassy shareholder letter | https://www.cnbc.com/2025/04/10/amazon-ceo-andy-jassys-2025-shareholder-letter.html |
| S9 | P | Amazon Q2 2026 earnings report | https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report |
| S10 | P | Jassy on AWS growth, Q2 2026 | https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-revenue-growth-q2-2026-earnings |
| S11 | J | Futurum — Amazon Q2 2026 | https://futurumgroup.com/insights/amazon-q2-2026-aws-momentum-accelerates-as-ai-investment-climbs/ |
| S12 | P | About Amazon — Amazon Web Services | https://www.aboutamazon.com/what-we-do/amazon-web-services |
| S13 | P | AWS ML Blog — production-ready AI agents at scale (2025-07-16) | https://aws.amazon.com/blogs/machine-learning/enabling-customers-to-deliver-production-ready-ai-agents-at-scale/ |
| S14 | P | AWS Weekly Roundup 2026-08-10 (Kiro Crew, Dogwood, Web Search) | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-heroes-summit-web-search-on-amazon-bedrock-dogwood-kiro-crew-and-more-august-10-2026/ |
| S15 | P | Top announcements, What's Next with AWS 2026 | https://aws.amazon.com/blogs/aws/top-announcements-of-the-whats-next-with-aws-2026/ |
| S16 | J | Constellation Research — AgentCore policy/evaluations | https://www.constellationr.com/insights/news/aws-adds-ai-agent-policy-evaluation-tools-amazon-bedrock-agentcore |
| S17 | P | AWS Open Source Blog — Strands Agents 1.0 | https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/ |
| S18 | P | Strands Agents site | https://strandsagents.com/ |
| S19 | P | Kiro blog — Introducing Kiro Crew | https://kiro.dev/blog/introducing-kiro-crew/ |
| S20 | J | SiliconANGLE — Kiro Crew launch | https://siliconangle.com/2026/08/04/aws-launches-kiro-crew-autonomous-agentic-orchestrator-24-7-code-development/ |
| S21 | J | InfoQ — AWS open sources Kiro Crew | https://www.infoq.com/news/2026/08/kiro-crew-coding-agents/ |
| S22 | J | SiliconANGLE — Garman re:Invent 2025 keynote | https://siliconangle.com/2025/12/03/five-thoughts-ceo-matt-garmans-keynote-aws-reinvent/ |
| S23 | P | AWS News Blog — AWS MCP Server GA | https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/ |
| S24 | P | AWS What's New — Announcing AWS Builder Center | https://aws.amazon.com/about-aws/whats-new/2025/07/aws-builder-center-available/ |
| S25 | P | AWS What's New — Free Tier $200 credits | https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/ |
| S26 | J | CNBC — Amazon devices event 2025 | https://www.cnbc.com/2025/09/30/amazon-devices-alexa-echo-kindle.html |
| S27 | P | MCP Blog — MCP joins the Agentic AI Foundation | https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ |
| S28 | J | CNBC — Amazon designing own AI chips for devices (403 on fetch) | https://www.cnbc.com/2026/07/02/amazon-ai-chips-devices.html |
| S29 | W | WindowsNews — Panay ambient AI plan | https://windowsnews.ai/article/panos-panay-reveals-amazons-plan-to-make-devices-disappear-with-ai-custom-silicon-and-satellite-inte.433812 |
| S30 | W | Thurrott — Panay quality tiers | https://www.thurrott.com/amazon/318571/panos-panay-details-amazons-new-consumer-product-strategy |
| S31 | W | Futurum — Amazon CES 2026 | https://futurumgroup.com/insights/amazon-ces-2026-do-ring-fire-tv-and-alexa-add-up-to-one-strategy/ |
| S32 | P | Amazon Developer — Upcoming changes to Appstore for Android | https://developer.amazon.com/apps-and-games/blogs/2025/02/upcoming-changes-to-amazon-appstore-for-android-devices-and-coins-program |
| S33 | P | Amazon Developer — Announcing Vega OS / Vega Developer Tools | https://developer.amazon.com/apps-and-games/blogs/2025/09/announcing-vega-os |
| S34 | P | Amazon Developer — Introducing Amazon Devices Builder Tools | https://developer.amazon.com/apps-and-games/blogs/2026/05/introducing-amazon-builder-tools |
| S35 | P | About Amazon — Fire TV upgrade & Ember Artline | https://www.aboutamazon.com/news/devices/new-fire-tv-upgrades-features-2026 |
| S36 | P | Amazon Ads — Fire TV ads | https://advertising.amazon.com/channels/fire-tv |
| S37 | P | Amazon Developer on X — Vega OS | https://x.com/AmazonAppDev/status/1973093688973860960 |
| S38 | W | TechMyMoney — Vega sideloading | https://techmymoney.com/2026/07/05/fire-tv-stick-sideloading-is-ending-on-amazons-new-vega-os-devices/ |
| S39 | P | Vega docs — Set up Amazon Devices Builder Tools | https://developer.amazon.com/docs/vega/0.24/mcp-server.html |
| S40 | P | About Amazon — Alexa+ on Fire TV at no additional cost | https://www.aboutamazon.com/news/devices/alexa-plus-fire-tv-free-ai |
| S41 | P | Amazon Ads — Prime Video ads 2026 | https://advertising.amazon.com/library/news/prime-video-advertising-2026 |
| S42 | P | About Amazon — Introducing Alexa+ | https://www.aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence |
| S43 | P | About Amazon — Alexa+ available to everyone in the US | https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us |
| S44 | P | About Amazon — Amazon at CES 2026 | https://www.aboutamazon.com/news/devices/amazon-ces-2026-fire-tv-ring-alexa-plus |
| S45 | P | Alexa+ blog — new ways to build experiences (2026-07-23) | https://developer.amazon.com/alexaplus/blogs/2026/07/alexa-plus-new-ways-to-build-experiences |
| S46 | P | Alexa+ for Builders | https://developer.amazon.com/alexaplus/ |
| S47 | P | Alexa+ MCP Toolkit Overview | https://developer.amazon.com/docs/alexaplus/add-ons/mcp-toolkit-overview.html |
| S48 | J | PetaPixel / CNBC — Siminoff AI & crime | https://petapixel.com/2025/10/23/ring-ceo-claims-ai-powered-cameras-can-eliminate-most-crime/ |
| S49 | J | TechCrunch — Ring's intelligent assistant era | https://techcrunch.com/2026/01/13/ring-founder-details-the-camera-companys-intelligent-assistant-era |
| S50 | J | TechCrunch — Ring app store bets on AI | https://techcrunch.com/2026/03/31/ring-app-store-bets-on-ai-to-go-beyond-home-security/ |
| S51 | P | Ring Developer | https://developer.ring.com/ |
| S52 | P | Ring get-started docs | https://developer.amazon.com/docs/ring/get-started.html |
| S53 | J | CNBC — Ring cancels Flock partnership | https://www.cnbc.com/2026/02/12/amazons-ring-cancels-flock-partnership-amid-super-bowl-ad-backlash.html |
| S54 | J | TechCrunch — Amazon acquires Bee | https://techcrunch.com/2025/07/22/amazon-acquires-bee-the-ai-wearable-that-records-everything-you-say/ |
| S55 | J | TechCrunch — Why Amazon bought Bee | https://techcrunch.com/2026/01/12/why-amazon-bought-bee-an-ai-wearable/ |
| S56 | P | About Amazon — Building Bee at Amazon | https://www.aboutamazon.com/news/devices/bee-amazon-wearable-ai-device-new-features |
| S57 | P | Bee developer docs | https://docs.bee.computer/ |
| S58 | P | Devpost — About | https://info.devpost.com/about |
| S59 | P | Linux Foundation — AAIF formation press release | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation |
| S60 | P | MCP Blog — One Year of MCP: November 2025 spec release | https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/ |
| S61 | W | WorkOS — MCP in 2026 | https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026 |
| S62 | P | MCP Blog — 2026-07-28 specification release candidate | https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ |
| S63 | P | Callstack — Ultimate Guide to React Native TV Development | https://www.callstack.com/ebooks/the-ultimate-guide-to-react-native-tv-development |
| S64 | P | Hacktoberfest — Questions | https://hacktoberfest.com/questions/ |
