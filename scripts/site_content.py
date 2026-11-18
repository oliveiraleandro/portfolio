"""Editorial sources: TOML front matter and a deliberately small Markdown subset."""
import json
import re
import tomllib
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def required_text(data, key, source):
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{source}: campo obrigatório vazio ou inválido: {key}')
    return value


def inline(text):
    """Escape raw HTML; allow emphasis, strike, links and explicit line breaks."""
    token = re.compile(r'\*\*(.+?)\*\*|\*(.+?)\*|_(.+?)_|~~(.+?)~~|\[([^\]\n]+)\]\(([^\s)]+)\)|  \n', re.S)
    result, position = [], 0
    for match in token.finditer(text):
        result.append(escape(text[position:match.start()]))
        strong, em, underscore, strike, label, url = match.groups()
        if strong is not None:
            result.append('<strong>' + inline(strong) + '</strong>')
        elif em is not None or underscore is not None:
            result.append('<em>' + inline(em if em is not None else underscore) + '</em>')
        elif strike is not None:
            result.append('<s class="evolution-strike" aria-hidden="true">' + inline(strike) + '</s>')
        elif url is not None:
            if urlsplit(url).scheme not in ('', 'http', 'https', 'mailto', 'tel') or url.startswith('//'):
                raise ValueError(f'Protocolo de link não permitido: {url}')
            result.append(f'<a href="{escape(url)}">{inline(label)}</a>')
        else:
            result.append('<br>')
        position = match.end()
    result.append(escape(text[position:]))
    return ''.join(result)


def blocks(text):
    rendered = []
    for block in re.split(r'\n\s*\n', text.strip()):
        if not block.strip():
            continue
        heading = re.fullmatch(r'(#{2,3}) (.+)', block)
        if heading:
            level = len(heading[1])
            rendered.append(f'<h{level}>{inline(heading[2])}</h{level}>')
        elif re.search(r'^(?:#{1,6} |[-*+] |\d+\. |```|>|\|)', block, re.M):
            raise ValueError('Use parágrafos, ## subtítulos e ### subtítulos menores; listas, tabelas e blocos de código não são suportados.')
        else:
            rendered.append('<p>' + inline(block) + '</p>')
    return '\n'.join(rendered)


def read_case(path):
    try:
        raw = path.read_text(encoding='utf-8')
        if not raw.startswith('+++\n'):
            raise ValueError('O arquivo deve começar com +++ e os campos TOML.')
        header, markdown = raw[4:].split('\n+++\n', 1)
        data = tomllib.loads(header)
        for key in ('name', 'page_title', 'description'):
            required_text(data, key, path)
        tags = data.get('tags')
        if not isinstance(tags, list) or not tags or any(not isinstance(t, str) or not t.strip() for t in tags):
            raise ValueError('tags deve conter textos não vazios.')
        card = data.get('card')
        if not isinstance(card, dict):
            raise ValueError('Seção [card] ausente.')
        for key in ('description', 'image'):
            required_text(card, key, path)
        markdown = markdown.strip()
        title, body = markdown.split('\n\n', 1)
        if not title.startswith('# ') or not title[2:].strip() or not body.strip():
            raise ValueError('Informe # Título, uma linha em branco e os parágrafos do case.')
        data['title'] = title[2:]
        data['body'] = body
        data['slug'] = path.parent.name
        if not SLUG.fullmatch(data['slug']):
            raise ValueError('Identificador do case inválido.')
        if 'next' in data and not SLUG.fullmatch(data['next']):
            raise ValueError('Identificador de próximo case inválido.')
        # Validate the Markdown before any outputs are written.
        inline(data['title'])
        blocks(body)
        return data
    except (ValueError, TypeError, KeyError) as error:
        raise ValueError(f'{path.relative_to(ROOT)}: {error}') from error


def load_cases():
    return {p.parent.name: read_case(p) for p in sorted((ROOT / 'projects').glob('*/content.md'))}


def load_home(cases=None):
    cases = load_cases() if cases is None else cases
    home = json.loads((ROOT / 'themes/content.json').read_text())
    for key in ('name', 'role'):
        required_text(home, key, 'themes/content.json')
    for section, keys in (('intro', ('before', 'emphasis', 'after', 'description')),
                          ('menu', ('contact', 'switch_theme')),
                          ('labels', ('projects', 'archive', 'latest', 'presentation'))):
        for key in keys:
            required_text(home[section], key, f'themes/content.json [{section}]')
    def card(slug):
        if not isinstance(slug, str) or slug not in cases:
            raise ValueError(f'themes/content.json: case desconhecido: {slug}')
        case = cases[slug]
        return {**case['card'], 'name': case['name'], 'tags': case['tags'],
                'path': f'projects/{slug}/index.html'}
    slugs = [home['featured'], *home['archive'], home['experiment']]
    if len(slugs) != len(set(slugs)):
        raise ValueError('themes/content.json: projetos repetidos na home.')
    for key in ('featured', 'experiment'):
        home[key] = card(home[key])
        for field in ('title', 'alt'):
            required_text(home[key], field, f'card do {key}')
    home['archive'] = [card(slug) for slug in home['archive']]
    return home


def render_case(case, cases, home):
    from build_footer import apply_footer
    slug = case['slug']
    template = Template((ROOT / 'templates/cases' / f'{slug}.html').read_text())
    fields = {key: escape(value) for key, value in case.items() if isinstance(value, str)}
    fields.update(site_name=escape(home['name']), site_role=escape(home['role']),
                  title=inline(case['title']), tags=''.join(f'<li>{escape(t)}</li>' for t in case['tags']))
    body = case['body']
    if '$lead' in template.template:
        lead, separator, body = body.partition('\n\n')
        if not separator or lead.startswith('#'):
            raise ValueError(f'{slug}: informe abertura e pelo menos um parágrafo de desenvolvimento.')
        fields['lead'] = inline(lead)
    fields['body'] = blocks(body)
    for section in ('captions', 'accessibility'):
        values = case.get(section, {})
        expected = {key for key in template.get_identifiers() if key.startswith('caption_' if section == 'captions' else 'alt_')}
        if set(values) != expected:
            raise ValueError(f'{slug}: campos de {section} diferem do template: {sorted(set(values) ^ expected)}')
        for key in values:
            fields[key] = escape(required_text(values, key, slug))
    if 'next' in case:
        if case['next'] not in cases:
            raise ValueError(f'{slug}: próximo case inexistente: {case["next"]}')
        fields['next_url'] = f'../{case["next"]}/'
        fields['next_name'] = escape(cases[case['next']]['name'])
    if '$timeline' in template.template:
        from build_evolution import render_timeline
        fields['timeline'] = render_timeline()
    fields['footer'] = '<footer id="contato"></footer>'
    result = template.substitute(fields)
    result = apply_footer(result, f'projects/{slug}/index.html')
    return result
