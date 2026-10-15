# Product Framework: the rules every product follows

Claude loads this every session and applies these rules whenever we plan or
work on a product.

Page 2 of the four "How we deliver" pages, read in this order:
1. **Product Workflow** (`memos/role-workflow.md`): the six steps (Discover, Define, Build, Govern and test, Release and adopt, Measure and iterate), what happens in each, and their go/no-go gates.
2. **Product Framework** (this page): the rules every product follows.
3. **Product Machine** (`product-machine.md`): every task in every step, marked Auto, Draft, Me or Partner, and how one product manager runs many projects at once.
4. **Product Playbook** (`playbook/`): how to do each of the 44 sub-steps the first time.

## Who's involved and who decides
Agree this at the start of Discover (sub-step 1.0), with real names. Gaps are
written as [name needed] until they're filled.

| Who | What they decide or do | Where they come in |
|---|---|---|
| Sponsor | The outcome, the funding and the go/no-go at every gate, together with the people named below for that gate | Every gate |
| User leaders and pilot users | How the work is done today, and feedback on the product; user leaders decide with the sponsor whether to scale | Discover (interviews, mock-up), Release and adopt (pilot; the step 5 gate) |
| Product manager (this role) | Scope, priorities and trade-offs; owns the product until a long-term owner is named; brings the gate pack and recommends at every gate | Every step |
| Long-term owner | Holds the product after launch, for example someone in a revenue line; identified during the project | Named in Define if known (2.8), confirmed before scaling (5.7) |
| Data owners | What data may be used; they sign the data contract | Define (2.3; they agree at the Define gate), Build (3.2) |
| Platform teams | The technical design | Define (2.2), Build |
| Model risk (the risk partner) | The risk rating and the approval | Briefed in Discover (1.0); agrees at the Discover and Define gates; rating in Define (2.4); approval at the step 4 gate, which the sponsor can't overrule |
| Compliance, privacy and security | The controls and their sign-off | Told the control requirements in Define (2.4); sign-off in Govern and test (4.2 to 4.7) |
| Credit policy owner (higher-risk path only) | Whether a product that informs credit decisions may go live, and what its drafts may contain (control K3) ⚠️ [name needed] | Define (2.4), Govern and test (4.7) |
| Vendor risk | Whether the vendors and AI models we use are approved | Define (2.2, starts any missing review), Govern and test (4.6) |
| IT | The AI tools the team may use, and every connection the product makes | Discover (1.0), Define (2.2), Govern and test (4.5) |
| Finance | How impact is counted, and the impact numbers | Define (2.7), the Measure and iterate gate |
| Analytics | Checks the sizing and impact numbers | Discover (1.2), Measure and iterate (6.2) |
| Operations | Running the product day to day | The monitoring plan (4.8), then after launch |

**Decisions and trade-offs:** record each one in the decision log, with the
options, who decided and why, so partners stay aligned.

**Gates in writing:** when every criterion is met, the decider approves the gate
pack in writing; a meeting happens only when a criterion is contested or a
decider asks for one (Product Machine).

**The risk and issue list:** one list of dependencies, risks and issues, each
item with an owner and a date, reviewed weekly. Its top item is the **limiting
factor**: the one thing holding the project back right now, named with its
owner. It opens the tracker and the weekly status note.

## Projects, AI products and feature waves
How the work is cut up, so every gate knows what it decides (gaps 1 to 3 from the
2026-10-15 audit, decided 2026-10-15).

| Level | What it is | Example (RM plan) |
|---|---|---|
| Project | All the work for one user group | The RM project |
| Core use case | One of the seven lines the project is organized on | Account intelligence and meeting prep |
| AI product | A capability we build and release | The pre-meeting brief |
| Feature wave | A set of AI products released together | Feature wave 1 |

| Gate | Passed for |
|---|---|
| 1 Discover and 2 Define | The project, the first time; after that, each feature wave, through the quick pass (below) |
| 3 Build and 4 Govern and test | Each AI product |
| 5 Release and adopt | Each feature wave |
| 6 Measure and iterate | Each AI product, monthly (keep, change or stop); the project, quarterly (invest more, adjust or stop) |

**The quick pass for the next feature wave.** After the first pass, each new
feature wave (chosen in sub-step 6.5) goes through Discover and Define quickly,
reusing what the project already has. A wave that serves a new user group starts
a new project, with the full pass:
- **Always done:** 2.3 update the data contract, and the data owner signs the new fields; 2.4 update the risk intake, and the risk partner confirms the rating; 2.5 user stories and acceptance criteria for the wave; 2.7 measures, quality bar and value model for the wave's AI products.
- **Reused unless something changed:** 1.0 to 1.7 (record a baseline in 1.7 for any new measure, and show users a short 1.6 mock-up of any new AI product), 2.1, 2.2 (redone if the wave needs a different platform or delivery path), 2.6, and 2.8, where only the wave's scope and pilot group are updated. The product manager lists in the gate pack what was reused and what was redone.
- **Gates 1 and 2 together, in writing,** from one short gate pack, with a meeting only if a criterion is contested.

**Change after launch.** A **material change** goes back through step 4 before
it reaches users: new data, a new action the product can take, users outside the
group step 4 approved, a new AI model we choose, or a vendor model change
the vendor announces as major. Smaller vendor updates trigger the 6.3 re-test
(M32), and are judged as below. Step 4 approves
the full planned user group from 2.8 (recorded in 4.7), so user waves inside it
(5.7) are not a material change. The product manager
proposes whether a change is material and the risk partner confirms. Any other
change is re-tested (6.3), logged in the release notes and told to the risk
partner. Comes from: our choice, resting on the model risk guidance's
expectation that changes are reviewed. ⚠️ The bank's model risk policy has the
final word on what counts as material.

## The five kinds of measures
The main outcome measure is agreed in Discover (1.1) and its baseline recorded in
1.7; the full set is set in Define (2.7) and tracked in Measure and iterate.
These are the five the job description names. Pick one or two of each per product, and
define each one exactly (source, formula, owner) so the dashboard can be built
from it.

| Kind | What it tells us | Example measures |
|---|---|---|
| Usage | Whether people use what it gives them | Answers or insights opened and acted on; drafts and briefs used |
| Quality | Whether its answers are right and useful | Accuracy on the test set, % of answers with sources, thumbs up or down |
| Business impact | Whether it moves the outcome the sponsor cares about | Hours saved per user, cost or time per task, more client meetings, pipeline created, revenue won |
| Adoption | Whether it has become part of the routine | Weekly active users, % of target users, repeat use week after week, use inside the routines managers run |
| Risk and controls | Whether it stays safe | Incidents, human overrides, guardrail blocks, review findings |

Leading measures show up within weeks (use, insights acted on, pipeline
created); lagging ones take months (closed revenue). Report both, so a good
start isn't mistaken for a result. The gate at the end of Release and adopt uses
leading measures; lagging ones are judged in Measure and iterate.

The machine itself has its own measures (days from kickoff to pilot, days at
each gate, releases per month, the wait index), on the Product Machine page.

## The quality bar
How good is good enough. Thresholds are set in Define (2.7) as [X] until
agreed. In Build (3.6 and 3.7) the test set checks accuracy, sources and
permissions, and users grade a sample for relevance and usefulness. Step 4
confirms them on the frozen version.

| Test | What it means | Threshold |
|---|---|---|
| Accuracy | Numbers and facts match the source | [X] |
| Sources shown | Every answer links to where it came from | [X] |
| Relevance | Users rate it relevant to their work | [X] |
| Usefulness | Users would act on it | [X] |
| Permissions | No one sees data they shouldn't | Zero tolerance |

**Gaps:** only the sponsor (and, in step 4, the risk partner) can accept a documented gap on accuracy, sources
shown, relevance or usefulness, recorded in the decision log with a date to
close it. Permissions, and any threshold that comes from law or bank policy,
can never be waived.

## AI principles
These apply to every agent and every AI product, in every step.
- **Two kinds of agents at work on products.** Some help the team do the work (the general agents in the Agent Library); others are the product users see (a project's own agents, in its memo's Appendix A). My research helpers (H1 and on) are a separate group: they also live in the Agent Library but aren't part of any product or the product machine.
- **Assistive first.** AI drafts or suggests, and a named person decides. Autonomy grows only with evidence, through the automation check in the Product Machine (cut first, then automate).
- **Cut first, then automate.** Every requirement says where it comes from: law or regulator, bank policy, or our choice. Law and bank policy are never cut; our choices are challenged at every gate before anything is automated.
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
| From the job description (accountabilities and requirements, `job-description.md`) | Where it lives |
|---|---|
| Own products from discovery through governed release, adoption and improvement | All six steps |
| Work with bankers to find needs; turn them into clear products | Discover → Define |
| User stories, acceptance criteria, backlog priorities, release scope, success measures, control requirements, trade-offs | Define |
| Configure AI capabilities (agents, retrieval, data flows, automations, integrations) in tools bankers use | Define (2.2, the platform) → Build |
| Governed delivery: risk, controls, privacy, responsible AI and regulation built in from the start | Governance thread in every step (Product Workflow); formal approval in Govern and test; the quality bar; AI principles |
| Lead with limited oversight: priorities, decisions, dependencies, testing, controls, release readiness, issues | Who decides; decision log; the Product Machine; Build to Release gates |
| Drive adoption and change in a regulated environment | Release and adopt |
| Define and monitor usage, quality, impact, adoption, and risk and control measures | The five kinds of measures; Define and Measure and iterate |
| Align business, technology, data, risk, compliance and operations partners | Who decides; decision log |

## Starting a new project
Start every project with sub-step 1.0 in the Product Playbook (kickoff): name
the outcome and the sponsor, fill in who's involved and who decides (above) with
real names, copy the Product Machine's task tables into the shared tracker with
an owner and a date for each task, brief the risk partner and create the project
file, with this project's question, governance thread and gate for each of the
six steps (from the Product Workflow). Then work through Discover with the playbook, writing each step up in the
layout above. The plan's working copy is `memos/<project>.md`, as the RM memo
does; people read it as a designed page in the Document Library.

_Last updated: 2026-10-15_
