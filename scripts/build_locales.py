#!/usr/bin/env python3
"""Generate English pages from Portuguese HTML and a reviewed text catalog.

Run from any directory. --check verifies translations and generated files without
writing. The published site remains plain HTML/CSS/JS and needs no runtime build.
"""

import argparse
from build_footer import apply_footer
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index.html",) + tuple(
    f"projects/{name}/index.html" for name in ("sebrae", "sinapse", "cervello", "iconatus")
)
SWITCHER = re.compile(r'<nav class="language-switcher".*?</nav>', re.S)
METADATA = re.compile(r'\n<!-- locale:start -->.*?<!-- locale:end -->\n', re.S)
PLACEHOLDER = "<!-- language-switcher -->"


def relative(target, current):
    """Keep routes relative so the site also works in a hosting subdirectory."""
    result = posixpath.relpath(target, posixpath.dirname(current) or ".")
    if result == "index.html":
        return "./"
    if result.endswith("/index.html"):
        return result[:-len("index.html")]
    return result


class EnglishPage(HTMLParser):
    def __init__(self, source, catalog):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.destination = "en/" + source
        self.catalog = catalog
        self.output = []

    def translate(self, value):
        key = html.unescape(value).strip()
        if not key:
            return value
        translation = self.catalog.get(key)
        if not isinstance(translation, str) or not translation.strip():
            raise ValueError(f"{self.source}: missing translation for {key!r}")
        leading = value[:len(value) - len(value.lstrip())]
        trailing = value[len(value.rstrip()):]
        return leading + html.escape(translation, quote=False) + trailing

    def local_url(self, value):
        url = urlsplit(value)
        if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            return value
        target = posixpath.normpath(posixpath.join(posixpath.dirname(self.source), url.path))
        page = posixpath.normpath(posixpath.join(target, "index.html")) if url.path.endswith("/") else target
        if page in PAGES:
            target = "en/" + page
        # Assets continue to point to their original location, outside /en/.
        return urlunsplit(("", "", relative(target, self.destination), url.query, url.fragment))

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        replacements = {}
        for name, value in attrs:
            if value is None:
                continue
            if name in ("alt", "aria-label") or (
                tag == "meta" and name == "content" and (
                    values.get("name") == "description" or
                    values.get("property") in ("og:title", "og:description")
                )
            ):
                replacements[name] = html.unescape(self.translate(value))
            elif name in ("href", "src"):
                replacements[name] = self.local_url(value)
            elif tag == "html" and name == "lang":
                replacements[name] = "en-US"
        raw = self.get_starttag_text()
        for name, value in replacements.items():
            raw = re.sub(
                rf'(\s{re.escape(name)}\s*=\s*)([\"\'])(.*?)\2',
                lambda m: m[1] + '"' + html.escape(value, quote=True) + '"',
                raw, flags=re.S | re.I,
            )
        self.output.append(raw)

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(self.translate(data))

    def handle_comment(self, data):
        self.output.append(f"<!--{data}-->")

    def handle_decl(self, data):
        self.output.append(f"<!{data}>")

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")


def add_locale_controls(content, source, english):
    current = ("en/" if english else "") + source
    pt = relative(source, current)
    en = relative("en/" + source, current)
    # Each link has its own lang attribute, so its accessible name must use
    # that language too. aria-current already announces the selected option.
    labels = (
        "Site language" if english else "Idioma do site",
        "Português (Brasil)",
        "English (United States)",
    )
    links = []
    for lang, name, href, active, label in (
        ("pt-BR", "Português", pt, not english, labels[1]),
        ("en-US", "English", en, english, labels[2]),
    ):
        state = ' aria-current="page"' if active else ' data-language-switch'
        links.append(
            f'      <a class="language-option" href="{href}" lang="{lang}" '
            f'hreflang="{lang}"{state} aria-label="{label}">{name}</a>'
        )
    nav = f'<nav class="language-switcher" aria-label="{labels[0]}">\n' + "\n".join(links) + '\n    </nav>'
    content = content.replace(PLACEHOLDER, nav)
    metadata = (
        '\n<!-- locale:start -->\n'
        f'  <link rel="alternate" hreflang="pt-BR" href="{pt}">\n'
        f'  <link rel="alternate" hreflang="en-US" href="{en}">\n'
        f'  <meta property="og:locale" content="{"en_US" if english else "pt_BR"}">\n'
        f'  <meta property="og:locale:alternate" content="{"pt_BR" if english else "en_US"}">\n'
        f'  <script src="{relative("js/language.js", current)}" defer></script>\n'
        '<!-- locale:end -->\n'
    )
    return content.replace("</head>", metadata + "</head>")


def generate():
    catalog = json.loads((ROOT / "translations/en-US.json").read_text())
    outputs = {}
    for source in PAGES:
        content = METADATA.sub("", apply_footer((ROOT / source).read_text(), source))
        content, count = SWITCHER.subn(PLACEHOLDER, content)
        if count != 1:
            raise ValueError(f"{source}: expected exactly one language switcher")
        parser = EnglishPage(source, catalog)
        parser.feed(content)
        parser.close()
        outputs[source] = add_locale_controls(content, source, False)
        outputs["en/" + source] = add_locale_controls("".join(parser.output), source, True)
    return outputs


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--check", action="store_true")
    options = args.parse_args()
    # Render everything before writing, so missing translations cause no partial update.
    outputs = generate()
    stale = []
    for name, content in outputs.items():
        path = ROOT / name
        if options.check:
            if not path.exists() or path.read_text() != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    if stale:
        raise SystemExit("Regenerate localized pages: " + ", ".join(stale))
    print(f"{'Checked' if options.check else 'Generated'} {len(outputs)} pages; all translations present.")


if __name__ == "__main__":
    main()
