# Designed pages: source files

The HTML behind each designed page, so any session can rebuild or edit it.
Edit here, publish to the same link, then save a draft.

| Page | Link | Source |
|---|---|---|
| RM Analytics Framework design page (summary + six parts) | https://claude.ai/artifact/3c7ZxKjJcjWRyV7BbzKfhY | `rm-analytics-canvas/` (`full-plan-source.dc.html` is the unsplit plan the six parts are built from) |
| RM analytics plan, one continuous page | https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk | `rm-analytics-plan.html` (rendered from `full-plan-source.dc.html`) |
| Product Workflow (How we deliver, page 1 of 4) | https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv | `role-workflow.html` (made by hand from `memos/role-workflow.md`; its "How we deliver" strip comes from `series()` in `pagekit.py`) |
| Product Framework | https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ | `product-framework.html` (built by `md-page-build.py` from `product-framework.md`; How we deliver, page 2 of 4) |
| Product Machine (how one product manager runs many AI projects; How we deliver, page 3 of 4) | https://claude.ai/artifact/S8Wbygy24cjguTMxZsN2QF | `product-machine.html` (built by `product-machine-build.py` from the tables in `product-machine.md`; How we deliver, page 3 of 4) |
| Product Playbook (field manual for all six steps) | https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4 | `playbook.html` (built by `playbook-build.py` from `playbook/*.md`; How we deliver, page 4 of 4) |
| Tech Stack Guide | https://claude.ai/artifact/DDmD65zw7LjnP5v2nHDFW2 | `tech-stack.html` (built by `md-page-build.py` from `tech-stack.md`) |
| Job Description | https://claude.ai/artifact/9CUyQt1EDbmu1R7DVRyvkM | `job-description.html` (built by `md-page-build.py` from `job-description.md`) |
| Open Items (the one log of everything still open) | https://claude.ai/artifact/NsW5AH5XFNHmDNYJvmVDMb | `open-items.html` (built by `md-page-build.py` from `open-items.md`; updated at every wrap-up) |
| Bank Business Briefing (how the bank earns money, the corporate segment, and where AI work lines up) | https://claude.ai/artifact/7ZVT7LtdqxwAma4UrBgTPX | `bank-business.html` (built by `md-page-build.py` from `memos/bank-business.md`; re-run Example 5 in `prompting.md` each quarter to refresh the words) |
| Portfolio Manager Core Use Cases (what banks deploy in credit, lined up with the RM core use cases; was "Credit Market Scan") | https://claude.ai/artifact/2tySJZL41pf72igzanYbaT | `credit-market-scan.html` (built by `md-page-build.py` from `memos/credit-market-scan.md`) |
| Prompting Guide | https://claude.ai/artifact/Secfj5fBtpVA1veroUU7A7 | `prompting.html` (built by `md-page-build.py` from `prompting.md`) |
| Workflow Maps (reference page) | https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX | `workflows.html` (built by `workflows-build.py` from `memos/role-workflow.md` (questions, gates, governance), `playbook/`, `product-machine.md` and the RM memo's Appendix B) |
| Agent Library (reference page) | https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn | `agents.html` (built by `agents-build.py` from `playbook/agents.md` and the RM memo's Appendix A) |
| Steps Catalog (reference page) | https://claude.ai/artifact/8UncWMYUq7hsJUhn5NSYEB | `steps.html` (built by `catalogs-build.py` from `memos/role-workflow.md` (questions, gates, governance), `playbook/` and `product-machine.md`) |
| Controls Catalog (reference page) | https://claude.ai/artifact/7GmH3iBG6jcDkdacUysUrQ | `controls.html` (built by `catalogs-build.py` from `playbook/controls.md`) |
| RM Core Use Cases (McKinsey's five frontline use cases and the RM plan's seven; was "McKinsey Use Cases") | https://claude.ai/artifact/RpZD7TtRQb9WYD8GdAYu6X | `mckinsey-use-cases.html` (built by `md-page-build.py` from `memos/mckinsey-frontline-ai.md`) |
| Glossary (reference: the words we use) | https://claude.ai/artifact/LRQHSz65beh9XewB6qsQvQ | `glossary.html` (built by `md-page-build.py` from `glossary.md`) |
| **Document Library** (pinned to my sidebar; lists every page above) | https://claude.ai/artifact/LTpbCT4kN4LcyEoYnh7vgj | `library.html` (built by `library-build.py` from `library.json`) |

**Shared page kit:** `pagekit.py` holds the house style and the Markdown-to-page code used by `playbook-build.py` and `md-page-build.py`. To give another working file a designed page, add it to `PAGES` in `md-page-build.py`.

**Rendering canvas pages:** serve `.dc.html` files through a local web server (`python3 -m http.server`) with the canvas runtime beside them as `support.js` (kept in the repo in `rm-analytics-canvas/`). To check every page renders fully, run `node designs/render-check.js`. Opened straight from disk, the runtime can't load and table rows are dropped.
