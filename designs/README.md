# Designed pages: source files

The HTML behind each designed page, so any session can rebuild or edit it.
Edit here, publish to the same link, then save a draft.

| Page | Link | Source |
|---|---|---|
| RM Analytics Framework design page (summary + six parts) | https://claude.ai/artifact/3c7ZxKjJcjWRyV7BbzKfhY | `rm-analytics-canvas/` (`full-plan-source.dc.html` is the unsplit plan the six parts are built from) |
| RM analytics plan, one continuous page | https://claude.ai/artifact/KxPNQLCj6HASThmQpYtfhk | `rm-analytics-plan.html` (rendered from `full-plan-source.dc.html`) |
| Six-step workflow visual | https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv | `role-workflow.html` |
| The delivery machine (how one PM runs many AI projects) | https://claude.ai/artifact/S8Wbygy24cjguTMxZsN2QF | `delivery-machine.html` (built by `delivery-machine-build.py` from the tables in `product-framework.md`) |
| Delivery Playbook (field manual for all six steps) | https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4 | `playbook.html` (built by `playbook-build.py` from `playbook/*.md`) |
| Product Framework | https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ | `product-framework.html` (built by `md-page-build.py` from `product-framework.md`) |
| Tech Stack Guide | https://claude.ai/artifact/DDmD65zw7LjnP5v2nHDFW2 | `tech-stack.html` (built by `md-page-build.py` from `tech-stack.md`) |
| Job Notes | https://claude.ai/artifact/SpcnPMbMEgyxZSoYVsRdES | `job-notes.html` (built by `md-page-build.py` from `job-notes.md`) |
| Job Description | https://claude.ai/artifact/9CUyQt1EDbmu1R7DVRyvkM | `job-description.html` (built by `md-page-build.py` from `job-description.md`) |
| Prompting Guide | https://claude.ai/artifact/Secfj5fBtpVA1veroUU7A7 | `prompting.html` (built by `md-page-build.py` from `prompting.md`) |
| **Document Library** (pinned to my sidebar; lists every page above) | https://claude.ai/artifact/LTpbCT4kN4LcyEoYnh7vgj | `library.html` (built by `library-build.py` from `library.json`) |

**Shared page kit:** `pagekit.py` holds the house style and the Markdown-to-page code used by `playbook-build.py` and `md-page-build.py`. To give another working file a designed page, add it to `PAGES` in `md-page-build.py`.

**Rendering canvas pages:** serve `.dc.html` files through a local web server (`python3 -m http.server`) with the canvas runtime beside them as `support.js`. Opened straight from disk, the runtime can't load and table rows are dropped.
