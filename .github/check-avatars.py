#!/usr/bin/env python3
"""Check that all avatar images in guests.json are reachable."""

import json
import sys
import urllib.request

guests = json.load(open("guests.json"))
errors = []

for g in guests:
    url = g.get("avatar", "")
    if not url:
        errors.append(f"[{g['name']}] missing avatar")
        continue
    if not url.startswith("http://") and not url.startswith("https://"):
        print(f"OK  {g['name']}  (local)")
        continue
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            if r.status != 200:
                errors.append(f"[{g['name']}] avatar HTTP {r.status}: {url}")
            else:
                print(f"OK  {g['name']}")
    except Exception as e:
        errors.append(f"[{g['name']}] avatar unreachable: {url} ({e})")

if errors:
    print("\nErrors detected:")
    for err in errors:
        print(f"  ✗ {err}")
    sys.exit(1)
