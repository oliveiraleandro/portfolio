#!/usr/bin/env python3
"""Generate all cases and home themes; --check validates without writing."""
import argparse
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

from site_content import ROOT, load_cases, load_home, render_case
from build_themes import build_outputs


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src', 'poster'):
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag == 'img' and 'alt' not in attrs:
            raise ValueError('Imagem sem atributo alt.')


def validate_outputs(outputs):
    parsed = {}
    def parse(path):
        if path not in parsed:
            parser = References()
            parser.feed(outputs[path] if path in outputs else path.read_text())
            parsed[path] = parser
        return parsed[path]
    for page in outputs:
        parser = parse(page)
        for ref in parser.references:
            url = urlsplit(ref)
            if url.scheme in ('http', 'https', 'mailto', 'tel') or url.netloc:
                continue
            if url.scheme:
                raise ValueError(f'{page.relative_to(ROOT)}: protocolo não permitido: {ref}')
            target = ((ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else
                      (page.parent / unquote(url.path))).resolve() if url.path else page
            if target.is_dir():
                target /= 'index.html'
            if not target.is_relative_to(ROOT) or (target not in outputs and not target.is_file()):
                raise ValueError(f'{page.relative_to(ROOT)}: arquivo ausente ou fora do site: {ref}')
            if url.fragment and target.suffix == '.html' and unquote(url.fragment) not in parse(target).ids:
                raise ValueError(f'{page.relative_to(ROOT)}: âncora ausente: {ref}')


def generate_outputs():
    cases = load_cases()
    if not cases:
        raise ValueError('Nenhum projects/*/content.md encontrado.')
    home = load_home(cases)
    outputs = {ROOT / 'projects' / slug / 'index.html': render_case(case, cases, home)
               for slug, case in cases.items()}
    outputs.update(build_outputs(home))
    validate_outputs(outputs)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        outputs = generate_outputs()
        stale = [path for path, value in outputs.items() if not path.exists() or path.read_text() != value]
        if args.check and stale:
            raise ValueError('Execute python3 scripts/build_site.py. Páginas desatualizadas: ' +
                             ', '.join(str(p.relative_to(ROOT)) for p in stale))
        for path in stale:
            path.write_text(outputs[path], encoding='utf-8')
        print(f'{len(outputs)} páginas verificadas; {len(stale)} atualizadas. Conteúdo, imagens e links válidos.')
    except (ValueError, KeyError, TypeError, FileNotFoundError) as error:
        raise SystemExit(f'Erro de conteúdo: {error}') from error


if __name__ == '__main__':
    main()
