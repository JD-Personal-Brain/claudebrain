# The RM Assistant: the full delivery plan

Associated Bank · Corporate and Commercial Banking · October 2026

The detail behind the three short RM pages, read in RM Detail. The product, its capabilities, waves and
decisions are in RM Detail, Part 3; the rules every product follows are in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). Appendix A specifies the product's
agents and Appendix B its workflows (B1 to B9), so the team can build from them. A working hypothesis
until Discover with the bank's RMs.

**The limiting factor: our working assumption is the length of the bank's AI review (Open Items PL7); not
confirmed yet.** ⚠️ The real blockers are a first question for the bank (what usually holds up a new AI
tool there?). The review would matter most for the very first capability (the follow-up's recap and email,
in M365 Copilot), together with any recording policy the bank has. The other likely one, also to confirm:
approval to use client data (the data contract, the signed list of data the product may use, needs the
data owners' signatures [names needed]; aimed for week 2).

---

## 1. The outcome

The assistant has two goals that work together:

- **More revenue opportunities:** better insight into which clients to call, and why.
- **More time to act on them ("banker capacity"):** less time on meeting prep, call notes and CRM updates.

New revenue can come from three places. Finding out which is biggest is the
first job:

| Lever | What the assistant looks for | Capabilities |
|---|---|---|
| **Win new clients** | Prospects that look like our best clients, and referrals from other parts of the bank | Prospect lookalikes |
| **Grow existing clients** | Clients who need a product they don't have yet, such as treasury management, including referrals between teams (for example, RM to treasury specialist) | Monday opportunity list, referral prompts |
| **Keep clients** | Early signs a client may leave, such as falling balances or less activity | Early warning |

---

## 2. The value model

The business case is built in Discover from real data. The structure is set
now, and the **[X]** values are filled in with the bank's numbers, not
invented here.

| Part | How it's calculated |
|---|---|
| **Revenue from insights** | RMs in scope [X] × qualified opportunities surfaced per RM per month [X] × share acted on [X]% × win rate [X]% × average first-year revenue per win [$X] |
| **Time freed** | RMs in scope [X] × hours saved per week [X]. Reported as hours and client-facing time, not turned into revenue: any revenue that time creates already shows up in the results against the comparison group, so counting it again would count the same win twice (decided 2026-10-17) |
| **Costs** | Licenses (for example, Copilot or Agentforce seats) + build effort + running costs (AI usage, data) + change management |
| **Net value** | Revenue above the comparison group, minus costs. Target payback: [X] months, judged for wave 1 as a whole; the time savers are judged on hours freed and client-facing time against an hours target the sponsor agrees [X], not on payback |

Each core use case gets its own line once targets are set in Define.

**How it's proven:** pilot RMs are compared with similar RMs not yet using
the assistant, and every AI-sourced opportunity is tagged in Salesforce from day
one. Finance agrees the method before the pilot starts.

---

## 3. Who's involved and who decides

The roles, what each one decides and the gates each joins are set once in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). For the RM project they are:

| Role (Product Framework) | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed] |
| User leaders | RM leaders and market managers (⚠️ titles to confirm): they choose the pilot group, use the assistant's insights in the weekly pipeline meeting, or whatever team meeting managers already run (⚠️ to confirm), and decide with the sponsor whether to scale (gate 5) |
| Pilot users | Pilot RMs: they co-design and test, and their feedback steers the backlog |
| Data owners | The owners of the client data, which we expect sits in Salesforce and Snowflake (⚠️ to confirm) [names needed] |
| Platform teams | Salesforce, Microsoft, AWS and data engineering (⚠️ to confirm how the bank's teams are set up) |
| Long-term owner | To be decided by a date set in Define (sub-step 2.8); confirmed before scaling (5.7); for example, someone in a revenue line |
| Also for RMs: sales leadership and HR | Whether acting on the assistant's insights is recognized in how RMs are measured and paid |

The risk partner, compliance, privacy and security, vendor risk, IT, Finance, Analytics and Operations
join as the Product Framework sets out. No planned RM capability
takes the higher-risk path, so the credit policy owner isn't involved; any insight
that suggests a credit product goes to compliance (control K3; none in wave 1, whose list suggests only deposit and treasury gaps).

---

## 4. How the work flows

Six steps, each ending in a go/no-go gate, run as the [Product Workflow](https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv)
sets out: its questions, gates and sub-steps (the Product Playbook) aren't repeated here. The first pass
overlaps: a working prototype in week 1, wave 1 live in about weeks 4–6 (the meeting follow-up first);
then steps 3–6 repeat in cycles of a week or two, and each new feature wave takes the quick pass through
Discover and Define (Product Framework). What's different for RMs:

| Step | Gate for RMs | What's specific to RMs | General agents used (the analysis agents, M20 to M33; M1 to M19 run every step as the Product Machine sets out) |
|---|---|---|---|
| **1. Discover** | The sponsor, with the risk partner, agrees the target lever, the main measure and today's baseline (from a first rough sizing; confirmed at gate 2), and confirms the wave 1 capabilities | Frame "new revenue" as three levers (section 1) and two goals; size them with pipeline, win/loss, balances and products; interview and shadow RMs and managers, starting from the RM user workflow (how they find opportunities today, and what gets in the way); learn how RMs are measured and paid; test the prototype on sample data every few days | M20 interview synthesizer (Teams transcripts only with consent), M21 opportunity sizer, M22 time-use analyst |
| **2. Define** | The brief, data contract and risk rating agreed; the full set of measures and the value model show payback within [X] months; dates proposed for waves 2 and 3 | The data contract covers documents too (meeting recaps and call transcripts: their source, owner, re-indexing and who may see them); the risk intake lists consent before recording (control K24) for the meeting follow-up; Finance agrees how AI-sourced revenue is tagged and compared; any insight that suggests a credit product, such as a line of credit, is reviewed by compliance (control K3: the AI never makes a credit decision and never sets or suggests a price; fair-lending rules apply to business credit too) | M23 requirements drafter, M24 data contract checker (then on every data refresh), M25 risk intake assistant |
| **3. Build** | Meets the quality bar in testing; every control is built and passes its control test | Simple, explainable rules find the opportunities and AI only explains them (K22); every insight shows the numbers behind it (K7); one-click use, change or reject with a reason (K1); each RM sees only clients they may already see (K4); filters block sensitive data and off-topic answers (K8); every AI action logged (K12); the test set uses real client examples graded by experienced RMs | M26 test grader |
| **4. Govern and test** | All sign-offs recorded and the monitoring plan agreed, for each AI product | Register the product in the bank's model inventory (⚠️ to confirm) and confirm its rating (model risk guidance SR 11-7; ⚠️ SR 26-2 may replace it; to check); red-team for other RMs' clients and credit requests; check opportunities are spread fairly across client segments and regions; show consent captured before any recording (K24); the monitoring plan watches the share of recaps from consented recordings versus the RM's own notes | M27 red-team agent, M28 fairness monitor (then monthly), M29 evidence pack assembler |
| **5. Release and adopt** | Weekly use and leading results hit targets (at least [X]% of pilot RMs active weekly, at least [X]% of insights acted on); no serious incidents; long-term owner confirmed before scaling | A pilot group of RMs and their managers, with a comparison group; build it into a routine managers already run, such as a weekly pipeline meeting (⚠️ to confirm), so use becomes a habit; train on RMs' own clients; champions and a Teams channel answer "how do I…?"; recognize AI-sourced wins with sales leadership | M30 feedback triage |
| **6. Measure and iterate** | Each month, keep, change or stop each AI product; each quarter, the sponsor with Finance decides to invest more, adjust or stop, on results against the comparison group | Leading measures first (insights acted on, pipeline created, client time gained), visible within weeks; closed revenue against the comparison group from about month 6; plus cost per active RM and per acted-on insight, because the goal is a product that pays for itself | M31 impact analyst, M32 quality watchdog, M33 improvement scout |

---

## 5. How we deploy AI

The AI principles (assistive first, cut first then automate, one job each, built
where the work happens) are the Product Framework's; the assistant's own limits
(its jobs, workflows, data, controls and feedback) are on The RM Assistant page.
What's specific to RMs:

**Choosing the platform.** The pilot picks one delivery platform, using five criteria:
1. Where RMs spend most of their day.
2. What data the assistant needs, and where it lives.
3. Fit with the bank's existing approvals and controls.
4. Cost model (per user vs. per use).
5. Speed to a working pilot.

**Starting point, our assumption to confirm in Discover:** if RMs work mainly in Salesforce,
show insights on the Salesforce client record (Agentforce, Prompt Builder),
with Snowflake (or Fabric; which holds what is to confirm) as the data and signal engine. Send the Monday opportunity list through
Teams or Outlook (Power Automate). Keep to as few AI paths as wave 1 needs: M365 Copilot for the meeting
follow-up's recap and email, and one Salesforce path (Agentforce or Prompt Builder) for insights, the brief and call notes. Add AWS
Bedrock only where custom AI work is needed beyond that. Every extra platform adds build work and another review.

**What ships when:** in feature waves of capabilities (the capabilities and their waves are in RM Detail, Part 3, section 3),
with a release every week or two in between.

**The data flywheel.** The meeting follow-up's call notes, which RMs approve,
also improve the quality of the client records (the CRM). Better data makes better
insights; better insights earn more use; more use produces more data. That
loop compounds over time and is a reason to build both goals together.

**The quality bar for RMs.** The tests and who may accept a gap are the Product
Framework's; thresholds are set in Define. For RMs, accuracy means every number
in an insight matches the source data, and permissions mean no RM ever sees a
client they aren't allowed to see (zero tolerance).

---

## 6. The project plan (estimate)

Building starts on day one: a working version takes days, so the plan is paced by what most often holds
banks up (our assumption for Associated, to confirm): access to real client data and sign-off from the AI
review. The risk partner sees each version as it is built. Weeks are estimates to confirm in the first days.

**What lets us move this fast.** The six conditions in the [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ#what-lets-a-project-move-fast), each checked in the first days. For RMs: condition 2 means features already in Salesforce, M365 Copilot and Power Platform (⚠️ to confirm with IT and risk in week 1); condition 3 holds, because wave 1 suggests only deposit and treasury gaps, so we expect a low rating (⚠️ the risk partner decides); data owners are asked to sign the data contract by week 2 (⚠️ their timing, to confirm).

**Backup plan if data access or review runs long.** The meeting follow-up's
recap and email go first: they're drafted from the RM's own notes in M365 Copilot (Teams transcripts
come later, only where recording is allowed and the client agrees, control K24), so we assume they
need the least new data and review (⚠️ to confirm). RMs keep shaping the brief,
opportunity list and call notes in the test environment, so they're ready the day access and
sign-off land, by about week 10. The dates for later waves, proposed at gate 2, allow for it. The
call is made at gate 2 (week 2).

**Wave 1: the first six weeks**

| Week | What gets done | Owner | Proof it's done |
|---|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner briefed; data access and test environments requested; working prototype built on sample data; a first rough sizing of the levers | Product manager, platform team | Prototype shown to the sponsor |
| 1 | **Gate 1:** the sponsor, with the risk partner, sees the prototype and agrees the target lever, the main measure and today's baseline (from a first rough sizing in days 1–5; confirmed at gate 2), and confirms wave 1 | Sponsor, with the risk partner | Decision log entry |
| 1–2 | RM interviews and shadowing with 6–10 RMs and their managers (our estimate), using the prototype; improve it every few days; sizing of the levers refined | Product manager, pilot RMs, analyst | RM feedback log; sized levers |
| 2 | **Gate 2:** data contract, early risk rating, the full set of measures and the value model, Finance attribution method, dates proposed for waves 2 and 3; split decision if needed | Sponsor, data owners, risk partner | Signed data contract; early risk rating |
| 2–3 | Recap and email set up in M365 Copilot on sample notes (week 2); after gate 2, a small test set graded by RMs (gate 3); controls tested, including consent before recording (K24); evidence pack and sign-offs (gate 4); readiness for this part: incident dry run, comparison group, training | Platform team, risk partner, operations | Gate 3 and gate 4 entries in the decision log; readiness checklist |
| About 4 | **Meeting follow-up live with pilot RMs** | Product manager | First weekly usage report |
| 3–5 | After gate 2, connect real data in the test environment; build the test set and evidence pack; risk partner reviews each version | Platform teams, product manager | Test results against the quality bar |
| 4–5 | Sign-offs for the brief, the opportunity list and saving call notes (a material change to the follow-up, back through step 4); release readiness (training, support, incident process, comparison group) | Risk, compliance, privacy, security, operations | Sign-offs recorded; readiness checklist complete |
| About 4–6 | **Client brief, Monday opportunity list and call notes into Salesforce live with pilot RMs** | Product manager | Usage and act-on rates in Power BI; share of meetings logged |

**By day 90 (about week 13):** wave 1 has been live with pilot RMs for about
two months and leading measures are coming in (if the backup plan is used, the recap and email are still live from about week 4; the rest has about three weeks). How far waves 2 and 3 have
got depends on the dates proposed at gate 2 and confirmed at each wave's quick-pass gates.

---

## 7. Top risks and how I'd handle them

| Risk | How I'd handle it |
|---|---|
| **CRM data may be incomplete** (common at banks when RMs skip logging; ⚠️ to confirm) | Lean on account data first (we expect it in Snowflake); the time-saving features improve CRM data over time (the flywheel) |
| **RMs don't trust the insights** | Show the reason and the numbers behind every insight; co-design with pilot RMs; managers model use |
| **Governance takes longer than planned** | Brief risk partners in week one; keep each feature wave low-risk, internal-only and on approved platforms; build the evidence pack as we go; if it still runs long, split wave 1 (see the backup plan in section 6) |
| **Incentives don't reward acting on insights** | Agree recognition for AI-sourced wins with sales leadership before launch |
| **Costs grow with usage** | Track cost per active RM; use the smallest AI model that meets the quality bar |
| **Revenue attribution is disputed** | Agree the comparison-group method and tagging with Finance in Define |
| **Data access takes longer than planned** | Request access on day one; start with data that's already certified; keep the first release's data needs small |
| **Client privacy in recorded meetings** | Client consent and any recording policy the bank has (⚠️ to confirm) apply; notes are drafts until the RM approves |

---

## 8. What I'd confirm in the first weeks

This approach is built on the platforms named in the role: Salesforce,
Snowflake, Microsoft Fabric and Power BI, Microsoft 365 Copilot, Power
Platform and AWS Bedrock. I've been told all of them are live, so the plan
builds on them. I'd confirm early (this is the one full list; the Executive Summary asks the top few):

- What usually holds up a new AI tool at the bank?
- Which revenue lever matters most to the business right now?
- How will success be judged in the first 6 months?
- Which RM teams would make a good pilot group?
- Who owns the client data in Snowflake and Salesforce?
- How are RMs measured and rewarded today?
- How many RMs and treasury management officers are there, by market, and how are referrals to treasury, capital markets and wealth credited?
- The value model's inputs: win rate, first-year revenue per win, client-facing hours per RM, fee income by line, deposits and treasury management use?
- How long does AI governance review usually take?
- Is recording client meetings in Teams allowed, how is consent captured, and who owns the recording policy?
- What team and budget are available for the pilot?
- How each platform is set up for RMs today: which features, licenses and connections? Do RMs work mainly in Salesforce, or in Outlook and Teams?
- Which client data sits in Snowflake and which in Fabric?
- Do managers run a weekly pipeline meeting, or another team routine the assistant could plug into?

---

## Appendix A: Agent specs

The product's own agents (A1, A2, A3 and A5), written so a platform team can build them and a risk
partner can review them. AI sales coaching (wave 3): agent spec not written yet. **[X]** values are set in Define.

**Rules for every agent:**
- **One job.** If a request falls outside it, the agent says so and stops.
- **Read-only by default.** Any change to a record, or anything that reaches a client, needs a named person's click.
- **Approved models and data only.** Uses only AI models and data sources approved for this product.
- **Never guesses.** If its inputs are missing, stale or fail a check, it stops and alerts its owner rather than producing a weaker answer.
- **Everything logged.** Each run records who, what, when, which sources and what it produced, for audit and for measuring.

### Agents RMs use (the product)

**A1. Signal finder** · wave 1 · runs on Snowflake (Cortex)
- **Job:** each night, scan each RM's clients for opportunity signals using the agreed rules and scores (product gaps, deposit and treasury only in wave 1; from wave 2, early warnings and referral needs). From wave 2, also monthly: find prospect lookalikes in the licensed prospect data, using the criteria compliance approves.
- **Inputs:** certified Snowflake views of balances, products, activity and trends; the rule set owned by the business; from wave 2, the licensed prospect data named in the data contract.
- **Allowed actions:** read the certified views and the licensed prospect data; write signals to a signals table.
- **Not allowed:** contacting clients; changing Salesforce; inventing signals outside the rule set.
- **Outputs:** a list of signals per RM, each with the rule that fired and the numbers behind it.
- **Stops when:** every in-scope client has been scanned, or the data is older than [X] hours (then it alerts the data owner and produces nothing).
- **Proof it worked:** run log with clients scanned and signals found; a sample of signals matches the source numbers exactly.
- **Person in charge:** business owner of the rules; data owner for the inputs.

**A2. Insight writer** · wave 1 · runs on Salesforce Prompt Builder (or AWS Bedrock if needed)
- **Job:** turn each signal into a plain-English reason, talking points and a suggested next step, citing the numbers.
- **Inputs:** signals from A1; the Salesforce client record.
- **Allowed actions:** read signals and the client record; write a draft insight to the assistant's own insights panel, shown on the client record; it changes no client record field.
- **Not allowed:** recommending credit decisions or pricing; stating any number not in its inputs.
- **Outputs:** one insight per signal, with its sources shown.
- **Stops when:** every signal has an insight, or a guardrail blocks one (logged and sent to the product manager).
- **Proof it worked:** test-set score meets the quality bar (accuracy, sources, relevance); every number traces to the source.
- **Person in charge:** the RM decides whether to act; the product manager owns quality.

**A3. Prep and follow-up assistant** · wave 1 · runs on Salesforce Agentforce or M365 Copilot
- **Job:** before a client meeting, draft a one-page brief. After it, draft the recap, follow-up email and call notes for Salesforce.
- **Inputs:** the Salesforce client record; open insights; the RM's calendar; the Teams meeting recap (recorded only with client consent) or the RM's own notes.
- **Allowed actions:** read the inputs; create drafts for the RM; save an approved call note to Salesforce, tagged "AI-drafted", only after the RM's click.
- **Not allowed:** sending anything to a client; saving to Salesforce without the RM's approval.
- **Outputs:** a brief, a recap, a draft email and draft call notes, all marked as drafts.
- **Stops when:** the drafts are delivered to the RM. If there's no recording or consent, it drafts from the RM's own notes or asks for them.
- **Proof it worked:** the RM approves or edits each draft (logged); share of drafts used with light edits ≥ [X]%.
- **Person in charge:** the RM approves before anything is saved or sent.

**A5. Client Q&A** · wave 3 · runs on Salesforce Agentforce or a Copilot Studio agent in Teams
- **Job:** answer "what should I know before my call with this client?" and similar questions.
- **Inputs:** Salesforce and Snowflake, read-only, only clients the RM is allowed to see.
- **Allowed actions:** read; answer with sources; propose a record update for the RM to click.
- **Not allowed:** answering about clients outside the RM's permissions; giving credit or pricing advice.
- **Outputs:** an answer with its sources, or "I don't have that information."
- **Stops when:** the question is answered, or it is out of scope (it says so and names who can help).
- **Proof it worked:** test-set score meets the quality bar; zero permission breaches in red-team testing.
- **Person in charge:** the RM; the product manager for quality.

A4 (the weekly opportunity digest) was merged into workflow B1 on 2026-10-18: it is a scheduled Monday send with no AI in it, so it is a step, not an agent. A6 (a how-to helper) was removed on 2026-10-17: champions and a Teams channel answer "how do I…?" questions in the pilot. Neither number is reused.

### Agents the team uses

The team uses the product machine's general agents (M20 to M33 for RMs), specified in full in the
[Agent Library](https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn); which ones each step uses is in section 4.

## Appendix B: Workflows

Each RM-facing capability as a step-by-step flow. Every RM-facing flow (B1–B8)
has one **decision point** where the RM decides, and everything is logged.
B9 is the release routine behind them. AI sales coaching (wave 3): workflow not
written yet.

**B1. Monday opportunity list** (wave 1)
- **Trigger:** every night (signals); every Monday morning (the Monday send).
- **Steps:** 1. A1 scans clients and writes signals. 2. A2 writes an insight for each. 3. Insights appear in the assistant's panel on the Salesforce client record (no record field changes). 4. Every Monday, a scheduled send (Power Automate) messages each RM their top [X] insights in Teams or Outlook, ranked by the agreed score, with links to each client record; it messages only the RM (and, if agreed, their manager), and sends a short "nothing new" note when there's nothing. 5. **Decision point:** the RM accepts, rejects (with a reason) or changes each insight. 6. On accept, the RM creates an opportunity in Salesforce, tagged "AI-sourced." 7. M30 sorts the feedback. 8. Managers review the list in the weekly pipeline meeting, or whatever team meeting they already run (⚠️ to confirm).
- **Logged:** signals, insights, Monday sends, opens, decisions and reasons, opportunities created.
- **Measures:** share of insights acted on; pipeline from AI-sourced opportunities.

**B2. Pre-meeting client brief** (wave 1)
- **Trigger:** a client meeting on the RM's calendar, [X] hours before; or the RM asks.
- **Steps:** 1. A3 pulls the client record, open insights and recent activity. 2. It drafts a one-page brief with sources. 3. The brief reaches the RM in Teams or Outlook. 4. **Decision point:** the RM uses it and rates it with one click.
- **Logged:** briefs created, opened and rated.
- **Measures:** briefs used; prep time saved (RM survey); rating.

**B3. Meeting follow-up: recap and email** (wave 1; first in the backup plan)
- **Trigger:** a client meeting ends.
- **Steps:** 1. M365 Copilot produces the recap (from a recording only with client consent; otherwise from the RM's notes). 2. A3 drafts the follow-up email and action items. 3. **Decision point:** the RM edits and sends it themselves. Nothing is sent automatically.
- **Logged:** drafts created; drafts sent after RM edits.
- **Measures:** time to follow-up; drafts used; time saved.

**B4. Meeting follow-up: call notes into Salesforce** (wave 1; live with the brief and the opportunity list about weeks 4–6)
- **Trigger:** the B3 recap is ready.
- **Steps:** 1. A3 drafts the Salesforce activity note and next steps. 2. **Decision point:** the RM approves or edits. 3. On approval, the note is saved to Salesforce, tagged "AI-drafted."
- **Logged:** drafts, approvals and edits.
- **Measures:** share of meetings logged in Salesforce (the data flywheel); admin time saved.

**B5. Early warning: client may leave** (wave 2)
- **Trigger:** A1 finds a warning signal, such as falling balances or less activity.
- **Steps:** 1. A2 explains the signal with the numbers. 2. An alert appears on the client record and in the next Monday send. 3. **Decision point:** the RM decides whether and how to reach out, and logs the action.
- **Logged:** alerts, RM actions, outcomes.
- **Measures:** clients kept against the comparison group.

**B6. Referral prompts** (wave 2)
- **Trigger:** A1 spots a likely need another team serves, such as treasury management.
- **Steps:** 1. A2 explains the need. 2. **Decision point:** the RM clicks "refer" or dismisses it. 3. On refer, Power Automate creates the referral in Salesforce and notifies the specialist. 4. The specialist accepts it and the referral is tracked to close.
- **Logged:** prompts, referrals, acceptances, outcomes.
- **Measures:** referrals made and won.

**B7. Client Q&A** (wave 3)
- **Trigger:** the RM asks a question in Salesforce or Teams.
- **Steps:** 1. A5 checks the RM's permissions. 2. It answers from permitted data, with sources. 3. **Decision point:** the RM acts; any record update needs their click.
- **Logged:** questions, answers, sources, updates.
- **Measures:** questions answered; answer ratings; zero permission breaches.

**B8. Prospect lookalikes** (wave 2)
- **Trigger:** monthly.
- **Steps:** 1. A1 finds prospects that look like the bank's best clients in the licensed prospect data, using agreed and explainable criteria (wave 2's data contract update adds that data). 2. A2 explains each match. 3. **Decision point:** the RM decides whether to pursue each one.
- **Logged:** prospects shown, pursued and won.
- **Measures:** new clients against the comparison group.
- **Check:** compliance reviews the criteria before launch, because prospect selection can raise fair-lending questions.

**B9. Every release (every week or two)**
- **Trigger:** any change to prompts, rules, data or models.
- **Steps:** 1. M32 re-runs the test set. 2. If the score is below the quality bar, the release stops. 3. If the change is material (Product Framework), it goes back through step 4 before release. 4. Release; M32 watches live quality for [X] days.
- **Logged:** test scores, approvals, release notes.
- **Measures:** quality trend; releases rolled back.

_Last updated: 2026-10-19_
