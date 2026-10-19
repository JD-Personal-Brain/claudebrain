# Product Machine: how one product manager runs many projects

Claude loads this every session. It is the operating model: every task in
every step, marked by who does it, and how the work moves toward automation.
Page 3 of the four "How we deliver" pages: the Product Workflow
(`memos/role-workflow.md`) shows the steps, the Product Framework
(`product-framework.md`) sets the rules, this page runs the work, and the
Product Playbook (`playbook/`) says how to do each sub-step the first time.
Designed page: https://claude.ai/artifact/S8Wbygy24cjguTMxZsN2QF (built from this
file by `designs/product-machine-build.py`).

I'm one person running several projects at once, so the machine has to run
mostly by itself. Automation does the routine work and pushes tasks to people
against the timeline, so my time goes only where a person is needed.
Every project uses the same steps, tracker and templates, so they all run the
same way side by side. *(Added 2026-10-09. Tool choices are guesses until I see
the bank's setup: verify each one.)*

## Three kinds of work, plus partner sign-offs
Every task in every step is marked as one of these:
- **Auto (runs on its own):** a workflow or agent does it and tells the right person. No one has to remember it.
- **Draft (AI drafts, a person checks):** AI does the first version, and a named person approves it.
- **Me (only a person):** decisions, agreement between people, relationships and trade-offs. This is where my hours go.
- **Partner:** a decision only a named partner can make, such as a risk or compliance sign-off. Never automated.

**Not sure yet:** whether the bank lets automations message people or update
trackers by themselves. Confirm this at the first project, because it decides
how much can be **Auto**.

## Each step's tasks, by kind
One row per task, numbered to match the sub-steps in `playbook/`. **Kind** is the
target once the machine is running. The first time through, many tasks are
done one kind closer to a person, so the work can be logged before it's
automated; each playbook step's review table shows both. The gate check below
moves tasks toward **Auto** over time. ⚠️ marks an Auto task that sends requests,
reminders, reports or alerts to people outside the project team, or changes a live
system, so it depends on the bank allowing that. The project team is the product
manager, analysts and the data and platform engineers on the product; the sponsor,
partners and users are outside it. Dashboards people open themselves don't count.

**1. Discover**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 1.0 | Agree the sponsor's role and who decides; brief the risk partner (and the credit policy owner when a higher-risk path is likely) | Me | Meeting | Sponsor, risk |
| 1.0 | Set up the tracker, decision log and project file | Draft | M1 Kickoff pack builder | Me |
| 1.0 | Confirm the AI tools the team may use and record them in the project file | Me | Meeting with IT and risk | Project file |
| 1.1 | Agree the outcome and measure | Me | Meeting | Sponsor |
| 1.1 | Write the outcome note | Draft | M2 Outcome note drafter (M365 Copilot) | Sponsor confirms |
| 1.2 | Size the opportunity | Draft | M21 Opportunity sizer (Snowflake Cortex Analyst, Power BI) | Analyst checks, then sponsor |
| 1.3 | Schedule interviews and shadowing | Auto ⚠️ | M3 Interview scheduler (Outlook, Power Automate) | Users |
| 1.3 | Interview and shadow users | Me | Teams, in person | — |
| 1.3 | Pull themes from interview notes | Draft | M20 Interview synthesizer (M365 Copilot) | Me |
| 1.4 | Map where users' time goes | Draft | M22 Time-use analyst (Snowflake Cortex, Power BI) | Users confirm |
| 1.5 | Learn how users are measured and rewarded | Me | Conversations | Sponsor, if there's a gap |
| 1.6 | Build the mock-up and summarize reactions | Draft | Prototype skill, M4 Reaction summarizer | Me |
| 1.6 | Run the reaction sessions | Me | In person, Teams | Users |
| 1.7 | Choose the first target | Me | Meeting | Sponsor |
| 1.7 | Record the baseline, once the measure is set | Auto ⚠️ | M5 Baseline recorder (Power BI) | Sponsor |
| 1.7 | Build the gate pack | Draft | M6 Gate pack drafter | Sponsor |
| Gate | Go/no-go | Me | In writing; a meeting only if contested | Sponsor, risk |

**2. Define**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 2.1 | Write the problem and outcome | Draft | M23 Requirements drafter | Sponsor approves |
| 2.2 | Score the platforms against the five criteria | Draft | M7 Platform fit checker | Me |
| 2.2 | Choose the platform and delivery path | Me | Meetings with platform teams | Decision log |
| 2.3 | Data contract (fields, freshness, checks) | Draft | M24 Data contract checker (Snowflake) | Data owner signs |
| 2.4 | Risk intake and control requirements | Draft | M25 Risk intake assistant | Model risk rates it; the credit policy owner on the higher-risk path |
| 2.5 | User stories and acceptance criteria | Draft | M23, story library | Me |
| 2.6 | Backlog priorities and trade-offs | Me | Backlog tool | Sponsor |
| 2.6 | Decision log entries | Draft | M8 Decision log drafter (M365 Copilot) | Me |
| 2.7 | Measures, quality bar and value model | Draft | M9 Measures sheet builder (Power BI) | Sponsor, Finance |
| 2.8 | Scope release 1 and the pilot group | Me | Backlog tool | Sponsor, user leaders |
| 2.8 | Record the long-term owner, or "to be decided" with a date to decide by | Me | Meeting | Sponsor |
| 2.8 | Complete the brief and the gate pack | Draft | M6 Gate pack drafter | Sponsor |
| Gate | Go/no-go | Me | In writing; a meeting only if contested | Sponsor, risk, data owner; the credit policy owner on the higher-risk path |

On the quick pass for a later feature wave, gates 1 and 2 are decided together in writing (Product Framework).

**3. Build**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 3.1 | Design the solution | Me | With platform teams | Platform teams, risk |
| 3.1 | Draft the agent specs | Draft | M10 Agent spec drafter | Me |
| 3.2 | Prepare trusted data views | Me | With the data engineer (Snowflake) | — |
| 3.2 | Run data quality checks on every refresh | Auto ⚠️ | Snowflake checks; M24 in ongoing mode | Data owner, on failure |
| 3.3 | Build the rules and prompts | Draft | Bedrock or Prompt Builder | Users check |
| 3.4 | Build in the controls | Me | Guardrails, Einstein Trust Layer | Risk |
| 3.4 | Re-run the control tests on every release | Auto | M11 Controls checker (test environment only) | Me, on failure |
| 3.5 | Deliver where users work, with sources and feedback | Me | Salesforce, Teams, Power Automate | Users |
| 3.6 | Build the test set | Draft | M12 Test case generator | Users approve the answers |
| 3.7 | Run the test set on every version | Auto | M26 Test grader | Me, on failure |
| 3.7 | Build the gate pack | Draft | M6 Gate pack drafter | Sponsor |
| Gate | Go/no-go | Me | In writing; a meeting only if contested | Sponsor |

**4. Govern and test**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 4.1 | Update the intake and register the product | Draft | M25 Risk intake assistant | Risk confirms the rating |
| 4.2 | Compare the data actually used with the contract | Auto ⚠️ | M13 Data-use checker | Privacy |
| 4.2 | Walk privacy through it | Me | Meeting | Privacy |
| 4.3 | Test and red-team the frozen version | Auto | M26 Test grader, M27 Red-team agent | Risk reviews every failure |
| 4.4 | Agree the groups and thresholds with compliance | Partner | Meeting | Compliance |
| 4.4 | Check fairness | Auto ⚠️ | M28 Fairness monitor | Compliance reviews |
| 4.5 | Re-run the control tests | Auto | M11 Controls checker | Risk |
| 4.5 | Show the controls working to risk; confirm the release route and IT's approval of every connection | Me | Meeting, audit log | Risk, IT |
| 4.6 | Confirm the vendor reviews | Me | Approved vendors list | Vendor risk |
| 4.7 | Put together the evidence pack | Draft | M29 Evidence pack assembler | Me, then risk |
| 4.7 | Send sign-off requests and chase them | Auto ⚠️ | M14 Sign-off router (Power Automate approvals) | Risk, compliance, privacy, security; the credit policy owner on the higher-risk path; credit risk for early warning rules |
| 4.7 | The sign-offs themselves | Partner | — | Recorded in the tracker |
| 4.7 | Unblock a stuck sign-off | Me | Meeting | — |
| 4.8 | Draft the monitoring plan alongside 4.5 (it goes into the evidence pack), then finalise it | Draft | Monitoring plan template | Risk, operations |
| Gate | Go/no-go | Partner | In writing; a meeting only if contested | Risk, sponsor |

The step 4 gate is a Partner decision: the risk partner's approval can't be overruled; the risk partner and the sponsor approve the signed evidence pack.

**5. Release and adopt**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 5.1 | Track the readiness checklist | Auto | M15 Readiness tracker | Me |
| 5.1 | Build the pilot dashboard | Draft | Power BI, from the 2.7 measures sheet | Sponsor |
| 5.1 | Dry-run the incident process: who is called, how the product is paused | Me | With operations | Operations, risk |
| 5.2 | Move the product from test to live | Auto ⚠️ | M16 Release automation (the platform's release tools) | Platform team |
| 5.2 | Weekly usage report | Auto ⚠️ | Power BI | Sponsor, user leaders |
| 5.3 | Build it into a routine managers already run | Me | Meetings | Managers |
| 5.4 | Train users on their own work | Me | Teams, in person | Pilot users |
| 5.4 | Answer "how do I…?" questions from the FAQ (the product's own help, if a release includes one) | Auto ⚠️ | The product's FAQ or help | Users; the product team keeps content current |
| 5.5 | Recruit champions | Me | A Teams channel | Champions |
| 5.5 | Spot wins to celebrate | Draft | M17 Wins spotter | Me, then sponsor and user leaders |
| 5.6 | Sort feedback into bugs, quality issues and ideas; flag likely incidents | Auto ⚠️ | M30 Feedback triage | Backlog; operations and me for incidents; I check a weekly sample |
| 5.6 | Fix and tell users what changed; decide whether a fix is a material change | Me | Release notes | Users; the risk partner confirms a material change |
| 5.6 | Log every incident, its owner and the fix | Me | Incident log | Operations, risk |
| 5.7 | Confirm the long-term owner before scaling | Me | Meeting | Sponsor |
| 5.7 | Write the scale recommendation | Draft | M6 Gate pack drafter | Sponsor |
| Gate | Go/no-go to scale | Me | In writing; a meeting only if contested | Sponsor, user leaders |

**6. Measure and iterate**
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| 6.1 | Live dashboard for all five kinds of measures | Auto | Power BI | Sponsor, user leaders |
| 6.2 | Monthly impact note against baseline and comparison group | Draft | M31 Impact analyst | Analytics checks, then sponsor |
| 6.3 | Re-test after every change; alert when quality slips | Auto | M32 Quality watchdog | Product manager, on alert |
| 6.3 | Act on an alert: fix, roll back or pause, per the monitoring plan | Me | — | Operations, risk |
| 6.3 | Decide whether a change is material (it goes back through step 4) | Me | — | Risk partner confirms |
| 6.4 | Monthly keep/change/stop pack | Draft | M18 Monthly review pack drafter | Me |
| 6.4 | Keep/change/stop decision | Me | In writing; a meeting only if contested | Sponsor |
| 6.4 | Quarterly summary for invest more, adjust or stop | Draft | M18 Monthly review pack drafter | Sponsor, Finance |
| 6.5 | Rank the candidates for the next feature wave | Draft | M33 Improvement scout | Me, then sponsor |
| 6.6 | Total time and waits from the sub-step logs (the first-time log on the first project) | Draft | M19 Log summarizer | Me |
| 6.6 | Record the machine's measures for this project | Draft | M19 Log summarizer | Me |
| 6.6 | Improve the machine: update the Product Machine, the Product Framework and the playbook | Me | — | — |
| Gate | Keep, change or stop; invest more, adjust or stop | Me | In writing; a meeting only if contested | Sponsor, Finance |

## Across every project (the running layer)
| # | Task | Kind | Tool (guess) | Goes to |
|---|---|---|---|---|
| All | Each project's tasks go into the one shared tracker (M1 at 1.0); owners keep statuses current | Draft | M1 Kickoff pack builder, then the shared tracker (tool to confirm) | Everyone on the project |
| All | Remind owners before a due date; tell me when something is late | Auto ⚠️ | Power Automate | Owners, then me |
| All | Name the limiting factor: the one thing holding the project back right now, with its owner. It opens the tracker and the weekly status note, and my time goes there first | Me | The tracker | Sponsor and the owner |
| All | Weekly status note for each project, from the tracker, opening with the limiting factor | Draft | M365 Copilot | Me, then sponsor and partners |
| All | Decision log and risk and issue list, from meeting notes | Draft | M8 Decision log drafter (M365 Copilot) | Me |
| All | One view of all projects: step, limiting factor, late items, product measures and the machine's measures | Auto | Power BI | Sponsors and user leaders |

## The automation check at every gate
At each gate, before go/no-go, take every **Me** and **Draft** task through the
check in this order: **cut first, then automate** (the order Elon Musk's
"algorithm" uses; see the Elon Mode page). Automating a task that
shouldn't exist only locks in the waste.

**First, cut:**
1. **Should it exist?** Who required it, and where does the requirement come from: law or regulator, bank policy, or our choice (each control's "Comes from" line in the Controls Catalog or, for sub-steps and gates, "Where the requirements come from" in the Product Playbook)? Law and bank policy stay. Our choices can be challenged.
2. **Can we delete it?** If yes, delete it, and record in the decision log what it did and who agreed. If nothing we delete ever has to come back, we aren't cutting enough (Musk's rule of thumb: about 1 in 10 comes back; ⚠️ sources give 10% or 20%).
3. **Can we simplify it?** Fewer steps, fewer hand-offs, fewer people to wait on.
4. **Can we make it faster?** Shorten the longest wait first; the wait index (below) shows where.

Run questions 1 and 2 on **Auto** tasks too: an alert nobody reads is waste.

**Then, automate what's left:**
5. **Did it repeat?** Will it come up again, in this project or the next one?
6. **Is it stable?** Did we do it the same way at least twice?
7. **Is it safe alone?** It makes no decision, nothing reaches a client, and the bank's rules allow it.

Yes to 5, 6 and 7 → move it one kind toward **Auto** before the next project, and
update that step's task table above. The reverse also applies: if an **Auto** task went
wrong, move it back to a person until it's fixed.

## Gates in writing when they're clean
When every gate criterion is met, the decider approves the gate pack in writing,
and the approval goes in the decision log. A gate meeting happens only when a
criterion is contested or someone who decides asks for one. Partner sign-offs in
step 4 don't change: each named partner still signs, and at the step 4 gate the
risk partner and the sponsor approve the signed evidence pack in writing (⚠️ the bank's approval policy may
require a committee meeting). ⚠️ Whether the bank's
culture accepts gates in writing is a guess; confirm it at the first project.

## Measuring the machine
The machine is a product too, so it gets its own measures, recorded for every
project in sub-step 6.6 and shown in the one view of all projects. Targets are
[X] until the first project sets a baseline; after that, each project should
beat the last.

| Measure | What it is | Where it comes from |
|---|---|---|
| Days from kickoff to pilot | Calendar days from sub-step 1.0 to the pilot launch (5.2) | The tracker |
| Days at each gate | Calendar days from the gate pack being ready to the decision | The decision log (gate pack ready and decision dates) |
| Releases per month in the pilot | How many improved versions reach pilot users each month (how fast we iterate) | Release notes (5.6) |
| Wait index | For each sub-step: calendar days from start to finish, divided by hours of real work. A high number means waiting, not working; fix the highest first | The sub-step log (start, finish, hours, waits), kept on every project, not only the first; summarized by M19 in 6.6 |

Every project keeps a light log per sub-step (start, finish, hours, waits); the full first-time log is only for the first time.

## Many projects at once
- **One machine for every project.** The same steps, tables and tracker, so any project can be compared with any other.
- **Limit the person-heavy steps.** Discover and Define need the most of my time, so at most [X] projects are in them at once. Release and adopt also has many person-only tasks (working with users), so plan for it too. Build, Govern and test, and Measure and iterate lean more on AI drafts and automation, so more projects can be there.
- **Stagger the gates.** No two gate packs from different projects land in the same week.
- **Plan the product manager's week.** [X] hours on decisions and gates, [X] on users, [X] on partners and sign-offs, [X] checking drafts. If person-only work runs over, the automation check comes first.

_Last updated: 2026-10-19_
