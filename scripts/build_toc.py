"""Write _toc.yml from the notebooks currently in pages/.

Runs in the build Action, so releasing a page is just adding its file to pages/.
Pages appear in file-name order; each title is the first level-1 heading in the notebook.
"""
import json
import pathlib

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


def main():
    pages = sorted((ROOT / "pages").glob("*.ipynb"))
    lines = ["format: jb-book", "root: intro"]
    if pages:
        lines.append("chapters:")
        for p in pages:
            title = title_of(p).replace('"', "'")
            lines.append(f'  - file: pages/{p.stem}')
            lines.append(f'    title: "{title}"')
    (ROOT / "_toc.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"_toc.yml: {len(pages)} page(s)")


if __name__ == "__main__":
    main()
