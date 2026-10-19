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

## Saved prompts: the Prompt Library
Our core prompts, the ones we reuse and improve over time, live in the Prompt
Library (`prompt-library.md`): the use case kit, a full product memo, the
business briefing on the bank, the showcase prototype with live agents and copying a user group's work to the next group. Examples 1 to 3 above are here to teach the
template; the Prompt Library holds the prompts worth keeping.

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

_Last updated: 2026-10-19_
