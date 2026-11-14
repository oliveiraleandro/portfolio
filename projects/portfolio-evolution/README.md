# Evolução do portfólio

Case em português: `projects/portfolio-evolution/index.html`.

- Intervalo: `c623256ca7cfdb8051e493cb3468a84eb90058d4` até `3cd2208`, de 14/09 a 14/11/2026.
- 22 commits registrados; 21 têm uma home renderizável. O primeiro tem `index.html` vazio e é apresentado como referência de design, nunca como screenshot de uma página funcional.
- Timeline somente visual, exibindo apenas desktop: referência inicial e 22 capturas de versões funcionais, sem títulos, datas, descrições ou SHAs visíveis. O histórico completo permanece em `timeline.json`.
- Imagens publicáveis: `public/images/cases/portfolio-evolution/`. O prefixo public é parte da URL neste site estático.
- `timeline.json` registra SHA completo, data autoral do Git, descrição, dimensões, navegador e arquivos das capturas.
- Cada captura foi refeita a partir de um export isolado do commit, sem mudar o checkout. São reconstruções atuais do código histórico, não imagens capturadas na data do commit.
- Português, escala 1, desktop 1440 × 1000 e celular 390 × 844, animações desativadas. Fontes e imagens são aguardadas; recursos quebrados interrompem a geração.
- Capturas completas e do viewport são salvas em WebP. PNGs originais ficam no diretório temporário informado pelo script; não são necessários para servir o site.
- O último marco reúne os seis temas do mesmo commit. Cada imagem vem da página individual do tema naquele export, evitando depender do sorteio da home. O marco do vídeo mostra o pôster com movimento reduzido.

## Reprodução

Requer Node.js, Python 3, Playwright, Sharp e Chrome. As dependências de captura não são necessárias na hospedagem. `NODE_PATH` pode apontar para uma instalação existente das dependências; `CHROME_PATH` define o executável do navegador.

```sh
node scripts/capture_evolution.cjs --desktop-only --commits 594104f,b18b050,7507658,3cd2208
python3 scripts/build_evolution.py
```

O script de captura usa `HEAD` como fim do intervalo. Antes de ampliar a timeline, revise as descrições em `capture_evolution.cjs` e os destaques em `build_evolution.py`. As referências iniciais WebP foram convertidas dos PNGs em `c623256:references/`.

A geração de inglês já falhava no HEAD anterior com uma tradução ausente (`Ver case completo — SEBRAE`). As traduções dos novos textos da home foram adicionadas ao catálogo, mas a sincronização das páginas inglesas continua pendente da revisão de traduções anteriores.
