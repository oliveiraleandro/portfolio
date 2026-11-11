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
<div class="container">
<section class="story-section" id="experimento-com-ia">
<h2>Onde a IA me ajudou no redesign</h2>
<p>Estudo IA no meu tempo livre e na minha segunda graduação. Como já assinava o ChatGPT, decidi usá-lo o máximo possível no redesign do meu portfólio. Queria descobrir, na prática, até onde eu conseguia ir com ele.</p>
<p>Comecei com pedidos bem abertos e usei como referência imagens de interfaces que eu mesmo tinha desenhado. Assim, pude explorar ideias sem montar um protótipo no Figma para cada uma. Nas imagens, a composição me convencia: os elementos pareciam funcionar bem juntos. Quando eu navegava pela página, nem sempre encontrava a mesma harmonia.</p>
<p>À medida que fui definindo a paleta, ficou mais difícil pedir ajustes pequenos. Às vezes eu já sabia qual cor queria testar, mas dava trabalho explicar a diferença entre aquele tom e o que estava na tela. Como o portfólio é estático e eu conheço HTML e CSS, passei a trocar os valores de cor direto no código.</p>
<p>Trocar um valor leva segundos. Escolher o tom que eu quero manter pode levar bem mais tempo, e gosto de ter esse tempo para comparar. É nessas pequenas escolhas que consigo sair da solução mais previsível e dar ao portfólio a minha cara.</p>
</section>
<ol class="evolution-timeline" aria-label="Evolução visual do portfólio">
<li class="evolution-step"><div class="evolution-captures">{references}</div></li>
{''.join(items)}</ol></div>
</article></main></body></html>'''
(CASE / 'index.html').write_text(html)
print('Built', CASE / 'index.html')
