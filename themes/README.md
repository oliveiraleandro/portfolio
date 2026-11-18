# Manutenção das prévias

Edite `content.json` para alterar a apresentação, os rótulos do menu e os identificadores dos projetos. Os textos, imagens e tags dos cards vêm de `projects/<case>/content.md`. Consulte [EDITAR_CONTEUDO.md](../EDITAR_CONTEUDO.md). Os caminhos de imagens e páginas partem da raiz do repositório. A lista `archive` determina a ordem dos projetos anteriores. A ação do WhatsApp usa o script existente em `js/contact.js`.

A partir da raiz do repositório, gere as prévias:

```sh
python3 scripts/build_site.py
```

Verifique se as páginas estão atualizadas e se os caminhos, as âncoras e a sequência de destinos são válidos:

```sh
python3 scripts/build_site.py --check
```

Cada `index.html` em uma pasta de tema é uma saída gerada e pode ser aberto diretamente pelo navegador. O gerador também monta o `index.html` da raiz. Ao abrir a home diretamente, a página sorteia um dos temas cadastrados, com a mesma probabilidade. O botão “Trocar tema” avança na ordem do catálogo e, após o último tema, volta ao primeiro. A URL permanece a da home. Sem JavaScript, a página exibe Ateliê, que usa o CSS em `themes/atelie/`.

## Adicionar um tema

Crie uma pasta em `themes/` com `theme.css` e `theme.json`. Por exemplo:

```json
{"title": "Novo tema", "layout": "editorial"}
```

Escolha `editorial` para a composição em seções, `desktop` para a composição em janelas ou `documento` para a apresentação com destaque e índice de projetos. Os três layouts usam os modelos em `templates/`. Um novo tema pode fornecer `art.html` para a arte da abertura editorial, `intro.html` para rearranjar o título e a descrição, e `header.html` para outra apresentação do menu. Reutilize os campos dos modelos comuns. No cabeçalho, `$switch_theme` e `$contact` inserem as ações compartilhadas. Se existir, `menu.js` será carregado para interações específicas, como o menu Iniciar do XP.

Execute o gerador e abra o novo `index.html`. O mesmo cadastro inclui o tema no sorteio da home. O pacote de publicação leva a home gerada e os recursos visuais dos temas.
