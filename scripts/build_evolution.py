#!/usr/bin/env python3
"""Build the minimal Portuguese image timeline from the capture manifest."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'projects/portfolio-evolution'
data = json.loads((CASE / 'timeline.json').read_text())
asset = '../../public/images/cases/portfolio-evolution/'
visual = {'338d3e6', 'df69626', 'db2f11a', '965b240', '8c59af2', '585f05b', 'cfa01e6', 'd5d556e', '8c79505', '763e258', '4771bec', 'a95c60c', 'e41a75e', '594104f', 'b18b050', '7507658', '3cd2208'}


def preview(entry, device, label):
    images = entry['images']
    description = escape(f"Home em português — {entry['title']}, {label}")
    return f'''<figure class="evolution-{device}"><a class="figure-image-link" href="{asset}{images[device]}" target="_blank" rel="noopener" aria-label="Ampliar: {description}"><img src="{asset}{images[device+'Viewport']}" width="{1440 if device=='desktop' else 390}" height="{1000 if device=='desktop' else 844}" loading="lazy" alt="{description}"></a></figure>'''


items = []
for entry in data['commits']:
    if entry['sha'][:7] not in visual:
        continue
    captures = ''.join(preview(view, 'desktop', 'desktop') for view in entry.get('themes', [entry]))
    items.append(f'<li class="evolution-step"><div class="evolution-captures">{captures}</div></li>')

references = ''.join(
    f'''<figure class="evolution-{device} evolution-reference"><a class="figure-image-link" href="{asset}2026-09-14-c623256-reference-{device}.webp" target="_blank" rel="noopener" aria-label="Ampliar referência inicial de design, {label}"><img src="{asset}2026-09-14-c623256-reference-{device}.webp" loading="lazy" alt="Referência inicial de design da home, {label}; não é uma captura do site"></a></figure>'''
    for device, label in [('desktop', 'desktop')]
)
html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>A evolução do meu portfólio — Leandro Oliveira</title>
  <link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon.png">
<meta name="description" content="As imagens mostram como o desenho do meu portfólio mudou ao longo do tempo.">
  <link rel="stylesheet" href="../../css/cases/base.css">
  <link rel="stylesheet" href="../../css/cases/header.css">
  <link rel="stylesheet" href="../../css/cases/article.css">
  <link rel="stylesheet" href="../../css/cases/evolution.css">
  <script src="../../js/header.js?v=sticky-1" defer></script>
</head><body><a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header container"><a class="identity" href="../../"><span>Leandro Oliveira</span><span class="role">Product Designer</span></a><div class="header-actions"><a class="text-link home-link" href="../../"><span aria-hidden="true">←</span> Página inicial</a></div></header>
<main id="conteudo"><article class="case portfolio-evolution">
<header class="case-hero container"><h1>Um portfólio também<br>é um <s class="evolution-strike" aria-hidden="true">produto</s> experimento.</h1><ul class="tags"><li>Design de interface</li><li>Desenvolvimento</li><li>Iteração</li></ul>
<div class="case-intro" id="experimento-com-ia">
<p>Estudo inteligência artificial no meu tempo livre e na minha segunda graduação. Quando decidi redesenhar este portfólio, já assinava o ChatGPT. Aproveitei o projeto para experimentar em quais decisões de design ele poderia me ajudar.</p>
<p>Mostrei ao ChatGPT algumas interfaces que eu havia desenhado e deixei em aberto como organizar a página. Assim, pude comparar várias composições antes de montar um protótipo no Figma. Algumas pareciam equilibradas quando eu via a imagem inteira. Ao percorrer a página, percebia que os elementos já não funcionavam tão bem juntos.</p>
<p>Na hora de escolher as cores, passei a trabalhar diretamente no código. Como conheço HTML e CSS, podia trocar um tom e conferir o resultado na própria página. Gosto de dedicar tempo a essa escolha. Ver a cor junto do texto e das imagens me ajuda a decidir se quero mantê-la.</p>
</div></header>
<div class="container">
<ol class="evolution-timeline" aria-label="Evolução visual do portfólio">
<li class="evolution-step"><div class="evolution-captures">{references}</div></li>
{''.join(items)}</ol></div>
</article></main></body></html>'''
(CASE / 'index.html').write_text(html)
print('Built', CASE / 'index.html')
