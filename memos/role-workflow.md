# Product Workflow: how every AI product moves from idea to adoption

_Working copy of the designed page (https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv).
Claude loads this every session. It is the one home of the six steps, their
questions, governance threads and gates, and what happens in each step._

Page 1 of the four "How we deliver" pages, read in this order:
1. **Product Workflow** (this page): the steps and their go/no-go gates.
2. **Product Framework** (`product-framework.md`): the rules every product follows.
3. **Product Machine** (`product-machine.md`): every task, marked by who does it.
4. **Product Playbook** (`playbook/`): how to do each sub-step the first time.

> **Source.** The six steps and gates were first taken from my RM analytics memo
> (`memos/rm-analytics-framework.md`, memo v6, 2026-10-08) with the RM details
> removed; the sub-steps below come from the Product Playbook. Memo v8 (2026-10-09) follows
> the same six steps and gates and is the full worked example, with agent specs
> and workflows in its appendices. Its sub-steps are
> tailored to RM work and aren't yet numbered like the playbook's 44; that's part
> of applying the product machine to the RM memo (work item W9 in the Open Items log).

## The six steps at a glance
Every AI product goes through six steps, each ending in a **go/no-go gate**. The
first pass through all six is fast. After that, steps 3 to 6 repeat in short
cycles, and each new feature wave takes a quick pass through Discover and
Define (the quick pass, in the Product Framework, which also says which gate is passed for a project, an AI product or a feature wave). **Governance runs through every step:** step 4 is the formal approval,
not the first time risk partners see the product.

| Step | Question | Governance thread | Gate |
|---|---|---|---|
| 1. Discover | Which problem or opportunity is worth solving first? | Risk partner briefed on the idea | Sponsor agrees on the target, the measure and today's baseline |
| 2. Define | What exactly do we build first, and how will we know it worked? | Risk intake and early rating; data use approved | Brief, data contract and risk rating agreed; value model shows payback within [X] months |
| 3. Build | What's the smallest version users will use and trust? | Controls built in; test set created | Meets the quality bar in testing; every control is built and passes its control test |
| 4. Govern and test | Is it safe, fair and controlled? | Formal validation and sign-offs | All sign-offs recorded; monitoring plan agreed |
| 5. Release and adopt | Will users use it every week? | Live monitoring; incident process | Weekly use and leading results hit targets; no serious incidents; long-term owner confirmed before scaling |
| 6. Measure and iterate | Is it delivering the outcome, and what comes next? | Ongoing monitoring | Each month (and at the end of each feature wave): keep, change or stop each AI product; each quarter: invest more, adjust or stop overall |

**Building starts early:** a rough clickable mock-up within
days of the first interviews (sub-step 1.6), on sample data. The pace is set by the
limiting factor (usually data access and review), not build time.

## What happens in each step
One item per playbook sub-step, in the same order (1.0 to 6.6).
Each sub-step on the designed page links to its card on the Steps Catalog
(https://claude.ai/artifact/8UncWMYUq7hsJUhn5NSYEB); the steps as a clickable map are on
the Workflow Maps (https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX). Both read each step's
question, governance thread and gate from the table above, so they can't drift from it.
- **1. Discover:** kick off the project (sponsor, who decides, tracker, risk briefing) · frame the outcome with the sponsor · size the opportunity with real data · interview and shadow users · map where their time goes · understand how they're measured and rewarded · test a rough mock-up · pick the first target and record today's numbers.
- **2. Define:** write the problem and the outcome (one sentence each, measurable) · choose the platform and delivery path · define the data contract (exact fields, freshness, quality checks) · start the risk intake and list the control requirements · write user stories and acceptance criteria · set priorities and record the trade-offs · set the measures (the five kinds, in the Product Framework), quality bar and value model · scope the first release and the pilot group.
- **3. Build:** design the solution and choose the AI capabilities (agents, retrieval with sources, data flows, workflow automations or system integrations) · prepare trusted data · build the logic: simple rules first, AI explains (it doesn't invent) · build in the controls · deliver it where users work, with the source behind every answer and one-click feedback · build the test set (real examples with known good answers) · test against the quality bar.
- **4. Govern and test:** confirm the risk rating and register the product · review data and privacy · gather the testing evidence (accuracy, made-up answers, red-teaming) · check fairness · confirm the controls work (human approval, guardrails, audit logs) · confirm the vendor reviews · assemble the evidence pack and get sign-offs from risk, compliance, privacy and security · agree the monitoring plan.
- **5. Release and adopt:** confirm release readiness · launch the pilot, with a comparison group · build it into routines (the core of adoption) · train users on their own work · recruit champions and celebrate wins · fix fast · scale in user waves after a go/no-go check.
- **6. Measure and iterate:** track the measures on a live dashboard · compare with the baseline and the comparison group · re-test after every change, and watch for quality slipping ("drift") · hold the monthly keep / change / stop review · feed the next feature wave · improve the machine itself.

_Last updated: 2026-10-15_
