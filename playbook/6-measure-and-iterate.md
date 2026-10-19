# Step 6: Measure and iterate, the first time

**The question:** is it delivering the outcome, and what comes next?
**The gate:** each month (and at the end of each feature wave): keep, change or stop each AI product; each quarter: invest more, adjust or stop overall.
**Governance thread:** ongoing monitoring.

This step never really ends: it runs every month for as long as the product
lives. The last sub-step (6.6) improves the product machine itself, so the
next project starts more automated than this one did. Fill in the first-time
log (see the Product Playbook's opening page) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general practice, not from Associated Bank. Lines marked ⚠️ are
> guesses about the bank.

---

## 6.1 Track the measures on a live dashboard

- **Goal:** extend the pilot dashboard (built in 5.1) to all five kinds of measures, updated automatically.
- **Why it matters:** if numbers have to be pulled by hand each month, they'll be late, and decisions will be made without them.
- **Know first:** the measures sheet (2.7), the data sources, and who builds dashboards (Power BI). ⚠️
- **First time, step by step:**
  1. Extend the pilot dashboard to one page per measure kind: usage, quality, business impact, adoption, risk and controls, plus a cost page (spend on licenses and model use), which feeds the value model.
  2. Split **leading** measures (use, insights acted on, pipeline created, visible within weeks) from **lagging** ones (closed revenue, which takes months).
  3. Check each number against its source by hand once.
  4. Share it with the sponsor and user leaders, and set it to refresh automatically.
- **Output:** the live dashboard.
- **Done when:** it refreshes by itself and matches the sources.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which numbers you couldn't get automatically, and why.
  - Agent: the dashboard is **Auto** once built. Save it as a template for the next project.
- **For the RM Assistant:** a first read on closed revenue at about month 6, firming up over the following quarters (memo section 4).

---

## 6.2 Compare with the baseline and the comparison group

- **Goal:** show the product's real effect, not just activity.
- **Why it matters:** "people use it" isn't the outcome. Leaders fund what moves the number they care about.
- **Know first:** the baseline (1.7), the comparison group (2.8), and the method Finance agreed (2.7).
- **First time, step by step:**
  1. Each month, compare the pilot group with the comparison group on the main measure.
  2. Compare both with the baseline.
  3. Write three lines: what moved, by how much, and how confident you are.
  4. Have Analytics check the numbers before anyone sees them.
- **Output:** a monthly impact note.
- **Done when:** Analytics has checked it.
- **Automation watch:**
  - First time: **Draft**.
  - Note: the questions leaders asked about the numbers. Answer them in next month's note.
  - Agent: **M31 Impact analyst** (agent library). Analytics validates before reporting. *Draft*.
- **For the RM Assistant:** AI-sourced pipeline and revenue, pilot RMs against similar RMs.

---

## 6.3 Re-test after every change, and watch for drift

- **Goal:** catch quality slipping before users do.
- **Why it matters:** AI quality can slip over time, as data, models or prompts change ("drift"). Users stop trusting a tool after a few bad answers.
- **Know first:** the test set (3.6) and the monitoring plan (4.8).
- **First time, step by step:**
  1. Re-run the full test set after every change, and at least monthly.
  2. Compare the score with the last run and with the quality bar.
  3. Watch the live signals: rejection rate, guardrail blocks and user overrides. Each month, check the rule behind a sample of answers.
  4. If a threshold is crossed, follow the monitoring plan: fix, roll back or pause.
  5. Before any change goes live, decide whether it is a **material change** (Product Framework): if so, it goes back through step 4 first; if not, re-test, log it in the release notes and tell the risk partner.
- **Output:** the score trend and any alerts acted on.
- **Done when:** this runs on every change without anyone remembering to do it.
- **Automation watch:**
  - First time: **Draft**.
  - Note: what caused each drop.
  - Agent: **M32 Quality watchdog** (agent library) re-runs the test set and alerts. The product manager decides whether to fix or roll back. Aim for **Auto**.
- **For the RM Assistant:** watch RM rejections of insights; a rising rate is the earliest warning.

---

## 6.4 Hold the monthly keep / change / stop review

- **Goal:** a monthly decision on each AI product, based on evidence.
- **Why it matters:** without a regular decision, weak AI products linger and strong ones don't get more investment.
- **Know first:** the dashboard (6.1), the impact note (6.2) and quality trends (6.3).
- **First time, step by step:**
  1. Build a short pack: each AI product's use, quality and impact, plus the top user feedback.
  2. Recommend keep, change or stop for each one, with the reason.
  3. Send the pack to the sponsor; they decide in writing, with a 30-minute meeting only if a call is contested.
  4. Record the decisions and update the backlog.
  5. If the decision is stop: switch it off, tell users, update the model inventory, stop its ongoing agents and keep the logs as the bank's retention rules require ⚠️.
  6. Every third month, roll the monthly packs, the impact note (6.2) and the machine's measures (6.6) into a quarterly summary for the invest more / adjust / stop decision (M18).
- **Output:** the decisions, recorded, an updated backlog and, every third month, the quarterly summary.
- **Done when:** every AI product has a decision for the month.
- **Automation watch:**
  - First time: **Draft** for the pack, **Me** for the decision.
  - Note: what the sponsor looked at first. Put that at the top next time.
  - Agent: **M18 Monthly review pack drafter** (agent library) built from the dashboard and the impact note. *Draft*.
- **For the RM Assistant:** each feature wave's AI products reviewed separately.

---

## 6.5 Feed the next feature wave

- **Goal:** choose what comes next, and send it back through Discover and Define, quickly.
- **Why it matters:** the first release is a start. The value comes from steady feature waves.
- **Know first:** the backlog, the feedback themes, and what the sponsor wants next.
- **First time, step by step:**
  1. List the candidates: backlog items, ideas from users and the next lever from Discover.
  2. Rank them using the same scoring as 1.7.
  3. Take the top one through the **quick pass** (Product Framework): 2.3, 2.4, 2.5 and 2.7 always, everything else reused unless it changed, and gates 1 and 2 together in writing.
  4. Agree the next feature wave with the sponsor.
- **Output:** the next feature wave, agreed.
- **Done when:** the next feature wave has a scope and a date.
- **Automation watch:**
  - First time: **Draft**.
  - Note: how much of Discover and Define you could skip or reuse.
  - Agent: **M33 Improvement scout** (agent library) proposes and ranks candidates. The product manager and the sponsor decide. *Draft*.
- **For the RM Assistant:** the next standard AI products, such as early warnings and referral prompts in feature wave 2.

---

## 6.6 Improve the machine itself

- **Goal:** make the next project faster and more automated than this one.
- **Why it matters:** this is how one product manager ends up running many projects: each one leaves the machine better.
- **Know first:** the sub-step logs from every step (the full first-time log on the first project), and the automation review tables at the end of each playbook file.
- **First time, step by step:**
  1. Read back through the sub-step logs from steps 1 to 6.
  2. Total the time per step, work out each sub-step's wait index (calendar days from start to finish, divided by hours of real work), and mark the highest.
  3. Run the automation check on every Me and Draft task, cut first: decide what to delete, simplify or speed up (starting with the highest wait index). Record each deletion in the decision log with who agreed, and list which earlier deletions had to come back (if none did, we aren't cutting enough). Then, for each agent idea that passed the rest of the check, decide: build it now, later, or never.
  4. Record the machine's measures for this project (days from kickoff to pilot, days at each gate, releases per month in the pilot and the wait index; see "Measuring the machine" in the Product Machine), compare them with the last project, and add them to the one view of all projects.
  5. Update the Product Machine task tables (Auto, Draft or Me), the Product Framework and this playbook with what you learned.
  6. Write a one-page "what I'd do differently" note for the next project.
- **Output:** updated Product Machine task tables, Product Framework and playbook, a list of what was deleted, a build list of agents, the machine's measures for this project, and the lessons note.
- **Done when:** the next project can start from the updated files.
- **Automation watch:**
  - First time: **Me**.
  - Note: which agents you built, and how much time they saved on the next project.
  - Agent: **M19 Log summarizer** (agent library) that totals time, waits and each sub-step's wait index from the sub-step logs. *Draft*.
- **For the RM Assistant:** the RM project is the first run, so its logs set the starting point for every project after it.

---

## The Measure and iterate gate

- **Who decides:** the sponsor, with Finance confirming the impact numbers (in writing when the gate is clean; a meeting only if a criterion is contested or a decider asks for one; see the Product Machine).
- **Bring:** the monthly pack (each feature wave) or a quarterly summary (overall).
- **Each month (and at the end of each feature wave):** keep, change or stop each AI product.
- **Each quarter:** invest more, adjust or stop overall, based on results against the comparison group.
- **No-go means:** change the AI product and check again next month, or stop, record why, and retire the AI product (see 6.4).
- **Record:** the date the gate pack was ready, the decision date, the decision, who decided and any conditions, in the decision log.

---

## Measure and iterate automation review (do this at the gate)

Run the automation check from the Product Machine on every Me and Draft task,
using your first-time logs: cut first (should it exist, delete, simplify, make
it faster), then automate what's left (repeat? stable? safe alone?). Then update this shortlist and the Measure and iterate
table on the Product Machine page.

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 6.1 | None (the live dashboard template, an asset) | Draft | Auto | Asset: agent library |
| 6.2 | M31 Impact analyst | Draft | Draft | Yes, M31 |
| 6.3 | M32 Quality watchdog | Draft | Auto | Yes, M32 |
| 6.4 | M18 Monthly review pack drafter | Draft | Draft | Yes, M18 |
| 6.4 | None: the keep / change / stop decision stays with a person | Me | Me | — |
| 6.5 | M33 Improvement scout | Draft | Draft | Yes, M33 |
| 6.6 | M19 Log summarizer | Me | Draft | Yes, M19 |
| 6.6 | None: improving the machine stays with a person | Me | Me | — |

**First time** = how the task is done on the first project. **Aim for** = its kind on the Product Machine page.

_Last updated: 2026-10-18_
