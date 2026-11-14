# Manutenção das prévias

Edite `content.json` para alterar a apresentação, os rótulos do menu, os textos dos cases e os destinos. Os caminhos de imagens e páginas partem da raiz do repositório. A lista `archive` determina a ordem dos projetos anteriores. A ação do WhatsApp usa o script existente em `js/contact.js`.

A partir da raiz do repositório, gere as prévias:

```sh
python3 scripts/build_themes.py
```

Verifique se as páginas estão atualizadas e se os caminhos, as âncoras e a sequência de destinos são válidos:

```sh
python3 scripts/build_themes.py --check
```

Cada `index.html` em uma pasta de tema é uma saída gerada e pode ser aberto diretamente pelo navegador. O gerador também monta o `index.html` da raiz. Cada carregamento da home sorteia um dos temas cadastrados, com a mesma probabilidade. O botão “Trocar tema” volta à home e exclui o tema atual do sorteio. A URL permanece a da home. Sem JavaScript, a página exibe Ateliê, que usa o CSS em `themes/atelie/`.

## Adicionar um tema

Crie uma pasta em `themes/` com `theme.css` e `theme.json`. Por exemplo:

```json
{"title": "Novo tema", "layout": "editorial"}
```

Escolha `editorial` para a composição em seções ou `desktop` para a composição em janelas. Os dois layouts usam os modelos em `templates/`. Um novo tema pode fornecer `art.html` para a arte da abertura editorial, `intro.html` para rearranjar o título e a descrição, e `header.html` para outra apresentação do menu. Reutilize os campos dos modelos comuns. No cabeçalho, `$switch_theme` e `$contact` inserem as ações compartilhadas. Se existir, `menu.js` será carregado para interações específicas, como o menu Iniciar do XP.

Execute o gerador e abra o novo `index.html`. O mesmo cadastro inclui o tema no sorteio da home. O pacote de publicação leva a home gerada e os recursos visuais dos temas.
