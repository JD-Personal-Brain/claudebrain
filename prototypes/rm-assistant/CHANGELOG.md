# Changelog: RM Assistant Prototype

Each delivered version is kept as its own file (`prototype-v<N>.html`) and never changed.
Fixes made before a version is delivered stay in that version.

## Version 1 (2026-10-18)
First version, built from Prompt 4 in the Prompt Library.
- Wave 1 screens: the Monday opportunity list (B1), the pre-meeting client brief (B2) and the meeting follow-up (B3, B4), for one sample RM with 12 made-up clients.
- Three agents: A1 Signal finder (6 rules in code), A2 Insight writer and A3 Prep and follow-up assistant (both live on Claude, with recorded runs as the fallback).
- Outside data: the Federal Reserve's 10-year Treasury yield, as a dated copy (fetched 2026-10-18, latest August 2026).
- Controls shown working: K1, K2, K3, K4, K7 (number check), K8 (guardrails), K12 (audit log), K22, K24 and K25.
- Product manager view with the five kinds of measures; a guided tour under 2 minutes, and the tour as a video.
- Before delivery, a deep audit (words, plan alignment, design, an executive walk-through) led to: plain names instead of codes on screen, an opening summary, a step-by-step agent timeline, use / change / reject on every output, wider guardrails with innocent questions allowed, a scan of every finished draft for prices and credit promises, a stale-data stop and an empty-notes stop (K25), decisions kept across re-runs, the approval line stamped only when the RM approves, a flow diagram, what a pilot would need, and a dark-mode fix.
