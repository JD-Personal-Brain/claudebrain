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
- The tour video now has a voiceover (Kokoro, an open-source voice), with each step timed to its line.

## Version 2 (2026-10-18)
The six open items from the version 1 audits.
- The Monday list no longer shows "Growing balances": it isn't a product gap, and wave 1 suggests only deposit and treasury gaps.
- Market rates are background for the RM only ("Background for you (not to quote)"), never a talking point, so the brief can't read as quoting a rate (K8). The agents' instructions say the same.
- The brief arrives a set number of hours before each meeting ([X], as in the RM plan), not "the day before".
- Screen labels no longer show workflow codes (B1 to B4); they're in the label's tooltip and on "How it's built".
- The brief's Use it / Change it / Reject buttons moved to a bar at the bottom, the same place as the follow-up's approve buttons.
- The measures screen shows a labeled, made-up sample pilot week under each session number, instead of a screen of zeros.

## Version 3 (2026-10-18)
- The tour on the page now speaks: the same voice as the tour video (Kokoro, an open-source voice) reads each step. A "Voice on / Voice off" button in the tour card turns it off, and the choice is remembered. Steps last as long as their line, so the tour runs about 2 minutes 5 seconds.
