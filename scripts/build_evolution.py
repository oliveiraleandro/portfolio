#!/usr/bin/env python3
"""Build the minimal Portuguese image timeline from the capture manifest."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'projects/portfolio-evolution'
data = json.loads((CASE / 'timeline.json').read_text())
asset = '../../public/images/cases/portfolio-evolution/'
visual = {'338d3e6', 'df69626', 'db2f11a', '965b240', '8c59af2', '585f05b', 'cfa01e6', 'd5d556e', '8c79505', '763e258', '4771bec', 'a95c60c', 'e41a75e'}


def preview(entry, device, label):
    images = entry['images']
    description = escape(f"Home em português — {entry['title']}, {label}")
    return f'''<figure class="evolution-{device}"><a class="figure-image-link" href="{asset}{images[device]}" aria-label="Ampliar: {description}"><img src="{asset}{images[device+'Viewport']}" width="{1440 if device=='desktop' else 390}" height="{1000 if device=='desktop' else 844}" loading="lazy" alt="{description}"></a></figure>'''


items = []
for entry in data['commits']:
    if entry['sha'][:7] not in visual:
        continue
    items.append(f'''<li class="evolution-step"><div class="evolution-captures">{preview(entry,'desktop','desktop')}</div></li>''')

references = ''.join(
    f'''<figure class="evolution-{device} evolution-reference"><a class="figure-image-link" href="{asset}2026-09-14-c623256-reference-{device}.webp" aria-label="Ampliar referência inicial de design, {label}"><img src="{asset}2026-09-14-c623256-reference-{device}.webp" loading="lazy" alt="Referência inicial de design da home, {label}; não é uma captura do site"></a></figure>'''
    for device, label in [('desktop', 'desktop')]
)
html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>A evolução do meu portfólio — Leandro Oliveira</title>
<meta name="description" content="Uma timeline visual da evolução do meu portfólio.">
<link rel="stylesheet" href="../../css/reset.css"><link rel="stylesheet" href="../../css/variables.css?v=unified-colors-1"><link rel="stylesheet" href="../../css/base.css"><link rel="stylesheet" href="../../css/layout.css"><link rel="stylesheet" href="../../css/components.css?v=experiment-strike-2"><link rel="stylesheet" href="../../css/responsive.css"><link rel="stylesheet" href="../../css/evolution.css?v=experiment-title-2">
  <link rel="stylesheet" href="../../css/header.css?v=sticky-2">
  <script src="../../js/header.js?v=sticky-1" defer></script>
</head><body><a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header container"><a class="identity" href="../../"><span>Leandro Oliveira</span><span class="role">Product Designer</span></a><div class="header-actions"><a class="text-link home-link" href="../../"><span aria-hidden="true">←</span> Página inicial</a></div></header>
<main id="conteudo"><article class="case portfolio-evolution">
<header class="case-hero container"><h1>Um portfólio também<br>é um <s class="evolution-strike" aria-hidden="true">produto</s> experimento.</h1><ul class="tags"><li>Design de interface</li><li>Desenvolvimento</li><li>Iteração</li></ul></header>
<div class="container"><ol class="evolution-timeline" aria-label="Evolução visual do portfólio">
<li class="evolution-step"><div class="evolution-captures">{references}</div></li>
{''.join(items)}</ol></div>
</article></main></body></html>'''
(CASE / 'index.html').write_text(html)
print('Built', CASE / 'index.html')
