#!/usr/bin/env python3
"""Render a single footer template into existing Portuguese and English footers.

Run after page generation. --check detects drift without modifying any files.
Pages without a footer (the image-only timeline) remain unchanged.
"""
import argparse
import html
import json
from pathlib import Path
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]
FOOTER = re.compile(r'<footer\b[^>]*\bid="contato"[^>]*>.*?</footer>', re.S)
STYLE = re.compile(r'\s*<link\b[^>]*href="[^"]*css/footer\.css[^\"]*"[^>]*>')


def apply_footer(content, page):
    if not FOOTER.search(content):
        return content
    template = (ROOT / 'templates/footer.html').read_text().rstrip()
    if page.startswith('en/'):
        catalog = json.loads((ROOT / 'translations/en-US.json').read_text())
        for text in ('WhatsApp', 'Ative o JavaScript para abrir o contato pelo WhatsApp.',
                     'Boas conversas também', 'constroem grandes produtos.'):
            template = template.replace(text, html.escape(catalog[text], quote=False))
    directory = posixpath.dirname(page) or '.'
    template = template.replace('{{icon}}', posixpath.relpath('projects/common/icons/whatsapp.svg', directory))
    content = FOOTER.sub(lambda _: template, content)
    stylesheet = posixpath.relpath('css/footer.css', directory)
    content = STYLE.sub('', content)
    return content.replace('</head>', f'\n  <link rel="stylesheet" href="{stylesheet}">\n</head>')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    pages = [ROOT/'index.html']
    if (ROOT/'en/index.html').is_file():
        pages.append(ROOT/'en/index.html')
    pages += sorted((ROOT/'projects').glob('*/index.html'))
    pages += sorted((ROOT/'en/projects').glob('*/index.html'))
    stale = []
    count = 0
    for path in pages:
        content = path.read_text()
        if not FOOTER.search(content):
            continue
        count += 1
        updated = apply_footer(content, path.relative_to(ROOT).as_posix())
        if content != updated:
            if args.check:
                stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(updated)
    if stale:
        raise SystemExit('Regenerate shared footer: ' + ', '.join(stale))
    print(f'{"Checked" if args.check else "Updated"} {count} shared footers.')


if __name__ == '__main__':
    main()
