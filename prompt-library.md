# Prompt Library: our core prompts

The prompts we use again and again, kept in one place so we can find them, reuse
them and improve them over time. Each one is built from the Prompting Guide
(`prompting.md`): its template, a reason for every rule, long material first and
the request last. The Prompting Guide teaches how to write a prompt; this page
holds the ones worth keeping.

## How to use this page
- **To run a prompt:** copy it into a new session, fill in the `[brackets]`, and send it (leave any `{next group: ...}` as written; it names the group that comes after). Or just ask Claude by name, for example "run the use case kit prompt for RMs".
- **To improve one:** say what to keep and what to change ("When the answer is off" in the Prompting Guide). Claude updates the prompt here, raises its version number and adds a line to its "What changed" note.
- **To add one:** when a prompt is worth reusing, Claude asks whether to save it here.
- **Tip numbers** (tip 4, tip 6, tip 9) point to "Anthropic's advice, in plain English" in the Prompting Guide: tip 4 is tags, tip 6 is long material first, tip 9 is draft, check, improve.

| # | Prompt | What it gives me | Version |
|---|---|---|---|
| 1 | The use case kit | The standard set of pieces every use case has (a leader layer and a working layer), the use case measured against it, and the gaps fixed | 2 (2026-10-18) |
| 2 | A full product memo | A full product plan for a new use case, from my saved files | 1 (2026-10-09) |
| 3 | A business briefing on the bank | The Bank Business Briefing, rebuilt from public sources each quarter | 1 (2026-10-09) |
| 4 | A showcase prototype with live agents | A clickable prototype of a user group's AI assistant, with three agents running live on Claude, a guided tour and a video, built from our framework | 1 (2026-10-18) |

## Prompt 1: the use case kit (organize a use case, find its gaps, fix them)
**Version 2** (2026-10-18). First run: relationship managers (RMs).

Sets the standard set of pieces every use case should have, in two layers: a
**leader layer** I communicate from (for Andy and bank leaders) and a **working
layer** I and the team work from. It runs first on the RM work, where most of
the material already exists, so the kit is tested against real work before it's
copied to portfolio managers (PMs). It runs in two stages and stops between them
for my yes, because a new structure needs a sample before anything is built
(rule R27). The inputs are files in the repo, so Claude reads them itself; the
paths are listed in tags (tip 4) and the request comes last (tip 6). Stage 1
step 7 and stage 2 step 5 are "draft, check, improve" (tip 9).

```
Inputs:   <use_case_work>
          Everything already built for [relationship managers (RMs)]:
          [memos/rm-analytics-framework.md] (the full plan, with
          Appendix A agent specs and Appendix B workflows),
          [memos/rm-ai-reference.md] (RM Detail:
          every RM working file in one document), [memos/use-case-library.md]
          (the Use Case Library), [memos/mckinsey-frontline-ai.md], [memos/rm-analytics-audit.md],
          [memos/rm-analytics-market-scan.md], the three short pages
          [memos/rm-executive-summary.md], [memos/rm-assistant.md]
          and [memos/rm-plan.md], [Map 2 on the Workflow Maps
          (an RM's week with AI, built by designs/workflows-build.py)],
          the [RM product agents] on the Agent Library
          (designs/agents.html), and the [rm] section of
          designs/library.json (the section's id; portfolio managers'
          is credit)
          </use_case_work>
          <base> memos/role-workflow.md, product-framework.md (above all
          "How each step is written up" and "Projects, AI products and
          feature waves"), product-machine.md, playbook/, glossary.md
          </base>
          <decisions> open-items.md: every open item that mentions
          [RMs or the RM plan], and every closed decision (C) about it,
          with its date </decisions>
          <bank> memos/bank-business.md </bank>
          <how_i_work> me/profile.md, learning/rules.md </how_i_work>
          <workflow_routine> .claude/skills/user-workflow/SKILL.md
          </workflow_routine>

Role:     You are a principal product leader who has set up product
          portfolios at large regulated companies, and you're coaching
          a new Principal Applied AI Product Manager at a commercial
          bank. You're also good at organizing information, so that
          each fact has one home and each reader finds what they need.

Context:  I'm thinking through how I'd do the Principal Applied AI
          Product Manager job at Associated Bank (job-description.md). A use case is a whole
          area of work for one user group (glossary). I have a lot of
          work for the [RM] use case but no agreed answer to: what is
          the standard set of pieces every use case should have? I want
          that answer, the use case kit, so every use case we turn on
          starts from the same kit. The kit has two layers:
          - The leader layer: what I communicate from. Mainly for Andy
            (the hiring leader) and bank leaders deciding whether to
            back and fund the work. Short, in their terms, no internal
            labels.
          - The working layer: what I and the team work from day to
            day: plans, specs, workflows, measures, decisions.
          The [RM] use case goes first because most of its pieces
          exist. The kit will then be copied to {next group: portfolio managers
          (PMs)}, so it must be written generally, with the [RM]
          version as the worked example. I also want to learn: explain
          why each piece exists, so I could defend the kit to a
          product leader at the bank.

Steps:    STAGE 1: propose (change no existing files)
          1. Take stock. List every piece of [RM] work in
             <use_case_work>: what it is, who it's for, which layer it
             belongs to, where it lives (file, page, section), how
             current it is, and anything it repeats from another piece.
          2. Propose the kit. For each piece give: its name, the one
             question it answers, its reader, its layer, required or
             optional, its one home (which page owns it), and what it
             links to. Test each against two questions: does a leader
             need it to decide, or does the team need it to work? Cut
             anything that fails both (cut first, then add). Consider
             at least these, and add or drop any with a reason:
             the leader summary; the case for change (the user problem
             and the value); the user workflow, today and with AI
             (required, built with <workflow_routine>); the core use
             cases and the return profile of each; the AI products in
             feature waves; the value model; the plan through the six
             steps; who decides; measures and the dashboard design;
             risks and controls; agent specs; workflows; open
             decisions; a clickable mock-up; sources and market scan.
          3. Show how the layers connect: each leader-layer item links
             down to its exact section in the working layer (rule R30),
             and how the kit appears in the use case's section of the
             Document Library.
          4. Grade the [RM] work against the kit. For each piece:
             Have, Partly, Missing, Out of date or Repeated. Look hard
             for "Out of date": decisions closed after the plan was
             written (in <decisions>), changes to <base> since then,
             and wording in the glossary's retired-wording table.
          5. Rank the gaps: first what blocks the leader layer, then
             what blocks the team, then the rest. For each, say the
             fix, the effort (small, medium, large) and whether it
             needs a decision from me.
          6. Make a small sample of the leader layer's layout and of
             the library section, built from real [RM] content
             (rule R27).
          7. Check the draft against the Goal and the Rules, then
             improve it. Stop and wait for my yes.

          STAGE 2: build (only after my yes, and only what I approved)
          1. Fix the gaps one at a time, in the ranked order. Edit the
             working copy first, then rebuild the designed pages built
             from it.
          2. Ask me each decision as it comes, one at a time, with
             your recommendation.
          3. Write the kit itself down as a reusable template, so the
             {next group: PM} use case can start from it.
          4. Update the Document Library's [RM] section to match the
             kit.
          5. Run the audit, fix what it finds, save a draft to GitHub
             and tell me what would be merged. Don't merge.

Rules:    Change no existing files in stage 1; the only new thing is
          the review page, a temporary draft kept out of
          designs/README.md and the Document Library until stage 2,
          because I approve the structure before anything is built.
          Keep the order of work already agreed in <decisions> (for
          [RMs]: the [Elon mode review comes before the Andy
          edition (W3), and the workflow map is W2]) and say which
          open items the kit covers, because those are already
          planned.
          Give every fact one home and link to it from everywhere
          else, because copies drift apart.
          Respect closed decisions in <decisions> and don't reopen
          them, because I've already decided; if one looks wrong,
          say so once and leave it.
          Leave the {next group: PM} pages untouched and report anything you find
          in them once, labeled Optional, because they come after the
          [RM] work (rule R31).
          Don't add new pages, files or skills I haven't approved;
          propose them in stage 1, because I keep the system small.
          Use [X] for numbers we don't have, and treat outside figures
          (such as McKinsey's) as benchmarks, never our targets,
          because leaders will check every number.
          Cite a source for every outside fact and leave out any fact
          you can't source; mark your own judgment with ⚠️, because
          I need to know what's proven and what's your view.
          Use the glossary's words, one meaning each, because the
          audit fails on anything else.
          Keep the AI assistive (AI drafts or suggests, a named person
          decides), because the bank will require it.
          Write in plain English and explain any technical word,
          because I'm not a developer and leaders aren't either.

Goal:     Using everything above, give me the use case kit and the
          [RM] use case measured against it. Done means: after stage 1
          I can say in two minutes what every use case must have and
          why, which [RM] pieces are missing or out of date, and in
          what order we fix them; after stage 2 the [RM] use case
          matches the kit, and the kit is ready to copy to {next group: PMs}.

Output:   Stage 1: one designed review page (the temporary draft)
          with five parts:
          1. The kit (one table: piece, question, reader, layer,
             required or optional, home)
          2. Why each piece exists (two or three lines each, so I
             learn)
          3. How the layers connect (a simple map)
          4. The [RM] work graded against the kit, and the ranked gaps
          5. The samples, and the decisions I need to make
          Then a chat message of about 5 lines with the page link and
          one question: my first decision.
          Stage 2: a short report per gap fixed (pass or fail, with
          proof), then the audit result and what would be merged.

Tone:     A senior product leader coaching a peer: direct and clear,
          explaining the why, no selling.
```

**For the next use case:** change every `[bracket]` from the RM version to the
new one: the user group, its files in `<use_case_work>`, its open items and its
section in the library (portfolio managers' section id is `credit`). Change each
`{next group: ...}` to the group after it, or delete those words if none is planned. In stage 1, start from the agreed kit instead of proposing one, and
only grade, rank and fix.

**What changed:** version 1, first written 2026-10-17. Version 2 (2026-10-18): the inputs list the three short RM pages and RM Detail, and the kit is now agreed (C50): three short pages for people (an executive summary, the product, the plan) plus one detail document for AI; for the next use case, start from that kit.

## Prompt 2: a full product memo (like the RM Assistant's full plan)
**Version 2** (2026-10-18).

Builds a plan for a new use case from my saved files. The five files go in as
Inputs, in tags (tip 4), and the request comes last (tip 6). Step 4 is
"draft, check, improve" (tip 9). Expect a strong first draft: the RM memo took
7 rounds, so follow up with an audit against `memos/role-workflow.md` and `product-framework.md`, then a fix round.

```
Inputs:   <job_description> [job-description.md] </job_description>
          <workflow> [memos/role-workflow.md] </workflow>
          <framework> [product-framework.md] </framework>
          <tech_stack> [tech-stack.md] </tech_stack>
          <my_notes> [what the hiring leader told me] </my_notes>

Role:     You are a Principal Applied AI Product Manager at a
          commercial bank, writing for its business and risk leaders.

Context:  The first use case is The RM Assistant: one personal AI
          assistant for each relationship manager (RM), with limits on
          its jobs, workflows, data and controls, and capabilities added
          feature wave by feature wave. Assume the goal is new revenue
          that more than pays for the tool, because that's my working
          assumption. The bank wants working versions quickly, so plan
          for speed, paced by what really blocks us.

Steps:    1. Write the six steps in <workflow> as one table, the
             layout in <framework>; link to what it already says
             instead of repeating it.
          2. Mark every fact about the bank (its people, data, tools,
             policies) as an assumption to confirm.
          3. Use only tools named in <tech_stack>.
          4. Draft it, check it against the Goal and the checklist,
             then improve it.

Rules:    Use [X] placeholders, never invented numbers, because leaders
          will check them. Cite a source for every outside fact, so it
          can be verified. Keep the AI assistive (AI suggests, the RM
          decides), because the bank will require it. Plain English.

Goal:     Using everything above, write a memo on how I'd deliver this
          first use case. Done means a business leader could read the
          summary in 2 minutes and approve a pilot.

Output:   Outcome, value model, who's involved, how the work flows
          (one table), how we deploy AI, project plan, risks, what
          I'd confirm first, Appendix A (agents) and Appendix B
          (workflows). The short pages for people are built from it.
```

**For a different use case:** change the Context (the use case, its goal and any assumptions) and the user group named in the Rules. Everything else stays.

**What changed:** version 1, written 2026-10-09 as Example 4 in the Prompting Guide; moved here 2026-10-17. Version 2 (2026-10-18): built around one product with capabilities, the six steps as one table, bank facts marked as assumptions, and the output matching the RM full plan (memo v11); the job-description table was dropped (the Product Framework maps it).

## Prompt 3: a business briefing on the bank (like the Bank Business Briefing)
**Version 1** (2026-10-09).

Gathers the public facts about the bank's business and maps each revenue line
to my work. The saved files go in as Inputs, in tags (tip 4), and the request
comes last (tip 6). Step 7 is "draft, check, improve" (tip 9). Re-run it each
quarter when new results come out; the output is `memos/bank-business.md`.

```
Inputs:   <job_description> [job-description.md] </job_description>
          <value_model> [section 2, "The value model", of
          memos/rm-analytics-framework.md] </value_model>
          <tech_stack> [tech-stack.md] </tech_stack>

Role:     You are a bank analyst who also knows how commercial
          bankers work day to day, briefing a new product manager.

Context:  I'm going after the Principal Applied AI Product Manager
          role at Associated Bank, which sits in [Corporate and
          Commercial Banking]. I need one business picture of the
          bank, so every AI product I plan ties to a real revenue
          line and I can say where the return comes from. Business
          and risk leaders may read it, so it has to hold up with
          people who know the bank well.

Steps:    1. Gather from public sources, in this order: the latest
             annual and quarterly reports (10-K, 10-Q), the latest
             earnings release and investor presentation, the
             earnings call, the bank's own commercial web pages,
             then trade press for recent news.
          2. Describe the whole bank briefly: size, footprint,
             reporting segments, and how it earns money (interest
             income against fee income).
          3. Go deep on [Corporate and Commercial Banking]: who it
             serves, its units, every product and service, its
             specialty industries, its leaders and its growth plan.
          4. List each revenue line in that business. For each one:
             how it earns money, its size and trend, who sells it,
             and what limits its growth today.
          5. Map each revenue line to the four outcomes in
             <job_description> (revenue workflows, banker capacity,
             operating efficiency, adoption) and to the terms of
             <value_model>. Say which lines AI work could move
             most, and why.
          6. List what public sources can't answer and I must
             confirm inside the bank.
          7. Draft it, check every number against its source and
             against the Goal, then improve it.

Rules:    Give every number its period and a link to its source,
          because leaders will check them.
          Write [X], never an estimate, where no public number
          exists, because a made-up figure would mislead. The
          value model's inputs (win rate, revenue per win) are
          internal, so expect them to stay [X].
          Mark your own conclusions with ⚠️ and keep them apart
          from facts, because I need to know what the bank said
          and what you inferred.
          If a page won't open, say so and leave the gap, because
          filling it from memory risks out-of-date facts.
          Say when an acquisition distorts a comparison (American
          National closed on April 1, 2026), because growth
          across that date isn't organic.
          Use public information only, because nothing non-public
          about the bank belongs in my files.
          Use plain English and explain each banking term the
          first time, because I'm new to commercial banking.

Goal:     Using everything above, write a business briefing on
          Associated Bank, focused on [Corporate and Commercial
          Banking]. Done means that after a 2-minute read of the
          summary I can name every revenue line in that business,
          say roughly how big it is, and point to the AI work
          that could move it.

Output:   1. Summary (5 lines)
          2. The bank at a glance
          3. How the bank earns money
          4. [Corporate and Commercial Banking] in depth
          5. Revenue lines (one table)
          6. Alignment map: revenue line × job outcome × value
             model term
          7. Strategy and what's changing
          8. Risks and limits
          9. To confirm inside the bank
          10. Sources, with dates
          Stamp it "as of [date], through [latest quarter]". Save
          the working copy as memos/bank-business.md, then make
          the designed page and add it to the Document Library.

Tone:     An analyst's briefing: factual and direct, no selling.
```

**For a different part of the bank:** change the `[brackets]` (for example, to Community, Consumer, and Business). Everything else stays.

**Tip from the first run (2026-10-09):** the annual report is too long to open in one go. The segment's own results are in the quarterly report's "Segment Reporting" note.

**What changed:** version 1, written 2026-10-09 as Example 5 in the Prompting Guide; moved here 2026-10-17.

## Prompt 4: a showcase prototype with live agents (like the RM Assistant Prototype)
**Version 1** (2026-10-18). First run: relationship managers (RMs).

Builds a clickable prototype of a user group's AI assistant to show bank leaders
we can turn the plan into working code: three agents running live on Claude, a
guided tour and a short video for first-time users, and the code kept the way a
real team would keep it. It is a showcase, not the product: the real product
comes from the six steps after Discover. The inputs are files in the repo, so
Claude reads them itself; they go first and the request comes last (tip 6).
Step 9 is "draft, check, improve" (tip 9). Once I say yes to this prompt, Claude
runs it end to end without stopping to ask, and reports back at the end.

```
Inputs:   <product> [memos/rm-assistant.md: the product, its limits
          and its wave 1 capabilities] </product>
          <agents_and_workflows> [Appendix A (agents A1, A2, A3) and
          Appendix B (workflows B1 to B4) of
          memos/rm-analytics-framework.md] </agents_and_workflows>
          <controls> [playbook/controls.md] </controls>
          <framework> [product-framework.md: AI principles, the five
          kinds of measures, the quality bar] </framework>
          <workflow> [memos/role-workflow.md] </workflow>
          <tech_stack> [tech-stack.md] </tech_stack>
          <glossary> [glossary.md] </glossary>
          <prototype_rules> [the prototyping agreement in NOW.md and
          .claude/skills/prototype/SKILL.md] </prototype_rules>

Role:     You are a principal applied AI product manager who also
          writes production-quality front-end code, building a
          showcase for a commercial bank's executives.

Context:  I'm interviewing for Principal Applied AI Product Manager
          at Associated Bank. The executives who see this decide
          whether to hire me to deploy AI. They must come away
          thinking: this person can take the idea of [an RM's
          work], package it as working code with live AI agents,
          govern it, and get people to use it. It is a prototype
          to prove we can build, not the product: the real one
          comes from Discover onward, so every fact about the
          bank stays an assumption. Viewers may be senior and
          short of time, and may open it with no one to explain it.

Steps:    1. Read the inputs. Write a "done" checklist (below,
             plus anything you add) before building.
          2. Build The [RM] Assistant's wave 1 screens: [the Monday
             opportunity list, the pre-meeting client brief and
             the meeting follow-up], for one made-up [RM] persona
             with a book of about 12 made-up clients.
          3. Run three agents live on Claude through the page's
             "ask Claude" feature (the artifact `sample`
             capability), each matching its spec in
             <agents_and_workflows>: [A1 Signal finder, written as
             simple, explainable rules in code (control K22), with
             A2 Insight writer explaining each signal in plain
             English; A3 drafting the brief; A3 drafting the
             follow-up email and call note]. Show each agent
             working: its steps, the data it read and its sources.
          4. Feed the agents from one real public data source as
             well as the sample data (for example, public company
             filings or economic data), to show a live outside
             feed. First test which sources the published page
             can reach; if none, use a dated saved copy and say so
             on screen.
          5. Show the controls working on screen: the person
             decides (K1), read-only until the [RM] approves (K2),
             users see only their own clients (K4), every answer
             shows its source (K7), guardrails (K8: it refuses a
             credit decision or a price), the audit log (K12),
             consent before recording (K24) and agents stop rather
             than guess (K25). Add one-click feedback on every
             output and a small "product manager view" with the
             five kinds of measures, filled from this session.
          6. Build a guided tour that plays like a video on first
             visit (captions, highlighted steps, under 2 minutes,
             skippable, replayable), then record it as a video
             file. If live AI isn't available to a viewer, offer a
             replay of a recorded run, clearly labeled.
          7. Keep the code the way a real team would: source files
             under prototypes/[rm-assistant]/ with a README (how
             it works, how to run, how to change it), a build
             script that writes prototype-v1.html, a changelog,
             and automated tests that click through every
             checklist item with Claude stood in by a test double.
          8. Publish it as a designed page, add it to the Document
             Library in the [RM] section, and save a draft to
             GitHub.
          9. Draft it, check it against the Goal and the
             checklist, as an executive and as a first-time [RM],
             then improve it. Run the audit at the size it picks.

Rules:    Use made-up clients, people and numbers, marked "sample
          data" on screen, because nothing real or non-public may
          appear. Use the house style and no bank logo or brand
          colors, and label it a concept by me, because the page
          must never look like the bank's own product.
          Keep the AI assistive: it drafts and suggests, and the
          [RM] approves anything saved or sent, because the bank
          will require it (K1, K2). Every number an agent states
          must come from its inputs, because a made-up figure is
          the top risk in banking AI. Use the words in <glossary>
          and name agents, workflows and controls by their
          numbers, so the prototype visibly ties to the plan.
          Make your own best call on every open choice and keep
          going, because I've asked for the full build without
          check-ins; list each call in the final report. Say
          plainly anything you couldn't test (such as a live
          agent run inside claude.ai), because a claim I can't
          trust is worse than a gap. Plain English on screen.

Goal:     Using everything above, build the [RM] Assistant
          Prototype. Done means an executive with no one beside
          them opens one link, watches a short tour, runs three
          live agents on a sample client and, in 5 minutes,
          understands what the assistant does, how it stays safe
          and how we'd get [RMs] to use it.

Output:   The published page, the video file, the code in
          prototypes/[rm-assistant]/ and a draft on GitHub. Then a
          short report: the scope, the done checklist with pass or
          fail and proof for each item, the calls I made, what I
          couldn't test, and one question for me.

Tone:     Confident and clear, like a product demo: impressive by
          showing, never by selling.
```

**The done checklist it starts from** (step 1 adds to it):
1. The tour starts on first visit, runs under 2 minutes, and can be skipped and replayed.
2. Each of the three agents runs on a sample client and shows its steps, inputs and sources.
3. The outside data source shows a live or dated value, labeled with where it came from.
4. Asking for a credit decision or a price is refused, and every agent action lands in the audit log.
5. Nothing is saved or sent until the persona clicks approve.
6. Every screen says "sample data", and nothing looks like the bank's own product.
7. The page passes the render check at laptop and phone widths, with screenshots of the top and bottom.
8. The automated tests pass; the video file plays; the code has a README, a build script and a changelog.

**For a different user group:** change the `[brackets]` (for portfolio managers: their assistant, their wave 1 capabilities and their agents). Everything else stays.

**What changed:** version 1, written 2026-10-18.

_Last updated: 2026-10-18_
