"""Write _toc.yml from the notebooks currently in pages/, grouped into weeks by weeks.yml.

Runs in the build Action, so releasing a page is just adding its file to pages/.

weeks.yml lists, per week, a landing page (weeks/weekN.md, its title is the first heading) and the page file stems
that belong to it. A page that is listed but not released yet is skipped. A released page that no week lists is still
shown, after the weeks, so nothing disappears silently. Page titles are the first level-1 heading of each notebook.
"""
import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


def title_of(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in "".join(cell.get("source", [])).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return path.stem


def entry(p, indent):
    title = title_of(p).replace('"', "'")
    return [f"{indent}- file: pages/{p.stem}", f'{indent}  title: "{title}"']


def main():
    pages = {p.stem: p for p in sorted((ROOT / "pages").glob("*.ipynb"))}
    weeks_file = ROOT / "weeks.yml"
    weeks = (yaml.safe_load(weeks_file.read_text(encoding="utf-8")) or {}).get("weeks", []) if weeks_file.exists() else []
    lines = ["format: jb-book", "root: intro"]
    used = set()
    body = []
    for w in weeks:
        landing = ROOT / (w["file"] + ".md")
        if not landing.exists():
            raise SystemExit(f"weeks.yml: {landing.name} does not exist")
        present = [pages[s] for s in w.get("pages", []) if s in pages]
        used.update(p.stem for p in present)
        body.append(f"  - file: {w['file']}")
        if present:
            body.append("    sections:")
            for p in present:
                body += entry(p, "      ")
    rest = [p for s, p in pages.items() if s not in used]
    for p in rest:
        body += entry(p, "  ")
    if rest:
        print("note: not listed in weeks.yml:", ", ".join(p.stem for p in rest))
    if body:
        lines.append("chapters:")
        lines += body
    (ROOT / "_toc.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"_toc.yml: {len(pages)} page(s), {len(weeks)} week(s)")


if __name__ == "__main__":
    main()
