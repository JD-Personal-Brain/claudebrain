# Product framework: how I organize product work

Claude loads this every session. Whenever we plan or work on a product, we
organize it by these six steps.

> **Source.** Taken from my RM analytics memo (`memos/rm-analytics-framework.md`,
> memo v6, 2026-10-08) with the RM details removed. Memo v8 (2026-10-09) is
> aligned back to this page and the job description, and is the full worked
> example, with agent specs and workflows in its appendices. It's still waiting for my review, so update this page if the review
> changes the steps.

## The six steps at a glance
Each step ends in a **go/no-go gate**. The first pass through all six is fast.
After that, steps 3 to 6 repeat in short cycles, and each new set of features
takes a quick pass through Discover and Define. **Governance runs through every
step.** Step 4 is the formal approval, not the first time risk partners see the product.

| Step | Question it answers | Governance thread | Gate (go/no-go) |
|---|---|---|---|
| **1. Discover** | Which problem or opportunity is worth solving first? | Risk partners briefed on the idea | Sponsor agrees on the target, the measure and today's baseline |
| **2. Define** | What exactly do we build first, and how will we know it worked? | Risk intake and early rating; data use approved | Brief, data contract and risk rating agreed; value model shows payback within [X] months |
| **3. Build** | What's the smallest version users will use and trust? | Controls built in; test set created | Meets the quality bar in testing; every control has proof |
| **4. Govern and test** | Is it safe, fair and controlled? | Formal validation and sign-offs | All sign-offs recorded; monitoring plan agreed |
| **5. Release and adopt** | Will users use it every week? | Live monitoring; incident process | Weekly use and results hit targets; no serious incidents |
| **6. Measure and iterate** | Is it delivering the outcome, and what comes next? | Ongoing monitoring | Each month: keep, change or stop each feature; each quarter: invest more, adjust or stop overall |

## What happens in each step
- **1. Discover:** kick off (sponsor, who decides, tracker, risk briefing) · frame the outcome with the sponsor · size the opportunity with real data · interview and shadow users · map where their time goes · understand how they're measured and rewarded · test a rough mock-up · pick the first target and record today's numbers.
- **2. Define:** one-sentence problem and measurable outcome · choose the platform and delivery path · data contract (exact fields, freshness, quality checks) · start the risk intake and list the control requirements · user stories with acceptance criteria · backlog priorities and the trade-offs behind them · the five kinds of measures (below), quality bar and value model · scope the smallest useful first release and pilot group.
- **3. Build:** configure the right AI capability: agents, retrieval (search over documents, with sources), data flows, workflow automations or system integrations · prepare trusted data · simple, explainable logic first (AI explains, it doesn't invent) · deliver it where users already work · show the source behind every answer · one-click feedback · build in the controls · build the test set (real examples with known good answers) · test against the quality bar.
- **4. Govern and test:** confirm the risk rating · review data and privacy · testing evidence (accuracy, made-up answers, red-teaming) · fairness check · confirm controls (human approval, guardrails, audit logs) · vendor reviews · sign-offs from risk, compliance, privacy and security · agree the monitoring plan.
- **5. Release and adopt:** confirm release readiness · pilot with a comparison group · build it into existing routines (the core of adoption) · train on users' own work · recruit champions · celebrate wins · fix fast · scale in waves after a go/no-go check.
- **6. Measure and iterate:** live dashboards · compare with the baseline and comparison group · re-test after every change and watch for quality slipping ("drift") · monthly keep/change/stop review · feed the next wave · improve the delivery machine itself.

## Running the work (every step)
- **Who's involved and who decides:** sponsor (outcome, funding, go/no-go) · user leaders and pilot users (workflow, feedback) · product manager (scope, priorities, trade-offs) · data owners (what data may be used) · platform teams (technical design) · model risk (risk rating, approval) · compliance, privacy and security (controls, sign-off) · operations (running it day to day). Agree this at the start of Discover.
- **Decisions and trade-offs:** record each one with who decided and why, so partners stay aligned.
- **Dependencies, risks and issues:** one list, each item with an owner and a date; review it weekly.

## The delivery machine: running many projects with one PM
I'm one person running several projects at once, so the framework has to run
mostly by itself. Automation does the routine work and pushes tasks to people
against the timeline, so my time goes only where a person is needed.
Every project uses the same steps, tracker and templates, so they all run the
same way side by side. *(Added 2026-10-09. Tool choices are guesses until I see
the bank's setup: verify each one.)*

### Three kinds of work, plus partner sign-offs
Every task in every step is marked as one of these:
- **Auto (runs on its own):** a workflow or agent does it and tells the right person. No one has to remember it.
- **Draft (AI drafts, a person checks):** AI does the first version, and a named person approves it.
- **Me (only a person):** decisions, agreement between people, relationships and trade-offs. This is where my hours go.
- **Partner:** a decision only a named partner can make, such as a risk or compliance sign-off. Never automated.

**Not sure yet:** whether the bank lets automations message people or update
trackers by themselves. Confirm this at the first project, because it decides
how much can be **Auto**.

### Each step's tasks, by kind
One row per task, numbered to match the sub-steps in `playbook/`. **Kind** is the
target once the machine is running. The first time through, many tasks are
done one kind closer to a person, so the work can be logged before it's
automated; each playbook step's review table shows both. The gate check below
moves tasks toward **Auto** over time. ⚠️ marks an Auto task that depends on the
bank allowing automations to message people.

**1. Discover**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 1.0 | Agree the sponsor's role and who decides; brief a risk contact | Me | Meeting | Sponsor, risk |
| 1.0 | Set up the tracker, decision log and project file | Draft | Kickoff pack builder | Me |
| 1.1 | Agree the outcome and measure | Me | Meeting | Sponsor |
| 1.1 | Write the outcome note | Draft | Outcome note drafter (M365 Copilot) | Sponsor confirms |
| 1.2 | Size the opportunity | Draft | A8 Opportunity sizer (Snowflake, Power BI) | Analyst checks, then sponsor |
| 1.3 | Schedule interviews and shadowing | Auto ⚠️ | Interview scheduler (Outlook, Power Automate) | Users |
| 1.3 | Interview and shadow users | Me | Teams, in person | — |
| 1.3 | Pull themes from interview notes | Draft | A7 Interview synthesizer (M365 Copilot) | Me |
| 1.4 | Map where users' time goes | Draft | A9 Time-use analyst (Salesforce, Power BI) | Users confirm |
| 1.5 | Learn how users are measured and rewarded | Me | Conversations | Sponsor, if there's a gap |
| 1.6 | Build the mock-up and summarize reactions | Draft | Prototype skill, reaction summarizer | Me |
| 1.6 | Run the reaction sessions | Me | In person, Teams | Users |
| 1.7 | Choose the first target | Me | Meeting | Sponsor |
| 1.7 | Record the baseline, once the measure is set | Auto | Baseline recorder (Power BI) | Sponsor |
| 1.7 | Build the gate pack | Draft | Gate pack drafter | Sponsor |
| Gate | Go/no-go | Me | Meeting | Sponsor, risk |

**2. Define**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 2.1 | Write the problem and outcome | Draft | A10 Requirements drafter | Sponsor approves |
| 2.2 | Score the platforms against the five criteria | Draft | Platform fit checker | Me |
| 2.2 | Choose the platform and delivery path | Me | Meetings with platform teams | Decision log |
| 2.3 | Data contract (fields, freshness, checks) | Draft | A11 Data contract checker (Snowflake) | Data owner signs |
| 2.4 | Risk intake and control requirements | Draft | A12 Risk intake assistant | Model risk rates it |
| 2.5 | User stories and acceptance criteria | Draft | A10, story library | Me |
| 2.6 | Backlog priorities and trade-offs | Me | Backlog tool | Sponsor |
| 2.6 | Decision log entries | Draft | Decision log drafter (M365 Copilot) | Me |
| 2.7 | Measures, quality bar and value model | Draft | Measures sheet builder (Power BI) | Sponsor, Finance |
| 2.8 | Scope release 1 and the pilot group | Me | Backlog tool | Sponsor |
| 2.8 | Complete the brief and the gate pack | Draft | Gate pack drafter | Sponsor |
| Gate | Go/no-go | Me | Meeting | Sponsor, risk, data owner |

**3. Build**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 3.1 | Design the solution | Me | With platform teams | Platform teams, risk |
| 3.1 | Draft the agent specs | Draft | Agent spec drafter | Me |
| 3.2 | Prepare trusted data views | Me | With the data engineer (Snowflake) | — |
| 3.2 | Run data quality checks on every refresh | Auto | Snowflake checks; A11 in ongoing mode | Data owner, on failure |
| 3.3 | Build the rules and prompts | Draft | Bedrock or Prompt Builder | Users check |
| 3.4 | Build in the controls | Me | Guardrails, Einstein Trust Layer | Risk |
| 3.4 | Re-run the control tests on every release | Auto | Controls checker (test environment only) | Me, on failure |
| 3.5 | Deliver where users work, with sources and feedback | Me | Salesforce, Teams, Power Automate | Users |
| 3.6 | Build the test set | Draft | Test case generator | Users approve the answers |
| 3.7 | Run the test set on every version | Auto | A13 Test grader | Me, on failure |
| Gate | Go/no-go | Me | Meeting | Sponsor |

**4. Govern and test**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 4.1 | Update the intake and register the product | Draft | A12 Risk intake assistant | Risk confirms the rating |
| 4.2 | Compare the data actually used with the contract | Auto | Data-use checker | Privacy |
| 4.2 | Walk privacy through it | Me | Meeting | Privacy |
| 4.3 | Test and red-team the frozen version | Auto | A13 Test grader, A14 Red-team agent | Risk reviews every failure |
| 4.4 | Check fairness | Auto | A15 Fairness monitor | Compliance reviews |
| 4.5 | Re-run the control tests | Auto | Controls checker | Risk |
| 4.6 | Confirm the vendor reviews | Me | Approved vendors list | Vendor risk |
| 4.7 | Put together the evidence pack | Draft | A16 Evidence pack assembler | Me, then risk |
| 4.7 | Send sign-off requests and chase them | Auto ⚠️ | Sign-off router (Power Automate approvals) | Risk, compliance, privacy, security |
| 4.7 | The sign-offs themselves | Partner | — | Recorded in the tracker |
| 4.7 | Unblock a stuck sign-off | Me | Meeting | — |
| 4.8 | Draft the monitoring plan | Draft | Monitoring plan template | Risk, operations |
| Gate | Go/no-go | Partner | Meeting | Risk, sponsor |

**5. Release and adopt**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 5.1 | Track the readiness checklist | Auto | Readiness tracker | Me |
| 5.1 | Build the pilot dashboard | Draft | Power BI, from the 2.7 measures sheet | Sponsor |
| 5.2 | Move the product from test to live | Auto ⚠️ | The platform's release tools | Platform team |
| 5.2 | Weekly usage report | Auto | Power BI | Sponsor, user leaders |
| 5.3 | Build it into a routine managers already run | Me | Meetings | Managers |
| 5.4 | Train users on their own work | Me | Teams, in person | Pilot users |
| 5.4 | Answer "how do I…?" questions | Auto | A6 Onboarding coach | Users; the product team keeps content current |
| 5.5 | Recruit champions | Me | A Teams channel | Champions |
| 5.5 | Spot wins to celebrate | Draft | Wins spotter | Me, then leaders |
| 5.6 | Sort feedback into bugs, quality issues and ideas | Auto | A17 Feedback triage | Backlog; I check a weekly sample |
| 5.6 | Fix and tell users what changed | Me | Release notes | Users |
| 5.7 | Write the scale recommendation | Draft | Gate pack drafter | Sponsor |
| Gate | Go/no-go to scale | Me | Meeting | Sponsor, user leaders |

**6. Measure and iterate**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 6.1 | Live dashboard for all five kinds of measures | Auto | Power BI | Sponsor |
| 6.2 | Monthly impact note against baseline and comparison group | Draft | A18 Impact analyst | Analytics checks, then sponsor |
| 6.3 | Re-test after every change; alert when quality slips | Auto | A19 Quality watchdog | Product manager, on alert |
| 6.4 | Monthly keep/change/stop pack | Draft | Monthly review pack drafter | Me |
| 6.4 | Keep/change/stop decision | Me | Meeting | Sponsor |
| 6.5 | Rank the candidates for the next wave | Draft | A20 Improvement scout | Me, then sponsor |
| 6.6 | Total time and waits from the first-time logs | Draft | Log summarizer | Me |
| 6.6 | Improve the machine: update this framework and the playbook | Me | — | — |
| Gate | Keep, change or stop; invest more, adjust or stop | Me | Meeting | Sponsor, Finance |

### Across every project (the running layer)
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| All | One tracker for all projects: task, owner, date, status (I set it up once) | Auto | A shared tracker (tool to confirm) | Everyone on the project |
| All | Remind owners before a due date; tell me when something is late | Auto ⚠️ | Power Automate | Owners, then me |
| All | Weekly status note for each project, from the tracker | Draft | M365 Copilot | Me, then stakeholders |
| All | Decision log and risk/issue list, from meeting notes | Draft | M365 Copilot | Me |
| All | One view of all projects: step, late items, measures | Auto | Power BI | Sponsors and leaders |

### The automation check at every gate
At each gate, before go/no-go, ask of every **Me** and **Draft** task:
1. **Did it repeat?** Will it come up again, in this project or the next one?
2. **Is it stable?** Did we do it the same way at least twice?
3. **Is it safe alone?** It makes no decision, nothing reaches a client, and the bank's rules allow it.

All three yes → move it one kind toward **Auto** before the next project, and
update the table above. The reverse also applies: if an **Auto** task went
wrong, move it back to a person until it's fixed.

### Many projects at once
- **Same machine for every project:** the same steps, tables and tracker, so any project can be compared with any other.
- **Limit the Me-heavy steps.** Discover and Define need the most of my time, so at most [X] projects are in them at once. Steps 3 to 6 are mostly Auto and Draft, so more projects can be there.
- **Stagger the gates** so that no two gate meetings land in the same week.
- **My week, planned:** [X] hours on decisions and gates, [X] on users, [X] on partners and sign-offs, [X] checking drafts. If **Me** work runs over, the automation check comes first.

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
3. Copy the delivery machine's task tables into the shared tracker, with an owner and a date for each task.
4. Work through Discover first, using the write-up layout and the field manual in `playbook/` (how to do each sub-step the first time, and what to log so it can be automated).
5. Keep the plan in `memos/<project>.md`, as the RM memo does.

_Last updated: 2026-10-09_
