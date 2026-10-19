"""Reads video/narration.json aloud with Kokoro (open-source text-to-speech: code MIT, model Apache 2.0),
one clip per tour step, and writes lens.json with each clip's length. Needs: pip install kokoro-onnx soundfile,
and kokoro-v1.0.onnx and voices-v1.0.bin from github.com/thewh1teagle/kokoro-onnx/releases (model-files-v1.0)
in the current folder. Run: python narrate.py ../video/narration.json <out folder>"""
import json, sys, soundfile as sf
from kokoro_onnx import Kokoro
cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
k = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
lens = []
for i, line in enumerate(cfg["lines"]):
    a, sr = k.create(line, voice=cfg["voice"], speed=cfg["speed"], lang="en-us")
    sf.write(f"{out}/step{i:02d}.wav", a, sr); lens.append(round(len(a) / sr, 2))
json.dump({"sr": sr, "lens": lens}, open(f"{out}/lens.json", "w"))
print(lens, round(sum(lens), 1))
