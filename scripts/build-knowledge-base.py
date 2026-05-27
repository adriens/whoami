import argparse
import json
from datetime import date
from pathlib import Path

OUTPUT = Path("output/knowledge-base.md")
DATA = Path("data")
RESUME = Path("manual/resume.json")


def section(title: str, level: int = 2) -> str:
    return f"\n{'#' * level} {title}\n"


def build_resume(resume: dict) -> str:
    b = resume["basics"]
    lines = [section("Profil")]
    lines.append(f"**{b['name']}** — {b['label']}\n")
    lines.append(f"{b['summary']}\n")

    lines.append(section("Expérience", 3))
    for w in resume.get("work", []):
        end = w.get("endDate", "présent")
        lines.append(f"**{w['position']}** @ {w['name']} ({w['startDate']} → {end})")
        lines.append(f"{w['summary']}")
        for h in w.get("highlights", []):
            lines.append(f"- {h}")
        lines.append("")

    lines.append(section("Compétences", 3))
    for s in resume.get("skills", []):
        kw = ", ".join(s.get("keywords", []))
        lines.append(f"**{s['name']}** ({s['level']}) : {kw}")

    lines.append(section("Projets open source", 3))
    for p in resume.get("projects", []):
        name = p.get("name", "")
        url = p.get("url", "")
        desc = p.get("description", "")
        lines.append(f"**{name}** — {url}")
        lines.append(f"{desc}")
        for h in p.get("highlights", []):
            lines.append(f"- {h}")
        lines.append("")

    return "\n".join(lines)


def build_articles(data_dir: Path, lite: bool) -> str:
    articles_dir = data_dir / "dev_to"
    if not articles_dir.exists():
        return ""
    lines = [section("Articles DEV.to")]
    total = 0
    for user_dir in sorted(articles_dir.iterdir()):
        user = user_dir.name
        md_files = sorted((user_dir / "articles").glob("*.md")) if (user_dir / "articles").exists() else []
        if not md_files:
            continue
        lines.append(section(f"@{user} ({len(md_files)} articles)", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            if lite:
                # frontmatter uniquement
                lines.append(content.split("---\n\n")[0].strip() + "\n---")
            else:
                lines.append(content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} articles au total*\n")
    return "\n".join(lines)


def build_videos(data_dir: Path, lite: bool) -> str:
    youtube_dir = data_dir / "youtube"
    if not youtube_dir.exists():
        return ""
    lines = [section("Vidéos YouTube")]
    total = 0
    for channel_dir in sorted(youtube_dir.iterdir()):
        channel = channel_dir.name
        md_files = sorted((channel_dir / "videos").glob("*.md")) if (channel_dir / "videos").exists() else []
        if not md_files:
            continue
        lines.append(section(f"Chaîne : {channel} ({len(md_files)} vidéos)", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            if lite:
                lines.append(content.split("---\n\n")[0].strip() + "\n---")
            else:
                lines.append(content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} vidéos au total*\n")
    return "\n".join(lines)


def build_kaggle(data_dir: Path, lite: bool) -> str:
    kaggle_dir = data_dir / "kaggle"
    if not kaggle_dir.exists():
        return ""
    lines = [section("Datasets Kaggle")]
    total = 0
    for user_dir in sorted(kaggle_dir.iterdir()):
        md_files = sorted((user_dir / "datasets").glob("*.md")) if (user_dir / "datasets").exists() else []
        if not md_files:
            continue
        lines.append(section(f"@{user_dir.name} ({len(md_files)} datasets)", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            if lite:
                lines.append(content.split("---\n\n")[0].strip() + "\n---")
            else:
                lines.append(content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} datasets au total*\n")
    return "\n".join(lines)


def build_books(data_dir: Path, lite: bool) -> str:
    goodreads_dir = data_dir / "goodreads"
    if not goodreads_dir.exists():
        return ""
    lines = [section("Livres lus (Goodreads)")]
    total = 0
    for user_dir in sorted(goodreads_dir.iterdir()):
        md_files = sorted((user_dir / "books").glob("*.md")) if (user_dir / "books").exists() else []
        if not md_files:
            continue
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            if lite:
                lines.append(content.split("---\n\n")[0].strip() + "\n---")
            else:
                lines.append(content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} livres au total*\n")
    return "\n".join(lines)


def build_linkedin(data_dir: Path, lite: bool) -> str:
    linkedin_dir = data_dir / "linkedin"
    if not linkedin_dir.exists():
        return ""
    lines = [section("Articles LinkedIn Pulse")]
    total = 0
    for user_dir in sorted(linkedin_dir.iterdir()):
        md_files = sorted((user_dir / "articles").glob("*.md")) if (user_dir / "articles").exists() else []
        if not md_files:
            continue
        lines.append(section(f"@{user_dir.name} ({len(md_files)} articles)", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            if lite:
                lines.append(content.split("---\n\n")[0].strip() + "\n---")
            else:
                lines.append(content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} articles au total (dataset statique 2016–2021)*\n")
    return "\n".join(lines)


def build_github(data_dir: Path, lite: bool) -> str:
    github_dir = data_dir / "github"
    if not github_dir.exists():
        return ""
    lines = [section("Repos GitHub")]
    total = 0
    for user_dir in sorted(github_dir.iterdir()):
        md_files = sorted((user_dir / "repos").glob("*.md")) if (user_dir / "repos").exists() else []
        if not md_files:
            continue
        lines.append(section(f"@{user_dir.name} ({len(md_files)} repos)", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            if lite:
                lines.append(content.split("---\n\n")[0].strip() + "\n---")
            else:
                lines.append(content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} repos au total*\n")
    return "\n".join(lines)


def build_huggingface(data_dir: Path, lite: bool) -> str:
    hf_dir = data_dir / "huggingface"
    if not hf_dir.exists():
        return ""
    lines = [section("HuggingFace — Datasets & Spaces")]
    total_ds = 0
    total_sp = 0
    for author_dir in sorted(hf_dir.iterdir()):
        ds_files = sorted((author_dir / "datasets").glob("*.md")) if (author_dir / "datasets").exists() else []
        sp_files = sorted((author_dir / "spaces").glob("*.md")) if (author_dir / "spaces").exists() else []
        if not ds_files and not sp_files:
            continue
        lines.append(section(f"@{author_dir.name}", 3))
        if ds_files:
            lines.append(section("Datasets", 4))
            for md in ds_files:
                content = md.read_text(encoding="utf-8")
                lines.append(content.split("---\n\n")[0].strip() + "\n---" if lite else content.strip())
                lines.append("\n---\n")
                total_ds += 1
        if sp_files:
            lines.append(section("Spaces", 4))
            for md in sp_files:
                content = md.read_text(encoding="utf-8")
                lines.append(content.split("---\n\n")[0].strip() + "\n---" if lite else content.strip())
                lines.append("\n---\n")
                total_sp += 1
    lines.insert(1, f"*{total_ds} datasets, {total_sp} spaces au total*\n")
    return "\n".join(lines)


def build_stagiaires(data_dir: Path, lite: bool) -> str:
    stagiaires_dir = data_dir / "stagiaires"
    if not stagiaires_dir.exists():
        return ""
    lines = [section("Stagiaires & Projets tutorés")]
    total = 0
    for owner_dir in sorted(stagiaires_dir.iterdir()):
        if not owner_dir.is_dir():
            continue
        md_files = sorted((owner_dir / "stagiaires").glob("*.md")) if (owner_dir / "stagiaires").exists() else []
        if not md_files:
            continue
        lines.append(section(f"@{owner_dir.name}", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            lines.append(content.split("---\n\n")[0].strip() + "\n---" if lite else content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} stagiaires / projets tutorés au total*\n")
    return "\n".join(lines)


def build_iot(data_dir: Path, lite: bool) -> str:
    iot_dir = data_dir / "iot"
    if not iot_dir.exists():
        return ""
    lines = [section("IoT — Devices & Gadgets")]
    total = 0
    for owner_dir in sorted(iot_dir.iterdir()):
        if not owner_dir.is_dir():
            continue
        devices_dir = owner_dir / "devices"
        md_files = sorted(devices_dir.glob("*.md")) if devices_dir.exists() else []
        if not md_files:
            continue
        lines.append(section(f"@{owner_dir.name}", 3))
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            lines.append(content.split("---\n\n")[0].strip() + "\n---" if lite else content.strip())
            lines.append("\n---\n")
            total += 1
    lines.insert(1, f"*{total} devices au total*\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generer knowledge-base.md pour NotebookLM")
    parser.add_argument("--lite", action="store_true", help="Frontmatters uniquement, sans corps des articles")
    args = parser.parse_args()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    resume = json.loads(RESUME.read_text(encoding="utf-8"))
    mode = "lite" if args.lite else "full"

    parts = [
        f"# Adrien Sales — Knowledge Base ({mode})\n",
        f"*Généré le {date.today()}*\n",
        build_resume(resume),
        build_articles(DATA, lite=args.lite),
        build_videos(DATA, lite=args.lite),
        build_books(DATA, lite=args.lite),
        build_kaggle(DATA, lite=args.lite),
        build_huggingface(DATA, lite=args.lite),
        build_linkedin(DATA, lite=args.lite),
        build_github(DATA, lite=args.lite),
        build_iot(DATA, lite=args.lite),
        build_stagiaires(DATA, lite=args.lite),
    ]

    OUTPUT.write_text("\n".join(p for p in parts if p), encoding="utf-8")
    size_kb = OUTPUT.stat().st_size // 1024
    print(f"Done. {OUTPUT} ({size_kb} Ko, mode={mode})")


if __name__ == "__main__":
    main()
