# Rules

One line each. Claude follows these every session.
Rules at Level 2 or higher go at the top.

- **R18 (Level 3).** Nothing is offered for merging into main until it passes the **audit** skill: checker, fresh reviewer, fixes, second reviewer. The audit is step 0 of every wrap-up. *(from L15)*
- **R7 (Level 3, automatic).** Check every change the way I will see it before saying it's done: for files, look at where the edit landed; for designed pages, run the render check on every page (`designs/render-check.js`: no empty tables, nothing cut off, no sideways scrolling, no stray marks) and look at screenshots that include the top and the bottom of each changed page. *(from L7, L7b, L7c, L7d, L19)*
- **R6 (Level 3).** Never ask me for something already saved in the repo. The startup hook updates this copy from main automatically; if it warns, tell me first. Before ever saying a file is missing, check origin/main. *(from L6, L6b)*
- **R13 (Level 3).** Write for me, not in shorthand. Short must never beat clear: reread every message as a newcomer before sending. Say what happened, what it means for me and whether I need to do anything. Name the exact step every time ("save a draft" or "merge into main"), never just "save to GitHub." *(from L10, L10b, L10c, L10d)*
- **R16 (Level 2).** Before writing anything, decide who reads it. If a person will read it (me included: memos, plans, manuals, playbooks, summaries), deliver it as a designed, branded page from the start, without being asked; the .md is only the working copy, and if a designed version exists, update it in place. Only files that only Claude uses (rules, skills, NOW.md, logs) stay plain. *(from L13, L13b)*
- **R8 (Level 2).** Every suggested or recommended action starts with a bold **Needed** or **Optional** label and a one-line reason, including answers to "should I...?" *(from L8, L8b)*
- **R3 (Level 2).** Keep momentum and stay on my real task. Answer my question first; for setup problems, fix what you can, give me at most one step, then get back to the work. Save drafts without asking; ask only before merging into main or something big. *(from L3, L3b)*
- **R2 (Level 3).** Keep anything I need to review tiny: about 5 lines and one question. This includes the final wrap-up message. *(from L2, L2b)*
- **R1.** Before explaining how a tool or process works, check it first, or say "I'm not certain." *(from L1)*
- **R5.** Stick to the goal I stated. If a new detail might change the direction, ask before switching. *(from L5)*
- **R9.** Before a big task, write a "done" checklist; at the end, show pass or fail for each item, with proof. *(from idea 9)*
- **R10.** After each finished stage of a big task, update NOW.md with what's done and the one next step. *(from idea 10)*
- **R11.** Before saying something follows a tip, rule or standard, check it against that rule's actual wording, point by point. *(from L9)*
- **R12.** When writing a prompt, build it from `prompting.md` (template pieces, a reason for each rule, long material first) and run its checklist before handing it over. *(from the 2026-10-09 prompting agreement)*
- **R14.** Work isn't safe until it's in main. If the startup check reports unmerged work, tell me first and offer to bring it in; at wrap-up, offer to merge right away. *(from L11)*
- **R17.** When I say yes to an idea, build its home in the same session with the **make-skill** skill: a new skill, a step in an existing skill, a rule with a test, or a one-off task on "What's next" or in the Open Items log. If there's no time, put it there right away, so an approval never sits only in `ideas.md`. *(from L14; strengthened 2026-10-09 with make-skill)*
- **R19.** Don't retry a fix that failed unless there's a new reason to expect it to work. Say what failed, why, and what's different this time; after two failed tries, stop and tell me. *(from idea 12)*
- **R20.** Before writing "not public", "not found" or a guessed date, re-check the sources already opened and run one search for it. If it's still missing, say where Claude looked. *(from L16)*
- **R21.** Before writing that a step, section or file covers something, open it and find the words. If they aren't there, write "not covered yet" so the gap shows. *(from L17)*
- **R22.** Never ask me to read or proofread reference pages (the Agent Library, Workflow Maps, Steps Catalog, Controls Catalog or any page built to look things up). Claude keeps them in line with the working files through the audit. My review list holds only decisions and what I've said I'll read. *(from L18)*
- **R23.** When a term, count or definition changes, search the whole repo for every old form (singular, plural and the number) and fix each hit before saying it's done. *(from L20)*

_Retired on 2026-10-09: R4 and R15, the rules about explaining approval pop-ups. They were training wheels from when I was new, and I asked for them to be removed. Their numbers are not reused._
