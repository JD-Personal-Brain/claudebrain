# RM Detail

Everything about the relationship manager (RM) work at Associated Bank in one document, for an AI to read. Give this whole document to an AI model so it has the full context: the product, the plan, every step, the agent specs, the workflows and the McKinsey research (the earlier RM audit and market scan are kept as separate working files). People should read the three short pages above it in the RM section: the RM Executive Summary, RM Assistant and the RM Assistant Plan.

> **How to read it (for the AI).** The parts below are the working files, copied in whole and in this order. Later parts give more detail on earlier ones. Lines marked ⚠️ are guesses or hypotheses to confirm at the bank; [X] marks a number not yet known: never invent a value for it. The product is a working hypothesis until Discover with the bank's RMs. Built automatically from the working files; never edit this file by hand.

## Part 1: Executive summary

Working file: `memos/rm-executive-summary.md`.

For the leaders of the relationship manager business · Associated Bank · October 2026

> ⚠️ **A working hypothesis.** Built from outside research and public Associated job postings, not yet from how the bank's relationship managers (RMs) work today. The first conversations with RM leaders test it.

### The problem
RMs win the bank's commercial business, but at many commercial banks they spend only about 25–30% of their time with clients (McKinsey). The rest goes to meeting prep, call notes, CRM updates and hunting for the next opportunity. Better insight only pays off if RMs have the time to act on it.

### The product: The RM Assistant
Each RM gets **their own AI assistant**, inside the tools they already use: Salesforce, Teams and Outlook. It helps the RM win business and frees up the time to win it. It drafts and suggests; **the RM always decides**. It never contacts a client on its own, never sets or suggests a price and never makes a credit decision. [What it is and all its capabilities](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2).

### What RMs get first (wave 1)
| Capability | What the RM gets | Why it matters |
|---|---|---|
| **Pre-meeting client brief** | One page before each client meeting: the relationship, recent activity, open opportunities, talking points | Less prep time, better meetings |
| **Meeting follow-up** | The recap, the follow-up email and the call notes for Salesforce, drafted for the RM to approve | Admin off the RM's plate; better CRM data |
| **Monday opportunity list** | Each Monday, the clients to call this week, with the reason and the numbers behind it | New revenue from existing clients |

Later waves add early warning on clients who may leave, referral prompts and prospect lookalikes, then client Q&A and AI sales coaching.

### The value
- **More revenue per RM:** pipeline and wins from the assistant's suggestions. McKinsey reports about 3–15% higher revenue per RM where banks rework a frontline area end to end (an outside benchmark, not our target).
- **More time with clients:** hours saved each week.
- Both are proven against similar RMs not yet using it, with targets set from the bank's own numbers. [Outside evidence for each core use case](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X)

### How fast
Wave 1 is live in about six weeks: the meeting recap and email first (about weeks 2–4), then the client brief, Monday opportunity list and call notes (about weeks 4–6). The first read on closed revenue comes at about month 6. [The plan, week by week](https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk)

**What could slow us down:** not known yet. Possible hold-ups include getting approval to use client data and the bank's AI review, but the real ones are a question for the first conversations (below).

### What I need, and what I'd confirm
1. A business sponsor for the RM work.
2. Time with 6–10 RMs and their managers, and a willing pilot group.
3. Named owners for the Salesforce and Snowflake client data.
4. An early risk partner.

To confirm in the first weeks: what usually holds up a new AI tool here; which revenue lever matters most now (new, growing or keeping clients); how RMs are measured and paid today; how long the AI review takes and whether recording client meetings in Teams is allowed; and what team and budget the pilot has.

## Part 2: The product: RM Assistant (short version for people)

Working file: `memos/rm-assistant.md`.

> ⚠️ **A working hypothesis** (agreed 2026-10-17), built from outside research and public Associated job postings. Conversations with the leaders of relationship managers (RMs) and Discover confirm or change it.

### The product in one line
Each RM gets **their own AI assistant**, inside Salesforce, Teams and Outlook, to help them win business and free up the time to win it. It starts with three **capabilities** and gains more, feature wave by feature wave. Every later AI product for RMs is a new capability of the same assistant.

### 1. Its limits
These limits make it safe to give every RM one.
- **Jobs:** only the capabilities below. Anything else, it says so and stops.
- **Where it works:** the Salesforce client record, Teams and Outlook. No new app.
- **Data:** certified client data, only for the clients the RM may already see, plus the RM's own calendar, email and meetings.
- **Controls:** it drafts and suggests; the RM approves anything saved or sent. It never contacts a client, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything is logged.
- **Feedback:** one click on every output (use, change or reject), which steers what gets better next.

### 2. Capabilities, by moment in the RM's work
Each capability is one AI product and answers one core use case (see the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X) for the value and the research).

| Moment | Capability | What it does | Core use case | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the top clients to call, with the reason and the numbers | Prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients | Prospecting and next best opportunities | 2 |
| | Referral prompts | Flags a client need for a partner team, such as treasury management | Lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting | Account intelligence and meeting prep | 1 |
| | Client Q&A | Answers "what should I know about this client?" | Account intelligence and meeting prep | 3 |
| **During and after** | Meeting follow-up | Drafts the recap, the follow-up email and the call notes for Salesforce, for the RM to approve | Admin off the RM's plate | 1 |
| | AI sales coaching | Private guidance for the RM after a call | AI sales coaching | 3 |
| **Keep the book** | Early warning | Flags clients who may be drifting away | Keep clients | 2 |
| **Left out on purpose** | Pricing suggestions; contacting prospects on its own | — | Deal scoring and pricing; lead nurturing (full version) | Out |

### 3. What it's built on
One shared foundation, built once for every capability: client data from Salesforce and Snowflake, the RM's own work (calendar, email, meetings; transcripts only with client consent), outside prospect data the bank licenses (to confirm), a **signals engine** (simple, explainable rules find opportunities and risks; AI explains them in plain English with the numbers), drafting, and the controls and feedback above.

Every detail (the RM's job, the foundation part by part, what to confirm) is in [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n), the fourth page in the RM section.

## Part 3: The RM Assistant in full detail

Working file: `memos/rm-assistant-detail.md`.

The detailed working file behind the RM Assistant page. People read the short page (`memos/rm-assistant.md`); this file goes into RM Detail.

> ⚠️ **A hypothesis, not a plan yet** (agreed as our working hypothesis on 2026-10-17). Built from McKinsey's research, the RM plan and public Associated job postings, not from how the bank works today. The first test is the talk with the RM lead on Tuesday October 20; Discover confirms or changes the rest.

### The product in one line
Each relationship manager (RM) gets **their own AI assistant**, inside Salesforce, Teams and Outlook. Its job is to help the RM win business and to free up the time they need to win it. It starts with three **capabilities**, each doing one specific job in the RM's work, and gains more feature wave by feature wave. It is the base everything else builds on: every later AI product for RMs is a new capability of the same assistant.

### 1. A personal AI, with limits
The assistant is personal to each RM, and it is constrained in five ways. These limits are what make it safe to give every RM one.

| Limit | What it means |
|---|---|
| **Jobs** | It does only the capabilities listed on this page. Anything else, it says so and stops. |
| **Workflows** | It works where the RM already works: the Salesforce client record, Teams and Outlook. No new app to learn. |
| **Data** | Client data: certified data only. It also uses the RM's own calendar, email and meetings (transcripts only with consent) and any outside prospect data the bank licenses. Client data is always limited to the clients the RM is already allowed to see. |
| **Controls** | It drafts and suggests; the RM approves anything saved or sent. It never contacts a client on its own, never makes a credit decision and never sets or suggests a price. Meetings are recorded only with client consent. Everything it does is logged. |
| **Feedback** | Every output has one-click feedback (use, change or reject, with a reason). The feedback steers what gets better next. |

### 2. What an RM's job is
From Associated's public RM postings (seen through search results on job boards, 2026-10-17; ⚠️ check against the bank's own careers site):

| Part of the job | What it means | Where the assistant helps |
|---|---|---|
| **Find new business** | Prospecting: steady calling, centers of influence, new clients | Prospect lookalikes |
| **Grow and keep the book** | Manage a book of middle-market business clients; keep and deepen each relationship | Monday opportunity list, early warning, client briefs |
| **Cross-sell and refer** | Bring in deposits, loans and fee income; refer clients to treasury management, capital markets, private banking and wealth | Referral prompts |
| **Credit and advice** | Analyze client financials, recommend credit structures, present loans and take part in approval, within the bank's credit policy | Later, and only as drafts for the portfolio manager (see section 3) |
| **The work around it all** | Meeting prep, follow-ups, call notes and CRM updates | Client brief, meeting follow-up |

### 3. Capabilities, by moment in the RM's work
Each capability is one AI product (glossary). **Comes from** says which need it answers: one of McKinsey's five frontline use cases, our own core use cases (admin off the RM's plate, keep clients), or the RM's job.

| Moment | Capability | What it does | Comes from | Wave |
|---|---|---|---|---|
| **Find business** | Monday opportunity list | Each Monday, the RM's top clients to call, with the reason and the numbers behind it | McKinsey: prospecting and next best opportunities | 1 |
| | Prospect lookalikes | Companies that look like the bank's best clients | McKinsey: prospecting | 2 |
| | Referral prompts | Flags a client need for a partner team (for example treasury management); the RM decides and makes the referral | McKinsey: lead nurturing, including cross-sell | 2 |
| **Before the meeting** | Pre-meeting client brief | One page before each client meeting: the relationship, recent activity, open opportunities and talking points | McKinsey: account intelligence and meeting prep | 1 |
| | Client Q&A | Answers "what should I know about this client?" at any time | McKinsey: account intelligence and meeting prep | 3 |
| **During and after the meeting** | Meeting follow-up | During: Teams transcribes the meeting, only with client consent (without it, the assistant drafts from the RM's own notes), so the RM can listen instead of typing. After: drafts the recap, the follow-up email and the call notes for Salesforce; the RM approves before anything is saved or sent | Our own: admin off the RM's plate | 1 |
| **After the meeting** | AI sales coaching (after calls) | Private guidance for the RM after a call, seen only by that RM | McKinsey: AI sales coaching | 3 |
| **Grow and keep the book** | Early warning | Flags clients who may be drifting away (falling balances, less activity) | Our own: keep clients | 2 |
| **Credit hand-off** | Credit request draft | ⚠️ New idea, not decided: pulls the client's financials into a draft for the portfolio manager. Would take the higher-risk path (control K3) | The RM's job: credit and advice | Not planned |
| **Left out on purpose** | Pricing suggestions; contacting prospects on its own | — | McKinsey: deal scoring and pricing; lead nurturing (full version) | Out (decided 2026-10-15) |

**Wave 1 at a glance:** three capabilities: the pre-meeting client brief, the meeting follow-up and the Monday opportunity list. Together they cover the RM's whole meeting, before, during and after, plus the Monday call list. The order is the hypothesis; dates for waves 2 and 3 are proposed at gate 2 (the Define go/no-go) and confirmed at each wave's own quick-pass gates, once data access and review times are known. How the waves get delivered is in the [RM Assistant Plan](https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk).

### 4. The foundation underneath
Built once and shared by every capability, and later by portfolio managers.

| Part | What it is | Used by |
|---|---|---|
| **Client data** | The Salesforce client record and activity; balances, products and trends in Snowflake (certified data only) | Every capability |
| **The RM's own work** | Their calendar, email and Teams meetings (transcripts only with client consent) | Brief, meeting follow-up, AI sales coaching |
| **Outside prospect data** | ⚠️ To confirm: what the bank already licenses | Prospect lookalikes |
| **Signals engine** (the "analytics") | Simple, explainable rules find opportunities and risks in the data; AI writes the reason in plain English and shows the numbers | Opportunity list, referral prompts, early warning, prospect lookalikes |
| **Drafting** | Briefs, recaps, emails and notes, always marked as drafts | Brief, follow-up, Q&A, coaching |
| **Controls and logs** | The limits in section 1, built in once and tested for every capability | Every capability |
| **Feedback loop** | One-click feedback on every output, sorted and fed into the next release | Every capability |

### 5. How we'll know it works
- **More revenue per RM:** pipeline and wins from the assistant's suggestions, against RMs not yet using it [X].
- **More time with clients:** hours saved per week and client-facing hours [X].
- **Use:** RMs using it every week, and the share of suggestions acted on [X].

Targets are [X] until the bank's own numbers are in.

### 6. Portfolio managers next
Portfolio managers (PMs) get the same kind of assistant on the same foundation, with their own capabilities: credit memo and annual review drafts first, early warning second (decided 2026-10-15). It waits until we move into PM work. The credit request draft (section 3) would be where the two assistants meet.

### 7. What to confirm
- Are meeting prep, admin and the Monday call list the RM's biggest needs? How do RMs prepare for and log meetings today?
- Where do RMs spend their day: Salesforce, or Outlook and Teams?
- Is recording client meetings in Teams allowed, and how is consent handled?
- Which client data is certified, and who owns it? What outside prospect data does the bank license?
- How long does the bank's AI review take?

### 8. How it maps to the RM plan
The RM Assistant Plan (rebuilt around the assistant on 2026-10-17) delivers this page: the seven core use cases are the **needs** the capabilities answer, each capability is one AI product, and the product agents (A1 to A5) do the work: A1 and A2 are the signals engine and drafting in the **foundation**; A3, A4 and A5 deliver the capabilities. The plan's old "RM assistant" (wave 3) is the Client Q&A capability here.

## Part 4: The plan (short version for people)

Working file: `memos/rm-plan.md`.

How The RM Assistant gets delivered to relationship managers (RMs) · Associated Bank · October 2026

[RM Executive Summary](https://claude.ai/artifact/LPPq2gt5PSoiB8GzX8ZBE2) · [RM Assistant](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2) · [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n) (everything in full, for AI to read) · [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ) (the rules every product follows)

### The plan at a glance
The first 13 weeks (about 90 days), as estimates to confirm in the first days. Week 1 starts at kickoff, and each row links to its detail in RM Detail.

```gantt
weeks 13
Kickoff and a working prototype on sample data | 0 | 1 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-1-discover
Gate 1: the sponsor confirms wave 1 | 1 | 1 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-1-discover
Interviews and sizing with RMs | 0 | 2 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-1-discover
Gate 2: data contract, risk rating, value model | 2 | 2 | gate | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-2-define
Meeting recap and email: tests and sign-offs | 1 | 3 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-the-assistant-s-capabilities-wave-by-wav
**Meeting recap and email live** | 3 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-5-release-and-adopt
Brief, opportunity list and call notes: built and tested on real data | 1 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-3-build
Their sign-offs (call notes go back through step 4) | 3 | 5 | build | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-4-govern-and-test-formal-approval-g
**Brief, opportunity list and call notes live** | 5 | 13 | live | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-5-release-and-adopt
Small releases every week or two | 6 | 13 | ongoing | https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-step-6-measure-and-iterate
```

Waves 2 and 3 get dates at gate 2, once data access and review times are known. The first read on closed revenue comes at about month 6.

### 1. What could slow us down (to confirm)
The real blockers aren't known yet; they're a first question for the bank. Possible ones:
- **Approval to use client data.** Nothing reaches pilot RMs on real client data until the people responsible for it approve which data the assistant may use.
- **The bank's AI review.** The risk partner would see every version as it's built, so sign-off confirms what they already know.
- **Backup plan.** If either runs long, the meeting recap and email go first (they need the least new data and review), and the rest stays ready in the test environment, live by about week 10. The call is made at gate 2.

Detail: [the backup plan and the six conditions for moving fast](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-6-the-project-plan-estimate).

### 2. Who decides
| Role | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed]: the outcome, funding and every gate |
| User leaders | RM leaders and market managers: choose the pilot group, use the assistant in the weekly pipeline meeting, decide with the sponsor whether to scale |
| Pilot RMs | Co-design and test; their feedback steers what gets built |
| Data owners | Salesforce and Snowflake data [names needed]: sign the data contract |
| Risk partner | Rates the product and approves it at step 4; the sponsor can't overrule that approval |
| Sales leadership and HR | Whether acting on the assistant's insights counts in how RMs are measured and paid |

Detail: [who's involved and who decides](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-3-who-s-involved-and-who-decides).

### 3. How we'll prove the value
- **Revenue:** pipeline and wins from the assistant's suggestions, against similar RMs not yet using it. Every AI-sourced opportunity is tagged in Salesforce from day one, and Finance agrees the method before the pilot.
- **Time:** hours saved per week and client-facing time, reported as hours, not turned into revenue.
- **Use:** pilot RMs active each week, and the share of suggestions acted on.
- **Payback:** target [X] months for wave 1. All targets are set from the bank's own numbers at gate 2.

Detail: [the value model](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-2-the-value-model).

### 4. Top risks
| Risk | How I'd handle it |
|---|---|
| Data access or the AI review takes longer | Start both on day one; keep wave 1 internal, assistive and on approved platforms (the backup plan is in section 1) |
| RMs don't trust the insights | Show the reason and the numbers behind every insight; build it with pilot RMs; managers use it in their routines |
| CRM data is incomplete | Lean on account data in Snowflake first; approved call notes improve CRM data over time |
| Incentives don't reward acting on insights | Agree recognition for AI-sourced wins with sales leadership before launch |
| Client privacy in recorded meetings | Record only with client consent and under the bank's recording policy; notes stay drafts until the RM approves |

Detail: [every risk and how I'd handle it](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n#part-5-the-full-delivery-plan-with-every-7-top-risks-and-how-i-d-handle-them).

## Part 5: The full delivery plan, with every step, agent spec and workflow

Working file: `memos/rm-analytics-framework.md`.

Principal Applied AI Product Manager · Associated Bank · October 2026 (memo v10, 2026-10-17)

---

### Executive summary

**The product.** Each relationship manager (RM) gets **The RM Assistant**: their
own AI assistant inside Salesforce, Teams and Outlook. Its job is to help the RM
win business, and to free up the time they need to win it. It starts with three
capabilities and gains more, feature wave by feature wave, on one shared
foundation. What it is, its limits and every capability by moment in the RM's
work are on [the RM Assistant page](https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2);
this plan is how it gets delivered. It is a working hypothesis, to be tested in Discover.

**Wave 1: three capabilities that cover the RM's meeting and their week.**
1. **Pre-meeting client brief:** one page before each client meeting.
2. **Meeting follow-up:** the recap, the follow-up email and the call notes for Salesforce, drafted for the RM to approve.
3. **Monday opportunity list:** the clients to call this week, with the reason and the numbers behind each.

Later waves add early warnings, referral prompts and prospect lookalikes (wave 2),
then client Q&A and AI sales coaching (wave 3).

**The limiting factor: data access.** The data contract (the signed list of data
the product may use) needs the Salesforce and Snowflake data owners' signatures,
aimed for week 2. Owner: the product manager, who chases it from day one; the
signers are the Salesforce and Snowflake data owners [names needed]. The bank's
AI review is the second thing that sets the pace; for the very first capability (the
follow-up's recap and email, in M365 Copilot) it is the main one, together with the
bank's recording policy.

**The approach, in three points:**
1. **Build from day one, aimed at revenue.** A working prototype in week 1, shaped with RMs, and the first capability live within weeks.
2. **Pair insights with time.** RMs at many commercial banks spend only about 25–30% of their time with clients, according to McKinsey. Better opportunities only pay off if RMs have time to act on them, so wave 1 pairs the opportunity list with two time savers.
3. **Govern from day one and prove it with evidence.** Risk partners are involved from the first week. Results are measured against RMs not yet using the assistant, so revenue is never credited to AI by mistake.

**The plan (estimate):** a working prototype in week 1, built alongside
discovery. The meeting follow-up's recap and email go to pilot RMs in about
weeks 2–4; the brief, the opportunity list and saving call notes to Salesforce
in about weeks 4–6. Then small releases every week or two. Dates for waves 2
and 3 are proposed at gate 2 (the Define go/no-go, week 2) and confirmed at each
wave's own quick-pass gates, once data access and review times are known. A first read on closed revenue comes at about month 6.

**What I'd need:** a business sponsor, time with 6–10 RMs and their managers, named data owners, an early risk
partner, and a willing pilot group.

**How to use this plan.** the RM Assistant page says what the product is; the
rules every product follows (who decides, the quality bar, the AI principles)
are in the [Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ)
and aren't repeated here. The numbered sections 1–9, with the six steps, are the plan for
RMs. Appendix A specifies the assistant's agents in full (job, inputs, allowed
actions, outputs, when it stops and proof it worked) and shows how the team uses the product machine's
general agents, whose full specs are in the agent library. Appendix B sets out each of the plan's workflows (B1 to B9) step by step, so the
team can build directly from them.

---

### The assistant's capabilities, wave by wave

Every capability is one AI product, and each answers one of the seven core use
cases (McKinsey's five frontline use cases plus two of our own: admin off the
RM's plate and keep clients). McKinsey's reported returns for each core use case
are in the [Use Case Library](https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X)'s relationship manager section:
outside benchmarks, never our targets, which are set from the bank's data in Define.
The menu is a starting point; the sponsor and RMs confirm and order it in Discover.

| Wave | Capability (AI product) | Core use case it answers | Agents | Built mainly on | Our measure (target set in Define) |
|---|---|---|---|---|---|
| **Wave 1** (follow-up about weeks 2–4; the rest about weeks 4–6) | Pre-meeting client brief | Account intelligence and meeting prep | A3 | Salesforce, Snowflake, Agentforce or M365 Copilot | Prep time per meeting; client-facing hours [X] |
| | Meeting follow-up: recap, email draft and call notes into Salesforce (the RM approves) | Admin off the RM's plate | A3 | M365 Copilot in Teams and Outlook; Salesforce Agentforce for the notes | Hours saved per week; share of meetings logged [X] |
| | Monday opportunity list (product gaps) | Prospecting and next best opportunities | A1, A2, A4 | Snowflake signals, Power Automate digest | AI-sourced pipeline and wins, against the comparison group [X] |
| **Wave 2** (dates proposed at gate 2) | Early warning: client may leave | Keep clients | A1, A2 | Snowflake signals, Salesforce | Clients kept, against the comparison group [X] |
| | Referral prompts (for example, RM to treasury specialist) | Lead nurturing, including cross-sell | A1, A2 | Salesforce, Power Automate | Referrals made and won [X] |
| | Prospect lookalikes | Prospecting and next best opportunities | A1, A2 | Snowflake, Salesforce | New clients, against the comparison group [X] |
| **Wave 3** (dates proposed at gate 2) | Client Q&A ("what should I know about this client?") | Account intelligence and meeting prep | A5 | Salesforce Agentforce or Copilot Studio | Questions answered; answer ratings [X] |
| | AI sales coaching (after calls; private to the RM, measured only in aggregate) | AI sales coaching | Spec to come | M365 Copilot (Teams transcripts), Copilot Studio | Coaching used after calls; win rate and new-RM ramp-up time [X] |
| **Left out on purpose** | Pricing suggestions; contacting prospects on its own | Deal scoring and pricing; lead nurturing (the full version) | — | — | — |

**Why the follow-up and call notes are one capability (decided 2026-10-17):** both
come from the same meeting recap and the same agent (A3), so RMs get one flow:
the recap and email first (about weeks 2–4, since they run in M365 Copilot on the
RM's own meetings and need the least new data and review), then saving the call
notes to Salesforce once that's signed off (about weeks 4–6). Call notes are in
wave 1 because in McKinsey's survey of about 400 bankers, admin is one of the top
two problems at every stage of the sales funnel (decided 2026-10-10).

**How the follow-up passes its gates.** Because the recap and email go live first, the follow-up passes gates 3 and 4 twice: first for the recap and email (weeks 2–3), then for saving call notes to Salesforce, which is a material change (a new action, a record write) and goes back through step 4 (weeks 4–5; Product Framework, change after launch). Gate 5 is decided once, for wave 1 as a whole, after the brief, the list and call notes have been live for [X] weeks.

**Why there's no how-to helper (decided 2026-10-17):** a pilot group of a few RMs
learns from training on their own clients, champions and a Teams channel. A
separate help agent (A6) was one more build and review for little gain; its
number isn't reused. It can come back if the pilot shows the need.

**Why prospecting and coaching sit where they do (decided 2026-10-15; waves agreed 2026-10-17):**
McKinsey reports its biggest revenue numbers for prospecting, so prospect lookalikes
are in wave 2. AI sales coaching is in wave 3, because it needs call
transcripts, client consent before recording (control K24) and more review. Its agent
spec and workflow are not written yet. Autonomous lead nurturing and pricing stay out
(control K3: the AI never sets or suggests a price).

**Why this works:** standard capabilities on platforms the bank already runs
need less build and fit existing approvals. Each feature wave is internal-only and
assistive: the assistant suggests and drafts, and the RM decides. If the bank's
AI review applies to every new capability, the review sets the real pace, which is
why the risk partner is involved from week one.

---

### 1. The outcome

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

### 2. The value model

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

### 3. Who's involved and who decides

The roles, what each one decides and the gates each joins are set once in the
[Product Framework](https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ). For the RM project they are:

| Role (Product Framework) | For the RM project |
|---|---|
| Sponsor | A commercial banking leader [name needed] |
| User leaders | RM leaders and market managers: they choose the pilot group, run the weekly pipeline meeting where the assistant's insights are used, and decide with the sponsor whether to scale (gate 5) |
| Pilot users | Pilot RMs: they co-design and test, and their feedback steers the backlog |
| Data owners | The owners of the Salesforce and Snowflake data [names needed] |
| Platform teams | Salesforce, Microsoft, AWS and data engineering |
| Long-term owner | To be decided by a date set in Define (sub-step 8); for example, someone in a revenue line |
| Also for RMs: sales leadership and HR | Whether acting on the assistant's insights is recognized in how RMs are measured and paid |

The risk partner, compliance, privacy and security, vendor risk, IT, Finance,
Analytics and Operations join as the Product Framework sets out; the risk partner's
step 4 approval can't be overruled by the sponsor. No RM capability
takes the higher-risk path, so the credit policy owner isn't involved; any insight
that suggests a credit product goes to compliance (control K3).

**Keeping partners aligned.** Decisions go in the decision log, and dependencies,
risks and issues in the risk and issue list (Product Framework). Its top item is
the limiting factor: today, the data contract waiting for the data owners'
signatures, owned by the product manager.

---

### 4. How the work flows

Six steps, each ending in a **go/no-go gate** (Product Workflow). The first pass
through all six overlaps: a working prototype exists in week 1, and wave 1 is
live in about weeks 2–6 (the meeting follow-up first); after that, steps 3–6
repeat in cycles of a week or two, and each new feature wave takes the quick pass through
Discover and Define (Product Framework: four sub-steps always done, the rest reused
unless something changed, gates 1 and 2 decided together in writing). **Governance runs through every step**; Step 4 is the
formal approval gate, not the first time risk partners see the product.

| Step | Question it answers | Governance thread | Gate (go/no-go) |
|---|---|---|---|
| **1. Discover** | Which capabilities come first, and which revenue lever matters most? | Risk partner briefed on the idea | Sponsor confirms the capabilities for the wave and the target lever on first sizing; the baseline is confirmed at gate 2 (wave 1 the first time; later feature waves take the quick pass, gates 1 and 2 together in writing) |
| **2. Define** | What exactly do we build first, and how will we know it worked? | Risk intake and early rating; data use approved | Brief, data contract and risk rating agreed; value model shows payback within [X] months; dates proposed for the next waves |
| **3. Build** | What's the smallest version RMs will use and trust? | Controls built in; test set created | Meets the quality bar in testing; every control is built and passes its control test |
| **4. Govern and test** | Is it safe, fair and controlled? | Formal validation and sign-offs | All sign-offs recorded; monitoring plan agreed |
| **5. Release and adopt** | Will RMs use it every week? | Live monitoring; incident process | Weekly use and leading results hit targets (at least [X]% of pilot RMs active weekly, at least [X]% of insights acted on); no serious incidents; long-term owner confirmed before scaling |
| **6. Measure and iterate** | Is it creating new revenue, and what comes next? | Ongoing monitoring | Each month (and at the end of each feature wave): keep, change or stop each capability; quarterly: invest more, adjust or stop, based on results against the comparison group |

**Each step is described the same way** (Product Framework): Goal · Work (sub-steps and tools) ·
AI strategy (the agents) · AI for the team · AI for RMs · Data · Output ·
Checks · Gate.

---

### 5. How we deploy AI

The AI principles (assistive first, cut first then automate, one job each, built
where the work happens) are the Product Framework's; the assistant's own limits
(its jobs, workflows, data, controls and feedback) are on the RM Assistant page.
What's specific to RMs:

**Choosing the platform.** The pilot picks one delivery platform, using five criteria:
1. Where RMs spend most of their day.
2. What data the assistant needs, and where it lives.
3. Fit with the bank's existing approvals and controls.
4. Cost model (per user vs. per use).
5. Speed to a working pilot.

**Starting point, to confirm in Discover:** if RMs work mainly in Salesforce,
show insights on the Salesforce client record (Agentforce, Prompt Builder),
with Snowflake as the data and signal engine. Send the Monday opportunity list through
Teams or Outlook (Power Automate). Use one AI path for the pilot, and add AWS
Bedrock only where custom AI work is needed beyond what's built into
Salesforce. Every extra platform adds build work and another review.

**What ships when:** in feature waves of capabilities (see *The assistant's capabilities, wave by wave*),
with a release every week or two in between.

**The data flywheel.** The meeting follow-up's call notes, which RMs approve,
also improve CRM data quality. Better data makes better
insights; better insights earn more use; more use produces more data. That
loop compounds over time and is a reason to build both goals together.

**The quality bar for RMs.** The tests and who may accept a gap are the Product
Framework's; thresholds are set in Define. For RMs, accuracy means every number
in an insight matches the source data, and permissions mean no RM ever sees a
client they aren't allowed to see (zero tolerance).

---

### Step 1: Discover

**Goal:** Which revenue lever is biggest, and what are RMs missing that would help them win it?

| Sub-step | What happens | Tools that help |
|---|---|---|
| 0. Kick off | Sponsor and who decides agreed, tracker and project file set up, risk partner briefed, the team's approved AI tools confirmed with IT | M365 Copilot |
| 1. Frame the outcome | Agree with the sponsor on "new revenue," the three levers and the two goals | M365 Copilot in Word |
| 2. Size the levers | Estimate the dollars behind new clients, growth and keeping clients, including referrals | Salesforce (pipeline, win/loss), Snowflake (balances, products), Power BI |
| 3. Learn from RMs | Starting from the RM user workflow map, interview and shadow RMs and managers: how do they find opportunities today, and what gets in the way? | Teams meetings with M365 Copilot recaps; an approved LLM to find themes |
| 4. Map the RM's week | Check the RM user workflow map against real data: where time goes, and how much is lost to admin | Salesforce activity data; M365 Copilot usage reporting |
| 5. Understand incentives | How RMs are measured and paid, and whether acting on insights would be rewarded | Conversations with sales leadership and HR |
| 6. Test reactions | Show RMs a working prototype built on sample data, and improve it every few days | Copilot Studio, Power Apps, a Salesforce test environment |
| 7. Pick and baseline | Choose the wave 1 AI products from the standard menu and record today's numbers | Power BI |

**AI strategy:** Use AI to listen and size faster than a team could by hand. Nothing touches clients yet; a person checks every finding.

| Agent | Type | Job | Runs on | Reads from | Person in charge |
|---|---|---|---|---|---|
| M20 Interview synthesizer | For the team | Turns interview recaps into themes and quotes, linked to each source | M365 Copilot, Copilot Studio | Teams transcripts (only with consent), interview notes | Product manager reviews every theme |
| M21 Opportunity sizer | For the team | Answers plain-English questions to size each lever | Snowflake Cortex Analyst | Snowflake balances and products; Salesforce pipeline | An analyst checks the numbers |
| M22 Time-use analyst | For the team | Finds where RM time goes and which activities lead to won deals | Snowflake Cortex, Power BI | Salesforce activity and win/loss | Product manager checks with RMs |

- **AI for the team:** themes from interviews; a first pass over pipeline and activity data.
- **AI for RMs:** a working prototype on sample data, so RMs react to something real.
- **Data:** Salesforce pipeline and activity; client balances and products in Snowflake. Identify the data owners.
- **Output:** a ranked list of opportunities with sizes, the first target, the baseline, and a first value model.
- **Checks:** no client data in unapproved AI tools; risk partner briefed on the idea.
- **Gate:** the sponsor confirms the wave 1 AI products and the target lever on first sizing, with the risk partner agreeing; the baseline is recorded once the measures are set, and confirmed at gate 2.

---

### Step 2: Define

**Goal:** What exactly will we build first, for whom, and how will we know it worked?

| Sub-step | What happens | Tools that help |
|---|---|---|
| 1. Write the problem and outcome | One sentence each, with a measurable target | M365 Copilot in Word |
| 2. Choose the platform and delivery path | Apply the five criteria; confirm the pilot platform and the release plan | Salesforce, Copilot Studio, Power Automate |
| 3. Define the data contract | Exact fields, freshness and quality checks; for document sources (meeting recaps, call transcripts), the sources, their content owner, how often they're re-indexed and who may see each document | Snowflake, Salesforce |
| 4. Start the risk intake | Describe the AI product, get an early risk rating and list the control requirements, including consent before recording (K24) for the meeting follow-up | The bank's governance process |
| 5. Write user stories and acceptance criteria | Short "as an RM, I need…" statements, each with a test of done | An approved LLM to draft; the team reviews |
| 6. Set the measures, quality bar and value model | Revenue, capacity and adoption targets; quality thresholds; payback | Power BI |
| 7. Agree attribution with Finance | How AI-sourced revenue is tagged and compared | Salesforce |
| 8. Prioritize and scope the first release | Rank the backlog by value, effort and risk, and record the trade-offs; pick the smallest useful version and the pilot group; propose dates for waves 2 and 3 from the data access requests and the early risk rating; record the long-term owner, or a date to decide by | — |

**AI strategy:** Use AI as a drafting partner, so the team spends its time on decisions rather than documents. Nothing is approved by an agent.

| Agent | Type | Job | Runs on | Reads from | Person in charge |
|---|---|---|---|---|---|
| M23 Requirements drafter | For the team | Drafts the problem statement, user stories and acceptance criteria | M365 Copilot in Word, or Copilot Studio | Discover findings | Product manager edits; team and sponsor approve |
| M24 Data contract checker | For the team | Checks fields exist, are fresh and pass quality checks; flags gaps. After Define, runs on every data refresh and alerts the data owner on failure | Snowflake Cortex | Snowflake tables and their quality and access records | Data owner signs off |
| M25 Risk intake assistant | For the team | Pre-fills the risk intake and flags likely high-risk areas | Copilot Studio agent grounded in bank policies | Policy documents, product brief | A risk partner sets the rating |

- **AI for the team:** drafting stories, criteria and test questions for review.
- **AI for RMs:** defined, not built. For example: "Each Monday, show me my top 5 client opportunities, with the reason and a suggested next step," and "Before each call, give me a one-page brief; afterward, draft my notes for Salesforce."
- **Data:** a signed-off data contract, so no feature depends on data we don't have.
- **Output:** a one-page product brief, a prioritized backlog, the data contract, the risk rating and control requirements, and the value model.
- **Checks:** under control K3, the AI never makes a credit decision and never sets or suggests a price; it drafts or flags, and a named credit officer makes every credit decision. Any insight that suggests a credit product, such as a line of credit, is reviewed by compliance, because fair-lending rules (including the Equal Credit Opportunity Act) apply to business credit too.
- **Gate:** the brief, data contract and risk rating are agreed, the value model shows payback within [X] months, and dates are proposed for waves 2 and 3 (each is confirmed at that wave's quick-pass gates, once wave 1's step 4 pass shows real review times).

---

### Step 3: Build

**Goal:** Build the smallest version that RMs will actually use and trust.

**AI capabilities used:** agents (A1 Signal finder, A2 Insight writer, A3 Prep and
follow-up assistant and A4 Weekly opportunity digest; in later
feature waves, A5 Client Q&A and AI sales coaching, spec to come), retrieval with sources (each insight shows the client
data behind it), data flows (Snowflake signals into Salesforce), workflow
automations (the weekly digest) and system integrations (Salesforce, Teams
and Outlook).

| Sub-step | What happens | Tools that help |
|---|---|---|
| 1. Prepare the data | Trusted views of client signals: balance trends, product gaps, activity | Snowflake; Fabric and Power BI to explore |
| 2. Find the opportunities | Simple, explainable rules and scores first. AI explains them; it doesn't invent them | Snowflake (Cortex), AWS Bedrock |
| 3. Write the "why" and next step | An LLM turns each signal into a plain-English reason and talking points | Salesforce Prompt Builder or AWS Bedrock |
| 4. Deliver it where RMs work | On the client record, plus a weekly digest in Teams or Outlook | Salesforce Agentforce, Power Automate |
| 5. Free up RM time | Wave 1: pre-meeting briefs and the meeting follow-up (recap, email and call notes into Salesforce), approved by the RM | M365 Copilot (Teams recaps), Salesforce Agentforce |
| 6. Show the source | Every insight links to the numbers behind it | Built into the design |
| 7. Capture feedback | One click to accept, reject or change each insight, with a reason when rejected | Salesforce, Power Automate |
| 8. Build the test set | Real client examples with known good answers, graded by experienced RMs | AWS Bedrock model evaluation |

**AI strategy:** This is where the RM-facing agents are built: a small team of single-purpose agents, read-only by default, with the RM approving anything that changes a record or reaches a client.

| Agent | Type | Job | Runs on | Reads from | Person in charge |
|---|---|---|---|---|---|
| A1 Signal finder | For RMs | Scans each RM's clients overnight for opportunity signals using explainable rules and scores | Snowflake (Cortex) | Snowflake balances, products, trends | Business owns the rules; no client contact |
| A2 Insight writer | For RMs | Turns each signal into a plain-English reason and talking points, citing the numbers | Salesforce Prompt Builder or AWS Bedrock | A1 signals; Salesforce client record | The RM decides whether to act |
| A3 Prep and follow-up assistant (wave 1) | For RMs | Drafts a pre-call brief, then call notes and follow-ups | Salesforce Agentforce or M365 Copilot | Salesforce client record; Teams meeting recap (with client consent where recorded) | The RM approves before anything is saved or sent |
| A5 Client Q&A (wave 3) | For RMs | Answers "what should I know before my call with this client?" | Salesforce Agentforce or a Copilot Studio agent in Teams | Salesforce and Snowflake, read-only, only the RM's permitted clients | Any record update needs the RM's click |
| M26 Test grader | For the team | Scores every version against the test set and the quality bar | AWS Bedrock model evaluation | Test set, product outputs | Experienced RMs grade a sample |

- **AI for the team:** drafting prompts and test questions; checking every version against the test set.
- **AI for RMs:** wave 1: pre-meeting briefs, the meeting follow-up (with call notes into Salesforce) and the Monday opportunity list, with one-click feedback. Later feature waves add the next standard AI products. Assistive only.
- **Data:** live connections from Snowflake and Salesforce; each RM sees only clients they're already allowed to see.
- **Output:** a working product in a test environment, the test results and an evidence pack started.
- **Checks:** filters that block sensitive data and off-topic answers (Bedrock Guardrails, Salesforce Einstein Trust Layer); every AI action logged; client consent for any recorded meeting.
- **Gate:** meets the quality bar in testing, and every control is built and passes its control test.

---

### Step 4: Govern and test (formal approval gate)

**Goal:** Prove the product is safe, fair and controlled, so the bank can approve it.

| Sub-step | What happens | Tools that help |
|---|---|---|
| 1. Confirm the risk rating | Register the product in the model inventory and confirm its rating | The bank's model risk framework (in line with SR 11-7 guidance; ⚠️ SR 26-2 may replace it, to check: item W17) |
| 2. Review data and privacy | Confirm what client data the AI sees, and why it's allowed | Snowflake (Horizon access rules and masking) |
| 3. Gather testing evidence | Accuracy, rate of made-up answers, and red-teaming (trying to break it) | AWS Bedrock model evaluation |
| 4. Check fairness | Are opportunities, especially credit-related ones, spread fairly across client segments and regions? | Snowflake, Power BI |
| 5. Confirm controls | Human approval before anything reaches a client; consent captured before any recording (K24); guardrails; audit logs | Bedrock Guardrails, Einstein Trust Layer, Power Platform environments and data rules |
| 6. Confirm vendor reviews | Third-party risk reviews for the vendors involved | The bank's vendor risk process |
| 7. Get sign-offs | Risk, compliance, privacy and security | — |
| 8. Agree the monitoring plan | What is watched after launch (including the share of recaps from consented recordings versus the RM's own notes), the alert thresholds, who acts and how to pause the product | Power BI, Power Automate |

**AI strategy:** Use AI to test harder and document faster, but never to approve. Risk partners make every call.

| Agent | Type | Job | Runs on | Reads from | Person in charge |
|---|---|---|---|---|---|
| M27 Red-team agent | For the team | Generates thousands of tricky requests (another RM's clients, a credit decision) to try to break the product | AWS Bedrock | The product in test | Risk reviews every failure |
| M28 Fairness monitor | For the team | Checks opportunities are spread fairly across segments and regions; runs again monthly after launch | Snowflake, Power BI | Opportunity outputs, client segments | Compliance reviews results |
| M29 Evidence pack assembler | For the team | Compiles test results, data use and controls into review documents | M365 Copilot in Word | Test results, data contract, controls | Product manager and risk verify every claim |

- **AI for the team:** red-teaming at scale; assembling the evidence pack.
- **AI for RMs:** no change; the product is frozen for review.
- **Data:** proof that data use matches what was approved.
- **Output:** an approved product and an agreed monitoring plan.
- **Checks:** no surprises, because risk partners have been involved since Discover.
- **Gate:** all sign-offs recorded and the monitoring plan agreed.

---

### Step 5: Release and adopt

**Goal:** Get RMs using it every week, starting with a pilot.

| Sub-step | What happens | Tools that help |
|---|---|---|
| 1. Confirm release readiness | Support model (champions and the Teams channel, with the product manager behind them), incident process, training and communications ready; sign-offs in place | Power Platform environments, Teams |
| 2. Launch the pilot | A small group of RMs and their managers, alongside a comparison group | Power Platform environments (test to live), Salesforce release |
| 3. Build it into routines (the core of adoption) | Managers run weekly pipeline meetings from the insights, so use becomes a habit, not a training topic | Salesforce, Power BI |
| 4. Train in context | Short demos built on RMs' own clients; "how do I…?" questions go to champions and the Teams channel | Teams |
| 5. Recruit champions | Respected RMs who show peers how they use it | A Teams channel |
| 6. Recognize AI-sourced wins | Celebrate and credit wins that started from an insight | Salesforce, sales leadership |
| 7. Fix fast | Act on feedback every week | Feedback logged in Salesforce |
| 8. Scale in user waves | Expand only after a go/no-go check | Power BI adoption dashboard |

**AI strategy:** Adoption is a management routine, not a training event: new tools that arrive without a change in how teams work tend to get little use. AI helps RMs learn in the flow of work and turns feedback into fixes quickly.

| Agent | Type | Job | Runs on | Reads from | Person in charge |
|---|---|---|---|---|---|
| A4 Weekly opportunity digest | For RMs | Sends each RM their top opportunities every Monday | Power Automate, with A2 | Insights from A2, ranked by the agreed score | The RM decides what to pursue |
| M30 Feedback triage | For the team | Sorts feedback into bugs, quality issues and ideas, and routes it to the backlog | Power Automate with an approved LLM | Feedback logged in Salesforce | Product manager sets priorities |

- **AI for the team:** summarizing pilot feedback and spotting patterns.
- **AI for RMs:** the live product, still assistive.
- **Data:** usage, feedback and AI-sourced opportunities flowing into dashboards.
- **Output:** pilot results and a scale decision.
- **Checks:** live monitoring; every issue has an owner and an escalation path.
- **Gate:** weekly use and leading results hit targets (at least [X]% of pilot RMs active weekly, at least [X]% of insights acted on), and no serious incidents; the long-term owner is confirmed before scaling.

---

### Step 6: Measure and iterate

**Goal:** Prove it creates new revenue, and keep making it better.

**Leading and lagging measures.** Commercial deals often take months to
close, so each feature wave is judged first on *leading* measures (insights acted on,
opportunities and pipeline created, client time gained), visible within
weeks. *Lagging* measures, meaning closed revenue against the comparison
group, get a first read at about month 6 and firm up over the following
quarters.

| Type | Measure |
|---|---|
| **Usage** | Insights opened and acted on; briefs and follow-ups used; new opportunities created from insights in Salesforce |
| **Adoption** | Weekly active RMs; share of the target group using it; repeat use |
| **Quality** | Accuracy, relevance and usefulness against the quality bar |
| **Business impact** | Pipeline and closed revenue from AI-sourced opportunities, against the comparison group; client-facing hours and clients covered per RM |
| **Risk and controls** | Incidents, RM overrides, guardrail blocks |
| **Cost** | Cost per active RM and per acted-on insight |

The first five are the measures the role names. Cost is added because the
goal is a product that pays for itself.

| Sub-step | What happens | Tools that help |
|---|---|---|
| 1. Track the measures | Live dashboards | Power BI and Fabric, Salesforce reports, Snowflake |
| 2. Compare with the baseline | Pilot RMs vs. the comparison group | Power BI |
| 3. Re-test after every change | Re-run the test set; watch for quality slipping over time ("drift") | AWS Bedrock model evaluation |
| 4. Review monthly | With the sponsor: keep, change or stop | — |
| 5. Feed the next feature wave | Choose and order the next standard AI products | — |

**AI strategy:** Use AI to watch the product continuously and explain results in plain English, so decisions rest on evidence.

| Agent | Type | Job | Runs on | Reads from | Person in charge |
|---|---|---|---|---|---|
| M31 Impact analyst | For the team | Answers "how much pipeline came from AI insights this month?" against the comparison group | Snowflake Cortex Analyst, Power BI | AI-tagged Salesforce opportunities; Snowflake | Analytics validates before reporting |
| M32 Quality watchdog | For the team | Re-runs the test set after every change and alerts on drift | AWS Bedrock model evaluation, Power Automate | Test set, live outputs, feedback | Product manager decides to fix or roll back |
| M33 Improvement scout | For the team | Proposes the next backlog items or next lever from usage and feedback | M365 Copilot or Copilot Studio | Dashboards, feedback, reviews | Product manager and sponsor decide |

- **AI for the team:** impact analysis, quality monitoring and improvement ideas.
- **AI for RMs:** a better product with each release.
- **Data:** AI-sourced opportunities tagged in Salesforce from day one.
- **Output:** a monthly impact report and an updated backlog.
- **Checks:** ongoing monitoring under the model risk framework.
- **Gate:** each month (and at the end of each feature wave), keep, change or stop each AI product; each quarter, invest more, adjust or stop, based on results against the comparison group.

---

### 6. The project plan (estimate)

Building starts on day one. With today's AI tools, a working version takes
days, not months, so the plan is organized around what actually holds a bank
up: access to real client data and sign-off from the AI review. The risk
partner sees each version as it is built. Weeks are estimates to confirm in
the first days.

**What lets us move this fast.** Six conditions, each checked in the first days:

| Condition | Why it matters | Checked by |
|---|---|---|
| **1. Build from day one** | A working prototype on sample data in week 1; no real client data is needed until it's tested. | Product manager, platform team, week 1 |
| **2. Standard features only** | Wave 1 configures features already in Salesforce, M365 Copilot and Power Platform, which already have bank approval. | Product manager, platform teams, week 1 |
| **3. Low risk by design** | Internal only, assistive, read-only by default, nothing near credit decisions or pricing. Should earn a low risk rating. | Risk partner gives an early rating, week 2 |
| **4. Review as we go** | The risk partner sees each version as it's built, so sign-off confirms what they already know. | Product manager and risk partner, every week |
| **5. Data access on day one** | Requests go in on day one and wave 1 uses only certified data, because access is often the slowest step. | Data owners sign the data contract, week 2 |
| **6. Fast decisions** | Each gate is decided within days, in writing when every criterion is met, because waiting for decisions adds weeks. | Sponsor, with the people named for each gate |

**Backup plan if data access or review runs long.** The meeting follow-up's
recap and email go first: they run in M365 Copilot on the RM's own meetings and email, so they
need the least new data and review. RMs keep shaping the brief,
opportunity list and call notes in the test environment, so they're ready the day access and
sign-off land, by about week 10. The dates for later waves, proposed at gate 2, allow for it. The
call is made at Gate 2 (week 2).

**Wave 1: the first six weeks**

| Week | What gets done | Owner | Proof it's done |
|---|---|---|---|
| Days 1–5 | Sponsor kickoff; risk partner briefed; data access and test environments requested; working prototype built on sample data | Product manager, platform team | Prototype shown to the sponsor |
| 1 | **Gate 1:** sponsor sees the prototype and confirms wave 1 and the target lever on first sizing (the baseline follows once the measures are set) | Sponsor, with the risk partner | Decision log entry |
| 1–2 | RM interviews and shadowing using the prototype; improve it every few days; levers sized | Product manager, pilot RMs, analyst | RM feedback log; sized levers |
| 2 | **Gate 2:** data contract, early risk rating, value model, Finance attribution method, baseline confirmed, dates proposed for waves 2 and 3; split decision if needed | Sponsor, data owners, risk partner | Signed data contract; early risk rating |
| 2–3 | Recap and email set up in M365 Copilot: a small test set graded by RMs (gate 3); controls tested, including consent before recording (K24); evidence pack and sign-offs (gate 4); readiness for this part: incident dry run, comparison group, training | Platform team, risk partner, operations | Gate 3 and gate 4 entries in the decision log; readiness checklist |
| About 2–4 | **Meeting follow-up live with pilot RMs** | Product manager | First weekly usage report |
| 2–5 | Connect real data in the test environment; build the test set and evidence pack; risk partner reviews each version | Platform teams, product manager | Test results against the quality bar |
| 4–5 | Sign-offs for the brief, the opportunity list and saving call notes (a material change to the follow-up, back through step 4); release readiness (training, support, incident process, comparison group) | Risk, compliance, privacy, security, operations | Sign-offs recorded; readiness checklist complete |
| About 4–6 | **Client brief, Monday opportunity list and call notes into Salesforce live with pilot RMs** | Product manager | Usage and act-on rates in Power BI; share of meetings logged |

| Step | Weeks (estimate) | Ends with |
|---|---|---|
| **1. Discover** | Weeks 1–2, with a working prototype in week 1 (the quick pass before later feature waves) | Gate 1 (end of week 1): wave 1 AI products and target lever on first sizing (baseline confirmed at gate 2); interviews and sizing continue in week 2 |
| **2. Define** | Weeks 1–2, alongside discovery | Gate 2 (week 2): data contract, risk rating, value model, dates proposed for waves 2 and 3; split decision if needed |
| **3. Build** | From day 1. Wave 1: weeks 1–5; waves 2 and 3: dates proposed at gate 2 | Gate 3: each AI product meets the quality bar in testing, and every control is built and passes its control test |
| **4. Govern and test** | Risk partner reviews each version from week 1; sign-offs per AI product | Gate 4: each AI product approved for real RMs and real client data |
| **5. Release and adopt** | Follow-up recap and email live about weeks 2–4; the brief, the opportunity list and call notes about weeks 4–6; releases every week or two | Gate 5: each feature wave meets its weekly use and leading-result targets, with no serious incidents; long-term owner confirmed before scaling |
| **6. Measure and iterate** | Leading measures from the first live week; closed revenue read about month 6 | Gate 6: keep, change or stop each AI product monthly; invest more, adjust or stop each quarter |

**By day 90 (about week 13):** wave 1 has been live with pilot RMs for about
two months (about three weeks if the backup plan is used) and leading measures are coming in. How far waves 2 and 3 have
got depends on the dates proposed at gate 2 and confirmed at each wave's quick-pass gates.

---

### 7. Top risks and how I'd handle them

| Risk | How I'd handle it |
|---|---|
| **CRM data is incomplete** (RMs skip logging) | Lean on account data in Snowflake first; the time-saving features improve CRM data over time (the flywheel) |
| **RMs don't trust the insights** | Show the reason and the numbers behind every insight; co-design with pilot RMs; managers model use |
| **Governance takes longer than planned** | Brief risk partners in week one; keep each feature wave low-risk, internal-only and on approved platforms; build the evidence pack as we go; if it still runs long, split wave 1 (see the backup plan in Section 6) |
| **Incentives don't reward acting on insights** | Agree recognition for AI-sourced wins with sales leadership before launch |
| **Costs grow with usage** | Track cost per active RM; use the smallest AI model that meets the quality bar |
| **Revenue attribution is disputed** | Agree the comparison-group method and tagging with Finance in Define |
| **Data access takes longer than planned** | Request access in week 1; start with data that's already certified; keep the first release's data needs small |
| **Client privacy in recorded meetings** | Client consent and the bank's recording policy apply; notes are drafts until the RM approves |

---

### 8. What other banks are doing

A web scan (October 2026) found the same basic pattern at other banks:
signals from data, shown inside the CRM, with the reason visible and the RM
in control. Most published numbers are vendor or bank claims rather than
controlled results, so treat them as directional.

| Who | What they did | Source |
|---|---|---|
| BMO (commercial banking) | "Next Best Offer" engine ranks leads and offers for relationship teams, delivered through the CRM with the reason for each offer shown | [BMO AI](https://ai.bmo.com/?p=569) |
| Bank of America | Its CTO said AI prep tools mean a banker can cover about 50 clients instead of 15 in some cases (management claim, not audited) | Reuters, 2025, via [TechInformed](https://techinformed.com/?p=37424) |
| Morgan Stanley (wealth) | "Debrief", used with client consent, summarizes meetings, drafts a follow-up email for the advisor to review and send, and saves a note into Salesforce. Separately, its CFO said AI-matched referrals of prospects to advisors doubled to more than 100,000 (2024, year to date) | [Morgan Stanley](https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch) (June 2024), [The Daily Upside](https://www.thedailyupside.com/technology/artificial-intelligence/how-morgan-stanleys-ai-helped-close-100k-new-clients-this-year/) (Oct 2024) |
| JPMorgan (wealth) | Said its AI tools, including the adviser tool "Coach", helped advisers lift sales and handle client requests during the April 2025 selloff (no figure given) | Reuters, May 2025, via [AOL](https://www.aol.com/news/jpmorgan-says-ai-helped-boost-170825172.html) |
| Banco do Brasil | 12,000+ RMs get AI conversation summaries and sentiment in one workspace, with sentiment written back to the CRM | [NiCE case study](https://www.nice.com/resources/banco-do-brasils-bankers-stopped-working-yesterdays-data-and-let-ai-hand-them-todays) (vendor, 2026) |
| CaixaBank | Uses Salesforce Agentforce and Data Cloud, and built an AI assistant with Salesforce's AI tools to guide product applications; a specialist always finalizes the contract | [CaixaBank](https://www.caixabank.com/en/headlines/news/caixabank-and-salesforce-collaborate-to-personalise-customer-experience-in-banking-services-through-ai) (2025) |

**Industry figures (directional; checked against the article's text on 2026-10-10):**
- McKinsey says banks that rework one frontline area end to end can see about 3–15% higher revenue per RM and 20–40% lower cost to serve ([McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready); ⚠️ publication date not confirmed).
- RMs at many commercial banks spend only about 25–30% of their time in client conversations ([McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready), same article).

**What this approach takes from it:** pair insights with freed-up time; track
clients covered per RM; make adoption a management routine; capture why RMs
reject insights; include internal referrals; and prove results against a
comparison group, which is rare in published results.

---

### 9. What I'd confirm in the first weeks

This approach is built on the platforms named in the role: Salesforce,
Snowflake, Microsoft Fabric and Power BI, Microsoft 365 Copilot, Power
Platform and AWS Bedrock. I've been told all of them are live, so the plan
builds on them. I'd confirm early:

- Which revenue lever matters most to the business right now?
- How will success be judged in the first 6 months?
- Which RM teams would make a good pilot group?
- Who owns the client data in Snowflake and Salesforce?
- How are RMs measured and rewarded today?
- How long does AI governance review usually take?
- Is recording client meetings in Teams allowed, how is consent captured, and who owns the recording policy?
- What team and budget are available for the pilot?
- How each platform is set up for RMs today: which features, licenses and connections?

---

### Appendix A: Agent specs

Each agent named in Steps 1–6. AI sales coaching (wave 3): agent spec not written
yet (closed item C44, step 4 of the use case kit). The product's agents (A1 to A5) are written so a
platform team can build them and a risk partner can review them; the team's
agents are the product machine's general agents, specified in full in the
agent library. **[X]** values are set in Define.

**Rules for every agent:**
- **One job.** If a request falls outside it, the agent says so and stops.
- **Read-only by default.** Any change to a record, or anything that reaches a client, needs a named person's click.
- **Approved models and data only.** Uses only AI models and data sources approved for this product.
- **Never guesses.** If its inputs are missing, stale or fail a check, it stops and alerts its owner rather than producing a weaker answer.
- **Everything logged.** Each run records who, what, when, which sources and what it produced, for audit and for measuring.

#### Agents RMs use (the product)

**A1. Signal finder** · wave 1 · runs on Snowflake (Cortex)
- **Job:** each night, scan each RM's clients for opportunity signals using the agreed rules and scores (product gaps; from wave 2, early warnings and referral needs). From wave 2, also monthly: find prospect lookalikes in the licensed prospect data, using the criteria compliance approves.
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
- **Inputs:** the Salesforce client record; open insights; the RM's calendar; the Teams meeting recap (recorded only with client consent).
- **Allowed actions:** read the inputs; create drafts for the RM.
- **Not allowed:** sending anything to a client; saving to Salesforce without the RM's approval.
- **Outputs:** a brief, a recap, a draft email and draft call notes, all marked as drafts.
- **Stops when:** the drafts are delivered to the RM. If there's no recording or consent, it drafts from the RM's own notes or asks for them.
- **Proof it worked:** the RM approves or edits each draft (logged); share of drafts used with light edits ≥ [X]%.
- **Person in charge:** the RM approves before anything is saved or sent.

**A4. Weekly opportunity digest** · wave 1 · runs on Power Automate, with A2
- **Job:** every Monday, send each RM their top [X] opportunities.
- **Inputs:** insights from A2, ranked by the agreed score.
- **Allowed actions:** send a message to the RM in Teams or Outlook.
- **Not allowed:** messaging anyone other than the RM (and, if agreed, their manager).
- **Outputs:** one digest per RM, with links to each client record.
- **Stops when:** every pilot RM has a digest, or there are no new insights (then it sends a short "nothing new" note).
- **Proof it worked:** delivery log; open and act-on rates in Power BI.
- **Person in charge:** the RM decides what to pursue; the product manager owns timing and ranking.

**A5. Client Q&A** · wave 3 · runs on Salesforce Agentforce or a Copilot Studio agent in Teams
- **Job:** answer "what should I know before my call with this client?" and similar questions.
- **Inputs:** Salesforce and Snowflake, read-only, only clients the RM is allowed to see.
- **Allowed actions:** read; answer with sources; propose a record update for the RM to click.
- **Not allowed:** answering about clients outside the RM's permissions; giving credit or pricing advice.
- **Outputs:** an answer with its sources, or "I don't have that information."
- **Stops when:** the question is answered, or it is out of scope (it says so and names who can help).
- **Proof it worked:** test-set score meets the quality bar; zero permission breaches in red-team testing.
- **Person in charge:** the RM; the product manager for quality.

A6 (a how-to helper) was removed on 2026-10-17: champions and a Teams channel answer "how do I…?" questions in the pilot. Its number isn't reused.

#### Agents the team uses

These are the product machine's general agents (M20 to M33), specified in full in the
agent library. The table shows how this project uses each one: its RM inputs, owners and checks.

| Agent | Step | Job | Inputs | Allowed actions | Outputs | Stops when | Proof it worked | Person in charge |
|---|---|---|---|---|---|---|---|---|
| **M20. Interview synthesizer** | Discover | Turn interview recaps into themes and quotes | Teams transcripts (only with consent), interview notes | Read; draft | Themes, each linked to its source | All interviews processed | Product manager spot-checks each theme | Product manager |
| **M21. Opportunity sizer** | Discover | Answer plain-English sizing questions | Snowflake balances and products; Salesforce pipeline | Read-only queries | Sized levers with the query shown | Each lever sized | An analyst re-runs the key numbers | Analyst |
| **M22. Time-use analyst** | Discover | Find where RM time goes | Salesforce activity and win/loss | Read-only queries | Time-use breakdown | Breakdown complete | Product manager checks with RMs | Product manager |
| **M23. Requirements drafter** | Define | Draft problem statement, user stories, acceptance criteria | Discover findings | Draft only | Draft brief and stories | Drafts delivered | Team and sponsor approve | Product manager |
| **M24. Data contract checker** | Define | Check fields exist, are fresh and pass quality checks | Snowflake tables and their quality and access records | Read-only | Gap list | Every field checked in Define; after that, runs on every data refresh and alerts the data owner on failure | Data owner signs off | Data owner |
| **M25. Risk intake assistant** | Define | Pre-fill the risk intake; flag likely high-risk areas | Bank policies, product brief | Draft only | Pre-filled intake | Intake drafted | Risk partner sets the rating | Risk partner |
| **M26. Test grader** | Build | Score each version against the test set | Test set, product outputs | Read; score | Score report | Every test case scored | Experienced RMs grade a sample | Product manager |
| **M27. Red-team agent** | Govern | Try to break the product (other RMs' clients, credit requests) | The product in test | Send test requests in the test environment only | Failure list | All attack types run | Risk reviews every failure | Risk partner |
| **M28. Fairness monitor** | Govern | Check opportunities are spread fairly across segments and regions | Opportunity outputs, client segments | Read-only | Fairness report | Report complete; runs again monthly after launch | Compliance reviews results | Compliance |
| **M29. Evidence pack assembler** | Govern | Compile results, data use and controls into review documents | Test results, data contract, controls | Draft only | Evidence pack | Pack drafted | Product manager and risk verify every claim | Product manager |
| **M30. Feedback triage** | Release | Sort feedback into bugs, quality issues and ideas | Feedback logged in Salesforce | Read; tag; add to backlog | Tagged backlog items | All new feedback sorted | Product manager reviews a weekly sample | Product manager |
| **M31. Impact analyst** | Measure | Report pipeline and revenue from AI insights against the comparison group | AI-tagged Salesforce opportunities; Snowflake | Read-only queries | Monthly impact figures | Report complete | Analytics validates before reporting | Analytics |
| **M32. Quality watchdog** | Measure | Re-run the test set after every change; alert on drift | Test set, live outputs, feedback | Read; alert | Score trend and alerts | Each run complete | Alerts reviewed within [X] days | Product manager |
| **M33. Improvement scout** | Measure | Propose next backlog items or the next lever | Dashboards, feedback, reviews | Draft only | Ranked suggestions | List delivered | Product manager and sponsor decide | Product manager |

---

### Appendix B: Workflows

Each RM-facing capability as a step-by-step flow. Every RM-facing flow (B1–B8)
has one **decision point** where the RM decides, and everything is logged.
B9 is the release routine behind them. AI sales coaching (wave 3): workflow not
written yet (closed item C44, step 4 of the use case kit).

**B1. Monday opportunity list** (wave 1)
- **Trigger:** every night (signals); every Monday morning (digest).
- **Steps:** 1. A1 scans clients and writes signals. 2. A2 writes an insight for each. 3. Insights appear in the assistant's panel on the Salesforce client record (no record field changes). 4. A4 sends each RM their top [X]. 5. **Decision point:** the RM accepts, rejects (with a reason) or changes each insight. 6. On accept, the RM creates an opportunity in Salesforce, tagged "AI-sourced." 7. M30 sorts the feedback. 8. Managers review the list in the weekly pipeline meeting.
- **Logged:** signals, insights, opens, decisions and reasons, opportunities created.
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
- **Steps:** 1. A2 explains the signal with the numbers. 2. An alert appears on the client record and in the next digest. 3. **Decision point:** the RM decides whether and how to reach out, and logs the action.
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

## Part 6: Core use cases and outside research

Working file: `memos/use-case-library.md`.


**The need in one line:** RMs at many commercial banks spend only about 25–30% of their time with clients (McKinsey). Admin, weak leads and meeting prep take the rest. So the value is in two places: better opportunities, and the time to act on them.

| Core use case | Where the value is | Outside evidence (McKinsey unless noted) | Our AI product (wave) |
|---|---|---|---|
| **Prospecting and next best opportunities** | Finding the clients and prospects most likely to buy | About 30% pipeline growth and 10% higher revenue; one bank saw twice the conversion rate of traditional leads | Monday opportunity list (1); prospect lookalikes (2) |
| **Lead nurturing, including cross-sell** | More qualified leads and referrals between teams | Two to three times more qualified leads; 5% higher conversion (early pilots). Morgan Stanley: AI-matched referrals to advisors doubled to more than 100,000 (2024, its CFO) | Referral prompts (2). Contacting prospects on its own: out on purpose |
| **Account intelligence and meeting prep** | Better meetings in less prep time | About 25% less prep time; 10% more time with clients. Bank of America's CTO: AI prep lets a banker cover about 50 clients instead of 15 in some cases (not audited) | Pre-meeting client brief (1); client Q&A (3) |
| **Deal scoring and pricing** | Better margins, faster approvals | 10% margin gains; one bank cut deal turnaround from five days to two | Out on purpose: the AI never sets or suggests a price (fair-lending rules) |
| **AI sales coaching** | Better calls; new RMs up to speed sooner | Customer satisfaction up seven points; new bankers up to speed 20% faster | AI sales coaching (3) |
| **Admin off the RM's plate** (our own) | Hours back for clients; better CRM data | Admin ranks first or second of bankers' problems at every stage of a sale (survey of 406 bankers, October 2025); it earns part of the 10–12 hours a week McKinsey expects back per banker, and about 40% better coverage | Meeting follow-up, with call notes into Salesforce (1) |
| **Keep clients** (our own) | Clients kept before they drift away | No outside figure; set from the bank's own retention data | Early warning (2) |

**The headline numbers.** Banks that rework one frontline area end to end see about 3–15% higher revenue per RM and 20–40% lower cost to serve. 53% of bankers cite a shortage of high-quality leads as their biggest barrier. McKinsey's warning: "Banks are moving fastest on the least valuable tools."

**What other banks are doing.**
- **BMO** (commercial banking): a "Next Best Offer" engine ranks leads and offers in the CRM, with the reason shown ([BMO AI](https://ai.bmo.com/?p=569)).
- **Morgan Stanley** (wealth): "Debrief", used with client consent, summarizes meetings, drafts the follow-up email and saves a note into Salesforce ([Morgan Stanley, June 2024](https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch)).
- **Banco do Brasil:** 12,000+ RMs get AI conversation summaries in one workspace ([NiCE case study](https://www.nice.com/resources/banco-do-brasils-bankers-stopped-working-yesterdays-data-and-let-ai-hand-them-todays), vendor, 2026).
- **JPMorgan** (wealth) and **CaixaBank** report AI tools for advisers and bankers, without published results.

The pattern: signals from data, shown inside the CRM, with the reason visible and the banker in control. Results against a comparison group are rare.

**Source:** McKinsey, "Agentic AI is here. Is your bank's frontline team ready?" (Kumar Kanagasabai, Chris Lu, Shital Chheda; [link](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready)), based on a survey of about 400 US and Canadian bankers; checked against the article's text on 2026-10-10. ⚠️ Publication date not confirmed. Full exhibit data and every RM detail: [RM Detail](https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n).


## Part 7: McKinsey's research in full

Working file: `memos/mckinsey-frontline-ai.md`.

A core reference for choosing which core use cases and AI products to build for relationship managers (RMs), and the basis for the RM plan's seven core use cases. It summarizes McKinsey's
article "Agentic AI is here. Is your bank's frontline team ready?" and checks the
RM plan against its five use cases. Checked against the article's text, pasted
in by me on 2026-10-10.

> **Source.** Kumar Kanagasabai, Chris Lu and Shital Chheda (McKinsey):
> https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready
> Based on a survey of about 400 US and Canadian bankers, RMs and sales leaders.
> McKinsey's numbers come from its own client work and early pilots, not
> controlled studies, so treat them as directional. ⚠️ The page I pasted showed no
> publication date, so the date is unconfirmed (an earlier draft said December 2025).

### The headline numbers

| Finding | McKinsey's words |
|---|---|
| Revenue and cost | Banks that rewire one frontline area end to end "enjoy between 3 and 15 percent higher revenues per RM and 20 to 40 percent lower cost to serve" |
| Time with clients | "In many commercial banks, relationship managers spend just 25 to 30 percent of their time in client dialogue" |
| Time freed | "ten to 12 hours a week returned to each banker", improving the coverage ratio (clients per banker) by about 40 percent |
| Top problems | Excessive admin, low-quality leads, and difficult meeting prep. 53 percent cite a shortage of high-quality leads as their biggest barrier |
| Admin at every stage | McKinsey's Exhibit 3, the top three challenges at each stage of the banking sales funnel (% of respondents; Frontline Sales Survey, October 2025, 406 respondents). Prospecting: low-quality leads 37, admin 32, meeting prep 26. Outreach: admin 33, generic outreach 30, meeting prep 28. Early conversation: admin 31, low-quality leads 31, meeting prep 29. Late-stage conversation: admin 35, slow internal approvals 28, meeting prep 25. Negotiation: admin 33, slow approvals 32, hard to prioritize accounts 28. Deal close: admin 37, slow approvals 34, meeting prep 26. So admin ranks first or second at all six stages. Shared by me as a screenshot on 2026-10-10 |
| Where banks go wrong | "Banks are moving fastest on the least valuable tools" |

### The five use cases

| # | Use case | What the AI does | Reported impact (McKinsey) |
|---|---|---|---|
| 1 | **Prospecting** (market maps and next best opportunities) | Combines data sources into ranked lists of high-potential clients, refreshed as markets change | About 30% pipeline growth and 10% higher revenue; one bank saw twice the conversion rate of traditional leads |
| 2 | **Lead nurturing** (including cross-sell) | An agent replies to inquiries, sends tailored content and books meetings, passing only qualified leads to the RM | Two to three times more qualified leads; 5% higher conversion (early pilots) |
| 3 | **Account planning and meeting prep** (account intelligence) | Pulls data from many sources into an account plan or briefing in minutes, with talking points | About 25% less prep time; 10% more time with clients |
| 4 | **Deal structuring and pricing** (dynamic deal scoring) | Recommends pricing and discounts from past deals and client data, and speeds approvals | 10% margin gains; one bank cut deal turnaround from five days to two |
| 5 | **Coaching** (AI sales coaching) | Reviews call transcripts and gives each banker personal guidance | Customer satisfaction up seven points; new bankers up to speed 20% faster |

McKinsey ties these to the stages of a sale: prospecting and deal close
(use case 1), outreach (2), early and late-stage conversations (3, with
coaching in late stage), and negotiation (4).

### How our RM plan covers them

| McKinsey use case | In our RM plan | Coverage |
|---|---|---|
| 1. Prospecting and next best opportunities | Wave 2: prospect lookalikes (B8, moved up from wave 3 on 2026-10-15). Wave 1's Monday opportunity list finds next best opportunities in existing clients | **Covered.** New-client prospecting now comes in wave 2, because McKinsey reports its biggest numbers here |
| 2. Lead nurturing, including cross-sell | Wave 2: referral prompts (B6) for cross-sell between teams. Nothing contacts prospects on its own | **Partly, by design.** Our rule is that nothing reaches a client without the RM, so an agent that writes to prospects by itself is out of scope today |
| 3. Account intelligence and meeting prep (McKinsey: account planning and meeting prep) | Wave 1: pre-meeting client brief (B2). Wave 3: Client Q&A (B7) | **Covered**, and first in line |
| 4. Deal scoring and pricing (McKinsey: deal structuring and pricing) | Not in the plan. Under control K3 the AI never makes a credit decision and never sets or suggests a price | **Not covered, by design** (kept out on 2026-10-15). Pricing touches fair-lending rules, so it would need a much higher bar |
| 5. AI sales coaching | Wave 3: AI sales coaching from call transcripts (added 2026-10-15; its agent spec and workflow are still to write). | **Covered from wave 3** |

**Also in our plan, not in McKinsey's five:** early warning when a client may
leave (B5), and the meeting follow-up (B3) and call notes saved to the CRM (B4), both in wave 1,
which tackle McKinsey's number one problem, excessive admin.

**What this means:** wave 1 lines up with McKinsey's most-cited problem (meeting
prep and admin). Since the decisions of 2026-10-15 (below), prospecting comes in
wave 2 and coaching in wave 3 (waves agreed 2026-10-17). Autonomous lead nurturing
and pricing are left out on purpose, for governance reasons.

### What it changed: the RM plan now uses McKinsey's framework (decided 2026-10-10)

The RM plan is now built around The RM Assistant (memo v10, 2026-10-17): the seven core use cases are the needs its capabilities answer. Their return profiles live here: McKinsey's five above, plus our own two: **admin off the RM's plate** (problem: admin and CRM updates crowd out client time, McKinsey's top problem, which its five use cases don't name; return: part of the 10 to 12 hours a week McKinsey expects back per banker, and about 40% better coverage) and **keep clients** (problem: clients drift away before anyone notices; return: set from the bank's own retention data). Decided on 2026-10-15 (closed items C30 to C32 in the Open Items log):
- **Prospecting earlier: yes.** McKinsey's biggest revenue numbers are in prospecting, and our prospect lookalikes were in wave 3. Outside prospect data may set the pace.
- **Add coaching: yes** (placed in wave 3 on 2026-10-17, because it needs recording consent and more review: C41). Low risk, uses call transcripts the meeting features already need, and McKinsey reports faster ramp-up for new bankers.
- **Autonomous lead nurturing and pricing stay out for now: yes.** An agent that writes to prospects on its own, or recommends prices, conflicts with "nothing reaches a client without the RM" and the fair-lending control (K3). Revisit later with evidence.

### McKinsey's five principles for capturing the value

1. Define the business model and the value it should create.
2. Rework a frontline area end to end, not piece by piece, with a repeatable playbook for scaling.
3. Build reusable technology: an orchestration layer for agents, a data foundation (an "ontology" of the bank's workflows, decisions and knowledge), and trust and security.
4. Put governance in place: how much each agent may do on its own, monitoring and audit.
5. Upskill the workforce, as RM roles change.

**Where our framework already does this:** 1 is the value model and the
sponsor's outcome (Discover); 2 is the six-step process and the playbook; 3 is
the agent library, the data contract and the Glossary (our working vocabulary,
which plugs into the bank's ontology); 4 is the Controls Catalog and
"assistive first"; 5 is Release and adopt (training on users' own work and
champions). ⚠️ Role redesign (new roles such as "agent orchestrator") isn't
covered yet.

_Last updated: 2026-10-18_
