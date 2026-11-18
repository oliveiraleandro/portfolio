# Como atualizar os textos

A home e os seis cases têm fontes de conteúdo separadas do layout. Você não precisa editar HTML. Requer Python 3.11 ou mais recente, sem instalar pacotes.

## Onde editar

| O que mudar | Arquivo / campo |
| --- | --- |
| Nome, profissão, apresentação, menu e rótulos da home | `themes/content.json` |
| Projeto em destaque | `featured` em `themes/content.json` |
| Ordem dos projetos anteriores | Lista `archive` em `themes/content.json` |
| Projeto do experimento | `experiment` em `themes/content.json` |
| Textos e card do Datacare | `projects/datacare/content.md` |
| Textos e card do Iconatus | `projects/iconatus/content.md` |
| Textos e card do Sinapse | `projects/sinapse/content.md` |
| Textos e card do Cervello | `projects/cervello/content.md` |
| Textos e card do SEBRAE | `projects/sebrae/content.md` |
| Textos e card da evolução do portfólio | `projects/portfolio-evolution/content.md` |
| Frase, contato e mensagens do rodapé compartilhado | `templates/footer.html` |

Os identificadores na home são os nomes das pastas: por exemplo, `datacare` e `sebrae`. Para trocar a ordem, mova os identificadores na lista. Cada projeto deve aparecer uma única vez entre destaque, anteriores e experimento. Ao promover um projeto a destaque, preencha também `title` e `alt` na seção `[card]` do seu Markdown.

## Como editar um case

O começo de cada `content.md`, entre duas linhas `+++`, contém campos TOML. Mantenha os nomes dos campos e altere o texto entre aspas. Esse trecho organiza dados curtos; depois dele vem a narrativa em Markdown.

```text
+++
name = "Nome do projeto"
page_title = "Título da aba e do compartilhamento"
description = "Descrição para buscas e compartilhamento."
eyebrow = "Projeto · Desde 2023"
tags = ["Product Design", "Design System"]
next = "iconatus"

[card]
title = "Título do destaque na home"
description = "Resumo curto do projeto na home."
image = "projects/datacare/images/pipeline.png"
alt = "Descrição da imagem do card."

[captions]
caption_1 = "Legenda da primeira figura."

[accessibility]
alt_1 = "Descrição acessível do elemento correspondente."
+++

# Título que aparece no case

Este primeiro parágrafo é a abertura do case.

Este segundo parágrafo inicia o desenvolvimento. Você pode acrescentar,
remover ou reordenar os parágrafos, deixando uma linha em branco entre eles.
```

O exemplo é ilustrativo: edite o arquivo existente, preservando seus campos de legendas e acessibilidade. Cada layout tem uma quantidade própria de figuras e descrições. Os números seguem a ordem dos elementos no template; `alt_1` pode ser a descrição do logo ou de um controle, conforme a página. O próprio texto atual ajuda a identificar o elemento.

- `name`: nome do projeto no card e nos links de próximo case.
- `page_title`: título da aba e do compartilhamento; o gerador acrescenta seu nome.
- `description`: descrição para buscas e compartilhamento, separada do resumo do card.
- `eyebrow`: identificação curta acima do título, quando o layout tem esse elemento.
- `tags`: marcadores do case, reutilizados quando ele está em destaque na home.
- `next`: identificador do próximo case. A página de evolução não usa esse campo.
- `[card]`: título, resumo e imagem usados na home. O resumo pode ser diferente da abertura do case.
- `[captions]`: legendas das figuras; não inclua o link “Abrir imagem completa”, que o layout acrescenta quando aplicável.
- `[accessibility]`: alternativas de imagens e rótulos acessíveis, incluindo vídeos.

Use `\"` para uma aspa dentro de um campo entre aspas. Em TOML também é possível escrever `description = 'Texto com "aspas".'`. Não remova os delimitadores `+++`.

Depois do título `#`, o primeiro parágrafo é a abertura e os demais formam o corpo. Na evolução do portfólio, todos os parágrafos formam a introdução, pois o layout não tem uma abertura separada. As imagens históricas continuam vindo de `timeline.json`; a seleção e a montagem da timeline ficam em `scripts/build_evolution.py`.

O Markdown aceita parágrafos, `**negrito**`, `*itálico*` ou `_itálico_`, `[texto](https://exemplo.com)`, subtítulos `##` e `###`, e dois espaços no fim de uma linha para uma quebra explícita. `~~palavra~~` preserva o efeito riscado do título da evolução (oculto de leitores de tela, como no layout original). Não use esse efeito para informações essenciais. Listas, tabelas, imagens em Markdown, código e HTML não fazem parte deste formato editorial. Imagens e vídeos continuam organizados nos templates; texto com tags HTML aparece como texto literal.

## Gerar, visualizar e publicar

Na raiz do projeto:

```sh
python3 scripts/build_site.py
python3 -m http.server 8000
```

Abra `http://localhost:8000/`. Confira a home, use “Trocar tema” e abra o case editado. Confira também em largura de celular. Depois de editar novamente, execute o gerador outra vez e atualize o navegador. Não há atualização automática ao salvar.

Para conferir sem alterar arquivos:

```sh
python3 scripts/build_site.py --check
```

O comando verifica campos obrigatórios, correspondência entre legendas e templates, existência de imagens, vídeos, links locais e âncoras. Links externos não são acessados. Uma falha na validação interrompe a geração antes de gravar as páginas. `--check` também detecta HTML desatualizado ou editado manualmente. Corrija a fonte indicada pelo erro e gere novamente.

Para preparar a publicação:

```sh
bash scripts/prepare_publish.sh
```

Esse comando gera e verifica o site antes de preparar `dist/`. O workflow existente do GitHub Pages executa a mesma preparação. A edição local não publica automaticamente: envie as alterações pelo fluxo Git habitual. Versione os arquivos de conteúdo e os HTMLs gerados. Fontes editoriais, templates e scripts ficam fora de `dist/`.

## Limites e manutenção

Os arquivos `index.html` dos cases, dos temas e da raiz são gerados. Qualquer edição direta será sobrescrita. A disposição de galerias, vídeos, novas seções visuais e novas páginas ainda exige mudanças nos templates e eventual ajuste do gerador. Textos maiores podem alterar as quebras de linha e precisam de revisão visual.

Os layouts dos cases ficam em `templates/cases/`; os layouts da home continuam em `themes/`. O rodapé permanece compartilhado em `templates/footer.html`. O inglês continua suspenso: este fluxo não gera nem altera suas páginas ou o catálogo de traduções.

Para verificar mudanças no próprio gerador:

```sh
python3 scripts/test_content.py
python3 scripts/check_styles.py
python3 scripts/test_locales.py
```
