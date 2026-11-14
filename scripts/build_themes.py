#!/usr/bin/env python3
"""Gera as prévias locais dos temas. Passe --check para verificar sem gravar."""
import argparse
from html import escape
import re
from html.parser import HTMLParser
import json
import os
from pathlib import Path
from string import Template
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / "themes"
TEMPLATES = THEMES / "templates"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def render(template_file, **fields):
    return Template(template_file.read_text(encoding="utf-8").strip()).substitute(fields)


def project_fields(project, directory):
    fields = {k: escape(v) for k, v in project.items() if isinstance(v, str)}
    for key, field in (("path", "url"), ("image", "image")):
        target = ROOT / project[key]
        if not target.is_file():
            raise ValueError(f"Arquivo ausente: {target}")
        fields[field] = quote(os.path.relpath(target, directory))
    return fields


def generate(directory, content):
    config = read_json(directory / "theme.json")
    layout = config["layout"]
    if layout not in ("desktop", "editorial"):
        raise ValueError(f"Layout desconhecido em {directory}: {layout}")

    def template(name, fallback):
        local = directory / name
        return local if local.is_file() else TEMPLATES / fallback

    name = escape(content["name"])
    menu = content["menu"]
    switch_label = escape(menu["switch_theme"])
    switch_theme = (f'<form class="theme-switch" action="../../index.html" method="get">'
                    f'<button type="submit" name="trocar" value="{escape(directory.name)}">'
                    f'{switch_label}</button></form>')
    header = render(template("header.html", "header.html"), name=name, role=escape(content["role"]),
                    contact_label=escape(menu["contact"]),
                    switch_theme=switch_theme,
                    contact=f'<button class="tray" type="button" data-whatsapp hidden>{escape(menu["contact"])} ↗</button>')
    art = directory / "art.html"
    intro = render(template("intro.html", f"{layout}-intro.html"),
                   **{k: escape(v) for k, v in content["intro"].items()},
                   name=name, role=escape(content["role"]), presentation_label=escape(content["labels"]["presentation"]),
                   art=art.read_text().strip() if art.is_file() else "")

    fields = {}
    for section in ("featured", "experiment"):
        for key, value in project_fields(content[section], directory).items():
            fields[f"{section}_{key}"] = value
    cards = [render(TEMPLATES / f"{layout}-card.html", **project_fields(project, directory))
             for project in content["archive"]]
    labels = content["labels"]
    projects = render(template("projects.html", f"{layout}-projects.html"), **fields,
                      projects_label=escape(labels["projects"]), archive_label=escape(labels["archive"]),
                      latest=escape(labels["latest"]), cards="\n".join(cards),
                      tag_items="".join(f"<li>{escape(tag)}</li>" for tag in content["featured"]["tags"]),
                      tags=" · ".join(escape(tag) for tag in content["featured"]["tags"]))
    scripts = []
    if config.get("header_script"):
        scripts.append('<script src="../../js/header.js" defer></script>')
    if (directory / "menu.js").is_file():
        scripts.append('<script src="menu.js" defer></script>')
    body_attrs = f' class="{escape(config["body_class"])}"' if "body_class" in config else ""
    return render(TEMPLATES / "page.html", name=name, theme=escape(config["title"]),
                  body_attrs=body_attrs, header=header, intro=intro, projects=projects,
                  script="\n  ".join(scripts)) + "\n"


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.paths = []
        self.case_links = []
        self.words = []

    def handle_data(self, text):
        self.words.extend(text.split())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src", "action"):
            if key in attrs:
                self.paths.append(attrs[key])
        if "srcset" in attrs:
            self.paths.extend(candidate.strip().split()[0] for candidate in attrs["srcset"].split(","))
        if tag == "a" and not attrs["href"].startswith("#"):
            self.case_links.append(attrs["href"])


def validate(page, html, content):
    refs = References()
    refs.feed(html)
    for ref in refs.paths:
        url = urlsplit(ref)
        if url.path and not (page.parent / unquote(url.path)).is_file():
            raise ValueError(f"{page}: arquivo ausente: {ref}")
        if not url.path and url.fragment and url.fragment not in refs.ids:
            raise ValueError(f"{page}: âncora ausente: {ref}")
    projects = [content["featured"], *content["archive"], content["experiment"]]
    intro = content["intro"]
    required = [intro["description"], " ".join(intro[key] for key in ("before", "emphasis", "after")),
                *content["menu"].values(), *content["featured"]["tags"]]
    for project in projects:
        required.extend([project["name"], project["description"]])
        if "title" in project:
            required.append(project["title"])
    text = " ".join(refs.words)
    for phrase in required:
        if " ".join(phrase.split()) not in text:
            raise ValueError(f"{page}: texto ausente: {phrase}")
    expected = [(ROOT / item["path"]).resolve() for item in projects]
    actual = [(page.parent / unquote(ref)).resolve() for ref in refs.case_links]
    if list(dict.fromkeys(actual)) != expected:
        raise ValueError(f"{page}: os destinos ou a ordem dos cases divergem do conteúdo.")


def generate_home(pages, content):
    """Inline inert variants so the homepage also works under file:// and subpaths."""
    variants = []
    catalog = []
    fallback = None
    for page, html in pages.items():
        directory = page.parent
        slug = directory.name
        config = read_json(directory / "theme.json")
        # Rebase every local source, preserving responsive width/density descriptors.
        def from_root(match):
            attr, value = match.groups()
            if value.startswith("#"):
                return match.group(0)
            if attr == "srcset":
                candidates = []
                for candidate in value.split(","):
                    url, *descriptor = candidate.split()
                    path = os.path.normpath(directory.relative_to(ROOT) / url)
                    candidates.append(" ".join([path, *descriptor]))
                return f'srcset="{", ".join(candidates)}"'
            path = os.path.normpath(str(directory.relative_to(ROOT) / value))
            return f'{attr}="{path}"'

        body = html.split("<body", 1)[1].split(">", 1)[1].rsplit("</body>", 1)[0].strip()
        body = re.sub(r'\b(href|src|srcset|action)="([^"]+)"', from_root, body)
        scripts = re.findall(r'<script src="([^"]+)"', html)
        catalog.append({
            "id": slug, "style": f"themes/{slug}/theme.css",
            "bodyClass": config.get("body_class", ""),
            "scripts": [os.path.relpath(directory / src, ROOT) for src in scripts
                        if (directory / src).resolve() != ROOT / "js/contact.js"],
        })
        if slug == "atelie":
            fallback = body
        else:
            variants.append(f'<template data-theme id="theme-{escape(slug)}">\n{body}\n</template>')
    if fallback is None:
        raise ValueError("Tema Ateliê ausente")
    return render(TEMPLATES / "home.html", name=escape(content["name"]), role=escape(content["role"]),
                  description=escape(content["intro"]["description"]), catalog=json.dumps(catalog),
                  fallback=fallback, variants="\n".join(variants)) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = read_json(THEMES / "content.json")
    outputs = {}
    for config in sorted(THEMES.glob("*/theme.json")):
        page = config.parent / "index.html"
        outputs[page] = generate(config.parent, content)
        validate(page, outputs[page], content)
    count = len(outputs)
    outputs[ROOT / "index.html"] = generate_home(outputs, content)
    stale = [p for p, html in outputs.items() if not p.exists() or p.read_text() != html]
    if args.check and stale:
        raise SystemExit("Regenerar: " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
    for page in stale:
        page.write_text(outputs[page], encoding="utf-8")
    print(f"{count} temas verificados. {len(stale)} páginas atualizadas.")


if __name__ == "__main__":
    main()
