#!/usr/bin/env python3
"""Write live GitHub stats into the profile README as plain Markdown.

No images and no third-party services: the numbers come from the GitHub API
(with the workflow's built-in GITHUB_TOKEN) and are written between the
<!--START_STATS--> and <!--END_STATS--> markers in README.md.

    python scripts/generate_stats.py          # real data (needs GITHUB_TOKEN, OWNER)
    python scripts/generate_stats.py --demo   # sample data, prints the block
"""
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from datetime import date

API = "https://api.github.com"
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
START, END = "<!--START_STATS-->", "<!--END_STATS-->"
LEVEL = {"NONE": "⬛", "FIRST_QUARTER": "🟩", "SECOND_QUARTER": "🟨",
         "THIRD_QUARTER": "🟧", "FOURTH_QUARTER": "🟥"}
WEEKS_SHOWN = 26

GQL = """
query($login:String!){ user(login:$login){ contributionsCollection{
  totalCommitContributions totalPullRequestContributions
  totalIssueContributions totalPullRequestReviewContributions
  contributionCalendar{ totalContributions weeks{ contributionDays{
    date contributionCount contributionLevel weekday } } } } } }
"""


def _request(url, token, data=None):
    req = urllib.request.Request(
        url, data=data,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "User-Agent": "profile-stats", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def rest(path, token):
    return _request(f"{API}{path}", token)


def graphql(login, token):
    body = json.dumps({"query": GQL, "variables": {"login": login}}).encode()
    out = _request(f"{API}/graphql", token, body)
    if out.get("errors"):
        raise RuntimeError(out["errors"])
    return out["data"]["user"]["contributionsCollection"]


def collect(owner, token):
    user = rest(f"/users/{owner}", token)
    repos, page = [], 1
    while True:
        chunk = rest(f"/users/{owner}/repos?per_page=100&type=owner&page={page}", token)
        repos += chunk
        if len(chunk) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]
    langs = Counter()
    for r in own:
        try:
            langs.update(rest(f"/repos/{owner}/{r['name']}/languages", token))
        except Exception as e:  # keep going if one repo fails
            print("languages failed for", r["name"], e)
    data = {"repos": user["public_repos"], "followers": user["followers"],
            "stars": sum(r["stargazers_count"] for r in own),
            "forks": sum(r["forks_count"] for r in own), "langs": langs, "contrib": None}
    try:
        data["contrib"] = graphql(owner, token)
    except Exception as e:
        print("contributions unavailable:", e)
    return data


def streaks(days):
    longest = run = 0
    for d in days:
        run = run + 1 if d["contributionCount"] > 0 else 0
        longest = max(longest, run)
    current = 0
    for d in reversed(days):
        if d["contributionCount"] > 0:
            current += 1
        elif d is days[-1]:
            continue  # today may not have contributions yet
        else:
            break
    return current, longest


def heatmap(weeks):
    weeks = weeks[-WEEKS_SHOWN:]
    names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    rows = []
    for wd in range(7):
        cells = []
        for w in weeks:
            day = next((d for d in w["contributionDays"] if d["weekday"] == wd), None)
            cells.append(LEVEL.get(day["contributionLevel"], "⬛") if day else "⬛")
        label = names[wd] if wd in (1, 3, 5) else "   "
        rows.append(f"{label} {''.join(cells)}")
    return "\n".join(rows)


def bar(pct, width=14):
    filled = round(width * pct / 100)
    return "█" * filled + "░" * (width - filled)


def render(d):
    out = ["<div align=\"center\">", ""]
    out += ["| 📦 Public repos | ⭐ Stars earned | 👥 Followers | 🍴 Forks |",
            "|:-:|:-:|:-:|:-:|",
            f"| **{d['repos']}** | **{d['stars']}** | **{d['followers']}** | **{d['forks']}** |", ""]
    c = d["contrib"]
    if c:
        cal = c["contributionCalendar"]
        days = [x for w in cal["weeks"] for x in w["contributionDays"]]
        cur, longest = streaks(days)
        out += ["| 🔥 Contributions (last year) | 💾 Commits | 🔀 Pull requests | 🐞 Issues | 👀 Reviews | ⚡ Current streak | 🏆 Longest streak |",
                "|:-:|:-:|:-:|:-:|:-:|:-:|:-:|",
                f"| **{cal['totalContributions']}** | **{c['totalCommitContributions']}** | "
                f"**{c['totalPullRequestContributions']}** | **{c['totalIssueContributions']}** | "
                f"**{c['totalPullRequestReviewContributions']}** | **{cur} {"day" if cur == 1 else "days"}** | **{longest} {"day" if longest == 1 else "days"}** |", ""]
        out += [f"**Contribution activity** · last {WEEKS_SHOWN} weeks", "", "```text",
                heatmap(cal["weeks"]), "```",
                "<sub>⬛ none · 🟩 low · 🟨 medium · 🟧 high · 🟥 very high</sub>", ""]
    total = sum(d["langs"].values()) or 1
    top = d["langs"].most_common(6)
    if top:
        out += ["**Most used languages**", "", "| Language | Usage | |", "|:--|:--|--:|"]
        for name, n in top:
            pct = 100 * n / total
            out.append(f"| {name} | `{bar(pct)}` | {pct:.1f}% |")
        out.append("")
    out += [f"<sub>Updated automatically on {date.today().isoformat()} by a GitHub Actions workflow in this repo.</sub>",
            "", "</div>"]
    return "\n".join(out)


def main():
    if "--demo" in sys.argv:
        import random
        random.seed(3)
        weeks = []
        for w in range(53):
            weeks.append({"contributionDays": [
                {"date": f"2026-01-{(w*7+i)%28+1:02d}", "weekday": i,
                 "contributionCount": (n := random.choice([0, 0, 0, 1, 3, 6, 11])),
                 "contributionLevel": ["NONE", "FIRST_QUARTER", "SECOND_QUARTER", "THIRD_QUARTER", "FOURTH_QUARTER"][0 if n == 0 else 1 if n < 2 else 2 if n < 4 else 3 if n < 8 else 4]}
                for i in range(7)]})
        d = {"repos": 12, "stars": 6, "followers": 5, "forks": 2,
             "langs": Counter({"TypeScript": 60000, "JavaScript": 25000, "C#": 18000, "HTML": 9000}),
             "contrib": {"totalCommitContributions": 480, "totalPullRequestContributions": 22,
                         "totalIssueContributions": 4, "totalPullRequestReviewContributions": 7,
                         "contributionCalendar": {"totalContributions": 513, "weeks": weeks}}}
        print(render(d))
        return
    d = collect(os.environ["OWNER"], os.environ["GITHUB_TOKEN"])
    block = f"{START}\n{render(d)}\n{END}"
    text = open(README, encoding="utf-8").read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit("Markers not found in README.md")
    open(README, "w", encoding="utf-8").write(pattern.sub(lambda m: block, text))
    print("README updated")


if __name__ == "__main__":
    main()
