---
name: prototype
description: Build or change a clickable screen prototype (UI) as one HTML file the user can open in their browser. Use when the user says "prototype X", "mock up a screen", "make a clickable version", or asks for a change to an existing prototype (like "make the buttons green"). Follows the prototyping agreement in NOW.md.
---

# Prototype a screen

The user is learning to prototype for their new job. Every version is kept,
so any session can carry on.

## 1. Start
- **New prototype:** pick a short name (like `rm-dashboard`) and confirm it with the user in one line. Ask one question only if the purpose is unclear: who uses this screen, and to do what?
- **Change to an existing one:** open `prototypes/<name>/` and work from the highest version number.

## 2. Write the "done" checklist first
3 to 6 items the user can check by looking, for example "Clicking 7 then + then 2 shows 9." Show it to the user before building (rule R9).

## 3. Build
- One self-contained HTML file: no installs, opens with a double-click.
- Save it as `prototypes/<name>/prototype-v<N>.html`. A new prototype starts at v1; each change is the next number. **Never edit an older version**, because the user wants every step kept.
- For bank screens, use made-up but realistic data, and label it "sample data" on screen so nobody mistakes it for real numbers.

## 4. Check it the way the user will see it (rule R7)
- Open it with Playwright (Chromium is at `/opt/pw-browsers/chromium`), click through each checklist item, and take a screenshot.
- Show pass or fail for each checklist item, with proof. Fix failures before going on.

## 5. Deliver
- Send the file with `SendUserFile` so the user can open it.
- Update "Current:" under the prototyping agreement in NOW.md with the name and version.
- Save a draft to GitHub, then ask: "Merge into main now? (yes/no)"
