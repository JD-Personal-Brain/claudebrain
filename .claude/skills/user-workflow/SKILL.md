---
name: user-workflow
description: Map how one user group at the bank works today, where each AI product fits into that work, and how the work changes ("today and with AI"). Use when the user says "map the RM workflow", "the credit workflow", "user workflow for X", "how do RMs work today", "where does this product fit in their day", or works on item W1 in the Open Items log. One designed page per user group, in that group's section of the Document Library.
---

# Map a user workflow: today and with AI

People at the bank care about their own work, not our product process. This
routine meets them where they are: it lays out how a user group works today,
marks where each AI product touches that work, and shows the work afterwards.
Many AI products fix one discrete step; the map makes clear which steps change
and which don't. *(Idea 41, approved 2026-10-14. Glossary term: **user
workflow**, not the RM plan's numbered workflows B1 to B9.)*

## 1. Gather what we already have
Read before asking the user anything (rule R6):
- **The group's plan and use cases:** for RMs, `memos/rm-analytics-framework.md` (the AI products, the seven core use cases, and Appendix B, workflows B1 to B9) and `memos/mckinsey-frontline-ai.md`; for credit, `memos/credit-market-scan.md` (the Credit Core Use Cases page).
- **What the group's week looks like:** Map 2 on the Workflow Maps (`designs/workflows-build.py`, "How an RM uses the product") shows an RM's week with AI only; the user's notes in `job-notes.md`; the bank's terms in `glossary.md` ("Bank terms to map").
- **The bank itself:** `memos/bank-business.md`, `tech-stack.md` (the tools the group works in).

## 2. Today: the work as it is
List the group's work as 6 to 10 stages, in the order it happens (for RMs, something like: plan the week, find opportunities, prepare for a meeting, meet the client, follow up, update the CRM, refer to a specialist, keep the client). For RMs, the stages must line up with the four stages of Map 2 on the Workflow Maps ("Find the opportunity or risk", "Prepare", "Meet and follow up", "Log it"): nest yours under them, or update Map 2 in the same change, so the same week never has two different stage lists. For each stage:
- **What they do**, in plain words, and **the tools they use** (from `tech-stack.md`).
- **Time:** hours per week if known, else [X]. Never invent a number.
- **Pain:** what's slow or missed, with its source (a memo line, McKinsey, my notes), or marked ⚠️ as a guess.
Everything about how *this bank's* people work is a guess until it's confirmed with them: mark it ⚠️ and add the question to step 5's list.

## 3. Where AI fits
For each stage, name every AI product from the plan that touches it (for credit, until a credit plan exists, use the proposed credit counterparts from the Credit Core Use Cases page, each marked ⚠️ proposal; never invent products), its core use case, and what exactly it changes (what the AI drafts or finds, what the person still decides). Then mark the stages **no AI product touches**, and say so plainly: we change only what's listed, not the whole flow. Check (where a plan exists): every AI product in the plan appears at one stage or more; if one doesn't fit anywhere, flag it.

## 4. With AI: the work afterwards
Rewrite only the changed stages: what the person does now, what the AI does, and who decides (assistive first: AI drafts or suggests, a person decides). Time saved per stage is [X] until measured (sub-step 1.7's baseline). End with one short summary: which stages change, which stay the same, and what that means for the group's week.

## 5. What to confirm with the group
List the guesses (every ⚠️) as questions for interviews and shadowing (playbook sub-steps 1.3 and 1.4). Add any the bank must answer to the Open Items log, under "Inside the bank", as the next B number, ending with "(from: <group> user workflow)". First check it isn't already there (for RMs, see the questions on how RMs are paid, the value model's inputs, whether RMs work mainly in Salesforce, and the playbook's ⚠️ guesses).

## 6. Show a sample, then build the page (rule R27)
1. Before the first page for any group, make a small sample of the layout from real content (for example, three stages with today → AI → with AI), send a screenshot, and wait for a yes. Later groups reuse the approved layout.
2. Build the page with the **designed-doc** skill. Working copy: `memos/<group>-user-workflow.md`.
3. In `designs/library.json`, replace the group's placeholder row ("RM user workflow: today and with AI", "Credit user workflow: today and with AI") with the real page (id, name, what, status "Waiting for review", url, source, and remove `"todo": true`), add its .html file to `PAGE_FILE` in `designs/library-build.py`, and add it to `designs/README.md`. Rebuild and republish the library.

## 7. Check it (rule R7)
- Every stage has a source or a ⚠️; every unknown number is [X].
- Where the group has a plan, every AI product in it appears at one stage or more (step 3's check).
- Words match `glossary.md` (rule R25): user workflow, AI product, core use case.
- `python3 .claude/skills/audit/check.py` and `node designs/render-check.js` both report 0 problems; look at the page's screenshot, top and bottom.

## 8. Record it
Update item W1 in the Open Items log (which group is done), NOW.md's "Where things stand", and run the **audit** skill before offering to merge (rule R18).
