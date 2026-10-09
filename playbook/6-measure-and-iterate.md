# Step 6: Measure and iterate, the first time

**The question:** is it delivering the outcome, and what comes next?
**The gate:** each wave, keep, change or stop each feature; each quarter, invest more, adjust or stop overall.
**Governance thread:** ongoing monitoring.

This step never really ends: it runs every month for as long as the product
lives. The last sub-step (6.6) improves the delivery machine itself, so the
next project starts more automated than this one did. Fill in the first-time
log (see `README.md`) for every sub-step.

> ⚠️ **How much to trust this.** Written 2026-10-09 from my framework, the RM
> memo and general practice, not from Associated Bank. Lines marked ⚠️ are
> guesses about the bank.

---

## 6.1 Track the measures on a live dashboard

- **Goal:** one dashboard showing all five kinds of measures, updated automatically.
- **Why it matters:** if numbers have to be pulled by hand each month, they'll be late, and decisions will be made without them.
- **Know first:** the measures sheet (2.7), the data sources, and who builds dashboards (Power BI). ⚠️
- **First time, step by step:**
  1. Build one page per measure kind: usage, quality, business impact, adoption, risk and controls (plus cost).
  2. Split **leading** measures (use, insights acted on, pipeline created, visible within weeks) from **lagging** ones (closed revenue, which takes months).
  3. Check each number against its source by hand once.
  4. Share it with the sponsor and user leaders, and set it to refresh automatically.
- **Output:** the live dashboard.
- **Done when:** it refreshes by itself and matches the sources.
- **Automation watch:**
  - First time: **Draft**.
  - Note: which numbers you couldn't get automatically, and why.
  - Agent: the dashboard is **Auto** once built. Save it as a template for the next project.
- **For RM analytics:** a first read on closed revenue at about month 6, firming up over the following quarters (memo Step 6).

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
  - Agent: **A18 Impact analyst** (Appendix A). Analytics validates before reporting. *Draft*.
- **For RM analytics:** AI-sourced pipeline and revenue, pilot RMs against similar RMs.

---

## 6.3 Re-test after every change, and watch for drift

- **Goal:** catch quality slipping before users do.
- **Why it matters:** AI quality can slip over time, as data, models or prompts change ("drift"). Users stop trusting a tool after a few bad answers.
- **Know first:** the test set (3.6) and the monitoring plan (4.8).
- **First time, step by step:**
  1. Re-run the full test set after every change, and at least monthly.
  2. Compare the score with the last run and with the quality bar.
  3. Watch the live signals: rejection rate, guardrail blocks and user overrides.
  4. If a threshold is crossed, follow the monitoring plan: fix, roll back or pause.
- **Output:** the score trend and any alerts acted on.
- **Done when:** this runs on every change without anyone remembering to do it.
- **Automation watch:**
  - First time: **Draft**.
  - Note: what caused each drop.
  - Agent: **A19 Quality watchdog** (Appendix A) re-runs the test set and alerts. The product owner decides whether to fix or roll back. Aim for **Auto**.
- **For RM analytics:** watch RM rejections of insights; a rising rate is the earliest warning.

---

## 6.4 Hold the monthly keep / change / stop review

- **Goal:** a monthly decision on each feature, based on evidence.
- **Why it matters:** without a regular decision, weak features linger and strong ones don't get more investment.
- **Know first:** the dashboard (6.1), the impact note (6.2) and quality trends (6.3).
- **First time, step by step:**
  1. Build a short pack: each feature's use, quality and impact, plus the top user feedback.
  2. Recommend keep, change or stop for each one, with the reason.
  3. Meet the sponsor (30 minutes) and decide.
  4. Record the decisions and update the backlog.
- **Output:** the decisions, recorded, and an updated backlog.
- **Done when:** every feature has a decision for the month.
- **Automation watch:**
  - First time: **Draft** for the pack, **Me** for the decision.
  - Note: what the sponsor looked at first. Put that at the top next time.
  - Agent idea: a **monthly review pack drafter** built from the dashboard and the impact note. *Draft*.
- **For RM analytics:** each wave's standard use cases reviewed separately.

---

## 6.5 Feed the next wave

- **Goal:** choose what comes next, and send it back through Discover and Define, quickly.
- **Why it matters:** the first release is a start. The value comes from steady waves.
- **Know first:** the backlog, the feedback themes, and what the sponsor wants next.
- **First time, step by step:**
  1. List the candidates: backlog items, ideas from users and the next lever from Discover.
  2. Rank them using the same scoring as 1.7.
  3. Take the top one through a **short** Discover and Define, reusing everything you already have.
  4. Agree the next wave with the sponsor.
- **Output:** the next wave, agreed.
- **Done when:** the next wave has a scope and a date.
- **Automation watch:**
  - First time: **Draft**.
  - Note: how much of Discover and Define you could skip or reuse.
  - Agent: **A20 Improvement scout** (Appendix A) proposes and ranks candidates. The PM and the sponsor decide. *Draft*.
- **For RM analytics:** the next standard use cases, such as call notes saved to Salesforce in wave 2.

---

## 6.6 Improve the machine itself

- **Goal:** make the next project faster and more automated than this one.
- **Why it matters:** this is how one PM ends up running many projects: each one leaves the machine better.
- **Know first:** the first-time logs from every step, and the automation review tables at the end of each playbook file.
- **First time, step by step:**
  1. Read back through the first-time logs from steps 1 to 6.
  2. Total the time per step, and mark where you waited longest.
  3. For each agent idea that passed the three-question check, decide: build it now, later, or never.
  4. Update the task tables in `product-framework.md` (Auto, Draft or Me) and this playbook with what you learned.
  5. Write a one-page "what I'd do differently" note for the next project.
- **Output:** an updated framework and playbook, a build list of agents, and the lessons note.
- **Done when:** the next project can start from the updated files.
- **Automation watch:**
  - First time: **Me**.
  - Note: which agents you built, and how much time they saved on the next project.
  - Agent idea: a **log summarizer** that totals time and waits from the first-time logs. *Draft*.
- **For RM analytics:** the RM project is the first run, so its logs set the starting point for every project after it.

---

## The Measure and iterate gate

- **Who decides:** the sponsor; Finance for the impact numbers.
- **Bring:** the monthly pack (each wave) or a quarterly summary (overall).
- **Each wave:** keep, change or stop each feature.
- **Each quarter:** invest more, adjust or stop overall, based on results against the comparison group.
- **Record:** the decisions in the decision log.

---

## Measure and iterate automation review (do this at the gate)

| Sub-step | Agent | First time | Aim for | Already specified? |
|---|---|---|---|---|
| 6.1 | Live dashboard (template) | Draft | Auto | New |
| 6.2 | A18 Impact analyst | Draft | Draft | Yes, Appendix A |
| 6.3 | A19 Quality watchdog | Draft | Auto | Yes, Appendix A |
| 6.4 | Monthly review pack drafter | Draft | Draft | New |
| 6.5 | A20 Improvement scout | Draft | Draft | Yes, Appendix A |
| 6.6 | Log summarizer | Me | Draft | New |

_Last updated: 2026-10-09_
