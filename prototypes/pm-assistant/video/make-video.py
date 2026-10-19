"""Turns the raw tour recording into the final narrated video.
Inputs: the folder that tests/record-video.js wrote (pm-assistant-tour.webm and timing.json) and the
folder of voice clips from narrate.py (stepNN.wav and lens.json).
The raw recording runs a little slower than real time, so it is retimed to real time first; then each
voice clip is laid down at the moment its tour step really started.
Run: python3 video/make-video.py <recording folder> <clips folder> <output .mp4>"""
import json, os, subprocess, sys, wave, array

rec, clips, out = sys.argv[1], sys.argv[2], sys.argv[3]
timing = json.load(open(os.path.join(rec, "timing.json")))
raw = os.path.join(rec, "pm-assistant-tour.webm")
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", raw]).decode())
factor = timing["realSeconds"] / dur          # < 1 when the recording ran slow
lens = json.load(open(os.path.join(clips, "lens.json")))
sr = lens["sr"]
total = int((timing["realSeconds"] + 1) * sr)
mix = array.array("h", [0]) * total
seen = set()
for s in timing["steps"]:
    if s["step"] in seen: continue
    seen.add(s["step"])
    with wave.open(os.path.join(clips, f"step{s['step']:02d}.wav")) as w:
        assert w.getframerate() == sr
        data = array.array("h", w.readframes(w.getnframes())) if w.getsampwidth() == 2 else None
    if data is None: raise SystemExit("expected 16-bit clips")
    start = int((s["at"] + 0.35) * sr)          # a short beat after the step appears
    for i, v in enumerate(data):
        if start + i < total: mix[start + i] = v
voice = os.path.join(rec, "voice.wav")
with wave.open(voice, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(mix.tobytes())
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-i", voice, "-filter:v", f"setpts={factor:.5f}*PTS", "-r", "25",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "26", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out], check=True)
print("wrote", out, "retimed by", round(factor, 3), "with", len(seen), "voice clips")
