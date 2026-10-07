#!/bin/bash
# Runs automatically at the start of every cloud session, before Claude reads anything.
# It brings this working copy up to date with the latest main on GitHub, so Claude
# never works from an old copy (see lesson L6 in learning/lessons.md).
# Whatever this script prints is shown to Claude at the start of the session.

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

warn() {
  echo "⚠️ STARTUP CHECK FAILED: $1"
  echo "This copy of the repo may be OUT OF DATE with main. Before doing anything else,"
  echo "tell the user in plain words, and check origin/main before saying any file is missing."
  exit 0
}

# Get the latest main from GitHub (retry, in case the network is slow to start).
fetched=no
for wait in 2 4 8; do
  if git fetch -q origin main 2>/dev/null; then fetched=yes; break; fi
  sleep "$wait"
done
[ "$fetched" = yes ] || warn "could not reach GitHub to get the latest main."

branch=$(git rev-parse --abbrev-ref HEAD)

if git merge-base --is-ancestor origin/main HEAD; then
  echo "✅ Startup check: branch '$branch' already has everything from main."
  exit 0
fi

if git merge -q --ff-only origin/main 2>/dev/null; then
  echo "✅ Startup check: branch '$branch' was behind main and has been updated to match it."
elif git merge -q --no-edit origin/main 2>/dev/null; then
  echo "✅ Startup check: merged the latest main into branch '$branch'."
else
  git merge --abort 2>/dev/null
  warn "branch '$branch' has edits that conflict with main, so it could not be updated automatically."
fi
