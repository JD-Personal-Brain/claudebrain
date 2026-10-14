# Product framework: the rules every product follows

Claude loads this every session and applies these rules whenever we plan or
work on a product.

Page 2 of the four "How we deliver" pages, read in this order:
1. **Product Workflow** (`memos/role-workflow.md`): the six steps (Discover, Define, Build, Govern and test, Release and adopt, Measure and iterate), what happens in each, and their go/no-go gates.
2. **Product Framework** (this page): the rules every product follows.
3. **Delivery Machine** (`delivery-machine.md`): every task in every step, marked Auto, Draft, Me or Partner, and how one product manager runs many projects at once.
4. **The Delivery Playbook** (`playbook/`): how to do each of the 44 sub-steps the first time.

## Who's involved and who decides
Agree this at the start of Discover (sub-step 1.0), with real names. Gaps are
written as [name needed] until they're filled.

| Who | What they decide or do | Where they come in |
|---|---|---|
| Sponsor | The outcome, the funding and the go/no-go at every gate | Every gate; the step 4 gate together with risk |
| User leaders and pilot users | How the work is done today, and feedback on the product | Discover (interviews, mock-up), Release and adopt (pilot) |
| Product manager (this role) | Scope, priorities and trade-offs; owns the product until a long-term owner is named | Every step |
| Long-term owner | Holds the product after launch, for example someone in a revenue line; identified during the project | Named in Define if known (2.8), confirmed before scaling (5.7) |
| Data owners | What data may be used; they sign the data contract | Define (2.3), Build (3.2) |
| Platform teams | The technical design | Define (2.2), Build |
| Model risk | The risk rating and the approval | Briefed in Discover (1.0), rating in Define (2.4), approval in Govern and test |
| Compliance, privacy and security | The controls and their sign-off | Govern and test (4.2 to 4.7) |
| Operations | Running the product day to day | The monitoring plan (4.8), then after launch |

**Decisions and trade-offs:** record each one in the decision log, with the
options, who decided and why, so partners stay aligned.

**Dependencies, risks and issues:** one list, each item with an owner and a
date, reviewed weekly.

## The five kinds of measures
Set in Define (sub-step 2.7) and tracked in Measure and iterate. These are the
five the job description names. Pick one or two of each per product, and
define each one exactly (source, formula, owner) so the dashboard can be built
from it.

| Kind | What it tells us | Example measures |
|---|---|---|
| Usage | Whether people use what it gives them | Answers or insights opened and acted on; drafts and briefs used |
| Quality | Whether its answers are right and useful | Accuracy on the test set, % of answers with sources, thumbs up or down |
| Business impact | Whether it moves the outcome the sponsor cares about | Hours saved per user, more client meetings, pipeline created, revenue won |
| Adoption | Whether it has become part of the routine | Weekly active users, % of target users, repeat use week after week, use inside the routines managers run |
| Risk and controls | Whether it stays safe | Incidents, human overrides, guardrail blocks, review findings |

Leading measures show up within weeks (use, insights acted on, pipeline
created); lagging ones take months (closed revenue). Report both, so a good
start isn't mistaken for a result.

## The quality bar
How good is good enough. Thresholds are set in Define (2.7) as [X] until
agreed, the test set checks them in Build (3.6 and 3.7), and step 4 confirms
them on the frozen version.

| Test | What it means | Threshold |
|---|---|---|
| Accuracy | Numbers and facts match the source | [X] |
| Sources shown | Every answer links to where it came from | [X] |
| Relevance | Users rate it relevant to their work | [X] |
| Usefulness | Users would act on it | [X] |
| Permissions | No one sees data they shouldn't | Zero tolerance |

## AI principles
These apply to every agent and every AI product, in every step.
- **Two kinds of agents.** Some help the team do the work (the general agents in the Agent Library); others are the product users see (a project's own agents, in its memo's Appendix A).
- **Assistive first.** AI drafts or suggests, and a named person decides. Autonomy grows only with evidence, through the automation check in the Delivery Machine.
- **One job each.** Every agent has a clear job, a short list of allowed actions, read-only by default, and every action logged. Each one is written up as an agent spec before it's built.
- **Built where the work happens.** Use the tools people already work in (Outlook, Teams, Salesforce), and add a new platform only when it's needed.

## How each step is written up
Every project plan writes each step the same way, so plans are easy to compare.
The RM plan (`memos/rm-analytics-framework.md`) is the worked example.

| Heading | What goes there |
|---|---|
| Goal | The question this step answers for this product |
| Work | The sub-steps, and the tools that help with each |
| AI strategy | How AI is used in this step, and the agents that do it |
| AI for the team | What the agents do for the project team |
| AI for users | What users see of the product in this step |
| Data | The data this step uses, and who owns it |
| Output | What the step produces |
| Checks | The safeguards that must hold during the step |
| Gate | What the go/no-go decision needs |

## How the job description maps to this framework
| Job accountability (from `job-description.md`) | Where it lives |
|---|---|
| Own products from discovery through governed release, adoption and improvement | All six steps |
| Work with bankers to find needs; turn them into clear products | Discover → Define |
| User stories, acceptance criteria, backlog priorities, release scope, success measures, control requirements, trade-offs | Define |
| Configure AI capabilities (agents, retrieval, data flows, automations, integrations) in tools bankers use | Build |
| Governed delivery: risk, controls, privacy, responsible AI and regulation built in from the start | Governance thread in every step (Product Workflow); formal approval in Govern and test; the quality bar; AI principles |
| Lead with limited oversight: priorities, decisions, dependencies, testing, controls, release readiness, issues | Who decides; decision log; the Delivery Machine; Build to Release gates |
| Drive adoption and change in a regulated environment | Release and adopt |
| Define and monitor usage, quality, impact, adoption, and risk and control measures | The five kinds of measures; Define and Measure and iterate |
| Align business, technology, data, risk, compliance and operations partners | Who decides; decision log |

## Starting a new project
1. Name the outcome and the sponsor.
2. Fill in the six steps for this project (from the Product Workflow): its question, governance thread and gate for each step.
3. Fill in who's involved and who decides, above, with real names.
4. Copy the task tables from the Delivery Machine into the shared tracker, with an owner and a date for each task.
5. Work through Discover first, using the write-up layout above and The Delivery Playbook (how to do each sub-step the first time, and what to log so it can be automated).
6. Keep the plan in `memos/<project>.md`, as the RM memo does.

_Last updated: 2026-10-14_
