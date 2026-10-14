"""Crawl every internal link of a running dev server and report non-200 pages / broken static assets.
Usage: python tools/crawl.py [base_url]"""
import re
import sys
import urllib.request
import urllib.error

base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5055"
seen, todo, bad, assets = set(), ["/"], [], set()
while todo:
    u = todo.pop()
    if u in seen:
        continue
    seen.add(u)
    try:
        h = urllib.request.urlopen(base + u).read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        bad.append((u, e.code))
        continue
    except Exception as e:
        bad.append((u, str(e)[:60]))
        continue
    for m in re.findall(r'href="(/[^"#?]*)', h):
        if not m.startswith("/static") and m not in seen:
            todo.append(m)
    for m in re.findall(r'(?:src|href)="(/static/[^"?]+)', h):
        assets.add(m)
broken = []
for a in sorted(assets):
    try:
        urllib.request.urlopen(base + a)
    except Exception:
        broken.append(a)
print(len(seen), "pages crawled;", len(assets), "assets checked")
print("bad pages:", bad)
print("broken assets:", broken)
