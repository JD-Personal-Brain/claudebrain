# Changelog: PM Assistant Prototype

Each delivered version is kept as its own file (`prototype-v<N>.html`) and never changed.
Fixes made before a version is delivered stay in that version.

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
