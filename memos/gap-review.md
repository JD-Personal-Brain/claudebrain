# Gap review: where we stand and what's missing

A full look at everything built so far, against two goals: (1) put the RM
plan in front of Andy, and (2) let one product manager run many AI products,
from first idea through live and improving. Written 2026-10-10 from the working
files in the repo. ⚠️ marks a guess about the bank.

## The short answer

- **One product, end to end: strong on paper.** The six steps, their gates, all 44 sub-steps of the field manual, the Auto / Draft / Me marking on every task, 39 agent specs and 22 controls add up to a complete process for one product. Nothing in it has been tried on real work yet.
- **Ready for Andy: not yet.** Three things are missing: my own read of the plan, a short version written for him, and something that shows what an RM would actually see.
- **Many products at once: the layer above the products is missing.** The machine runs one product well. What's missing is how new ideas come in, how they're ranked against each other, how many I can run at once, and when a live product is retired.
- **The biggest risk isn't a missing document.** We've built faster than I've reviewed: 10 pages are still unread, and none of the 39 agents or the process itself has been run once. More pages won't fix that. Reading them and doing a dry run will.

## Scorecard

| Area | Rating | Where we are | Proof |
|---|---|---|---|
| Six-step process for one product | Strong | Steps, gates, 44 sub-steps, first-time logs, automation check at every gate | Product Framework; Delivery Playbook |
| RM plan (the first worked example) | Strong draft, not reviewed | Memo v8 with agent specs and workflows. I've read only the summary's opening and plan table | RM Analytics Plan; review item V1 in Open Items |
| Governance and controls | Partial | 22 controls named. 11 of them have a stage the playbook doesn't cover yet, such as who checks that only approved AI models are used | Controls Catalog; work item W13 in Open Items |
| Automating the process | Partial | Every task is marked Auto, Draft or Me, and 39 agents are specified. None is built or tested. How much can run alone depends on whether the bank lets automations message people ⚠️ | Agent Library; bank question B22 in Open Items |
| Showing what an RM sees | Missing | The plan promises a working prototype in week 1, but there's nothing to show yet. The only prototype so far is the practice calculator | `prototypes/` holds only the calculator |
| A version written for Andy | Missing | The plan is written as my working plan, with internal labels. It doesn't say that credit comes next, though Andy named both | Work item W9; parked item P2 in Open Items |
| Portfolio layer (many products) | Missing | "Many projects at once" in the Product Framework is four short points with placeholder numbers. There's no intake, no ranking across products and no retirement rule | The word "portfolio" appears nowhere in the framework or playbook |
| Ready-to-fill templates | Missing | The brief, data contract, risk intake, gate pack, evidence pack and monitoring plan are described, but none exists as a template yet. The Draft agents need these to fill in | Agent Library, "reusable assets": three listed, none built |
| Operating rhythm and stakeholders | Partial | Who decides is clear for every step. There's no weekly or monthly calendar for me across products, no map of who approves what and how long it takes, and no plan for who hears what and how often | Not covered yet in the framework or playbook |
| Knowing the RM's real day | Partial | The Bank Business Briefing is done. My own notes on bankers' problems stopped at step 1 | Job Notes |
| After launch: running and retiring | Partial | Incident steps exist (who to call, how to pause). There's no support model, no runbook and no rule for retiring a product | Playbook steps 4.8 and 5.1 |

## For Andy: what's needed before sharing the RM plan

1. **Needed: read the plan and check one source myself.** Why: I can't defend a plan I haven't read, and the McKinsey numbers were checked only through search summaries. These are review items V1 and V2 in Open Items.
2. **Needed: an RM mock-up.** Clickable screens of the Monday opportunity list and the pre-meeting client brief, on made-up sample data. Why: it turns "AI insights for RMs" into something Andy can see in 30 seconds, and it proves the "prototype in week 1" promise. The prototype skill builds it in one session.
3. **Needed: an "Andy edition" of the plan.** Two to three pages in his terms: the problem, what RMs get, the 90-day plan, what I'd need from him, and one line that credit comes next on the same structure. No internal labels or file names. Why: the full plan is 700 lines written for me, and he'll read the first page. It's built from pages we already have.
4. **Optional: a worked value example.** The value model filled in with clearly labeled sample numbers, to show how the payback is calculated. Why optional: our rule is never to invent numbers. If we do it, every number is marked "illustrative, not the bank's" or comes from the bank's public reports.
5. **Optional: questions for Andy on one page.** The seven questions marked "Ask Andy now" in Open Items (B1 to B7). Why: sharing the plan with questions makes it a conversation rather than a pitch.

## For running many products: what's missing

1. **Needed: the portfolio layer.** One intake form for every new idea. A scoring rule that ranks ideas across products (value, effort, risk, data readiness). A capacity rule: how many products can be in the hands-on Discover and Define steps at once. A rule for when a live product moves to "run" mode or is retired. Why: without it, each product is managed well on its own, but nothing decides what gets my time next.
2. **Needed: ready-to-fill templates.** The documents every product produces: one-page brief, data contract, risk intake, gate pack, decision log, evidence pack, monitoring plan and release-readiness checklist. Why: a Draft agent can only fill in a template that exists, and templates are how every product ends up looking the same. The bank may have its own for some of these ⚠️. Build ours now and swap in theirs when I see them.
3. **Needed: a tracker design.** The fields every task carries (product, step, sub-step, kind, owner, due date, status, gate), written so it works in whatever tool the bank uses. Why: the reminders, the weekly status notes and the all-projects view all read from the tracker, and we don't know the bank's tool yet (bank question B23).
4. **Needed: an operating rhythm.** My week and month across all products: which meetings I run, which reports arrive on their own, and a gate calendar so no two gates land in the same week. Plus an approvals map: who signs what, typical turnaround ⚠️, and who to go to when a sign-off is stuck. Why: with many products, the calendar is the machine. Sign-offs are where products stall.
5. **Needed before calling the RM framework ready: close the control gaps.** The 11 controls with an uncovered stage (work item W13). Why: governance is the part the bank will check hardest.
6. **Optional for now: a stakeholder map and communications plan.** For each partner: what they care about, how often they hear from me and which automatic report they get. Why optional: who decides is already clear. This adds how to keep them on side.
7. **Optional for now: run and retire.** The support model, the incident runbook and the retirement rule. Why optional: needed before the first product goes live, not before Andy.

## Prove the machine works: a dry run

**Optional, but the best test we have.** Take one small, made-up product through
all six steps in a few sessions, using the templates, and with two or three
agents (such as the gate pack drafter) built as Claude skills. Log where it
breaks. Why: today the whole machine is a design. A dry run shows the weak
spots before the bank does, and gives me a real story to tell: "I've run this
end to end."

## What we don't need more of

- **More catalogs or building-block pages.** We have 17 designed pages. Reading them is the bottleneck, not building more.
- **Credit planning.** It waits until I say the RM framework is ready, as decided on 2026-10-09.
- **More bank facts from public sources** before the Q3 results come out on October 22, 2026.

## Recommended order

| # | What | Who | Size |
|---|---|---|---|
| 1 | Read the RM plan and check the McKinsey numbers | Me | About 1 hour |
| 2 | Build the RM mock-up | Claude, with my review | One session |
| 3 | Build the Andy edition, then share it when I say | Claude, then me | One session |
| 4 | Portfolio layer, templates and tracker design | Claude drafts, I review | Two to three sessions |
| 5 | Operating rhythm and approvals map | Claude drafts, I review | One session |
| 6 | Close the control gaps | Claude, with my yes on each change | One session |
| 7 | Dry run of the machine | Claude and me | Three to four sessions |

Sizes are rough guesses from how long similar work took this week.

## How this was checked

Read in full: the RM plan (memo v8), its one-page summary, Open Items, Job
Notes and the playbook's overview. Skimmed: the headings of every playbook
step, the agent library and the controls catalog, plus the ideas list.
Searched every plan and playbook file for portfolio, intake, retirement,
templates, runbook, rhythm and stakeholder words to confirm what's missing.
Not checked: the designed pages themselves (this review used their working
copies), and no fact about the bank was re-verified.

_Last updated: 2026-10-10_
