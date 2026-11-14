"""Confere as folhas vinculadas e os imports locais de cada tema e case."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IMPORT = re.compile(r"""@import\s+(?:url\(\s*)?["']?([^\s"');]+)""", re.I)


class Stylesheets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and "stylesheet" in attrs.get("rel", "").lower().split():
            self.links.append(attrs["href"])


def check_page(page, allowed):
    parser = Stylesheets()
    parser.feed(page.read_text())
    seen = set()

    def check(source, href):
        url = urlsplit(href)
        if url.scheme == "https" and url.netloc == "fonts.googleapis.com":
            return
        target = (source.parent / unquote(url.path)).resolve()
        if url.scheme or url.netloc or not target.is_relative_to(allowed) or not target.is_file():
            raise SystemExit(f"{source.relative_to(ROOT)}: folha fora de {allowed.relative_to(ROOT)} ou ausente: {href}")
        if target in seen:
            return
        seen.add(target)
        css = re.sub(r"/\*.*?\*/", "", target.read_text(), flags=re.S)
        for imported in IMPORT.findall(css):
            check(target, imported)

    for href in parser.links:
        check(page, href)
    if not seen:
        raise SystemExit(f"Página sem folha local: {page.relative_to(ROOT)}")


if __name__ == "__main__":
    for page in (ROOT / "projects").glob("*/index.html"):
        check_page(page, ROOT / "css/cases")
    for config in (ROOT / "themes").glob("*/theme.json"):
        check_page(config.with_name("index.html"), config.parent)
    print("CSS dos temas e dos cases isolado.")
