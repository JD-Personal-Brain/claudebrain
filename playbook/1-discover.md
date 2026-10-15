# Step 1: Discover, the first time

**The question:** which problem or opportunity is worth solving first?
**The gate:** sponsor agrees on the target, the measure and today's baseline.
**Governance thread:** risk partner briefed on the idea.

Work through 1.0 to 1.7 in order. The risk partner is briefed on the idea before any build uses real client data. Some can overlap: 1.3, 1.4 and 1.5 usually
run in the same weeks. Fill in the first-time log (see `README.md`) for every
sub-step. At the end, run the automation review.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the relationship managers (RMs)
> memo and general practice, not from Associated Bank. Lines marked ⚠️ are
> guesses about how the bank works. Tools are named from `tech-stack.md`.

---

## 1.0 Kick off the project

- **Goal:** start with a named sponsor, the right people, a tracker and the risk partner briefed.
- **Why it matters:** without a named sponsor and agreed decision-makers, every later gate stalls on "who decides?"
- **Know first:**
  - Who is asking for this, and who owns the budget.
  - The bank's process for starting an AI project: is there an intake form or a review board? ⚠️ Not known yet.
  - Which tracker the bank uses for projects. ⚠️ Not known yet (see "Things to find out" in `tech-stack.md`).
- **First time, step by step:**
  1. Write one sentence about the project: "We want to [outcome] for [users], measured by [measure]."
  2. Meet the sponsor (30 minutes). Confirm that they own the outcome and the funding, and that they make the go/no-go call at each gate.
  3. Fill in "who's involved and who decides" (from `product-framework.md`) with real names. Mark gaps as [name needed].
  4. Set up the tracker: copy the six steps' task tables from `product-machine.md`, then give every Discover task an owner and a date. Name the first limiting factor and its owner at the top of the tracker.
  5. Brief the risk partner (from model risk) in 15 minutes: what the idea is, what data it might use, and that nothing touches clients yet. Ask what they'll need to see in Define.
  6. Start the decision log and the risk and issue list, dependencies included (both empty is fine).
  7. Create the project file: `memos/<project>.md`.
  8. Confirm which AI tools the team may use with bank data, and write the list in the project file. No client data goes into any other tool, even for a quick test.
- **Output:** a one-line project statement, the who-decides list, the tracker, the risk partner briefed, the decision log, and the list of AI tools the team may use.
- **Done when:** the sponsor has confirmed their role, every Discover task has an owner and a date, the risk partner has been briefed, and the approved AI tools list is in the project file.
- **Automation watch:**
  - First time: **Me** (sponsor and risk conversations) and **Draft** (setting up the tracker and files).
  - Note: how long setting up the tracker took, and what you copied by hand.
  - Agent: **M1 Kickoff pack builder** (agent library) that creates the tracker, decision log, project file and who-decides template from one project statement. *Draft*: you check it.
- **For RM analytics:** the plan for relationship managers (RMs). Sponsor = the commercial banking leader. The statement: "more new revenue from RMs, by finding opportunities and freeing time to act on them." The memo's "Who's involved" table (section 3) is the who-decides list.

---

## 1.1 Frame the outcome with the sponsor

- **Goal:** agree what "success" means, in a measure the sponsor already cares about.
- **Why it matters:** if the outcome is vague ("use AI more"), you can't size it, measure it or defend it at a gate.
- **Know first:**
  - The sponsor's own targets this year (revenue, efficiency, client numbers).
  - How the bank reports them today, and where (Salesforce, Power BI). ⚠️
- **First time, step by step:**
  1. Ask the sponsor: "If this works, what number moves, and by how much in a year?" Write their words down exactly.
  2. List the possible levers. Each is one way the outcome could move.
  3. Agree on one measure per lever, using a number the bank already tracks where possible.
  4. Agree on what is **out of scope**, such as credit decisions, which carry a much higher legal bar (see Governance in `tech-stack.md`).
  5. Write a one-page outcome note and send it to the sponsor to confirm.
- **Output:** the outcome note: goal, levers, one measure each, out of scope.
- **Done when:** the sponsor has confirmed the note in writing (an email reply is enough).
- **Automation watch:**
  - First time: **Me**. Agreeing a goal is a conversation.
  - Note: which questions got the most useful answers. They become a standard question list.
  - Agent: **M2 Outcome note drafter** (agent library) that turns the meeting recap into the one-page note (M365 Copilot). *Draft*.
- **For RM analytics:** two goals (more revenue opportunities, more time to act) and three levers (win new clients, grow existing clients, keep clients), as in memo section 1.

---

## 1.2 Size the opportunity with real data

- **Goal:** put a rough dollar figure on each lever, so you know which one is biggest.
- **Why it matters:** without sizing, the first target is picked by opinion, and the value model in Define has nothing to stand on.
- **Know first:**
  - Where the data lives (likely Salesforce for pipeline and win/loss, and Snowflake for balances and products ⚠️) and who owns it.
  - What you're allowed to query, and with which tools. Ask the data owner before running anything.
  - An analyst who can check the numbers.
  - Use only AI tools on the approved list from 1.0 (K23).
- **First time, step by step:**
  1. Write each lever as a plain question. Example: "How many clients have product A but not product B?"
  2. Ask the data owner for access, or ask an analyst to run the queries.
  3. Run each question and save the query alongside its answer.
  4. Turn each answer into a rough dollar range: count × typical revenue × a realistic hit rate. Use [X] where you don't have a number yet.
  5. Have the analyst re-run the two or three biggest numbers.
  6. Rank the levers by size, and note how confident you are in each.
- **Output:** a sizing table (lever, question, answer, dollar range, confidence, query used).
- **Done when:** every lever has a range and the biggest numbers have been checked by someone else.
- **Automation watch:**
  - First time: **Draft**. AI can run first-pass questions; a person checks them.
  - Note: which questions you asked. They will repeat on every project with a revenue goal.
  - Agent: **M21 Opportunity sizer** (agent library). It answers plain-English sizing questions read-only, on Snowflake Cortex Analyst. An analyst re-runs the key numbers.
- **For RM analytics:** size new clients (prospects that look like the best clients), growth (product gaps such as treasury management) and retention (falling balances). Use Salesforce pipeline and Snowflake balances.

---

## 1.3 Interview and shadow users

- **Goal:** learn how users really work today, and where it hurts.
- **Why it matters:** data shows *what* happens; only people tell you *why*, and what they'd actually use.
- **Know first:**
  - Who to talk to, by role: the who's-involved list from 1.0, user leaders' nominations, and the user workflow map for this user group if one exists.
  - How many: [X] per role. ⚠️ A common starting point is about 5 to 8 per role. Stop when you stop hearing new things.
  - The bank's rules on recording meetings and on using AI recaps. ⚠️ Confirm before recording.
  - Use only AI tools on the approved list from 1.0 (K23).
- **First time, step by step:**
  1. Start from the user group's workflow map (the user-workflow routine) if one exists: the interviews and shadowing test its "today" side and correct it. If there is no map yet, the interviews build its first version.
  2. Write a 30-minute interview guide of 8 to 10 open questions. Use `prompting.md` Example 1 to draft it, for example "Walk me through what you did after your last client meeting."
  3. Ask user leaders to nominate a mix of people: strong performers, average ones and skeptics.
  4. Send invitations and book the interviews.
  5. Run each interview. Listen more than you talk, and ask "show me" rather than "tell me".
  6. Shadow two or three people for half a day each, and write down every task and how long it takes. Note the team's regular routines (weekly pipeline meetings and similar), because 5.3 builds the product into them.
  7. After each one, write a 5-line summary the same day: biggest pain, a quote, and what surprised you.
  8. When done, pull out themes, with each theme linked to the interviews behind it, and update the workflow map.
- **Output:** interview notes, shadowing notes, and a themes list with quotes and sources.
- **Done when:** you've covered every role and the last two or three interviews added nothing new.
- **Automation watch:**
  - First time: **Me** for the conversations and the scheduling. **Draft** for themes.
  - Note: how long scheduling took (it usually takes more time than you expect), and whether your guide changed after the first few interviews.
  - Agents:
    - **M20 Interview synthesizer** (agent library): turns recaps into themes linked to their sources. You check every theme.
    - **M3 Interview scheduler** (agent library; Power Automate with Outlook) that sends invitations and reminders to nominated users. *Auto*, once the bank allows automations to message people ⚠️.
- **For RM analytics:** talk to RMs, their sales managers, and treasury specialists and credit analysts. The key question: "How do you decide which client to call next?"

---

## 1.4 Map where their time goes

- **Goal:** a picture of the user's week: what takes time, what's admin, and what leads to results.
- **Why it matters:** "banker capacity" claims need a baseline. You can't say you saved time without knowing where it went.
- **Know first:**
  - Activity data: Salesforce activities, and M365 Copilot or Viva Insights reports for email and meetings. ⚠️ Check what the bank has turned on.
  - Your shadowing notes from 1.3.
- **First time, step by step:**
  1. Start from the activities on the workflow map's "today" side, corrected in 1.3, and add any others from shadowing, such as meeting prep, client meetings, call notes, CRM updates and internal meetings.
  2. Pull the data you have for each one: counts and time where the data allows it.
  3. Fill the gaps with estimates from the interviews, labeled as estimates.
  4. Mark each activity as **client-facing**, **admin** or **internal**.
  5. If the data allows it, check which activities show up before won deals.
  6. Show the map to two or three users: "Does this look like your week?" Fix it.
- **Output:** a time map (activity, hours per week, type, source: data or estimate).
- **Done when:** users recognize it as their week.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which data sources were useful, and which were empty or untrusted.
  - Agent: **M22 Time-use analyst** (agent library). It reads activity data (for example, CRM activity) read-only. You confirm the results with users in person.
- **For RM analytics:** the memo targets meeting prep, call notes and CRM updates as the admin to cut.

---

## 1.5 Understand how they're measured and rewarded

- **Goal:** know whether using the new tool would help users hit their own goals.
- **Why it matters:** people adopt what helps them get paid or recognized. A tool that creates work their scorecard ignores won't get used.
- **Know first:**
  - Who owns the scorecards and incentives (sales leadership, HR).
  - What's confidential: you may only get the structure, not individual numbers.
- **First time, step by step:**
  1. Ask sales leadership: "What are users measured on, and what's paid?"
  2. Ask users the same question in interviews, and compare the answers.
  3. Check whether the outcome from 1.1 shows up in their scorecard.
  4. If it doesn't, write down the gap and raise it with the sponsor now, not at launch.
- **Output:** a short note: what users are measured on, whether it matches the outcome, and any gap.
- **Done when:** the sponsor knows about any gap and has said how it will be handled.
- **Automation watch:**
  - First time: **Me**. These are sensitive conversations.
  - Note: who had the real answer. Next project, go to them first.
  - Agent: none. This stays with a person.
- **For RM analytics:** if RMs are paid on closed revenue but not on referrals, cross-team referral insights will be ignored. Raise that early.

---

## 1.6 Test a rough mock-up

- **Goal:** get real reactions to something users can see and click, before anything is built.
- **Why it matters:** people can't tell you what they want in the abstract, but they react instantly to a screen.
- **Know first:**
  - The top 2 or 3 pains from 1.3 and 1.4.
  - What data you may show. Use **sample data only**, with no real client data.
  - Where to build it: a clickable HTML prototype, built with an AI tool from the approved list in 1.0 (sample data only), or Copilot Studio or Power Apps in a test environment.
- **First time, step by step:**
  1. Pick the one pain the mock-up should solve.
  2. Build a rough version in a day or two. Rough is fine.
  3. Show it to 3 to 5 users. Ask "What would you do next?", not "Do you like it?"
  4. Write down what they did, what confused them and what they asked for.
  5. Change it and show it again a few days later. Repeat 2 or 3 times.
  6. Keep every version.
- **Output:** the prototype versions and a reaction log (version, user, what they did, what changed).
- **Done when:** users can say what they'd use it for in their own words, or you've learned it's the wrong problem.
- **Automation watch:**
  - First time: **Draft** for the mock-up (Claude builds it with the `prototype` skill). **Me** for running the sessions and summarizing reactions.
  - Note: how long each version took to build, and what feedback came up every time.
  - Agent: **M4 Reaction summarizer** (agent library) that turns session notes into "what to change next". *Draft*.
- **For RM analytics:** a pre-meeting client brief and a weekly opportunity list, built on sample clients.

---

## 1.7 Pick the first target and record today's numbers

- **Goal:** choose what to build first, and lock in the "before" numbers it will be measured against.
- **Why it matters:** without a baseline, you can't prove impact later, and the value model is guesswork.
- **Know first:**
  - Everything from 1.1 to 1.6.
  - Where the baseline numbers will come from (Power BI or Snowflake), and who owns them.
- **First time, step by step:**
  1. List the candidate targets, starting from the workflow map's "where AI fits" list. Score each on size (1.2), pain (1.3 and 1.4), user reaction (1.6), data readiness and risk.
  2. Recommend one, with the reason and the runners-up.
  3. For its measure, record today's number for the target users, the date, the source and the exact definition.
  4. Propose a comparison group: similar users who won't get the tool at first. (Finance agrees the method in 2.7; the final group is confirmed in 2.8.)
  5. Write a first rough value model with [X] placeholders, using memo section 2 as the pattern (the general value model template is still to be built: item W3 in the Open Items log).
  6. Build the gate pack: the outcome note, the sizing table, themes, the time map, the incentive note, reactions, the recommendation and the baseline.
- **Output:** the recommendation, the recorded baseline, the proposed comparison group, the first value model and the gate pack.
- **Done when:** the baseline is recorded with its source, and the gate pack is ready.
- **Automation watch:**
  - First time: **Me** for the choice and for recording the baseline by hand. **Draft** for scoring and the gate pack.
  - Note: which parts of the gate pack you copied from earlier sub-steps. That copying can be automated.
  - Agents:
    - **M5 Baseline recorder** (agent library; Power BI) that snapshots the measure for the target users on a schedule from today on (the pilot and comparison groups are confirmed in 2.8). *Auto*.
    - **M6 Gate pack drafter** (agent library) pulls each sub-step's outputs into one document. *Draft*.
- **For RM analytics:** feature wave 1 = pre-meeting briefs, meeting follow-ups, call notes into Salesforce and the weekly opportunity list (memo Step 1).

---

## The Discover gate

- **Who decides:** the sponsor, with the risk partner's agreement (in writing when the gate is clean; a meeting only if a criterion is contested or a decider asks for one; see the Product Machine).
- **Bring:** the gate pack from 1.7.
- **Go means:** the sponsor agrees on the target, the measure and today's baseline. The risk partner has no blocking concern.
- **No-go means:** go back to the sub-step that fell short (usually 1.2 or 1.7), or stop the project and record why.
- **Record:** the date the gate pack was ready, the decision date, the decision, who decided and any conditions, in the decision log.

---

## Discover automation review (do this at the gate)

Run the automation check from the Product Machine on every Me and Draft task,
using your first-time logs: cut first (should it exist, delete, simplify, make
it faster), then automate what's left (repeat? stable? safe alone?). Then update this shortlist and the Discover
table in `product-machine.md`.

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 1.0 | M1 Kickoff pack builder | Draft | Draft | Yes, M1 |
| 1.1 | M2 Outcome note drafter | Me | Draft | Yes, M2 |
| 1.2 | M21 Opportunity sizer | Draft | Draft | Yes, M21 |
| 1.3 | M3 Interview scheduler | Me | Auto ⚠️ | Yes, M3 |
| 1.3 | M20 Interview synthesizer | Draft | Draft | Yes, M20 |
| 1.4 | M22 Time-use analyst | Draft | Draft | Yes, M22 |
| 1.5 | None (stays with a person) | Me | Me | — |
| 1.6 | M4 Reaction summarizer | Me | Draft | Yes, M4 |
| 1.7 | M5 Baseline recorder | Me | Auto ⚠️ | Yes, M5 (ongoing mode) |
| 1.7 | M6 Gate pack drafter | Draft | Draft | Yes, M6 |

**First time** = how the task is done on the first project. **Aim for** = its kind in `product-machine.md`.

**Rule for this table:** a new agent gets a full spec (mission, inputs,
allowed actions, outputs, stop condition, proof it worked, person in charge)
in the agent library (or, for an agent only one project needs, in that project memo's Appendix A) before it's built, following "One job each"
in `product-framework.md`.

_Last updated: 2026-10-15_
