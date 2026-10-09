#!/bin/bash
# Runs automatically at the start of every cloud session, before Claude reads anything.
# It brings this working copy up to date with the latest main on GitHub, so Claude
# never works from an old copy (see lesson L6 in learning/lessons.md).
# It also warns about work saved on other branches that never reached main
# (see lesson L11), so nothing sits forgotten on GitHub.
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
elif git merge -q --ff-only origin/main 2>/dev/null; then
  echo "✅ Startup check: branch '$branch' was behind main and has been updated to match it."
elif git merge -q --no-edit origin/main 2>/dev/null; then
  echo "✅ Startup check: merged the latest main into branch '$branch'."
else
  git merge --abort 2>/dev/null
  warn "branch '$branch' has edits that conflict with main, so it could not be updated automatically."
fi

# Look for work on other branches that main doesn't have yet. A branch counts
# only if merging it would actually change main, so already-merged branches stay quiet.
git fetch -q --prune origin 2>/dev/null
main_tree=$(git rev-parse origin/main^{tree})
found=no
for b in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin); do
  case "$b" in origin/main|origin/HEAD|origin) continue ;; esac
  merged_tree=$(git merge-tree --write-tree origin/main "$b" 2>/dev/null | head -1)
  [ "$merged_tree" = "$main_tree" ] && continue
  if [ "$found" = no ]; then
    echo "⚠️ UNMERGED WORK FOUND: these branches have saved work that is NOT in main,"
    echo "so new sessions can't see it. Tell the user first, in plain words, and offer to"
    echo "bring it into main (via a pull request) or delete the branch if it's not needed."
    found=yes
  fi
  echo "  • ${b#origin/} (last saved $(git log -1 --format=%cd --date=short "$b")), files:"
  git diff --name-only origin/main..."$b" | head -12 | sed 's/^/      /'
done
