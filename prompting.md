# Prompting: how we write prompts

Claude loads this every session. Whenever Claude writes a prompt for me, or
helps me write one, it follows this page.

> ⚠️ **Source.** Based on Anthropic's official prompting guide, read on
> 2026-10-09. Anthropic updates it often, so re-check it at a weekly review now and then:
> - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
> - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
>
> Anthropic does not publish a fixed list of prompt "pieces". The template
> below is our own checklist, built on their advice.

## The golden rule (Anthropic's words)
> "Show your prompt to a colleague with minimal context on the task and ask
> them to follow it. If they'd be confused, Claude will be too."

## Anthropic's advice, in plain English
1. **Be clear and direct.** Say exactly what you want: length, format, limits. Number the steps when order matters.
2. **Explain why.** Give the reason behind a rule, and Claude applies it more sensibly.
3. **Show examples.** 3 to 5 good ones that differ from each other.
4. **Use tags to separate parts**, like `<context>` and `<example>`. Any clear names work; keep them consistent.
5. **Give a role.** One sentence, like "You are a product manager at a bank."
6. **Long documents first, the question last.**
7. **Say what to do, not what not to do.** "Write in short paragraphs" beats "don't use bullets."
8. **Ask for extra effort out loud** if you want Claude to go above and beyond.
9. **Big jobs: draft, check, improve.** Write a draft, review it against the goal, then refine.

## Fill-in-the-blanks template
Use the pieces you need. **Goal, Context and Output** matter most; add the rest for big or risky tasks.

**Long material (notes, documents, data)?** Put **Inputs first** and **Goal and Output last**, so Claude reads everything before it sees the request (tip 6). See Example 2.

```
Role:     You are a ...
Goal:     I want ... Done means ...
Context:  Background, who it's for, and why it matters ...
Inputs:   The document, data or link to use ...
Steps:    1. ... 2. ... 3. ...
Rules:    Do ... Keep it under ... Because ...
Examples: Here's one I like: ...
Output:   Give me ... in this form: ...
Tone:     One main feel, said specifically: "friendly but direct" ...
```

**Tone:** pick one main feel and describe it specifically, like "confident but
not salesy." Plain "professional" leaves Claude guessing. Skip it when tone
doesn't matter. *(From the Claude Mastery course, 2026-10-09.)*

## Example 1: a basic prompt
Uses 6 pieces. No Inputs or Steps, because there's no document and no set order.

```
Role:     You are a product manager at a commercial bank.

Goal:     Write 5 questions I can ask commercial bankers to find
          where they lose time each week. Done means I could use
          them in a 20-minute chat tomorrow.

Context:  I'm new to the team. Bankers are busy and skeptical of
          new tools, so the questions should feel like a
          conversation, not a survey.

Rules:    Use plain, everyday words, because bankers will tune out
          jargon. Keep each question to one sentence.

Example:  A question I like: "Walk me through what you did after
          your last client meeting."

Output:   A numbered list of 5 questions. Under each, one line on
          what it helps me learn.
```

## Example 2: the full framework
Uses all 8 pieces. The notes come **first** and the request (Goal and Output)
comes **last**, so Claude reads the material before it sees what to do (tip 6).
The `<notes>` tags mark where the notes start and end (tip 4). Step 5 is
"draft, check, improve" (tip 9).

```
Inputs:   <notes>
          [paste your interview notes here]
          </notes>

Role:     You are a product manager at a commercial bank.

Context:  The notes above are from my interview with a commercial
          banker about where they lose time. My boss will use the
          summary to decide which AI tool we build first, so the
          problems need to be clear and ranked.

Steps:    1. Read the notes and list every time-wasting task
             mentioned.
          2. Group similar tasks together.
          3. Rank the groups by hours lost per week, biggest first.
          4. For the top 3, say whether AI could realistically help.
          5. Check your draft against the Goal, then improve it.

Rules:    Use only what's in the notes, because my boss will act on
          this and made-up details would mislead them. If something
          is unclear, flag it instead of guessing. Use plain words.

Example:  A finding I like: "Call notes: about 3 hours a week
          typing up meetings into Salesforce. AI could draft them
          from the meeting recording."

Goal:     Using the notes above, write a 1-page findings summary for
          my boss. Done means they can read it in 2 minutes and see
          the top problems worth solving.

Output:   A heading, then the top 3 problems as short paragraphs,
          then one line: "Open questions to ask next time."
```

## Example 3: meeting notes into a client follow-up email
Ready to reuse: paste the notes and fill in the `[brackets]`. Notes come
first and the request last (tip 6). `[CHECK: ...]` marks anything unclear,
so nothing made up reaches a client.

```
Inputs:   <notes>
          [paste your meeting notes here]
          </notes>

Role:     You are an experienced relationship manager who writes
          clear, warm client emails.

Context:  The notes above are from my meeting with [client name,
          company] on [date]. The email goes from me to the client,
          so it must be accurate and sound like a real person wrote it.

Steps:    1. Pull out what we discussed, what we agreed, and who
             owes what by when.
          2. Write the email.
          3. Check it against the notes and fix anything that
             doesn't match.

Rules:    Use only facts from the notes, because the client will
          take anything I send as a commitment. If something is
          unclear (a date, a number, who owns a task), put
          [CHECK: ...] in the email instead of guessing.
          Keep it under 200 words, because busy clients skim.
          Use plain, friendly words and no jargon.

Goal:     Using the notes above, write a follow-up email I can send
          after a quick read. Done means the client knows exactly
          what happens next and who does it.

Output:   A subject line, then the email: a one-line thank-you,
          a short recap, a "Next steps" list (owner + date for each),
          and a closing line.
```

## Example 4: a full product memo (like the RM analytics memo)
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

Context:  The first use case is AI-powered analytics for relationship
          managers (RMs). Assume the goal is new revenue that more than
          pays for the tool, because that's my working assumption. The
          bank wants working versions quickly, so plan a standard base
          of use cases rolled out in waves, then iterate.

Steps:    1. Organize the plan by the six steps in <workflow>, using
             the write-up layout in <framework> for each step.
          2. Add a table showing where the plan covers each
             accountability in <job_description>.
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

Output:   Executive summary, outcome, value model, who decides, the six
          steps, project plan, risks, how the plan covers the role,
          and what I'd confirm first.
```

**For a different use case:** change the Context (the use case, its goal and any assumptions) and the user group named in the Rules. Everything else stays.

## Example 5: a business briefing on the bank (like the Bank Business Briefing)
Gathers the public facts about the bank's business and maps each revenue line
to my work. The saved files go in as Inputs, in tags (tip 4), and the request
comes last (tip 6). Step 7 is "draft, check, improve" (tip 9). Re-run it each
quarter when new results come out; the output is `memos/bank-business.md`.

```
Inputs:   <job_description> [job-description.md] </job_description>
          <framework> [product-framework.md] </framework>
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

## When the answer is off: ask for changes, don't start over
Never just say "try again" or "make it better": that tells Claude nothing.
Say what to keep and what to change, one thing at a time.
1. **First draft:** use the full template and expect a solid start, not perfection.
2. **Change the direction:** "Keep the structure. Replace the generic points with three real examples."
3. **Polish:** "The intro is too long. Cut it to two sentences."

*(From the Claude Mastery course, 2026-10-09.)*

## Which model to use
Pick the smallest model that does the job well. I choose the model when I
start a session; Claude can't switch its own. At the start of a big or unusual
task, Claude says in one line if a different model would suit it better.

1. **Small, fast jobs** (classifying, tagging, short summaries, bulk cleanup) → **Haiku**.
2. **Everyday work** where I want my limits to stretch (drafting, cleanup, quick back-and-forth) → **Sonnet**.
3. **Real reasoning, or a mediocre answer won't do** (memos, plans, designed docs) → **Opus 5.5**, the default on my paid plan.
4. **Opus really fell short on a hard, long-running problem**, and I'm willing to spend the usage → **Fable 5.1**, if my plan includes it.

Not sure? Stay on the default (Opus 5.5).

> Source: a decision rule I was sent (2026-10-09). Version numbers change
> often: check the model picker in the Claude app for the current names.

## Our house style (from my profile and rules)
Add these to prompts written for me, when they fit:
- Plain English; explain any technical word.
- Ask me one question at a time.
- Say clearly what's a guess and what I should verify.

## Before using a prompt, check
- [ ] Would a newcomer understand it? (golden rule)
- [ ] Does it say what "done" looks like, and the output format?
- [ ] Does each rule have a reason?
- [ ] If the feel matters, is the tone specific (one main feel)?

_Last updated: 2026-10-14_
