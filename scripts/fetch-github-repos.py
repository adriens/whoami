import json, subprocess, base64, csv, re
from pathlib import Path
from datetime import date

USERNAME = "adriens"
BASE = Path(f"data/github/{USERNAME}")
REPOS_DIR = BASE / "repos"
REPOS_DIR.mkdir(parents=True, exist_ok=True)

result = subprocess.run(
    ["gh", "repo", "list", USERNAME, "--limit", "300",
     "--json", "name,description,url,stargazerCount,createdAt,updatedAt,primaryLanguage,repositoryTopics,isArchived,isFork,isPrivate"],
    capture_output=True, text=True
)
all_repos = json.loads(result.stdout)

repos = [r for r in all_repos if not r["isFork"] and not r["isPrivate"]]
print(f"Repos to process: {len(repos)}")


def slugify(name):
    return re.sub(r'[^a-zA-Z0-9\-_]', '-', name).lower()


def fetch_readme(name):
    r = subprocess.run(
        ["gh", "api", f"repos/{USERNAME}/{name}/readme", "--jq", ".content"],
        capture_output=True, text=True
    )
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return base64.b64decode(r.stdout.strip()).decode("utf-8", errors="replace")
    except Exception:
        return None


processed = []
no_readme = []

for i, repo in enumerate(repos):
    name = repo["name"]
    slug = slugify(name)
    lang = repo.get("primaryLanguage") or {}
    lang_name = lang.get("name", "") if lang else ""
    topics = [t["name"] for t in (repo.get("repositoryTopics") or [])]
    stars = repo.get("stargazerCount", 0)
    created = repo.get("createdAt", "")[:10]
    updated = repo.get("updatedAt", "")[:10]
    desc = repo.get("description") or ""
    url = repo.get("url", "")
    archived = repo.get("isArchived", False)

    readme = fetch_readme(name)
    has_readme = readme is not None

    frontmatter = f"""---
name: {name}
url: {url}
description: "{desc.replace('"', '\\"')}"
language: {lang_name}
topics: [{', '.join(topics)}]
stars: {stars}
created_at: {created}
updated_at: {updated}
archived: {str(archived).lower()}
has_readme: {str(has_readme).lower()}
---

"""
    content = frontmatter + (readme.strip() if readme else "*No README*")
    (REPOS_DIR / f"{slug}.md").write_text(content, encoding="utf-8")

    processed.append({
        "slug": slug,
        "name": name,
        "url": url,
        "description": desc,
        "language": lang_name,
        "topics": ", ".join(topics),
        "stars": stars,
        "created_at": created,
        "updated_at": updated,
        "archived": archived,
        "has_readme": has_readme
    })
    if not has_readme:
        no_readme.append(name)

    if (i + 1) % 20 == 0:
        print(f"  {i+1}/{len(repos)} done...")

fieldnames = ["slug", "name", "url", "description", "language", "topics", "stars",
              "created_at", "updated_at", "archived", "has_readme"]
with open(BASE / "_index.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for r in sorted(processed, key=lambda x: x["updated_at"], reverse=True):
        writer.writerow(r)

stats = {
    "username": USERNAME,
    "profile_url": f"https://github.com/{USERNAME}",
    "repo_count": len(repos),
    "with_readme": len(repos) - len(no_readme),
    "without_readme": len(no_readme),
    "last_fetched": str(date.today())
}
with open(BASE / "_stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)

print(f"\nDone: {len(repos)} repos, {len(no_readme)} without README")
print(f"No README: {no_readme[:10]}{'...' if len(no_readme) > 10 else ''}")
