# Documentação do portfólio

Estado registrado em 16/09/2026. Este documento descreve a implementação atual e as decisões aprovadas até esta data. Registros antigos de `design-qa.md` são históricos e podem descrever situações já resolvidas.

## Objetivo e escopo

Portfólio de Product/UX Design de Leandro Oliveira, em português, com interfaces reais e narrativa sobre problemas, decisões e aprendizados. A implementação é estática: HTML e CSS, com JavaScript pequeno apenas para o contato WhatsApp. Não há framework, gerador de páginas, gerenciador de dependências, backend ou build.

As referências orientam a direção de arte, sem exigir reprodução pixel a pixel. Prioridades: composição editorial, espaço em branco, tipografia forte, interfaces em grande escala, recortes intencionais e mobile em uma coluna. As alterações visuais devem priorizar CSS e preservar os assets originais.

## Páginas e arquivos

| Caminho | Finalidade |
| --- | --- |
| `index.html` | Home, apresentação, quatro projetos e contato |
| `projects/sebrae/index.html` | Case de digitalização da avaliação de ecossistemas de inovação |
| `projects/sinapse/index.html` | Case de automações financeiras e formulários |
| `projects/cervello/index.html` | Case de redesign de plataforma corporativa |
| `projects/iconatus/index.html` | Case CAP, plataforma imobiliária desktop e mobile |
| `projects/*/content.md` | Conteúdo editorial de referência de cada case |
| `projects/*/images/` | Screenshots originais dos projetos |
| `projects/*/logo.*` | Logos fornecidos |
| `projects/common/icons/` | Ícones de princípios e WhatsApp |
| `css/` | Estilos compartilhados e específicos da home |
| `js/contact.js` | Contato WhatsApp com obfuscação |
| `references/` | Referências visuais e orientações de arte |
| `review-screenshots/` | Capturas históricas de revisão |
| `design-qa.md` | Histórico de verificações e limitações |
| `.nojekyll` | Compatibilidade com publicação estática no GitHub Pages |

## Conteúdo editorial

Os quatro cases foram atualizados a partir dos respectivos `content.md`. Esses arquivos não são carregados pelo navegador: mudanças no Markdown precisam ser refletidas manualmente no HTML. Não existe sincronização automática ou script permanente de geração.

Ao atualizar um case, revisar também título, descrição, metadados Open Graph e resumo na home, quando afetados. Preservar figuras relevantes, textos alternativos e legendas. Não inventar resultados ou apresentar números mostrados nas interfaces como métricas de impacto do trabalho.

## Organização dos estilos

A ordem dos estilos compartilhados é reset, variáveis, base, layout, componentes e responsividade. A home carrega `home.css` ao final, para seus ajustes específicos.

| Arquivo | Responsabilidade |
| --- | --- |
| `css/reset.css` | Normalização básica |
| `css/variables.css` | Cores, espaçamentos, raios, larguras e variável de moldura |
| `css/base.css` | Tipografia, elementos gerais e fundo da página |
| `css/layout.css` | Containers, grids e estrutura dos cases |
| `css/components.css` | Logos, tags, figuras, galerias e contato |
| `css/responsive.css` | Adaptações compartilhadas por largura |
| `css/home.css` | Composições, painéis e acabamento exclusivos da home |

Os parâmetros `?v=...` nos links de estilos e em algumas imagens servem para renovar o cache da prévia. Quando uma mudança não aparecer, conferir o arquivo carregado e atualizar sua versão nas páginas afetadas.

## Decisões visuais da home

- Hero com screenshots de SEBRAE, Sinapse e Cervello; quatro faixas de projetos com imagens reais.
- Layout com texto e interfaces lado a lado no desktop, passando a uma coluna em telas menores.
- Interfaces ampliadas, com recortes contidos nas seções, sem sangramento para fora delas.
- Painéis suaves de fundo feitos com pseudo-elementos e cores de apoio de cada projeto.
- Numeração dos cases recuada em relação ao texto; links coloridos com seta Unicode `→`.
- Tags sem borda e com fundo semitransparente. Esse tratamento também está aplicado aos quatro cases, com as mesmas cores de projeto e opacidade de 7,5%, mantendo a quebra de linha das tags.
- Ícones Lucide na abertura com 24 × 24px: Route, Users Round e Chart No Axes Combined. SVGs inline com `stroke="currentColor"` herdam a cor do label; originais e licença em `projects/common/icons/`. Os três ícones anteriores foram removidos.
- Notas cursivas com SignPainter e alternativas do sistema (Snell Roundhand, Segoe Print, Bradley Hand e cursive). Story Script não foi incorporada; a aparência varia conforme as fontes disponíveis.

## Molduras e transparência das imagens

A cor de todas as bordas de imagens da home e dos cases é controlada em `css/variables.css`:

```css
--image-frame-color: rgb(255 255 255 / 0.15);
```

O valor atual representa branco com 15% de opacidade. Alterar essa variável atualiza todas as molduras; `--color-border` continua responsável por outras bordas da interface.

Nos cases, `.case .figure-image-link` aplica borda de 8px no desktop e 5px até 680px, raio de 16px (13px no mobile) e sombra `0 12px 32px rgb(31 50 78 / 0.1)`. O fundo da moldura é **transparente**. O fundo branco adicional foi removido porque se sobrepunha à borda e diminuía a transparência percebida. A regra intermediária `background-clip: padding-box` também foi removida, pois deixou de ser necessária.

Apesar do nome legado, `.figure-image-link` agora identifica um `div`, não um link. As 24 imagens dos cases não abrem ao clique direto. Links textuais “Abrir imagem completa” nas legendas de SEBRAE e Iconatus permanecem. As instruções para clicar na própria imagem foram removidas.

Na home, as molduras são aplicadas em `.hero-screen`, `.feature-screen` e `.art-sinapse img`, usando a mesma variável de cor. As galerias dos cases ainda têm painéis de fundo em `--color-surface`; esses painéis são distintos do fundo transparente da moldura.

## Imagens e comportamento responsivo

Preservar proporções e informar `width`, `height` e texto alternativo contextual. Imagens decorativas do hero têm alternativa vazia e ficam em um bloco oculto da árvore de acessibilidade. As figuras abaixo da abertura usam carregamento preguiçoso e decodificação assíncrona.

Os quatro modais da Sinapse receberam exports aproximadamente 2×: `image 5.png` (358 × 473), `image 6.png` (356 × 422), `image 7.png` (383 × 442) e `image 8.png` (680 × 617). Os atributos HTML foram atualizados. No case, os três modais são apresentados a até 240px de largura e o cálculo a até 510px, limitados pelo espaço disponível. Na home, a composição foi preservada com os novos arquivos.

No mobile da home, os modais de ferramenta e condição são ocultados para manter o foco no cálculo. Nos cases, galerias podem quebrar em linhas; a comparação da Cervello passa a uma coluna. Algumas imagens longas de Iconatus têm recorte por altura máxima (780px, ou 620px no mobile), com acesso à imagem completa pela legenda.

## Contato WhatsApp

Home e quatro cases têm botão com ícone local de 20 × 20px. O SVG de WhatsApp veio do Simple Icons 16.0.0 (CC0); os ícones da abertura foram substituídos pelos Lucide (ISC).

`js/contact.js` reconstrói o destino a partir de uma sequência codificada com XOR somente ao clicar e navega para `wa.me`. O telefone não deve ser acrescentado em texto puro aos arquivos de apresentação ou a esta documentação. A obfuscação reduz coleta estática, mas não impede recuperação por bots capazes de analisar ou executar JavaScript.

Os botões ficam ocultos até o JavaScript habilitá-los. Sem JavaScript, há mensagem orientando a ativá-lo. O contato não depende de serviço no servidor.

## Ferramentas e participação da IA

Implementação em HTML5, CSS3 e JavaScript puro. OpenAI Codex desktop foi utilizado para edição assistida, inspeção dos arquivos e revisão no navegador integrado. O modelo informado para esta sessão é **GPT-6**; este registro não atribui uma variante específica nem garante o modelo de eventuais sessões anteriores.

Python 3 foi usado para servir a prévia e executar verificações pontuais de caminhos, dimensões e estrutura. Capturas e medições de layout foram feitas pelo navegador integrado do Codex. As imagens dos produtos e logos são assets fornecidos, não interfaces geradas por IA.

## Executar e revisar

Na raiz, executar `python3 -m http.server 8000` e abrir `http://localhost:8000/`. Python é uma ferramenta de desenvolvimento, não uma dependência da hospedagem.

Verificações já realizadas durante as iterações: carregamento de imagens, caminhos locais, atualização editorial, ausência de links diretos nas 24 imagens e ausência de rolagem horizontal em verificações de desktop e mobile. A home foi examinada em 320, 390, 768 e 1440px; os quatro cases foram medidos em 320 e 1440px na etapa das molduras.

As mudanças finais de transparência e remoção do fundo foram conferidas no código, mas não receberam uma nova revisão visual completa de todas as páginas. As capturas em `review-screenshots/` representam etapas anteriores e não devem ser tratadas como retrato exato do estado atual. Os arquivos `home-polish-desktop.jpg` e `home-polish-mobile.jpg` também antecedem as últimas alterações.

Antes de publicar ou após mudanças amplas, revisar home e cases em 320, 390, 768, 1024 e 1440px, navegação por teclado, foco, textos alternativos, imagens, links e contato. A validação estrutural e as verificações pontuais não substituem uma auditoria completa de acessibilidade.

## Pendências e publicação

- Definir domínio público e adicionar `canonical`, `og:url` e `og:image` específicos por página; os HTMLs têm comentários TODO para isso.
- Concluir revisão visual final e atualizar capturas após aprovação das iterações.
- Confirmar necessidade de screenshots adicionais dos formulários da Sinapse; isso estava registrado como pendência editorial anterior.
- Referências específicas dos cases não estavam disponíveis na revisão anterior. As referências de home existentes são `home-destktop.png` (grafia original) e `home-mobile.png`.
- Confirmar publicação e repositório remoto; não há confirmação de deploy nesta documentação.

Para GitHub Pages, publicar a branch escolhida a partir da raiz, sem build. Os caminhos relativos permitem servir o projeto em subdiretório. Após publicar, testar as cinco páginas e seus assets na URL pública.

Uma tentativa anterior de `git diff --check` foi impedida pela solicitação de aceite da licença do Xcode no ambiente local. Nenhuma licença foi aceita pelo agente; essa ocorrência não é um erro do site.
