# Product framework: how I organize product work

Claude loads this every session. Whenever we plan or work on a product, we
organize it by these six steps.

> **Source.** Taken from my RM analytics memo (`memos/rm-analytics-framework.md`,
> memo v6, 2026-10-08) with the RM details removed. That memo is the full
> worked example. It's still waiting for my review, so update this page if the
> review changes the steps.

## The six steps at a glance
Each step ends in a **go/no-go gate**. The first pass through all six is fast.
After that, steps 3 to 6 repeat in short cycles, and each new set of features
takes a quick pass through Discover and Define. **Governance runs through every
step.** Step 4 is the formal approval, not the first time risk partners see the product.

| Step | Question it answers | Governance thread | Gate (go/no-go) |
|---|---|---|---|
| **1. Discover** | Which problem or opportunity is worth solving first? | Risk partners briefed on the idea | Sponsor agrees on the target, the measure and today's baseline |
| **2. Define** | What exactly do we build first, and how will we know it worked? | Risk intake and early rating; data use approved | Brief, data contract and risk rating agreed; value model makes sense |
| **3. Build** | What's the smallest version users will use and trust? | Controls built in; test set created | Meets the quality bar in testing |
| **4. Govern and test** | Is it safe, fair and controlled? | Formal validation and sign-offs | All sign-offs recorded; monitoring plan agreed |
| **5. Release and adopt** | Will users use it every week? | Live monitoring; incident process | Weekly use and results hit targets; no serious incidents |
| **6. Measure and iterate** | Is it delivering the outcome, and what comes next? | Ongoing monitoring | Keep, change or stop each feature; invest more, adjust or stop overall |

## What happens in each step
- **1. Discover:** frame the outcome with the sponsor · size the opportunity with real data · interview and shadow users · map where their time goes · understand how they're measured and rewarded · test a rough mock-up · pick the first target and record today's numbers.
- **2. Define:** one-sentence problem and measurable outcome · choose the platform and delivery path · data contract (exact fields, freshness, quality checks) · start the risk intake and list the control requirements · user stories with acceptance criteria · backlog priorities and the trade-offs behind them · the five kinds of measures (below), quality bar and value model · scope the smallest useful first release and pilot group.
- **3. Build:** configure the right AI capability: agents, retrieval (search over documents, with sources), data flows, workflow automations or system integrations · prepare trusted data · simple, explainable logic first (AI explains, it doesn't invent) · deliver it where users already work · show the source behind every answer · one-click feedback · build the test set (real examples with known good answers).
- **4. Govern and test:** confirm the risk rating · review data and privacy · testing evidence (accuracy, made-up answers, red-teaming) · fairness check · confirm controls (human approval, guardrails, audit logs) · vendor reviews · sign-offs from risk, compliance, privacy and security.
- **5. Release and adopt:** confirm release readiness · pilot with a comparison group · build it into existing routines (the core of adoption) · train on users' own work · recruit champions · celebrate wins · fix fast · scale in waves after a go/no-go check.
- **6. Measure and iterate:** live dashboards · compare with the baseline and comparison group · re-test after every change and watch for quality slipping ("drift") · monthly keep/change/stop review · feed the next wave.

## Running the work (every step)
- **Who's involved and who decides:** sponsor (outcome, funding, go/no-go) · user leaders and pilot users (workflow, feedback) · product manager (scope, priorities, trade-offs) · data owners (what data may be used) · platform teams (technical design) · model risk (risk rating, approval) · compliance, privacy and security (controls, sign-off) · operations (running it day to day). Agree this at the start of Discover.
- **Decisions and trade-offs:** record each one with who decided and why, so partners stay aligned.
- **Dependencies, risks and issues:** one list, each item with an owner and a date; review it weekly.

## The five kinds of measures (set in Define, tracked in Measure)
Usage · Quality · Business impact · Adoption · Risk and controls. These are the five the job description names.

## How each step is written up
Every step uses the same layout, so plans are easy to compare:
**Goal · Work** (sub-steps and tools) **· AI strategy** (the agents) **· AI for the team · AI for users · Data · Output · Checks · Gate**

## AI principles (every step)
- **Two kinds of agents:** some help the team do the work; others are the product users see.
- **Assistive first:** AI drafts or suggests, and a named person decides. Autonomy grows only with evidence.
- **One job each:** a clear job, a short list of allowed actions, read-only by default, and every action logged.
- **Built where the work happens:** use the tools people already work in, and add a new platform only when it's needed.

## The quality bar (thresholds set in Define)
Accuracy (numbers match the source) · Sources shown · Relevance (users rate it relevant) · Usefulness (users would act on it) · Permissions (no one sees data they shouldn't, with zero tolerance).

## How the job description maps to this framework
| Job accountability (from `job-description.md`) | Where it lives here |
|---|---|
| Own products from discovery through governed release, adoption and improvement | All six steps |
| Work with bankers to find needs; turn them into clear products | Discover → Define |
| User stories, acceptance criteria, backlog priorities, release scope, success measures, control requirements, trade-offs | Define |
| Configure AI capabilities (agents, retrieval, data flows, automations, integrations) in tools bankers use | Build |
| Governed delivery: risk, controls, privacy, responsible AI and regulation built in from the start | Governance thread in every step; formal approval in Govern and test |
| Lead with limited oversight: priorities, decisions, dependencies, testing, controls, release readiness, issues | Running the work; Build to Release gates |
| Drive adoption and change in a regulated environment | Release and adopt |
| Define and monitor usage, quality, impact, adoption, and risk and control measures | The five kinds of measures; Define and Measure and iterate |
| Align business, technology, data, risk, compliance and operations partners | Running the work: who decides, decision log |

## Starting a new project with this framework
1. Name the outcome and the sponsor.
2. Fill in the table above for this project: its question, governance thread and gate for each step.
3. Work through Discover first, using the write-up layout.
4. Keep the plan in `memos/<project>.md`, as the RM memo does.

_Last updated: 2026-10-09_
