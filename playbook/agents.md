# Agent library: the agents that run the delivery machine

These agents help the team run any project through the six steps. They're
reused on every project, so they're specified once here. A project's own
agents (the product users see, or agents only that project needs) go in its
memo's Appendix A, like A1 to A20 in the RM memo.

Written with the **agent-spec** skill. Every agent follows the AI principles in
`product-framework.md`: assistive first, one job each, read-only or draft-only unless a named
person approves, and every action logged. Auto agents act only within their
listed actions, and those marked ⚠️ wait until the bank allows it.

> ⚠️ **How much to trust this.** Written 2026-10-09 from the playbook, not
> from Associated Bank. "Runs on" tools are guesses from `tech-stack.md`, and
> every ⚠️ is a question to confirm at the bank. None of these agents is built yet.

---

### M1. Kickoff pack builder
- **Used in:** 1.0
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** create a new project's starting files from its one-line project statement.
- **Starts when:** the product manager writes the project statement.
- **Inputs:** the project statement; the task tables in `product-framework.md`; the who-decides list.
- **Allowed actions:** create draft files: the tracker with every task listed, the decision log, the risk and issue list and the project file.
- **Not allowed:** assigning owners or dates; contacting anyone.
- **Outputs:** a draft project pack, ready for owners and dates.
- **Stops when:** every file exists. If the statement is missing, it asks for it and creates nothing.
- **Proof it worked:** the tracker has one row for every task in the framework tables.
- **Person in charge:** product manager.
- **Runs on (guess):** Power Automate with Microsoft Lists or Planner.
- **To confirm:** ⚠️ which tracker the bank uses.

### M2. Outcome note drafter
- **Used in:** 1.1
- **For:** the team
- **Kind:** Me → Draft
- **Job:** turn the sponsor meeting recap into the one-page outcome note.
- **Starts when:** the product manager asks, after the sponsor meeting.
- **Inputs:** the meeting recap or notes.
- **Allowed actions:** read the recap; write a draft note.
- **Not allowed:** adding goals or numbers that aren't in the recap; sending it to anyone.
- **Outputs:** a draft outcome note: goal, levers, one measure each, what's out of scope.
- **Stops when:** the draft is written. Anything unclear is marked [CHECK].
- **Proof it worked:** every line of the note traces back to the recap.
- **Person in charge:** product manager (edits it); the sponsor confirms it.
- **Runs on (guess):** M365 Copilot in Word.
- **To confirm:** ⚠️ whether meeting recaps are allowed for sponsor meetings.

### M3. Interview scheduler
- **Used in:** 1.3
- **For:** the team
- **Kind:** Me → Auto ⚠️
- **Job:** book interviews and shadowing sessions with nominated users.
- **Starts when:** user leaders send the list of nominated people.
- **Inputs:** the nominee list; free and busy times; the interview length.
- **Allowed actions:** send invitations and reminders from the product manager's calendar.
- **Not allowed:** contacting anyone not on the list; sending anything except invitations and reminders.
- **Outputs:** booked interviews, shown in the tracker.
- **Stops when:** everyone is booked or has said no. It tells the product manager about anyone who didn't reply.
- **Proof it worked:** the tracker shows each nominee as booked, declined or no reply.
- **Person in charge:** product manager.
- **Runs on (guess):** Power Automate with Outlook.
- **To confirm:** ⚠️ whether the bank allows automations to send invitations for a person.

### M4. Reaction summarizer
- **Used in:** 1.6
- **For:** the team
- **Kind:** Me → Draft
- **Job:** turn notes from mock-up sessions into a short "what to change next" list.
- **Starts when:** after each round of mock-up sessions.
- **Inputs:** the reaction log: version, user, what they did and what confused them.
- **Allowed actions:** read the log; write a draft summary.
- **Not allowed:** changing the mock-up; inventing reactions.
- **Outputs:** the top changes, each linked to the sessions behind it.
- **Stops when:** every session in the round is summarized.
- **Proof it worked:** each suggested change cites at least one session.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot or an approved AI assistant.
- **To confirm:** none.

### M5. Baseline recorder
- **Used in:** 1.7
- **For:** the team
- **Kind:** Me → Auto
- **Job:** record each measure's "before" number on a schedule, from the day the measure is set.
- **Starts when:** the measure's definition and source are agreed in 1.7.
- **Inputs:** the measure's definition, its source and its owner.
- **Allowed actions:** read the source; save a dated snapshot.
- **Not allowed:** changing the definition; filling gaps with estimates.
- **Outputs:** a dated history of the measure, for the pilot group and the comparison group.
- **Stops when:** the product is retired or the measure is replaced. If the source is missing or late, it alerts the data owner.
- **Proof it worked:** the first snapshot matches the number recorded by hand in 1.7.
- **Person in charge:** product manager; the data owner owns the source.
- **Runs on (guess):** Power BI with scheduled refresh, or Snowflake.
- **To confirm:** ⚠️ who may set up scheduled snapshots.

### M6. Gate pack drafter
- **Used in:** 1.7, 2.8, 5.7 (and any gate)
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** put a step's outputs together into one gate pack.
- **Starts when:** the product manager asks, before a gate meeting.
- **Inputs:** the outputs listed in the step's playbook sub-steps.
- **Allowed actions:** read those outputs; write a draft pack.
- **Not allowed:** changing any output; deciding go or no-go.
- **Outputs:** a draft gate pack, with a list of anything missing.
- **Stops when:** every listed output is in, or marked missing.
- **Proof it worked:** the product manager checks every claim against its source.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot in Word.
- **To confirm:** ⚠️ whether the bank has a gate pack template.

### M7. Platform fit checker
- **Used in:** 2.2
- **For:** the team
- **Kind:** Me → Draft
- **Job:** score a product brief against the five platform criteria and list known blockers.
- **Starts when:** the product manager asks, at the start of Define.
- **Inputs:** the brief so far; the time map from 1.4; the "pick the layer" guide in `tech-stack.md`; known IT data rules.
- **Allowed actions:** read; write a draft scorecard.
- **Not allowed:** choosing the platform.
- **Outputs:** a scorecard for each candidate platform, with blockers and questions for the platform teams.
- **Stops when:** every candidate is scored.
- **Proof it worked:** the platform teams confirm or correct the blockers.
- **Person in charge:** product manager; platform teams check it.
- **Runs on (guess):** an approved AI assistant.
- **To confirm:** ⚠️ IT's data rules (DLP) for Power Platform connectors.

### M8. Decision log drafter
- **Used in:** 2.6 (and any meeting with a decision)
- **For:** the team
- **Kind:** Me → Draft
- **Job:** draft decision-log entries from meeting recaps.
- **Starts when:** after a meeting where something was decided.
- **Inputs:** the meeting recap.
- **Allowed actions:** read the recap; draft entries.
- **Not allowed:** recording a decision nobody stated; editing past entries.
- **Outputs:** draft entries: what was decided, the options, who decided and why.
- **Stops when:** every decision in the recap is drafted.
- **Proof it worked:** whoever made the decision confirms the entry.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot (Teams meeting recap).
- **To confirm:** ⚠️ whether meeting recaps are allowed for partner meetings.

### M9. Measures sheet builder
- **Used in:** 2.7
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** draft the measures sheet (the five kinds of measures, each with its source and formula) from the brief and the data contract.
- **Starts when:** the data contract and stories are drafted.
- **Inputs:** the brief; the data contract; the quality bar; the baseline from 1.7.
- **Allowed actions:** read; write a draft sheet.
- **Not allowed:** setting targets; inventing numbers (unknown numbers are [X]).
- **Outputs:** a draft measures sheet, ready for the dashboard.
- **Stops when:** each of the five kinds has at least one measure with a source.
- **Proof it worked:** Finance and the data owner confirm the sources and formulas.
- **Person in charge:** product manager.
- **Runs on (guess):** an approved AI assistant; Power BI for the dashboard later.
- **To confirm:** none.

### M10. Agent spec drafter
- **Used in:** 3.1
- **For:** the team
- **Kind:** Me → Draft
- **Job:** turn a user story or agent idea into a first agent spec in this format.
- **Starts when:** the product manager asks, during design.
- **Inputs:** the story or idea; the design; the data contract; the control list.
- **Allowed actions:** read; write a draft spec.
- **Not allowed:** widening an agent's allowed actions beyond what the story needs.
- **Outputs:** a draft spec with every field filled in, and questions marked ⚠️.
- **Stops when:** every field is filled in or marked as a question.
- **Proof it worked:** the platform team and the risk partner agree the spec.
- **Person in charge:** product manager.
- **Runs on (guess):** an approved AI assistant (Claude's **agent-spec** skill does this today).
- **To confirm:** none.

### M11. Controls checker
- **Used in:** 3.4, 4.5
- **For:** the team
- **Kind:** Me (3.4) / Draft (4.5) → Auto (test environment only)
- **Job:** re-run every control test on each new version.
- **Starts when:** a new version reaches the test environment.
- **Inputs:** the controls checklist and its test cases.
- **Allowed actions:** run the control tests in the test environment; record the results.
- **Not allowed:** running anything in the live environment; changing controls.
- **Outputs:** a pass or fail for each control, with proof.
- **Stops when:** every control is tested. Any failure alerts the product manager.
- **Proof it worked:** a control that was broken on purpose shows as a failure.
- **Person in charge:** product manager; risk reviews failures.
- **Runs on (guess):** AWS Bedrock evaluation or a test script in the platform.
- **To confirm:** ⚠️ which test environments exist for each platform.

### M12. Test case generator
- **Used in:** 3.6
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** suggest new test cases from user feedback and test failures.
- **Starts when:** each build cycle.
- **Inputs:** the test set; feedback; failures from earlier test runs.
- **Allowed actions:** read; propose new cases.
- **Not allowed:** writing the "good answer" (experienced users do that); changing old test set versions.
- **Outputs:** proposed cases, each with the reason it's needed.
- **Stops when:** the proposals are delivered.
- **Proof it worked:** users accept the cases that matter, and they catch real problems.
- **Person in charge:** product manager; experienced users approve the answers.
- **Runs on (guess):** AWS Bedrock or an approved AI assistant.
- **To confirm:** none.

### M13. Data-use checker
- **Used in:** 4.2
- **For:** the team
- **Kind:** Draft → Auto
- **Job:** compare the data the product actually reads with the signed data contract.
- **Starts when:** each new frozen version, and monthly after launch.
- **Inputs:** the access logs or query history; the data contract.
- **Allowed actions:** read; report differences.
- **Not allowed:** changing access.
- **Outputs:** a list of any fields read that aren't in the contract.
- **Stops when:** every field read is checked. Any difference alerts privacy and the product manager.
- **Proof it worked:** a field added on purpose in testing gets flagged.
- **Person in charge:** product manager; privacy reviews flags.
- **Runs on (guess):** Snowflake access history (Horizon).
- **To confirm:** ⚠️ which access logs are available.

### M14. Sign-off router
- **Used in:** 4.7
- **For:** the team
- **Kind:** Me → Auto ⚠️
- **Job:** send the evidence pack to each signer, track replies and chase anything late.
- **Starts when:** the evidence pack is final.
- **Inputs:** the evidence pack; the signer list; due dates.
- **Allowed actions:** send approval requests and reminders; record responses in the tracker.
- **Not allowed:** approving anything; changing the pack.
- **Outputs:** each sign-off recorded with its date and any conditions.
- **Stops when:** everyone has signed. Anything overdue goes to the product manager to unblock in person.
- **Proof it worked:** the tracker matches the signers' own replies.
- **Person in charge:** product manager.
- **Runs on (guess):** Power Automate approvals.
- **To confirm:** ⚠️ whether sign-offs may be recorded this way, or must use the bank's own system.

### M15. Readiness tracker
- **Used in:** 5.1
- **For:** the team
- **Kind:** Draft → Auto
- **Job:** keep the release readiness checklist current and flag gaps.
- **Starts when:** release planning begins.
- **Inputs:** the readiness checklist; the tracker.
- **Allowed actions:** read the tracker; tick items when their proof exists; flag what's missing.
- **Not allowed:** marking an item done without its proof.
- **Outputs:** a readiness view with gaps, owners and dates.
- **Stops when:** every item is ticked or has an owner and a date.
- **Proof it worked:** a spot check of ticked items against their proof.
- **Person in charge:** product manager.
- **Runs on (guess):** Power Automate with the tracker.
- **To confirm:** none.

### M16. Release automation
- **Used in:** 5.2
- **For:** the team
- **Kind:** Me → Auto ⚠️
- **Job:** move an approved version from test to live, step by step, using the platform's own release tools.
- **Starts when:** the release is approved and its date arrives.
- **Inputs:** the approved version; the release checklist from the first manual release.
- **Allowed actions:** run the platform's release steps for the approved version only.
- **Not allowed:** releasing an unapproved version; skipping a step.
- **Outputs:** the version is live, with a release log.
- **Stops when:** the release is done, or a step fails (then it stops and alerts the platform team).
- **Proof it worked:** the release log matches the checklist, and the first live outputs are checked by hand.
- **Person in charge:** platform team.
- **Runs on (guess):** Power Platform pipelines or the Salesforce release process.
- **To confirm:** ⚠️ the bank's change-management rules for automated releases.

### M17. Wins spotter
- **Used in:** 5.5
- **For:** the team
- **Kind:** Me → Draft
- **Job:** find wins that started from the product, for leaders to celebrate.
- **Starts when:** weekly.
- **Inputs:** AI-tagged opportunities and outcomes; feedback.
- **Allowed actions:** read; draft a short list of wins.
- **Not allowed:** sharing anything; naming clients beyond what the bank allows.
- **Outputs:** a draft wins list with the evidence for each.
- **Stops when:** the list is delivered.
- **Proof it worked:** each win checks out against the record.
- **Person in charge:** product manager; leaders choose what to share.
- **Runs on (guess):** Salesforce reports or Snowflake, with an approved AI assistant.
- **To confirm:** ⚠️ what client details may be shared internally.

### M18. Monthly review pack drafter
- **Used in:** 6.4
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** build the monthly keep/change/stop pack from the dashboard and the impact note.
- **Starts when:** monthly, before the review.
- **Inputs:** the dashboard; the impact note; quality trends; top feedback.
- **Allowed actions:** read; write a draft pack.
- **Not allowed:** making the keep/change/stop recommendation for the product manager.
- **Outputs:** a draft pack, one page per feature.
- **Stops when:** every live feature has a page.
- **Proof it worked:** the numbers in the pack match the dashboard.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot with Power BI.
- **To confirm:** none.

### M19. Log summarizer
- **Used in:** 6.6
- **For:** the team
- **Kind:** Me → Draft
- **Job:** total time spent and waits from the first-time logs, and list the automation candidates.
- **Starts when:** at the end of the first full pass through all six steps.
- **Inputs:** the first-time logs from every sub-step.
- **Allowed actions:** read; write a draft summary.
- **Not allowed:** deciding which agents to build.
- **Outputs:** time and waits by step, plus the candidates that passed the three-question check.
- **Stops when:** every log is read.
- **Proof it worked:** the totals add up to the logs.
- **Person in charge:** product manager.
- **Runs on (guess):** an approved AI assistant.
- **To confirm:** none.

---

## Not agents, but reusable assets
These come up in the review tables but aren't agents. Each one is a template or
a library, built once and reused.
- **Story library (2.5):** reusable user stories for permissions, logging, feedback and controls.
- **Monitoring plan template (4.8):** the standard plan, filled in for each product.
- **Live dashboard template (6.1):** one Power BI template for the five kinds of measures.

## Changes to project agents
Two agents in the RM memo's Appendix A got an **ongoing mode**, because the
playbook uses them after launch, not just once:
- **A11 Data contract checker:** after Define, it runs on every data refresh (3.2) and alerts the data owner on failure.
- **A15 Fairness monitor:** it runs again monthly after launch (4.4).

Both changes are made in the memo and its designed pages (2026-10-09).

_Last updated: 2026-10-09_
