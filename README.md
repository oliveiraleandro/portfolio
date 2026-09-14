# Portfólio — Leandro Oliveira

Site estático em português, sem JavaScript, frameworks, dependências ou build.

## Estado da implementação

Home e cases de SEBRAE, Sinapse, Cervello e Iconatus (CAP) implementados a partir dos conteúdos locais. Os arquivos de conteúdo originais foram preservados. CSS dividido em reset, tokens, base, layout, componentes e responsividade.

A direção de arte está em andamento. Os quatro cases têm imagens reais e logos inseridos. A home também usa composições com as interfaces reais dos quatro projetos. Faltam screenshots dos formulários da Sinapse. Foram analisadas as referências `references/home-destktop.png` (nome original preservado), `references/home-mobile.png` e seu README. As três referências de case e a referência de enquadramento não estavam presentes.

## Pendências antes de publicar

- Adicionar imagens dos formulários da Sinapse. Os quatro cases já usam assets reais nas páginas internas. Comentários `TODO ASSETS` indicam os pontos de composição. Inserir figuras também junto às decisões relevantes nos cases. Preservar proporções, informar width/height e alt contextual; usar lazy loading e decoding async abaixo da dobra. Ajustar grid, crops e sobreposições após conhecer os arquivos reais.
- Fornecer número/link WhatsApp. Os comentários `TODO WHATSAPP` contêm o modelo de CTA; substituir o aviso visível e adicionar o CTA discreto no cabeçalho. Não há link fictício ativo.
- Definir URL pública. Adicionar canonical e og:url específicos por página; adicionar og:image com URL absoluta de uma imagem real. Title, description, viewport e os demais metadados Open Graph já existem.
- Adicionar referências dos cases e concluir revisão visual desktop/mobile. Ver `design-qa.md`.

## Visualizar

Abra `index.html` diretamente no navegador. Opcionalmente, na raiz, execute `python3 -m http.server 8000` e abra http://localhost:8000. Python serve apenas para prévia; o site publicado não depende dele.

## Testar

- Abrir home e os quatro cases em 320, 390, 768, 1024 e 1440px. Confirmar ausência de rolagem horizontal e leitura confortável.
- Percorrer com Tab: atalho para conteúdo, cases, retorno à home e próximo projeto. Confirmar foco visível.
- Verificar links e imagens após adicionar assets. Validar os cinco HTMLs no Nu HTML Checker antes da publicação; não enviar conteúdos privados sem revisão.
- Repetir comparação com referências depois da composição de screenshots. Os testes estruturais locais não substituem uma auditoria completa de acessibilidade.

## Publicar no GitHub Pages

Depois de concluir as pendências, faça commit e push para a branch desejada. Nas configurações do repositório, em Pages, selecione publicação a partir da branch e pasta raiz (`/`). Não é necessário workflow de build. Os caminhos são relativos e funcionam em um subdiretório de projeto. Após a publicação, teste home, cases, CSS e WhatsApp na URL fornecida pelo GitHub.

## Arquivos

Modificados: `index.html`, `css/reset.css`, `projects/sebrae/index.html`, `projects/sinapse/index.html`, `projects/cervello/index.html`, `projects/iconatus/index.html`.

Criados: os outros cinco CSS, `README.md`, `design-qa.md` e `.nojekyll`.
