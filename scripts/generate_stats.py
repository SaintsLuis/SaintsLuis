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

# Only count the languages I actually write by hand. GitHub also reports generated or
# platform code (e.g. LLVM, Java/Kotlin from android/ folders), which would skew the result.
LANGUAGES = {"TypeScript", "JavaScript", "C#", "HTML", "CSS", "SCSS", "Astro"}

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


def plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def render(d):
    c = d["contrib"]
    heads = ["📦 Repos", "⭐ Stars", "👥 Followers"]
    vals = [d["repos"], d["stars"], d["followers"]]
    if c:
        cal = c["contributionCalendar"]
        days = [x for w in cal["weeks"] for x in w["contributionDays"]]
        cur, longest = streaks(days)
        heads += ["🔥 Contributions (last year)", "⚡ Streak", "🏆 Best streak"]
        vals += [cal["totalContributions"], plural(cur, "day"), plural(longest, "day")]
    out = ['<div align="center">', "",
           "| " + " | ".join(heads) + " |",
           "|" + ":-:|" * len(heads),
           "| " + " | ".join(f"**{v}**" for v in vals) + " |", ""]
    langs = Counter({k: v for k, v in d["langs"].items() if k in LANGUAGES})
    total = sum(langs.values())
    if total:
        parts = [f"{name} **{100 * n / total:.0f}%**" for name, n in langs.most_common(5)]
        out += ["**Top languages:** " + " · ".join(parts), ""]
    out += [f"<sub>Updated automatically on {date.today().isoformat()}.</sub>", "", "</div>"]
    return "\n".join(out)


def main():
    if "--demo" in sys.argv:
        days = [{"contributionCount": n} for n in [0, 2, 3, 0, 1, 4, 0, 0, 5, 1]]
        d = {"repos": 29, "stars": 6, "followers": 5, "forks": 2,
             "langs": Counter({"TypeScript": 60000, "JavaScript": 25000, "LLVM": 90000, "Java": 70000,
                               "C#": 18000, "HTML": 9000}),
             "contrib": {"contributionCalendar": {"totalContributions": 50, "weeks": [{"contributionDays": days}]}}}
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
