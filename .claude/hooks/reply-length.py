#!/usr/bin/env python3
"""Length warning on Claude's replies (idea 57, approved 2026-10-17; rule R2).
Runs as a Stop hook. If the reply Claude just finished runs past 8 non-empty
lines, it stops Claude once and asks for a short version: the outcome, what it
means for the user and at most one step, in about 5 lines. It never fires twice
in a row (stop_hook_active), so it can't loop."""
import json, sys

LIMIT = 8

def reply_text(path):
    # The last reply = the text blocks of every assistant entry since the user's last real message.
    parts = []
    for line in open(path, encoding="utf-8"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        msg = e.get("message") or {}
        content = msg.get("content")
        if e.get("type") == "user":
            real = isinstance(content, str) or any(isinstance(b, dict) and b.get("type") == "text" for b in (content or []))
            if real and not e.get("isMeta"):
                parts = []
        elif e.get("type") == "assistant" and isinstance(content, list):
            parts += [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    return "\n".join(parts)

def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    if data.get("stop_hook_active") or not data.get("transcript_path"):
        return 0
    try:
        text = reply_text(data["transcript_path"])
    except OSError:
        return 0
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) <= LIMIT:
        return 0
    sys.stderr.write(
        f"Length warning (rule R2): your reply to the user ran {len(lines)} lines, past the limit of {LIMIT}. "
        "Send a short follow-up instead of repeating it: the outcome and what it means for the user, "
        "then at most one step, in about 5 lines. If the long reply was a deliverable the user asked for "
        "in full, say so in one line and stop.\n")
    return 2

if __name__ == "__main__":
    sys.exit(main())
