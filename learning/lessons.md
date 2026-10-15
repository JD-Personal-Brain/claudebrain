# Lessons

The full story of each mistake. Newest at the top.
Each lesson produces one rule (in rules.md) and one test (in tests.md).

If a mistake happens again, its fix moves up a level:
1 = a rule · 2 = a sharper rule, moved to the top · 3 = a required step in a skill

---

### L28 · 2026-10-15 · Queued follow-up work I hadn't asked for
- **What happened:** I said yes to four decisions in the Open Items log (the four open decisions, now closed items C30 to C33) and wanted them recorded. Claude also wrote "the RM plan update is next" into the log, the RM Core Use Cases page and NOW.md, and was about to ask which feature waves to use. I had to say: I didn't ask for that next, just update those four.
- **Root cause:** Claude treated a decision as an order to start the work it implies, and wrote that next step into my files as if I'd agreed it. It confused recording a decision with planning what follows it.
- **Fix:** do exactly what I ask. When a decision implies more work, don't add it to the log, NOW.md or "What's next", and don't start it: at most, mention it once in the reply as **Optional** and let me choose.
- **Rule:** R31 · **Test:** T41 · **Level:** 1 · **Times it happened:** 1

### L27 · 2026-10-15 · Suggested moving content when I wanted links to the detail
- **What happened:** I asked how to improve the integration between the Product Workflow, the Workflow Maps and the Steps Catalog. Claude's main suggestion was to move the clickable map onto the Product Workflow page, and it built a sample of that. I had to explain: I wasn't asking to copy information across pages; the Product Workflow page summarizes, and from it I should be able to click down to the deeper layer.
- **Root cause:** Claude read "integration" as merging or moving content, not as navigation between layers. It went straight to a restructure instead of first asking what was missing for me as a reader: a way to get from the summary to the detail.
- **Fix:** when I ask to connect or integrate pages, the first answer is links: every item on a summary page links to its detail (the exact card or section), and each page links to the related ones. Content stays in its one home; moving or copying content between pages is suggested only if I ask for it.
- **Rule:** R30 · **Test:** T38 · **Level:** 1 · **Times it happened:** 1

### L26 · 2026-10-14 · A name I asked for wasn't applied everywhere
- **What happened:** I asked for the field manual to be called "The Delivery Playbook" (my first message hinted at it too). Claude changed only the places with no "the" in front, so pages still said "the Delivery Playbook", and I had to ask again.
- **Root cause:** Claude treated the rename as a narrow find-and-replace on one spelling and checked only that spelling, not every form a reader would see on the pages. Rule R23 (search every old form when a term changes) already covered this, so the rule failed: a repeat of L20 and L24.
- **Fix:** rule R23 moves to Level 3. When I set a name, Claude adds it to the audit checker's page-name check (check 11), which fails on any other form in the working files and on the built pages, and confirms on the rendered pages before saying it's done. The checker now does this for every old page name. Same day, the Document Library still described the pages with synonyms ("the steps, the rules, the operating model, the field manual") instead of their names, and I had to point it out: after any rename, reread every description of the renamed pages, not only the names.
- **Rule:** R23 · **Test:** T37 · **Level:** 3 · **Times it happened:** 3 (with L20, L24)

### L25 · 2026-10-14 · Moving content between pages dropped some of it
- **What happened:** while reorganizing the four "How we deliver" pages, I shrank the playbook's agent section and the agents' intro (including the note that none of them is built yet) stopped showing on any page. I also put the Usage and Adoption examples under the wrong measures. The audit's first reviewer caught both before anything was merged.
- **Root cause:** I checked the new pages for duplication and broken links, but never compared every removed line with where it landed. Moving content was treated like rewriting it.
- **Fix:** when content moves from one page or file to another, list every removed line and find each one in its new home (or record that it was cut on purpose and why) before the work goes to review; facts copied into a new table are checked against their source.
- **Rule:** R29 · **Test:** T36 · **Level:** 1 · **Times it happened:** 1

### L24 · 2026-10-14 · A merged branch kept an item number from the old numbering
- **What happened:** I merged the bank news scout branch, which was written before the Open Items log was renumbered. I shifted the item numbers only in the files that clashed, so the scout's new news log still said "W4" for the Briefing re-run (by then W12, later W13). The audit's reviewer caught it as a Must fix.
- **Root cause:** rule R23 says to sweep the whole repo when numbers change, but I swept only the files I was resolving. The files the branch added never clashed, so I never looked at them. Rule R23 failed, so this is a repeat of L20.
- **Fix:** rule R23 is sharper and moves to the top: after any renumbering, and whenever a branch written under older numbers is merged, search every file (including files the branch adds) for each item number and check that each one still points to the right item.
- **Rule:** R23 · **Test:** T27 · **Level:** 2 · **Times it happened:** 2

### L23 · 2026-10-14 · Built a whole new layout without showing a sample
- **What happened:** You asked for an index at the top of the Document Library. I built and published a full version (three dense columns of 121 links) without showing you a sample first. You called the layout awful. The next two versions, each shown as a small sample first, were approved.
- **Root cause:** your profile already said "show a small sample before building a whole page in a new look" (from 2026-10-13), but it was a preference line, not a rule or a step in the routine I follow for designed pages, and I read "new look" as colors and style only, not a new layout.
- **Fix:** rule R27, at the top of the rules: any new layout, look or structure for a page gets a small sample (a screenshot) and your yes before it's built or published. The designed-page routine (the designed-doc skill) now has this as a required step.
- **Rule:** R27 · **Test:** T32 · **Level:** 2 (the profile line already failed once) · **Times it happened:** 1

### L22 · 2026-10-14 · Kept a rule you never set, then worked around it
- **What happened:** The audit found three numbers used twice in the Open Items log under the old numbering (one for an open item and a closed item's history note; two others each in two closed items' history notes). I "marked" the problem instead of fixing it, citing the log's promise that a number never changes. You corrected me twice: when something is wrong we fix it right, and you never asked for fixed numbers. You want the items listed by priority, with numbers that can be swapped and added.
- **Root cause:** I wrote "every item keeps a number that never changes" into the log myself when I built it (2026-10-09), then treated my own design choice as your rule. Because nobody checked the numbering, it had drifted out of order and been reused.
- **Fix:** the log is renumbered in priority order within each kind (V1 is the first thing to read, W1 the first piece of work, D1 the first decision), with a new "Now" section at the top. Every file that points to an item was updated. The "never changes" wording is gone from the log, NOW.md and the glossary. The audit checker now fails if a kind's numbers don't run 1, 2, 3 in order down the page.
- **Rule:** R26 · **Test:** T31 · **Level:** 1 · **Times it happened:** 1

### L21 · 2026-10-14 · A new page name used a glossary word with a new meaning
- **What happened:** While reorganizing the Document Library, I renamed "Credit Market Scan" to "Credit Core Use Cases". The glossary defines "core use case" as one of the RM plan's seven lines, so the new name gave the word a second meaning. The audit's alignment sweep caught it as a Must fix.
- **Root cause:** rule R23 makes me sweep for old wording after a rename, but nothing made me check that the words in a new name mean what the glossary says. I picked the name for how it read, not against our definitions.
- **Fix:** before naming or renaming a page, section or item, check each key word against `glossary.md`. If the new use differs, either pick another word or update the glossary definition in the same change. This time the glossary now says core use cases cover RM and credit (through each one's credit counterpart), and adds "credit counterpart", "use case" and "user workflow".
- **Rule:** R25 · **Test:** T30 · **Level:** 1 · **Times it happened:** 1

### L20 · 2026-10-10 · A rename reached only the files I was editing
- **What happened:** We decided the RM plan has seven core use cases, with AI products under them. The deep audit still found "five core use cases" in the Document Library, the McKinsey page and the Open Items log, about 40 places where "use case" or "feature" still meant one AI product, and a memo line saying each core use case "becomes one line of the value model" when the value model has no such lines.
- **Root cause:** I changed the words where I was working and never searched every file for the old forms. I also wrote what a section would contain without opening it (rule R21).
- **Fix:** When a term, count or definition changes, search the whole repo for every old form (singular, plural, number) before calling it done, and fix or deliberately keep each hit.
- **Rule:** R23 · **Test:** T27 · **Level:** 1 → 2 (see L24) · **Times it happened:** 2

### L19 · 2026-10-10 · The bottom of two RM design-page parts was cut off
- **What happened:** I added a sentence to the team-agents table on the RM design page. Two parts grew taller than their frames, so their bottoms were cut off when you looked. This is the fourth rendering failure (empty tables in L7c, stray marks in L7d, now cut-off bottoms).
- **Root cause:** rule R7 relied on me remembering to render, and the audit rendered only pages I thought had changed, checking only some kinds of failure. A text edit to a canvas part changes its height, and nothing measured it against its frame.
- **Fix:** an automatic render check (`designs/render-check.js`) now renders every designed page and canvas part in every audit and fails on empty tables, cut-off parts, sideways scrolling, stray Markdown or a blank render. Audit step 2.2 requires it to report 0 problems, and the designed-doc skill runs it too. Tested: with the old frame size it reports the cut-off.
- **Rule:** R7 · **Test:** T7 · **Level:** 3 (now an automatic check) · **Times it happened:** 5

### L18 · 2026-10-10 · Asked me to read reference pages Claude should check itself
- **What happened:** The Open Items log listed the Agent Library, Workflow Maps, Steps Catalog and Controls Catalog as "reviews waiting on me", and the scorecard pointed me at them. I should never be asked to read these. They're reference pages built from the working files, and the 19-versus-39 agent count mismatch showed nobody was keeping them in line.
- **Root cause:** Claude treated every page it built as something for me to review, which made me the checker for Claude's own consistency work. Reference pages are Claude's to keep correct, through the audit, not mine to proofread.
- **Fix:** Building-block and reference pages are never put on my review list. Claude checks them against the working files in every audit and fixes drift itself. The audit skill now has a required alignment sweep (step 2b) that checks every core document against the four reference pages, not only the files a session changed, because the 19-versus-39 mismatch sat in two files no session had touched. My review list holds only what I must decide on or have said I'll read (for example, the RM plan).
- **Rule:** R22 · **Test:** T26 · **Level:** 1 · **Times it happened:** 1

### L17 · 2026-10-09 · Pointed controls at playbook steps that don't cover them
- **What happened:** In the new Controls Catalog, Claude wrote where each control is set, built, proved and watched. Two audits in a row found references the playbook doesn't support: about ten in the first pass, and six more in the controls Claude added while fixing the first.
- **Root cause:** Claude filled in each step number from where the control would logically belong, without opening that step and reading what it says.
- **Fix:** Before writing that a step covers something, open the step and find the words. If they aren't there, write "not covered yet" so the gap shows. The catalog builder also fails now if a control names a step that doesn't exist.
- **Rule:** R21 · **Test:** T25 · **Level:** 1 · **Times it happened:** 1

### L7d · 2026-10-09 · Stray underscores at the top of two designed pages
- **What happened:** The Bank Business Briefing went into main with its first line wrapped in underscores (Markdown for italics that the page builder doesn't handle across two lines). The new Open Items page had the same fault. Claude caught it only when it looked at the top of the Open Items page.
- **Root cause:** For the briefing, Claude checked one screenshot from the middle of the page, never the top. Rule R7 already covers this, so the rule failed again.
- **Fix:** An automatic check: the audit checker now fails if any built page shows a stray underscore at the start or end of a line. And the screenshot Claude looks at must include the top of the page.
- **Rule:** R7 · **Test:** T7 · **Level:** 3 (automatic check added) · **Times it happened:** 4

### L16 · 2026-10-09 · Said a number wasn't public when a source I'd already opened had it
- **What happened:** In the first draft of the Bank Business Briefing, Claude wrote that the bank publishes fee lines for the whole bank only, and guessed that Q3 results were "probably due in late October." The audit found the segment's fee lines in the annual report page the briefing already cited, and a press release giving the date (October 22, 2026).
- **Root cause:** Claude wrote "not public" and "not found" from what it remembered seeing, without going back through the sources it had opened or running one search for the missing fact.
- **Fix:** Before writing that something isn't public or wasn't found, re-check the sources already opened and run one search for it. If it's still missing, say where Claude looked.
- **Again on 2026-10-10:** I said I wasn't certain who McKinsey's Frontline Sales Survey covered, and that it might be salespeople from many industries. You corrected me: it's a banker survey. The McKinsey article already in our files says it covered about 400 US and Canadian bankers, RMs and sales leaders. Root cause: I raised a doubt about a fact without first checking our own files and the sources we'd already read.
- **Stronger fix (Level 2):** before saying "I'm not certain" about a fact, or offering an alternative reading of it, search the repo and the sources already opened. Say "not certain" only if that search comes up empty, and say where I looked.
- **Rule:** R20 · **Test:** T22 · **Level:** 2 · **Times it happened:** 2

### L10d · 2026-10-09 · Kept saying "the McKinsey link" without explaining it
- **What happened:** Across several messages and in NOW.md, Claude told me to "open the McKinsey link before sharing". I had no idea what it was.
- **Root cause:** The note was written into NOW.md as a reminder for Claude, in shorthand. Every later message copied the shorthand without rereading it as a newcomer. The wrap-up plain-words check only covers the final wrap-up message, not NOW.md or mid-session messages. A fourth time, at Level 3.
- **Fix:** Every "What's next" item in NOW.md now says what the thing is and why it matters, not just its name. The audit skill's plain-English check now includes NOW.md, so a shorthand item fails the audit. Automatic check suggested as idea 32.
- **Rule:** R13 · **Test:** T13 · **Level:** 3 (repeat of L10, L10b, L10c) · **Times it happened:** 4

### L13b · 2026-10-09 · Delivered the playbook as Markdown
- **What happened:** Claude wrote the six-step playbook (a field manual I'll read and use) as .md files and showed them to me that way. I had to ask again for a designed format.
- **Root cause:** R16 said "documents *other people* will read". Claude read that as "not for me", so a manual meant for me slipped through. Claude also decided the format only after writing, not before. A repeat of L13, so it moves to Level 2.
- **Fix:** Before writing anything, Claude asks itself: will a person read this, me included? If yes, it's a designed, branded page from the start, and the .md is only the working copy. Only files that just Claude reads (rules, skills, NOW.md, logs) stay as plain files. The designed-doc skill now opens with this check.
- **Rule:** R16 · **Test:** T16 · **Level:** 2 (repeat of L13) · **Times it happened:** 2

### L15 · 2026-10-09 · Frameworks offered for merging without an audit
- **What happened:** A full audit of the new playbook and delivery machine found 20 errors in Claude's work, including a step that went in a circle (Define's data, risk and stories each waited on another) and a wrong claim that a US privacy law (GLBA) covers business clients. I had already been asked whether to merge it.
- **Root cause:** Checking was done now and then, only when I asked. Nothing in the process required an audit before work was offered for merging, so errors reached the merge question.
- **Fix:** A new **audit** skill: a mechanical checker, a fresh reviewer, fixes, then a second reviewer to confirm. It runs as step 0 of every wrap-up and before anything that changes frameworks, the playbook, skills, rules, memos or designed pages is offered for merging.
- **Rule:** R18 · **Test:** T18 · **Level:** 3 (required step in the wrap-up skill) · **Times it happened:** 1

### L7c · 2026-10-09 · The scrolling plan page had all 12 tables empty
- **What happened:** The long scrolling RM plan page was published with every table empty: headings showed, but no rows. Claude then made it my default page for reviewing the plan. The audit found it.
- **Root cause:** When the plan was turned into one page, it was rendered by opening the source file straight from disk. From disk, the canvas runtime can't load itself, so the browser read the template on its own and dropped the table rows (the loops sat inside tables). Served through a web server, the same source renders every table (confirmed 2026-10-09). The check looked at a screenshot of the top of the page and never confirmed that the tables had content. A third time a page wasn't checked the way I see it, so it moves to Level 3.
- **Fix:** The audit skill's checker now fails on any empty table in a designed page. The designed-doc skill's on-screen check must run that checker, not just look at one screenshot.
- **Rule:** R7 · **Test:** T7 · **Level:** 3 (required step in the designed-doc and audit skills) · **Times it happened:** 3

### L8b · 2026-10-09 · Didn't say whether cleanup was needed or optional (test T8 failed)
- **What happened:** In a run-tests check, the answer to "Should I clean up the old files?" gave good reasons but never said whether the cleanup was needed or optional.
- **Root cause:** Claude answered "should I?" with a recommendation and treated the reasons as enough. R8 was worded around "giving instructions", so a yes/no recommendation slipped past it. A repeat of L8, so it moves to Level 2.
- **Fix:** Whenever Claude suggests or recommends any action, it starts with the label in bold, **Needed** or **Optional**, followed by a one-line reason.
- **Rule:** R8 · **Test:** T8 · **Level:** 2 (repeat of L8) · **Times it happened:** 2

### L14 · 2026-10-09 · Approved skills were never built
- **What happened:** I had said yes to four skill ideas (run-tests, prototype, write-prompt, new use case), but none were built. When I found out, I was confused about why approved skills didn't exist.
- **Root cause:** Our rules say Claude asks before adding a skill, but nothing says what happens after a yes. Each approval was recorded in `ideas.md` and then the session moved on. Only run-tests made it onto the "What's next" list in NOW.md, so the other three had no reminder at all.
- **Fix:** When I say yes to a skill or idea, Claude builds it in the same session. If there's no time, it goes straight onto "What's next" in NOW.md, so it's never just a row in `ideas.md`.
- **Rule:** R17 · **Test:** T17 · **Level:** 1 · **Times it happened:** 1

### L7b · 2026-10-09 · Said the designed plan was done without looking at it
- **What happened:** Claude published the full plan to the design page and called it done. Only the first quarter showed, because the canvas shows at most 8,000 pixels of each page and the plan was about 32,000. The one-page summary also ran past the bottom of its page. I said the doc was incomplete.
- **Root cause:** Claude checked that the code ran, but never looked at the page the way I would see it. A repeat of L7 (didn't check where a change landed), so it moves to Level 2.
- **Fix:** Before calling a designed page done, render it on screen, measure it, look at a screenshot and confirm nothing is cut off.
- **Rule:** R7 · **Test:** T7 · **Level:** 2 (repeat of L7) · **Times it happened:** 2

### L13 · 2026-10-09 · Gave me Markdown files for documents meant for people
- **What happened:** Claude delivered memo v8 and a one-page summary, meant for the hiring leader, as Markdown (.md) files. I said documents people will read must be real, designed, branded documents, like the earlier RM Analytics Framework design page.
- **Root cause:** Claude treated the repo's working copy as the finished product and didn't ask who would read it. It also missed that a designed version already existed and should be kept up to date.
- **Fix:** Anything another person will read is delivered as a designed, branded document or page (the RM memo lives on its design canvas). The .md file stays as Claude's working copy only. When a designed version exists, update it in place.
- **Rule:** R16 · **Test:** T16 · **Level:** 1 · **Times it happened:** 1

### L12 · 2026-10-09 · Pop-up notes when no pop-up appeared
- **What happened:** Claude put "Click Allow. Deny is always safe." before every GitHub action, but no pop-ups were appearing. I said it made no sense.
- **Root cause:** Claude followed R4's wording ("before every pop-up") as a ritual, without checking whether a pop-up was actually coming. It was noise that made messages longer and less clear.
- **Fix:** Only explain a pop-up when one actually appears or is clearly about to. GitHub actions in my cloud sessions run without pop-ups, so they need no note.
- **Rule:** R15 · **Test:** T15 · **Level:** 1 · **Times it happened:** 1

### L10c · 2026-10-09 · Shorthand a third time, right after the rule was sharpened
- **What happened:** In the wrap-up message, Claude wrote "everything is consistent except the wrap-up routine," "I'm blocked from changing it" and "the exact wording is in idea 16." I said I didn't understand any of it.
- **Root cause:** Claude packed three insider ideas into a few lines to keep the message short, and assumed I knew what they referred to. Keeping it short won out over keeping it clear. A repeat, so it moves to Level 3.
- **Fix:** Level 3 means a required step in a skill. (At the time Claude believed it couldn't edit its own skills; it can, and the step is now wrap-up step 9.) Until then: before sending any wrap-up or status message, Claude rereads it as a newcomer and rewrites any phrase that names something internal without explaining it.
- **Rule:** R13 · **Test:** T13 · **Level:** 3 (repeat of L10, L10b) · **Times it happened:** 3

### L10b · 2026-10-09 · Used shorthand again: "save to GitHub"
- **What happened:** Claude kept saying "save to GitHub" without saying whether it meant a draft (safe but hidden) or merging into main (official). I asked what it meant.
- **Root cause:** Claude used one loose phrase for two different steps, and assumed I knew the difference. A repeat of L10, so it moves to Level 2.
- **Fix:** Name the exact step every time: "save a draft" or "merge into main." Before sending, check every technical phrase is one I'd understand.
- **Rule:** R13 · **Test:** T13 · **Level:** 2 (repeat of L10; now 3, see L10c) · **Times it happened:** 2

### L11 · 2026-10-09 · Work stranded on a branch that never reached main
- **What happened:** The RM analytics framework (memo v6, audit, market scan) from 2026-10-08 was saved only on a side branch on GitHub. No pull request was ever opened, so it never reached main and later sessions couldn't see it. I found out only by asking, and it worried me that so much work could have been lost.
- **Root cause:** Getting work into main depended on someone remembering to wrap up and merge. Nothing checked for work left behind on other branches.
- **Fix:** The startup check now lists any branch with work that isn't in main, at the start of every session. Wrap-up offers to merge right away.
- **Rule:** R14 · **Test:** T14 · **Level:** 1 (plus an automatic check) · **Times it happened:** 1

### L10 · 2026-10-09 · Used shorthand I didn't understand
- **What happened:** After I merged the prototypes, Claude said "NOW.md still lists 'merge the prototypes pull request' as a next step. The next session can tick it off, so you don't need another save just for that." I replied "I don't understand."
- **Root cause:** Claude wrote in its own shorthand: it named an internal file and a to-do item, and said "save" without saying what that would mean for me. It assumed I knew what it was thinking.
- **Fix:** Before sending a message, read it as me: say what happened, what it means for me and whether I need to do anything. Name a file only with a few words on what it is.
- **Rule:** R13 · **Test:** T13 · **Level:** 1 (now 2, see L10b) · **Times it happened:** 1

### L3b · 2026-10-07 · Got too meta (again)
- **What happened:** A session meant for the job's tech stacks turned into a long back-and-forth about branches, permissions and safety checks. I said "it's getting too meta" and "please answer my question."
- **Root cause:** Each problem with the setup pulled Claude into explaining and asking about it, instead of fixing what it could, giving me the one step I had to do, and getting back to the real work. A repeat of L3, so it moves to Level 2.
- **Fix:** When a setup problem comes up, fix what Claude can, give me at most one step to do, and go straight back to the task I asked for. Answer my actual question first, before any side issue.
- **Rule:** R3 · **Test:** T3 · **Level:** 2 (repeat of L3) · **Times it happened:** 2

### L2b · 2026-10-09 · Wrap-up message too long (again)
- **What happened:** At the end of the last session, Claude's final wrap-up message ran about 15 lines (what's in it, a blocked item, 5 merge steps, next session). I said "say less."
- **Root cause:** Rule R2 was there, but the wrap-up skill itself asks for a lot at the end, so Claude followed the skill and forgot the rule. A repeat, so the fix moves to Level 3.
- **Fix:** The wrap-up skill now has a required length check: the final message is 5 lines or fewer.
- **Rule:** R2 · **Test:** T2 · **Level:** 3 (repeat of L2) · **Times it happened:** 3

### L9 · 2026-10-09 · Said an example followed a tip when it didn't
- **What happened:** Claude said Example 2 in `prompting.md` followed tip 6 (long material first, request last). It actually put the Goal at the top and the notes in the middle. I caught it by asking "where's the question?"
- **Root cause:** Claude wrote the example in the template's usual order, then claimed it met the tip without checking it against the tip's actual wording.
- **Fix:** Before saying something follows a tip, rule or standard, check it against that rule's actual wording, point by point. Example 2 is now reordered, and the template has a "long material" note.
- **Rule:** R11 · **Test:** T11 · **Level:** 1 · **Times it happened:** 1

### L8 · 2026-10-07 · Made optional tidying sound required
- **What happened:** Claude gave me step-by-step instructions to delete old branches, and I had to ask why. It was only optional tidying.
- **Root cause:** Claude went straight to the how, and didn't say whether the step was needed.
- **Fix:** Label every step as needed or optional, with a one-line reason.
- **Rule:** R8 · **Test:** T8 · **Level:** 1 · **Times it happened:** 1

### L7 · 2026-10-07 · Recorded a test result on the wrong test
- **What happened:** Claude wrote "T6 passed" under test T1 and told me T6 was marked passed.
- **Root cause:** Claude made the edit with a script and didn't look at where the change landed before reporting it done.
- **Fix:** After editing a file, check the changed line is in the right place before saying it's done.
- **Rule:** R7 · **Test:** T7 · **Level:** 1 · **Times it happened:** 1

### L6b · 2026-10-07 · Said the job description was missing (again)
- **What happened:** Asked for a tech summary, Claude said there was no job description and asked me to paste it, even though `job-description.md` was on main.
- **Root cause:** The session started on an old leftover branch (`claude/laughing-maxwell-nwehfl`) that was missing everything merged since, including rule R6 itself. A written rule can't help if the old copy doesn't contain it.
- **Deeper root cause (found while testing):** GitHub's default branch was still the old setup branch (`claude/focused-noether-hvnz1x`), so every new session started from that first version. I switched the default branch to main on 2026-10-07.
- **Fix:** A startup hook (`.claude/hooks/session-start.sh`) now runs automatically at the start of every cloud session and merges the latest main in before Claude reads anything. If it can't, it shows Claude a warning to pass on. Backup rule: check origin/main before ever saying something is missing.
- **Rule:** R6 · **Test:** T6 · **Level:** 3 (repeat of L6) · **Times it happened:** 4

### L6 · 2026-10-07 · Made me paste the job description again
- **What happened:** I had to paste the Associated Bank job description a third time. Claude said it couldn't find it, even though `job-description.md` was already on main.
- **Root cause:** The session was started from an old draft branch (`claude/focused-noether-hvnz1x`) instead of main, so its copy was missing everything merged since. Claude didn't check whether its copy was up to date. Also, the job description was only mentioned in NOW.md, not loaded automatically. It happened 3 times, so it starts at Level 2.
- **Fix:** `job-description.md` is now loaded automatically by CLAUDE.md in every session. At the start of each session, Claude checks that its copy matches the latest main version. If it doesn't, Claude says so first, before anything else.
- **Rule:** R6 · **Test:** T6 · **Level:** 2 → 3 (see L6b) · **Times it happened:** 3

### L5 · 2026-10-07 · Steered away from what I asked for
- **What happened:** I said I wanted to think through how to do a new job. When I mentioned I was still interviewing, Claude switched to interview prep, and I had to correct it.
- **Root cause:** Claude let a new detail replace my stated goal, instead of checking how that detail fit the goal.
- **Fix:** Keep my stated goal as the anchor. When a new detail could change the direction, ask before switching.
- **Rule:** R5 · **Test:** T5 · **Level:** 1 · **Times it happened:** 1

### L4 · 2026-10-07 · Pop-up without a plain-English explanation
- **What happened:** Claude triggered a GitHub pop-up without first explaining it, and described the problem in technical words. The user clicked Deny because they didn't understand it.
- **Root cause:** Claude was focused on fixing a technical problem and skipped the "Claude explains, I decide" checklist in CLAUDE.md. A rule already existed, so this counts as a failed rule and starts at Level 2.
- **Fix:** Right before every pop-up, give the 3 parts (what it's for, what it can do, which button to click) in everyday words, using an everyday comparison if one helps.
- **Rule:** R4 · **Test:** T4 · **Level:** 2 · **Times it happened:** 1

### L3 · 2026-10-07 · Got too in the weeds
- **What happened:** After being told to shorten things, Claude asked for approval one tiny piece at a time, which slowed everything down.
- **Root cause:** Claude over-corrected and lost sight of the bigger goal, which is to keep moving.
- **Fix:** Keep momentum. Group small things together, ask only about real decisions, and let the full review happen in the pull request.
- **Rule:** R3 · **Test:** T3 · **Level:** 1 · **Times it happened:** 1

### L2 · 2026-10-07 · Showed too much at once
- **What happened:** Claude showed three files in one message. After the correction, it was still too long.
- **Root cause:** Claude trimmed the wording but kept the same amount of content.
- **Fix:** Tiny pieces only, about 5 lines plus one question.
- **Rule:** R2 · **Test:** T2 · **Level:** 2 → 3 (see L2b) · **Times it happened:** 2

### L1 · 2026-10-07 · Explained saving without checking
- **What happened:** Claude said nothing would reach GitHub until the end. In fact, the cloud workspace backs up each saved file right away.
- **Root cause:** Claude described a process from an assumption.
- **Fix:** Check first, or say "I'm not certain."
- **Rule:** R1 · **Test:** T1 · **Level:** 1 · **Times it happened:** 1
