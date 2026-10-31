#!/usr/bin/env python3
"""Generate self-hosted GitHub stats cards (SVG) for the profile README.

Runs inside GitHub Actions with the built-in GITHUB_TOKEN, so the README never
depends on third-party stats services. Usage:
    python scripts/generate_stats.py          # real data (needs GITHUB_TOKEN, OWNER)
    python scripts/generate_stats.py --demo   # sample data, for previewing the design
"""
import json
import os
import sys
import urllib.request
from collections import Counter
from html import escape

API = "https://api.github.com"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

BG, BORDER = "#0b1020", "#1e293b"
TITLE, TEXT, MUTED, ACCENT = "#ffffff", "#cbd5e1", "#94a3b8", "#3b82f6"
LANG_COLORS = {
    "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "C#": "#178600",
    "HTML": "#e34c26", "CSS": "#563d7c", "Astro": "#ff5a03", "Python": "#3572a5",
    "SCSS": "#c6538c", "Dockerfile": "#384d54", "Shell": "#89e051",
}
FALLBACK = ["#60a5fa", "#a78bfa", "#34d399", "#f472b6", "#fbbf24", "#94a3b8"]


def get(path, token):
    req = urllib.request.Request(
        f"{API}{path}",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "User-Agent": "profile-stats"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect(owner, token):
    user = get(f"/users/{owner}", token)
    repos, page = [], 1
    while True:
        chunk = get(f"/users/{owner}/repos?per_page=100&type=owner&page={page}", token)
        repos += chunk
        if len(chunk) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]
    langs = Counter()
    for r in own:
        try:
            langs.update(get(f"/repos/{owner}/{r['name']}/languages", token))
        except Exception:
            pass
    return {
        "name": user.get("name") or owner,
        "repos": user["public_repos"],
        "followers": user["followers"],
        "stars": sum(r["stargazers_count"] for r in own),
        "forks": sum(r["forks_count"] for r in own),
        "langs": langs,
    }


def card(w, h, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
        f'<style>text{{font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif}}</style>'
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="{BG}" stroke="{BORDER}"/>'
        f'<text x="24" y="38" font-size="18" font-weight="700" fill="{TITLE}">{escape(title)}</text>'
        f'<rect x="24" y="48" width="36" height="3" rx="1.5" fill="{ACCENT}"/>{body}</svg>'
    )


def stats_svg(d):
    rows = [("Public repositories", d["repos"]), ("Stars earned", d["stars"]),
            ("Followers", d["followers"]), ("Forks", d["forks"])]
    body = ""
    for i, (label, value) in enumerate(rows):
        y = 84 + i * 30
        body += f'<text x="24" y="{y}" font-size="14" fill="{TEXT}">{escape(label)}</text>'
        body += f'<text x="326" y="{y}" font-size="14" font-weight="700" fill="{TITLE}" text-anchor="end">{value}</text>'
    return card(350, 200, "GitHub stats", body)


def langs_svg(d):
    total = sum(d["langs"].values()) or 1
    top = d["langs"].most_common(6)
    body, x, bar_w = "", 24, 302
    body += f'<clipPath id="c"><rect x="24" y="66" width="{bar_w}" height="10" rx="5"/></clipPath><g clip-path="url(#c)">'
    for i, (name, n) in enumerate(top):
        color = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        w = bar_w * n / total
        body += f'<rect x="{x:.1f}" y="66" width="{w:.1f}" height="10" fill="{color}"/>'
        x += w
    body += "</g>"
    for i, (name, n) in enumerate(top):
        color = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        col, row = i % 2, i // 2
        cx, cy = 24 + col * 160, 104 + row * 28
        body += f'<circle cx="{cx+5}" cy="{cy-4}" r="5" fill="{color}"/>'
        body += f'<text x="{cx+16}" y="{cy}" font-size="13" fill="{TEXT}">{escape(name)} <tspan fill="{MUTED}">{100*n/total:.1f}%</tspan></text>'
    return card(350, 200, "Most used languages", body)


def main():
    if "--demo" in sys.argv:
        d = {"name": "Demo", "repos": 12, "followers": 34, "stars": 56, "forks": 7,
             "langs": Counter({"TypeScript": 60000, "JavaScript": 25000, "C#": 18000, "HTML": 9000, "CSS": 5000, "Astro": 3000})}
    else:
        d = collect(os.environ["OWNER"], os.environ["GITHUB_TOKEN"])
    os.makedirs(OUT, exist_ok=True)
    out_dir = os.environ.get("STATS_OUT", OUT)
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "stats.svg"), "w", encoding="utf-8").write(stats_svg(d))
    open(os.path.join(out_dir, "languages.svg"), "w", encoding="utf-8").write(langs_svg(d))
    print("generated", out_dir)


if __name__ == "__main__":
    main()
