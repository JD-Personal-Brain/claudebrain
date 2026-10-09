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
- **2. Define:** one-sentence problem and measurable outcome · choose the platform · data contract (exact fields, freshness, quality checks) · start the risk intake · user stories with acceptance criteria · measures, quality bar and value model · scope the smallest useful first release and pilot group.
- **3. Build:** prepare trusted data · simple, explainable logic first (AI explains, it doesn't invent) · deliver it where users already work · show the source behind every answer · one-click feedback · build the test set (real examples with known good answers).
- **4. Govern and test:** confirm the risk rating · review data and privacy · testing evidence (accuracy, made-up answers, red-teaming) · fairness check · confirm controls (human approval, guardrails, audit logs) · vendor reviews · sign-offs from risk, compliance, privacy and security.
- **5. Release and adopt:** pilot with a comparison group · build it into existing routines (the core of adoption) · train on users' own work · recruit champions · celebrate wins · fix fast · scale in waves after a go/no-go check.
- **6. Measure and iterate:** live dashboards · compare with the baseline and comparison group · re-test after every change and watch for quality slipping ("drift") · monthly keep/change/stop review · feed the next wave.

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

## Starting a new project with this framework
1. Name the outcome and the sponsor.
2. Fill in the table above for this project: its question, governance thread and gate for each step.
3. Work through Discover first, using the write-up layout.
4. Keep the plan in `memos/<project>.md`, as the RM memo does.

_Last updated: 2026-10-09_
