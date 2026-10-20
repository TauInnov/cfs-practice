"""Rebuild the page list in README.md from the notebooks in pages/.

Runs in GitHub Actions on every push that touches pages/. The title of each
page is the first level-1 heading (a line starting with "# ") in its notebook.
"""
import json
import pathlib
import re

REPO = "TauInnov/cfs-practice"
BRANCH = "main"
ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- PAGES:START -->", "<!-- PAGES:END -->"


def title_of(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in "".join(cell.get("source", [])).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return path.stem


def main():
    pages = sorted((ROOT / "pages").glob("*.ipynb"))
    if pages:
        rows = ["| עמוד | הרצה | הורדה |", "|---|---|---|"]
        for p in pages:
            rel = f"pages/{p.name}"
            colab = f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/{rel}"
            badge = "https://colab.research.google.com/assets/colab-badge.svg"
            rows.append(f"| {title_of(p)} | [![Open in Colab]({badge})]({colab}) | [הורדה]({rel}) |")
        block = "\n".join(rows)
    else:
        block = "_עדיין לא נפתחו עמודים._"

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new = pattern.sub(f"{START}\n{block}\n{END}", text)
    if new != text:
        readme.write_text(new, encoding="utf-8")
        print(f"README updated: {len(pages)} page(s)")
    else:
        print("README unchanged")


if __name__ == "__main__":
    main()
