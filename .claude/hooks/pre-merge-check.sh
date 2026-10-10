#!/bin/bash
# Runs automatically before Claude merges a pull request into main (idea 36).
# It runs the audit checker and the render check on this working copy. If either
# finds a problem, the merge is blocked and the problems are shown to Claude.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
out1=$(python3 .claude/skills/audit/check.py 2>&1)
p1=$(echo "$out1" | grep -o 'problems: [0-9]*' | tail -1 | grep -o '[0-9]*')
PW="$(npm root -g 2>/dev/null)/playwright"
out2=$(PW="$PW" node designs/render-check.js 2>&1)
p2=$(echo "$out2" | grep -o 'problems: [0-9]*' | tail -1 | grep -o '[0-9]*')
if [ "${p1:-1}" != "0" ] || [ "${p2:-1}" != "0" ]; then
  {
    echo "MERGE BLOCKED by the pre-merge check (idea 36): fix these, save a draft, then merge again."
    echo "--- audit checker ---"; echo "$out1" | grep -v '^ok' | tail -20
    echo "--- render check ---"; echo "$out2" | grep -v '^ok' | tail -20
  } >&2
  exit 2
fi
exit 0
