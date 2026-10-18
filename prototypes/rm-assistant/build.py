"""Builds the prototype as one self-contained page: src/page.html with the styles and scripts
inlined, written to prototype-v<N>.html. Every version is kept: the build refuses to overwrite
a version that's already been delivered (listed in CHANGELOG.md) unless you pass --force.
Run: python3 build.py 1        (builds prototype-v1.html)"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
SCRIPTS = ["data/book.js", "data/market.js", "replay.js", "agents.js", "app.js", "tour.js"]  # load order matters

def read(p): return open(os.path.join(SRC, p), encoding="utf-8").read()

def build(version, force=False):
    out = os.path.join(HERE, f"prototype-v{version}.html")
    delivered = re.findall(r"^## Version (\d+)", open(os.path.join(HERE, "CHANGELOG.md")).read(), re.M)
    if os.path.exists(out) and str(version) in delivered and not force:
        raise SystemExit(f"prototype-v{version}.html was delivered already; build the next version instead (or pass --force while fixing it before delivery).")
    page = read("page.html").replace("/*CSS*/", read("styles.css"))
    js = "\n".join(f"// ===== src/{s} =====\n" + read(s) for s in SCRIPTS)
    page = page.replace("/*JS*/", js).replace('<span id="ver">1</span>', f'<span id="ver">{version}</span>')
    # The published page may load only Google Fonts; anything else would be blocked, so fail here.
    # Only what the page loads counts (scripts, images, stylesheets); plain <a> links to other pages are fine.
    hosts = set(re.findall(r'src="https?://([^/"]+)', page)) | set(re.findall(r'<link[^>]*href="https?://([^/"]+)', page))
    bad = hosts - {"fonts.googleapis.com", "fonts.gstatic.com"}
    if bad: raise SystemExit(f"external hosts not allowed on a published page: {sorted(bad)}")
    if "</script" in js.replace("<\\/script", ""): raise SystemExit("a script contains </script>")
    open(out, "w", encoding="utf-8").write(page)
    print(f"wrote {os.path.basename(out)} ({len(page) // 1024} KB)")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build(int(args[0]) if args else 1, "--force" in sys.argv)
