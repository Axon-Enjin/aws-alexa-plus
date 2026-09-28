# TRACK 2 — Alexa+ · Deep Research Meta Prompt

> **How to use:** Paste everything inside the `PROMPT` block into a deep-research tool (Gemini Deep Research, ChatGPT Deep Research, Perplexity Deep Research, Claude Research). Fill the `{{VARIABLES}}` first, or leave them as-is and the researcher will pick defaults. Run it once for a broad scan, then re-run Part B/C against the pitch you pick.
>
> **Companion files:** [hackathon.md](hackathon.md) (rules), [ORG.md](ORG.md) (sponsor goals).

---

````
PROMPT
======

# ROLE
You are a senior market-research analyst and product strategist specialising in
conversational AI, agentic commerce, and voice platforms. You combine a strategy
consultant's rigor (MBB / Big 4 style) with a hackathon judge's eye. You report
evidence first, then give your judgment, and you always label which is which.

# MISSION
Find, validate, and size the single best problem to build for in the Alexa+ track
of the "Build, Ship, Shape: Amazon Developer Hackathon". Then generate three
genuinely distinct solution pitches for it, and make the market and business case.
The output must help a builder pick an idea that scores highly on all four
equally weighted judging criteria AND could plausibly become a real Alexa+
integration (add-on) after the hackathon.

# VARIABLES (use the defaults if left blank)
- {{BUILDER_PROFILE}}  = solo or small team, AI-native, agent-assisted development
- {{HOME_MARKET}}      = Philippines-based builder; primary launch market = United States (Alexa+ availability). Flag Philippines/SEA differences where they matter.
- {{FOCUS_AREA}}       = open. If blank, evaluate across service categories.
- {{TIME_LEFT}}        = submission closes Oct 23, 2026, 12:00 PM PDT

# TRACK CONTEXT (treat as given; verify anything marked VERIFY)
- Requirement: a self-hosted MCP server (spec 2025-11-25 or later, Streamable HTTP
  transport) or an Agent Skill. Alternative path: a simulated Alexa+ experience in a
  web app using any agentic tool (repo must contain the simulation source).
- Gated Alexa+ Add-on tools (Category SDK, MCP Toolkit, CLI, Web Simulator) are NOT
  available to participants. Builders demo through their own front end or simulator.
- The repo must import and actually call the MCP server or Agent Skill at runtime,
  not just mention it.
- Judging (equally weighted, scored 1–5 each): Tech Implementation, Design, Potential
  Impact, Quality of the Idea. Friction logs add up to a 10% bonus.
- Judges call these OBVIOUS: a single-turn Q&A bot; a basic MCP wrapper around an
  existing API.
- Judges call these CREATIVE: an agentic workflow that orchestrates across services
  autonomously; a context-aware add-on that keeps state across sessions; purchasing
  capabilities; media support (cards, carousels); MCP Apps; Agent Skills.
- Sponsor signals (VERIFY):
  - Alexa+ is available to all U.S. customers (free with Prime).
  - It is built on "experts" that orchestrate services, with LLMs on Amazon Bedrock.
  - Amazon's vision is that customers "book, order, pay, and confirm through natural
    conversation," with discovery driven by customer context rather than brand
    recognition.
  - The Alexa+ MCP Toolkit supports spec 2025-11-25 over Streamable HTTP.
  - Launch partners include Canva, Headspace, Lyft, Priceline, Taskrabbit, Viator,
    Bosch, iRobot, Whirlpool, and Yale.
  - Amazon Wallet payments for add-ons were announced July 2026.
  - MCP spec 2026-07-28 is final (stateless; Tasks moved to an extension); whether
    Alexa+ supports it is unverified.
- Constraints: voice-first and multi-modal (Echo Show screens, Fire TV, Alexa.com,
  the app); authentication and account linking (OAuth); payments and consent;
  latency; hallucination risk on transactional actions.

# RESEARCH RULES (non-negotiable)
1. Every factual claim gets: source name, URL, publication date, and a source tier:
   - T1 Primary: government statistics, company filings (10-K, earnings calls),
     official company blogs and docs, protocol specs, peer-reviewed studies
   - T2 Expert: MBB / Big 4 reports, industry analysts (Gartner, Forrester, IDC,
     Juniper Research, eMarketer, CB Insights, Menlo Ventures, a16z / Sequoia state-
     of-AI reports), academic preprints (arXiv)
   - T3 Journalistic: Reuters, Bloomberg, FT, WSJ, The Verge, TechCrunch, The
     Information, Voicebot.ai
   - T4 Web: blogs, forums, Reddit, app reviews, vendor marketing
2. Label every statement [FACT] (sourced) or [INFERENCE] (your reasoning).
3. Never invent a number. If a figure can't be found, write `DATA GAP — <what is
   missing> — <how to get it>` and keep going. A visible gap beats a plausible guess.
4. When sources conflict, show both and mark the conflict `RESOLVED (<why>)` or
   `UNRESOLVED`.
5. Prefer data from 2024–2026. Flag anything older than 2023 as `STALE`. Legacy
   Alexa Skills data (pre-Alexa+) must be labelled LEGACY. It is a cautionary signal,
   not a baseline.
6. Paywalled reports: use the publisher's free executive summary, press release, or
   a reputable citing article, and say which one you used.
7. Do not estimate build effort in hours, sprints, or headcount. Describe scope as a
   list of components only.

# SOURCE MAP (search these deliberately)
- Big 3 (MBB):
  - McKinsey: agentic AI and agentic commerce, the state of AI, the economic
    potential of generative AI, consumer AI adoption
  - BCG: AI agents, consumer AI, the future of retail/commerce
  - Bain: technology report (AI agents), customer experience
- Big 4:
  - Deloitte: TMT Predictions (gen-AI agents), Connected Consumer survey, state of
    gen AI in the enterprise
  - PwC: AI agent survey, consumer insights survey
  - EY: AI pulse / consumer index
  - KPMG: trust in AI studies
- Industry data:
  - Juniper Research / eMarketer (voice commerce, smart-speaker users)
  - Edison Research + NPR "Smart Audio Report" (smart-speaker ownership)
  - Voicebot.ai consumer surveys
  - Gartner (agentic AI hype cycle and predictions), Forrester
  - Menlo Ventures (state of consumer/enterprise gen AI)
  - Similarweb (web traffic for incumbents)
- Primary / protocol:
  - Amazon 10-K and earnings calls, aboutamazon.com Alexa+ posts,
    developer.amazon.com Alexa+ builder docs
  - modelcontextprotocol.io spec and changelog; Agentic AI Foundation (Linux
    Foundation) announcements
  - Anthropic / OpenAI / Google agent announcements
- Category-specific (pick the ones that match candidate problems):
  - Home services: Angi, Thumbtack, Taskrabbit investor data
  - Travel: Skift, Phocuswright
  - Food: NRA (National Restaurant Association), Technomic
  - Health: CDC, KFF
  - Finance: Fed consumer surveys, CFPB
  - Philippines flag: PSA Philippines, DICT
- Competitive and ecosystem data:
  - MCP registries (official MCP registry, Smithery, mcp.so, Glama), GitHub stars/usage
  - Crunchbase, PitchBook, CB Insights (funding)
  - Competing assistants: Google Gemini, Apple Siri / Apple Intelligence, ChatGPT
    (agent mode / apps), Microsoft Copilot, Samsung Bixby, Meta AI
- Voice of customer: r/alexa, r/amazonecho, r/smarthome, r/LocalLLaMA (agent
  builders), r/mcp, Amazon customer reviews of Echo devices, app-store reviews of
  partner apps

---

# PART A — PROBLEM (the 5 tests)

Step A0 — Build a candidate list of 8–12 problems. Each must be a multi-step,
real-world job that is painful to do through apps or websites today, and that an
agent could complete through conversation. Write each problem as:
"<Specific person> struggles to <job> because <root cause>, which costs them <pain>."

Seed candidates to test (add your own):
- Coordinating household logistics across calendars, errands, and multiple members
- Booking local services (repairs, cleaning, appointments) with comparison and follow-up
- Managing recurring purchases, subscriptions, and bills without surprises
- Planning trips or events that span several providers (flights, stays, dining,
  tickets)
- Caregiving admin for aging parents (medications, appointments, deliveries)
- Small business owners handling bookings, orders, and customer questions by voice
- Accessibility: people with low vision, limited mobility, or low digital literacy
  navigating services
- Learning and tutoring that remembers progress across sessions

Step A1 — Score each candidate on the 5 tests. For every test, answer the questions,
cite evidence, and give a score from 1 to 5 with a one-line justification.

1. IS IT REAL? Does the problem exist in behaviour, not just in opinion?
   - Evidence of the behaviour: time-use data, surveys with n and method stated,
     transaction volumes
   - Voice of customer: at least 5 verbatim complaints from forums or reviews
     (quote under 25 words each, with a link)
   - Existing workarounds (spreadsheets, assistants, concierge services, human help)
   - Pass bar: at least one T1/T2 source AND observable workaround behaviour

2. IS IT LARGE? How many people have it, and how often?
   - Number of affected U.S. households or individuals, and frequency
   - Alexa+-reachable share: Alexa+ users (VERIFY the latest number) × incidence.
     Show the formula.
   - Transaction volume or spend flowing through the job each year
   - Pass bar: millions of affected users, or a smaller segment with high spend

3. IS IT SIGNIFICANT? How much does it hurt?
   - Cost in time, money, errors, missed obligations, or stress. Quantify.
   - What people already pay to offload it (concierge, virtual assistants, premium
     tiers)
   - Pain intensity: "hair on fire" or "nice to have"?
   - Pass bar: a measurable cost, or evidence that people already pay to offload it

4. IS IT RELEVANT? Does it fit this sponsor, this platform, and this builder?
   - Does it match Amazon's stated Alexa+ vision (book, order, pay, confirm; context-
     based discovery; smart home)? Cite Amazon sources.
   - Is voice/conversation genuinely better than an app for this job? If a
     three-tap app flow wins, fail.
   - Does it benefit from MCP specifically (tools, resources, elicitation, state)
     rather than a simple API call?
   - Can it be built as a self-hosted MCP server or Agent Skill and demoed within
     {{TIME_LEFT}}, without the gated Alexa+ tools?
   - OBVIOUS or CREATIVE per the track rubric?

5. IS IT URGENT? Why now?
   - Catalysts: Alexa+ general availability, MCP standardisation under the Linux
     Foundation, Amazon Wallet payments, agentic commerce adoption, falling LLM costs
   - Competitor timing: are Google, Apple, OpenAI, or Microsoft shipping the same
     agent capability? Does that close the window or validate the market?
   - Pass bar: a dated catalyst within the last 18 months

Step A2 — Output a PROBLEM SCORECARD table:
| # | Problem statement | Real | Large | Significant | Relevant | Urgent | Total /25 | Key evidence | Biggest doubt |
Rank the candidates. Pick the top problem (and one runner-up). Explain the pick in
3 sentences, name the strongest counterargument, and say what evidence would change
the pick.

---

# PART B — SOLUTION (Pixar "Three Pitches" rule)

Do not settle for the first idea. For the chosen problem, develop THREE pitches that
are meaningfully different from each other. Each pitch must differ from the others
on at least TWO of these axes:
- Who: primary user (individual vs. household vs. small business vs. caregiver)
- How: core mechanism (transactional agent that books and pays vs. memory/state
  keeper across sessions vs. orchestrator across several MCP servers vs. rich
  multi-modal experience with MCP Apps, cards, and carousels)
- Where: surface (Echo voice-only vs. Echo Show / Fire TV screen vs. Alexa.com web
  vs. cross-device with Ring/Bee)
- Model: business model (transaction fee vs. subscription vs. lead generation for
  providers vs. B2B MCP-as-a-service for brands that want an Alexa+ presence)

Pitch archetypes to force spread:
- Pitch 1 — "The Safe Bet": a focused, spec-perfect MCP server for one high-value
  transactional job
- Pitch 2 — "The Platform Play": the one most aligned with Amazon's strategy
  (multi-step, context-aware, cross-service or cross-device, uses payments or smart
  home)
- Pitch 3 — "The Wild Card": a surprising reframe of the problem (a new user group,
  an inverted flow, or an MCP-native capability no app has)

For EACH pitch provide:
- Name + one-line pitch ("For <ICP> who <problem>, <name> is a <category> that
  <key benefit>. Unlike <alternative>, it <differentiator>.")
- The hero moment: the first 30 seconds of the demo video, turn by turn (what the
  user says, what the agent does, what the screen shows)
- Conversation design: the happy path plus 2 failure/repair paths (ambiguity,
  missing info → elicitation, confirmation before spending money)
- MCP design: a list of tools (name, purpose, inputs), resources, prompts, and
  state/session strategy; transport (Streamable HTTP); auth approach; the spec
  version and why
- Tech stack: optional AWS services (Bedrock, AgentCore incl. Policy/Evaluations,
  Strands, Kiro/Kiro Crew) for the AWS Builder mini challenge; which component can
  be released open source for the Open Source mini challenge
- Scope as components (no time estimates): must-have for the demo vs. cut list
- OBVIOUS vs CREATIVE self-check against the judges' examples
- Top 3 risks, including trust/safety on purchases, hallucinated actions, latency,
  and any case where a conventional app would be faster or more reliable
- Evidence it would work: analogous products, adoption data, studies

Then output a PITCH COMPARISON MATRIX (score 1–5):
| Pitch | Tech Implementation | Design | Potential Impact | Quality of Idea | Buildability | Strategic fit with Amazon | Friction-log potential | Total |
Recommend one pitch. State why in one sentence, defend it, name the strongest
counterargument, and say what would flip the recommendation.

---

# PART C — VALUE (market value + business value)

Complete this for the recommended pitch. Add short notes on the other two.

C1. IDEAL CUSTOMER PROFILE (ICP)
There are two sides. Profile both:
- End user: demographics, household, Alexa devices owned, Prime status, tech
  comfort, the jobs they delegate
- Integration buyer (if B2B/B2B2C): the brand or service provider that would pay to
  be reachable through Alexa+. Include company size, vertical, budget owner (e.g.
  VP Digital / Head of Partnerships), buying triggers, and procurement process.
- Psychographics and jobs-to-be-done (functional, emotional, social)
- Trigger events; where they hang out; willingness to pay (with sources)
- Secondary ICP and anti-ICP

C2. COMPETITIVE MARKET ANALYSIS
- Direct: existing Alexa+ launch partners in the category; other MCP servers for
  the same job (search MCP registries)
- Assistant platforms: Google Gemini, Apple Siri / Apple Intelligence, ChatGPT
  (agents, apps), Microsoft Copilot, Meta AI, Samsung. What each can do for this
  job today.
- Vertical apps and concierge services (the status quo)
- Competitor table:
  | Competitor | Surface | Offer | Price/model | Traction (sourced) | Strengths | Weaknesses | Recent moves |
- Platform-owner risk: could Amazon build this as a first-party "expert"? How does
  the pitch survive that (vertical depth, data, provider network), or become the
  partner Amazon prefers?
- A 2×2 positioning map (choose axes that reveal white space) and the chosen white space
- Moat candidates: provider network, proprietary data, cross-session memory,
  integrations, trust

C3. MARKET SIZING — TAM / SAM / SOM
Do BOTH approaches, then reconcile them:
- Top-down: total category spend (e.g. home services, travel booking, grocery),
  narrowed to the share addressable through conversational/agentic channels (cite
  agentic-commerce forecasts and label them as forecasts), then to Alexa+.
- Bottom-up: Alexa+ users × category incidence × adoption rate × revenue per user
  or take rate per transaction. State every assumption.
- If B2B: number of brands in the vertical × adoption × annual contract value.
- TAM / SAM / SOM table with formulas. Mark every unsourced layer as DATA GAP.
- Philippines/SEA flag: Alexa+ availability outside the U.S.; is there a local
  analog market?

C4. BUSINESS VALUE
- For the end user: the measurable outcome (time saved, errors avoided, money saved)
- For Amazon: which stated goals it advances (Alexa+ engagement, commerce
  conversion, Amazon Wallet, smart home, the partner ecosystem). Cite Amazon sources.
- For the provider/brand: incremental bookings, lower CAC, a new channel
- For AWS (if used): the showcase value of the agent architecture
- Revenue model options: take rate, subscription, provider lead fees, B2B MCP
  hosting/integration fees. Note any Amazon rules on monetising add-ons (VERIFY).
- Unit economics sketch: revenue per transaction, inference cost per conversation,
  hosting cost, CAC. Show the inputs; mark any gaps.
- Go-to-market: becoming an Alexa+ partner (what the path is, per Amazon docs), MCP
  registries, direct brand sales, communities. What is the first 10 customers /
  first 1,000 users plan?
- Risks and mitigations: platform access (partner-gated), payments/consent and
  liability for agent actions, privacy (voice data), accuracy, spec churn
- Kill criteria: what signal in the first 90 days would show this is not worth
  continuing?

C5. VALIDATION PLAN
- 3 riskiest assumptions, ranked
- For each: a test (user interviews, a Wizard-of-Oz voice test, a landing page,
  provider outreach), a success threshold, and a source of participants
- 5 customer interview questions (non-leading, focused on past behaviour)
- 3 provider/brand discovery questions (if B2B)

---

# PART D — HACKATHON FIT CHECK
- Mapping to each judging criterion: what in the build or demo earns a 5/5?
- Spec compliance checklist: spec version declared, Streamable HTTP, tool metadata
  (names, descriptions, icons), elicitation, error handling, auth
- Mini challenge double-dips: AWS Builder (AgentCore/Strands/Bedrock doing real
  work) and Open Source (release the MCP server or a reusable library)
- Friction-log opportunities: MCP spec 2025-11-25 vs 2026-07-28 compatibility,
  Agent Skills authoring, testing without the gated simulator
- Submission red flags to avoid: MCP mentioned but not called in code, a single-turn
  demo, no visible state or orchestration, a video over 3 minutes

# OUTPUT FORMAT
Return a single Markdown report with exactly these sections:
0. Executive summary (≤ 12 bullets: chosen problem, recommended pitch, ICP,
   TAM/SAM/SOM headline, top risk, confidence level)
1. Problem candidates and scorecard
2. Deep dive: the chosen problem (the 5 tests with evidence)
3. Three pitches + comparison matrix + recommendation
4. ICP (end user + integration buyer)
5. Competitive analysis (table + positioning map description)
6. TAM / SAM / SOM (table with formulas)
7. Business value, revenue model, unit economics, GTM
8. Risks, kill criteria, validation plan
9. Hackathon fit check
10. DATA GAPS and UNRESOLVED conflicts (consolidated list)
11. Sources (numbered, with tier, date, URL)

Style: tables over prose, specific over vague, and no filler. Keep evidence and
judgment clearly separated. When confidence is low, say so. For any legal point,
add: "Regulatory awareness only — not legal advice. Consult a licensed attorney
in the relevant jurisdiction (Philippines and U.S.)."
````
