from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART_DIR = ROOT / "art"
TEMPLATE = ROOT / "site" / "index.template.html"
OUTPUT_DIR = ROOT / "_site"
OUTPUT = OUTPUT_DIR / "index.html"

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")
MAX_LINES = 20
MAX_LINE_LENGTH = 120


def validate_art(path: Path, content: str) -> None:
    username = path.stem
    if not USERNAME_PATTERN.fullmatch(username):
        raise ValueError(
            f"{path}: filename must be a GitHub-style username, e.g. art/octocat.txt"
        )

    lines = content.splitlines()
    if not lines:
        raise ValueError(f"{path}: artwork must not be empty")
    if len(lines) > MAX_LINES:
        raise ValueError(f"{path}: maximum is {MAX_LINES} lines")
    if any(len(line) > MAX_LINE_LENGTH for line in lines):
        raise ValueError(f"{path}: lines may contain at most {MAX_LINE_LENGTH} characters")


def render_card(path: Path) -> str:
    username = path.stem
    content = path.read_text(encoding="utf-8").rstrip()
    validate_art(path, content)
    safe_username = html.escape(username)
    safe_content = html.escape(content)
    return f'''        <article class="art-card">
            <h3>@{safe_username}</h3>
<pre>{safe_content}</pre>
        </article>'''


def main() -> None:
    cards = [render_card(path) for path in sorted(ART_DIR.glob("*.txt"))]
    template = TEMPLATE.read_text(encoding="utf-8")
    page = template.replace("{{GALLERY}}", "\n\n".join(cards))
    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"Built {OUTPUT} with {len(cards)} contribution(s).")


if __name__ == "__main__":
    main()
