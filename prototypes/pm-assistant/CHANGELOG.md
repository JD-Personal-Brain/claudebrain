# Changelog: PM Assistant Prototype

Each delivered version is kept as its own file (`prototype-v<N>.html`) and never changed.
Fixes made before a version is delivered stay in that version.

## Version 4 (2026-10-19)
The outside data feed is gone, from an Elon mode review the user approved: the 10-year Treasury yield never entered a draft, so it added code and a guardrail with nothing in the plan behind it. Versions 1 to 3 (`prototype-v1.html` to `prototype-v3.html` and their videos) are kept unchanged.
- Removed `src/data/market.js`, `scripts/fetch_market.py` and A7's market data tool: A7 now reads four sources (financials, loans and covenants, deposits and payments, documents and notes), and the borrower file has no market block. The market freshness rule is gone too.
- The draft guardrail now flags rate commentary in general ("rate outlook", "rates have risen" and similar), since drafts state facts from the borrower file only; the Treasury-specific patterns are gone.
- How it's built: the data box and the data list say there is no outside data feed, and why; the A7 and A8 rows and the testing paragraph no longer mention it. The controls screen's freshness row no longer mentions market data.
- The tour's borrower file step now says it "reads four sources itself"; that one voiceover line was re-voiced with Kokoro and the video re-recorded as `pm-assistant-tour-v4.mp4` (trimmed to 119.5 seconds).
- Tests: Prompt 4's checklist item 3 (an outside data source) is reported as "not used (removed in v4)", and now proves the feed is gone; the rate-commentary test plants a general rate line instead of a Treasury line.

## Version 3 (2026-10-19)
Fixes from an audit. Versions 1 and 2 (`prototype-v1.html`, `prototype-v2.html` and their videos) are kept unchanged.
- The tour no longer implies the assistant submits: the judgment step now says "Sam writes the judgment and approves the draft as final, then submits it through the bank's normal route. The assistant never submits." (tour and voiceover). That line and the "Try to break it" line were re-voiced with Kokoro, and the video re-recorded as `pm-assistant-tour-v3.mp4`. The test for checklist item 5 now also checks the tour text and the narration script.
- The draft's last section is renamed "Changes and items to note" (A8's prompt, the recorded drafts, the screens) and lists plain facts with sources only, for example "Requested line $4.5M; borrowing base $5.2M (Sep 30)", with no "would be close to" or other judgments. The live prompt says so; the tests check the name and that no conclusion phrases are left.
- A covenant breach (rule EW3) gets its own tag, "Breach: the bank's waiver and rating process applies", instead of "Look at this week"; the PM's choices (watch, raise, dismiss) are unchanged. New test.
- "Borrower risk rating" wherever the screen means a borrower's credit grade: the judgment box, the hold message, the guardrail replies and labels, the prompts, the tour, the controls and the How it's built page. The product's own risk rating (Govern and test) keeps its wording.
- The internal counter `submitted` is renamed `approvedFinal`.
- The early warning flags screen says "Sample borrowers chosen to show every rule; a real book would flag far fewer."
- Wave 1 drafts still leave the recommendation for the PM: the recommendation box stays, with its "required only if the bank's credit policy asks" note.

## Version 2 (2026-10-19)
Fixes from a review. Version 1 (`prototype-v1.html`, `pm-assistant-tour-v1.mp4`) is kept unchanged.
- The assistant never submits: the review button is now "Approve as final", and the status after approval reads "Approved by Sam Okafor; the PM submits it through the bank's normal approval route". The stamp, audit log, Today, controls and measures say the same; the tests check the new wording and that nothing is logged as submitted.
- Drafts state facts with sources and draw no conclusions for the PM: the 10-year Treasury line is gone from every draft (the sample lines are Prime-based, so the risk statement was wrong), along with conclusion phrases such as ": no warning signs in the account". A8 now drafts from the borrower file without the market data; the market data stays only as background in the borrower file. The live prompts say to state facts with sources, never draw conclusions and never comment on rates, and code flags any draft that mentions the Treasury yield or rate commentary, which turns approval off. New test.
- "Early warning watchlist" is now "Early warning flags" everywhere on screen (the bank's own watchlist is a formal credit term; "the bank's watchlist status" stays only where it means that term). The rules are renamed EW1 to EW5 (they clashed with Open Items numbers) and are labeled a sample set.
- Today: the early warning flags count and every early warning decision carry a "Wave 2 preview" tag.
- The controls screen says old data stops the early warning flags (one leftover "watchlist", fixed before delivery).
- The recommendation box notes it's "required only if the bank's credit policy asks for a recommendation (to confirm)"; it stays required for now, and approval is still held until the risk rating is written.
- The sticky action bar on the review screen no longer covers the draft: it has a clear edge and shadow, scrolling leaves room for it, the draft ends with space to clear it, and on phones it stays in the page flow.
- One deposit window everywhere: the deposit charts and captions show the last 3 months (June to September), matching the 3-month rule, so Menomonee's chart caption and text agree ($470K to $310K); Lakeshore's file summary uses the same window.
- The tour video was re-recorded as `pm-assistant-tour-v2.mp4` (the narration is unchanged, so the version 1 voice was reused). The README now gives one tour length, "under 2 minutes".

## Version 1 (2026-10-19)
First version, built from Prompt 4 in the Prompt Library with the user group changed to portfolio managers (PMs), and copied from the RM Assistant Prototype (version 4) so both share one house style and structure.
- One sample PM (Sam Okafor, the portfolio manager paired with the RM prototype's Jordan Ellis) with 12 made-up borrowers: three years of statement figures, loans with rates as written, covenants with their latest tests, deposits, payments, due dates, the last review and an RM note; plus 2 borrowers of another PM for the permissions test. The borrowers and their loans match the RM prototype's clients.
- Today: reviews and requests coming due, borrowers on the watchlist, drafts waiting and items missing or late.
- Borrower file (workflow B10, agent A7): five page tools gather the file, each step shown, every figure with its source, and a "missing or late" list; Claude summarizes it. The PM uses the file, asks the RM for what's missing (a drafted note the PM sends) or flags an error.
- Review and memo drafts (workflows B11 and B12, agent A8, live on Claude): the five routine sections of an annual review or credit memo; the risk rating and recommendation left blank "For the PM's judgment"; the credit officer who decides named at the top; marked "AI draft". Code checks every number against the file (K7), marks sections "needs input" when the file has a gap (K25; Chequamegon Timber Works is missing its FY2025 statements), removes any rating or recommendation the AI writes and scans for decisions and prices (K3, K8). Nothing is submitted until the PM has filled the judgment sections and approved.
- Early warning watchlist (workflow B13, agent A9, wave 2 preview): five plain rules in code (statements late, covenant within 10% of its limit, covenant breached, deposits down 25% or more over 3 months, payment past due), with Claude explaining the flags; the PM dismisses with a reason, watches, or raises it through the bank's process. A covenant and statement tracker (workflow B14) lists every test and due item.
- Controls and audit log: "Try to break it" (risk ratings, approvals, recommendations, prices, other PMs' borrowers, record changes and contacting borrowers blocked in code, while a PM's ordinary credit questions pass), and the live audit log.
- Outside data: the Federal Reserve's 10-year Treasury yield, as a dated copy (fetched 2026-10-19, latest August 2026), used only as background on floating-rate loans.
- Product manager view with the five kinds of measures; a voiced guided tour under 2 minutes, and the tour as a video (`pm-assistant-tour-v1.mp4`).
