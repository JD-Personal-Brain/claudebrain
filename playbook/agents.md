# Agent library: the agents that run the product machine, and my research helpers

These agents help the team run any project through the six steps. They're
reused on every project, so they're specified once here: M1 to M19 run the
machine's own paperwork and routing, and M20 to M33 do the team's analysis,
testing and monitoring work (they started as the RM project's helpers and were
made general on 2026-10-10). A project's own agents (the product users see, or
agents only that project needs) go in its memo's Appendix A, like A1 to A5 in
the RM memo. H1 and on are my own research helpers (see "My research helpers" near the end of the Agent Library page):
they keep my reference pages current and are not part of the product machine.

Written with the **agent-spec** skill. Every agent follows the AI principles in
`product-framework.md`: assistive first, one job each, read-only or draft-only unless a named
person approves, and every action logged. Auto agents act only within their
listed actions. ⚠️ on an Auto agent means it sends requests, reminders, reports
or alerts to people outside the project team, or changes a live system, so it
depends on the bank allowing that. Every agent follows K25 (agents stop rather
than guess): if an input is missing, stale or fails a check, it stops and alerts
its person in charge; a monitor never reports a pass on missing data.

> ⚠️ **How much to trust this.** Written 2026-10-09 from the playbook, not
> from Associated Bank. "Runs on" tools are guesses from `tech-stack.md`, and
> every ⚠️ is a question to confirm at the bank. None of the M agents is built yet; H1 is set up and running.

---

### M1. Kickoff pack builder
- **Used in:** 1.0
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** create a new project's starting files from its one-line project statement, and add the project's section to the one shared tracker (not a new tracker).
- **Starts when:** the product manager writes the project statement.
- **Inputs:** the project statement; the task tables in `product-machine.md`; the who-decides list in `product-framework.md`.
- **Allowed actions:** create draft files: the project's section of the shared tracker with every task listed, the decision log, the risk and issue list and the project file.
- **Not allowed:** assigning owners or dates; contacting anyone.
- **Outputs:** a draft project pack, ready for owners and dates, with a "limiting factor" field at the top of the tracker section (filled in by the product manager).
- **Stops when:** every file exists. If the statement is missing, it asks for it and creates nothing.
- **Proof it worked:** the project's tracker section has one row for every task in the Product Machine's task tables.
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
- **Kind:** Me → Auto ⚠️
- **Job:** record each measure's "before" number on a schedule, from the day the measure is set.
- **Starts when:** the measure's definition and source are agreed in 1.7.
- **Inputs:** the measure's definition, its source and its owner.
- **Allowed actions:** read the source; save a dated snapshot.
- **Not allowed:** changing the definition; filling gaps with estimates.
- **Outputs:** a dated history of the measure for the target users; split by pilot group and comparison group once 2.8 confirms them.
- **Stops when:** the product is retired or the measure is replaced. If the source is missing or late, it alerts the data owner.
- **Proof it worked:** the first snapshot matches the number recorded by hand in 1.7.
- **Person in charge:** product manager; the data owner owns the source.
- **Runs on (guess):** Power BI with scheduled refresh, or Snowflake.
- **To confirm:** ⚠️ who may set up scheduled snapshots.

### M6. Gate pack drafter
- **Used in:** 1.7, 2.8, 3.7, 5.7 (and any gate)
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** put a step's outputs together into one gate pack.
- **Starts when:** the product manager asks, before a gate decision (in writing, or a meeting if contested).
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
- **Stops when:** every control is tested. Any failure alerts the product manager. If a control's test case or the test environment is missing, it reports that control as "not checked", never as a pass, and alerts the product manager.
- **Proof it worked:** a control that was broken on purpose shows as a failure.
- **Person in charge:** product manager; risk reviews failures.
- **Runs on (guess):** AWS Bedrock evaluation or a test script in the platform.
- **To confirm:** ⚠️ which test environments exist for each platform.

### M12. Test case generator
- **Used in:** 3.6
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** draft the first test set at 3.6, then suggest new test cases from user feedback and test failures.
- **Starts when:** at 3.6, once release 1's stories are agreed; after that, each build cycle.
- **Inputs:** the release 1 user stories and acceptance criteria (2.5); the must-refuse cases from the control requirements (2.4); later, the test set, feedback and failures from earlier test runs.
- **Allowed actions:** read; propose new cases.
- **Not allowed:** writing the "good answer" (experienced users do that); changing old test set versions.
- **Outputs:** at 3.6, a draft first test set built from the stories, acceptance criteria and must-refuse cases; later, proposed new cases, each with the reason it's needed.
- **Stops when:** the proposals are delivered.
- **Proof it worked:** users accept the cases that matter, and they catch real problems.
- **Person in charge:** product manager; experienced users approve the answers.
- **Runs on (guess):** AWS Bedrock or an approved AI assistant.
- **To confirm:** none.

### M13. Data-use checker
- **Used in:** 4.2
- **For:** the team
- **Kind:** Draft → Auto ⚠️
- **Job:** compare the data the product actually reads with the signed data contract. Documents: not covered yet (privacy compares the documents retrieved with the contract's sources by hand).
- **Starts when:** each new frozen version, and monthly after launch.
- **Inputs:** the access logs or query history; the data contract.
- **Allowed actions:** read; report differences.
- **Not allowed:** changing access.
- **Outputs:** a list of any fields read that aren't in the contract.
- **Stops when:** every field read is checked. Any difference alerts privacy and the product manager. If access logs are missing or older than [X] days, it reports "not checked" and alerts privacy.
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
- **Allowed actions:** read the tracker; mark items "proof found" for the product manager to confirm; tick automatically only items backed by a system record (a recorded sign-off, a logged dry run); flag what's missing.
- **Not allowed:** marking an item done without its proof.
- **Outputs:** a readiness view with gaps, owners and dates.
- **Stops when:** every item is ticked, confirmed by the product manager, or has an owner and a date.
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
- **Job:** build the monthly keep/change/stop pack from the dashboard and the impact note; every third month, also a quarterly summary for the invest more / adjust / stop decision (6.4).
- **Starts when:** monthly, before the review.
- **Inputs:** the dashboard; the impact note; quality trends; top feedback.
- **Allowed actions:** read; write a draft pack.
- **Not allowed:** making the keep/change/stop recommendation for the product manager.
- **Outputs:** a draft pack, one page per AI product; every third month, a quarterly summary for the invest more / adjust / stop decision (6.4).
- **Stops when:** every live AI product has a page.
- **Proof it worked:** the numbers in the pack match the dashboard.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot with Power BI.
- **To confirm:** none.

### M19. Log summarizer
- **Used in:** 6.6
- **For:** the team
- **Kind:** Me → Draft
- **Job:** total time spent and waits from the sub-step logs (the full first-time log on the first project), work out each sub-step's wait index, and list the candidates to cut and to automate.
- **Starts when:** at the end of each project's first full pass through all six steps (sub-step 6.6).
- **Inputs:** the sub-step logs from every sub-step; the tracker (dates); the decision log (the dates each gate pack was ready and each decision was made); the release notes.
- **Allowed actions:** read; write a draft summary.
- **Not allowed:** deciding what to delete or which agents to build.
- **Outputs:** time and waits by step, sub-steps ranked by wait index (highest first), the tasks to consider cutting, the candidates that passed the automation check, and the four machine measures (days from kickoff to pilot, days at each gate, releases per month in the pilot, and the wait index).
- **Stops when:** every log is read.
- **Proof it worked:** the totals add up to the logs.
- **Person in charge:** product manager.
- **Runs on (guess):** an approved AI assistant.
- **To confirm:** none.

---

### M20. Interview synthesizer
- **Used in:** 1.3
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** turn interview and shadowing notes into themes and quotes, each linked to its source.
- **Starts when:** the product manager asks, after a round of interviews.
- **Inputs:** interview recaps or transcripts (only where recording is allowed) and the product manager's notes.
- **Allowed actions:** read the notes; write draft themes.
- **Not allowed:** inventing quotes; naming interviewees outside the project team.
- **Outputs:** a themes list, each theme with its quotes and the interviews behind it.
- **Stops when:** every interview is processed.
- **Proof it worked:** the product manager spot-checks every theme against the notes.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot or a Copilot Studio agent.
- **To confirm:** ⚠️ whether meeting recaps and transcripts are allowed for user interviews.

### M21. Opportunity sizer
- **Used in:** 1.2
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** answer plain-English sizing questions, so each lever gets a rough dollar range.
- **Starts when:** the product manager writes the sizing questions.
- **Inputs:** the questions; the data sources the data owner has approved for sizing.
- **Allowed actions:** run read-only queries; save each query with its answer.
- **Not allowed:** changing data; filling gaps with guesses (unknown numbers are [X]).
- **Outputs:** sized levers, each with the query shown.
- **Stops when:** every lever is sized.
- **Proof it worked:** an analyst re-runs the key numbers.
- **Person in charge:** an analyst; the product manager owns the questions.
- **Runs on (guess):** Snowflake Cortex Analyst, Power BI.
- **To confirm:** ⚠️ which data the team may query in Discover.

### M22. Time-use analyst
- **Used in:** 1.4
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** find where users' time goes, and which activities come before good results.
- **Starts when:** the main activities are listed from shadowing (1.4).
- **Inputs:** activity data (for example CRM activities and email or meeting reports).
- **Allowed actions:** run read-only queries; write a draft time map.
- **Not allowed:** reporting on named individuals beyond the project team.
- **Outputs:** a time map: activity, hours per week, type and source (data or estimate).
- **Stops when:** the map is complete.
- **Proof it worked:** the product manager confirms it with users in person.
- **Person in charge:** product manager.
- **Runs on (guess):** Snowflake Cortex, Power BI.
- **To confirm:** ⚠️ which activity and usage reports the bank has turned on.

### M23. Requirements drafter
- **Used in:** 2.1, 2.5
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** draft the problem statement, the outcome, user stories and acceptance criteria.
- **Starts when:** the Discover gate is passed.
- **Inputs:** the Discover gate pack (2.1); for stories in 2.5, also the control requirements from 2.4.
- **Allowed actions:** read; write drafts.
- **Not allowed:** approving anything; adding scope nobody asked for.
- **Outputs:** a draft brief and draft stories with acceptance criteria.
- **Stops when:** the drafts are delivered.
- **Proof it worked:** the team and the sponsor approve them.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot in Word, or a Copilot Studio agent.
- **To confirm:** none.

### M24. Data contract checker
- **Used in:** 2.3, 3.2
- **For:** the team
- **Kind:** Draft → Draft (2.3); Me → Auto ⚠️ (3.2, ongoing mode)
- **Job:** check that every field in the data contract exists, is fresh enough and passes its quality checks. Documents: not covered yet (for a product built on documents, the content owner checks re-indexing and permissions by hand until this agent gains a documents mode).
- **Starts when:** the field list is drafted in 2.3; after that, on every data refresh.
- **Inputs:** the data contract; the tables and their quality and access records.
- **Allowed actions:** read-only checks; alert the data owner on failure.
- **Not allowed:** changing data or access.
- **Outputs:** a gap list in Define; after that, a pass or fail for each refresh.
- **Stops when:** every field is checked. In its ongoing mode, it runs on every refresh until the product is retired. If a table or its quality record is missing or late, it reports "not checked" for those fields, never a pass, and alerts the data owner.
- **Proof it worked:** the data owner signs off the gap list; a field broken on purpose in testing gets flagged.
- **Person in charge:** the data owner.
- **Runs on (guess):** Snowflake Cortex and Snowflake data checks.
- **To confirm:** ⚠️ how the bank certifies trusted tables.

### M25. Risk intake assistant
- **Used in:** 2.4, 4.1
- **For:** the team
- **Kind:** Draft → Draft (2.4); Me → Draft (4.1)
- **Job:** pre-fill the bank's risk intake from the brief, and flag likely high-risk areas.
- **Starts when:** the brief's first lines exist (2.1); again before the formal rating in 4.1.
- **Inputs:** the bank's AI policies and intake form; the brief; the data field list.
- **Allowed actions:** read; draft the intake.
- **Not allowed:** setting the risk rating; submitting the intake.
- **Outputs:** a pre-filled intake, with likely high-risk areas flagged.
- **Stops when:** the intake is drafted.
- **Proof it worked:** the risk partner sets the rating and confirms the draft was accurate.
- **Person in charge:** the product manager; the risk partner confirms the draft's accuracy.
- **Runs on (guess):** a Copilot Studio agent grounded in the bank's policies.
- **To confirm:** ⚠️ the bank's intake form and process.

### M26. Test grader
- **Used in:** 3.7, 4.3
- **For:** the team
- **Kind:** Draft → Auto
- **Job:** score every version of the product against the test set and the quality bar.
- **Starts when:** a new version reaches the test environment.
- **Inputs:** the test set; the product's outputs; the quality bar thresholds.
- **Allowed actions:** run the test set in the test environment; score; report.
- **Not allowed:** changing the test set or the thresholds; releasing anything.
- **Outputs:** a score report against each part of the quality bar.
- **Stops when:** every test case is scored. A score below the bar alerts the product manager. If the test set, the thresholds or any output is missing, it reports "not scored" for those cases, never a pass, and alerts the product manager.
- **Proof it worked:** experienced users grade a sample, and their grades match.
- **Person in charge:** product manager.
- **Runs on (guess):** AWS Bedrock model evaluation.
- **To confirm:** ⚠️ which test environments exist for each platform.

### M27. Red-team agent
- **Used in:** 4.3
- **For:** the team
- **Kind:** Draft → Auto
- **Job:** try to break the product: ask for other users' data, a credit decision, a price or off-topic answers.
- **Starts when:** a frozen version is ready for review.
- **Inputs:** the product in test; the attack list, including the must-refuse cases.
- **Allowed actions:** send test requests in the test environment only.
- **Not allowed:** anything in the live environment; using real client data outside what the test environment allows.
- **Outputs:** a failure list.
- **Stops when:** every attack type is run.
- **Proof it worked:** a weakness planted on purpose in testing is found; risk reviews every failure.
- **Person in charge:** the risk partner.
- **Runs on (guess):** AWS Bedrock.
- **To confirm:** ⚠️ whether risk runs its own red-teaming as well.

### M28. Fairness monitor
- **Used in:** 4.4
- **For:** the team
- **Kind:** Draft → Auto
- **Job:** check that the product treats similar clients and users alike, across the groups compliance chose.
- **Starts when:** compliance agrees the groups and thresholds in 4.4; after that, monthly after launch (its ongoing mode).
- **Inputs:** the product's outputs; the group definitions and thresholds.
- **Allowed actions:** read-only analysis; write a report.
- **Not allowed:** changing the product; deciding whether a difference is acceptable.
- **Outputs:** a fairness report.
- **Stops when:** the report is complete; it runs again each month after launch. If outputs or group data for a period are missing, it reports "not checked" for that period and alerts compliance.
- **Proof it worked:** a bias planted on purpose in test data is flagged; compliance reviews the results.
- **Person in charge:** compliance.
- **Runs on (guess):** Snowflake, Power BI.
- **To confirm:** ⚠️ which groups compliance wants compared.

### M29. Evidence pack assembler
- **Used in:** 4.7
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** compile the test results, data use and controls into the evidence pack reviewers sign.
- **Starts when:** 4.1 to 4.6 are done and the monitoring plan is drafted.
- **Inputs:** the outputs of 4.1 to 4.6 and the draft monitoring plan (4.8); the bank's template, if there is one.
- **Allowed actions:** read; write a draft pack.
- **Not allowed:** changing any result; sending the pack.
- **Outputs:** a draft evidence pack.
- **Stops when:** the pack is drafted, with anything missing listed.
- **Proof it worked:** the product manager and risk verify every claim against its source.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot in Word.
- **To confirm:** ⚠️ whether the bank has an evidence pack template.

### M30. Feedback triage
- **Used in:** 5.6
- **For:** the team
- **Kind:** Me → Auto ⚠️
- **Job:** sort user feedback into bugs, quality issues and ideas, and add each to the backlog.
- **Starts when:** new feedback arrives.
- **Inputs:** feedback from the product's one-click buttons and comments.
- **Allowed actions:** read; tag; add items to the backlog; alert the product manager and operations to a likely incident.
- **Not allowed:** changing priorities; replying to users.
- **Outputs:** tagged backlog items; incident alerts.
- **Stops when:** all new feedback is sorted.
- **Proof it worked:** the product manager reviews a weekly sample.
- **Person in charge:** product manager.
- **Runs on (guess):** Power Automate with an approved AI model.
- **To confirm:** none.

### M31. Impact analyst
- **Used in:** 6.2
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** report the product's effect on the main measure, against the baseline and the comparison group.
- **Starts when:** monthly.
- **Inputs:** the tagged results data; the baseline; the method Finance agreed in 2.7.
- **Allowed actions:** read-only queries; write a draft impact note.
- **Not allowed:** changing the method; sharing figures before analytics checks them.
- **Outputs:** monthly impact figures and a three-line note.
- **Stops when:** the note is complete.
- **Proof it worked:** analytics validates the numbers before reporting.
- **Person in charge:** analytics.
- **Runs on (guess):** Snowflake Cortex Analyst, Power BI.
- **To confirm:** none.

### M32. Quality watchdog
- **Used in:** 6.3
- **For:** the team
- **Kind:** Draft → Auto
- **Job:** re-run the test set after every change and at least monthly, and alert when quality slips ("drift").
- **Starts when:** any change to prompts, rules, data or models, including vendor model updates (from the vendor's release notes, checked by the platform team); and monthly.
- **Inputs:** the test set; live outputs; feedback; the monitoring plan's thresholds.
- **Allowed actions:** run the test set; read live signals; alert.
- **Not allowed:** fixing, rolling back or pausing the product (the product manager decides).
- **Outputs:** the score trend and alerts.
- **Stops when:** each run is complete. If the test set, live outputs or thresholds are missing, it reports "not checked", never "no drift", and alerts the product manager.
- **Proof it worked:** alerts are reviewed within [X] days, and a drop introduced on purpose in testing triggers one.
- **Person in charge:** product manager.
- **Runs on (guess):** AWS Bedrock model evaluation, Power Automate.
- **To confirm:** none.

### M33. Improvement scout
- **Used in:** 6.5
- **For:** the team
- **Kind:** Draft → Draft
- **Job:** propose and rank the next backlog items or the next lever, from usage and feedback.
- **Starts when:** before each feature wave is planned.
- **Inputs:** the dashboard; feedback themes; the monthly reviews.
- **Allowed actions:** read; write a ranked list.
- **Not allowed:** choosing the next feature wave.
- **Outputs:** ranked suggestions, each with its evidence.
- **Stops when:** the list is delivered.
- **Proof it worked:** the product manager and the sponsor decide, and say which suggestions they used.
- **Person in charge:** product manager.
- **Runs on (guess):** M365 Copilot or a Copilot Studio agent.
- **To confirm:** none.

## My research helpers: agents that keep my own pages current
These aren't part of the product machine and don't belong to any project. They
keep the reference material I plan from up to date. Each runs as a Claude Code
scheduled task, from a skill in this repo.

### H1. Bank news scout
- **Used in:** none (keeps the Bank Business Briefing current)
- **For:** me
- **Kind:** Draft → Draft
- **Job:** find new public facts about Associated Bank that change the Bank Business Briefing, and draft the edits.
- **Starts when:** every Monday at 7:46 am Central (6:46 am after clocks change on November 1; a scheduled task), once on October 23, 2026 after the Q3 results (that run swaps in the Q3 figures throughout), or when I say "run the news scout".
- **Inputs:** the briefing (`memos/bank-business.md`); the scout's own log (`memos/bank-news-log.md`), so nothing is reported twice; public web pages and search results.
- **Allowed actions:** search the web and open public pages; edit the briefing, rebuild its page source and add to the log on a draft branch; save that branch to GitHub; write one summary.
- **Not allowed:** merging into main or opening a pull request; republishing the live page; sending email with any connector; using my work email; using non-public information; writing a number without its period and source; filling a gap from memory.
- **Outputs:** draft edits on a draft branch, one log entry and one summary.
- **Stops when:** the summary is written, including a short "nothing new" summary when nothing changed. A page that won't open is named in the summary and left as a gap.
- **Proof it worked:** the scheduled task's email notice in my personal inbox, the log entry and the draft branch.
- **Person in charge:** me.
- **Runs on (guess):** a Claude Code scheduled task, from the `bank-news-scout` skill (confirmed: set up and running).
- **To confirm:** that the first weekly notice (Monday October 19) reaches my personal inbox, and that its runs don't stop to wait for an approval (open item W1).

## Not agents, but reusable assets
These come up in the review tables but aren't agents. Each one is a template or
a library, built once and reused.
- **Story library (2.5):** reusable user stories for permissions, logging, feedback and controls.
- **Approved vendors list (4.6):** the bank's list, checked for every vendor the product relies on.
- **Release checklist (5.2):** written at the first manual release, then reused for every release.
- **Monitoring plan template (4.8):** the standard plan, filled in for each product.
- **Live dashboard template (6.1):** one Power BI template for the five kinds of measures.

## Agents with an ongoing mode
Ongoing mode means an agent first used once in a sub-step that then keeps
checking the live product until it's retired. Five agents have one:
- **M5 Baseline recorder:** set up in 1.7; it keeps recording each measure on a schedule until the product is retired or the measure is replaced, and alerts the data owner if the source is missing or late.
- **M13 Data-use checker:** it runs again monthly after launch (4.2) and alerts privacy on any difference.
- **M24 Data contract checker:** after Define, it runs on every data refresh (3.2) and alerts the data owner on failure.
- **M28 Fairness monitor:** set up in 4.4; its ongoing mode re-runs the check monthly after launch (4.4), and fairness is in the monitoring plan (4.8).
- **M32 Quality watchdog:** re-runs the test set on every change and at least monthly (6.3), and alerts the product manager when quality slips.

Agents built to run on a schedule from the start (M11, M17, M18, M26, M30 and M31) are not "ongoing mode": running repeatedly is their normal job.

_Last updated: 2026-10-15_
