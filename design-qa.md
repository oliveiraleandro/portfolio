# Revisão visual e funcional

final result: blocked

## Referências

- `references/home-destktop.png`: direção desktop, nome original preservado.
- `references/home-mobile.png`: direção mobile; inclui moldura de dispositivo, que não pertence ao site.
- `references/README.md`: princípios editoriais.
- Referências de SEBRAE, Sinapse, Cervello e enquadramento de interfaces ausentes.

## Evidência e limites

Implementação aberta no navegador integrado em `http://localhost:8000/`. Capturas exibidas na conversa: home desktop (969 × 965), home e cases mobile (viewport CSS 320 × 800), Cervello desktop (1440 × 1000). Capturas não foram persistidas em arquivo. Não foi produzida composição lado a lado nem normalização de densidade; a comparação formal solicitada permanece pendente. Não declarar fidelidade aprovada.

## Diferenças e achados

- P1 — Imagens: nenhuma screenshot ou logo real disponível. As referências dependem de grandes interfaces sobrepostas; a implementação atual contém apenas a narrativa. Inserir os assets reais e então ajustar o grid, escala, crops e ritmo. Não usar as interfaces fictícias das referências.
- P1 — Contato: número WhatsApp ausente. O CTA está preparado em comentário HTML e há um aviso textual visível, sem link fictício.
- P1 — Cases: sem imagens e sem referências específicas, não é possível avaliar a direção de arte final dos cases.
- Tipografia: stack de sistema, títulos grandes, peso 600, tracking negativo e leitura em coluna estreita. Fontes externas omitidas conforme briefing.
- Espaçamento: faixas amplas e respiro preservados; grid textual provisório desloca o conteúdo em relação às referências. Deve ser refeito com as imagens reais, sem reservar enormes caixas vazias.
- Cores: azul, verde e violeta suaves como apoio; sem filtros, gradientes ou interfaces recriadas.
- Conteúdo: textos dos arquivos locais preservados; resumos derivados dessas fontes. Métricas e limitações da Sinapse e resultados qualitativos do Cervello mantidos. Artefatos de citação interna removidos somente do HTML.

## Histórico

1. Primeira inspeção: home desktop e mobile e SEBRAE mobile. Detectada marcação de negrito multilinha literal no SEBRAE e seções vazias na conversão dos conteúdos.
2. Correção: negrito convertido e seções sem conteúdo removidas. Novas inspeções de Sinapse e Cervello mobile e Cervello desktop. Revisão final lado a lado das quatro páginas ainda pendente.

## Verificações realizadas

- Quatro páginas: aninhamento HTML, H1 único, IDs sem duplicação, âncoras existentes e destinos locais verificados por parser Python. Isso não equivale ao Nu HTML Checker.
- Home, Sinapse e Cervello: largura do documento igual a 320px no viewport de 320px.
- SEBRAE mobile inspecionado visualmente.
- Retorno do case à home testado no navegador.
- Console: nenhum erro capturado na consulta realizada.
- HTML sem scripts e sem estilos inline. CSS local, links relativos e ausência de recursos externos.

## Próxima revisão

Receber logos, screenshots, referências dos cases e WhatsApp; inserir figuras com alt, dimensões, lazy loading e legendas; concluir canonical e og:image após definir URL pública; capturar as quatro páginas em desktop e mobile, comparar lado a lado duas vezes, testar teclado e contraste e concluir validação HTML. Tablet e demais larguras ainda precisam de inspeção visual.

## Inclusão do case Iconatus · CAP

- Preparado a partir de `projects/iconatus/content.txt`, preservado integralmente no arquivo original. A frase de síntese foi usada na abertura; a instrução editorial que a antecedia não foi publicada.
- Incluído como quarto projeto na home e na sequência Cervello → Iconatus → SEBRAE.
- Reutiliza a tipografia, o ritmo e os componentes existentes. Fundo neutro provisório, sem inventar identidade de marca. Nenhuma referência específica de Iconatus disponível.
- Pontos de imagem marcados no HTML: abertura, antes/depois, home, listagem desktop/mobile, detalhe com abas, precificação e Design System.
- Inspeção de abertura no navegador em 1440 × 900 e 320 × 800; largura do documento em mobile de 320px, sem overflow horizontal. Um H1 e nenhum erro de console capturado. Capturas exibidas na conversa, sem arquivo persistido.
- Validação estrutural local repetida para os cinco HTMLs: aninhamento, H1, IDs e destinos relativos aprovados. Validação visual com screenshots reais continua pendente enquanto o usuário prepara os assets.
- Arquivos modificados nesta etapa: `projects/iconatus/index.html`, `index.html`, `projects/cervello/index.html`, `css/components.css`, `README.md` e este relatório. Nenhum arquivo novo necessário.


## Imagens reais — SEBRAE e Iconatus

Inseridas seis screenshots e um logo original em cada case, sem modificar os arquivos fornecidos. Todas as imagens foram abertas e analisadas antes da inserção. As figuras acompanham as decisões documentadas, com alt, dimensões, legendas, lazy loading e links relativos para os originais. Telas mobile longas recebem recorte vertical com acesso à versão completa. A busca de ofertas da Iconatus não foi descrita como evidência do indicador de visitas recentes, que não aparece nessa tela.

Revisão parcial no navegador: SEBRAE desktop a 1280 × 900 e mobile a 320 × 800; Iconatus mobile a 320 × 800. Primeira revisão mostrou ampliação dos arquivos SEBRAE; corrigida com limite de 823px e página recarregada. Links e estrutura dos dois HTMLs verificados por parser, incluindo os nomes Unicode e espaços dos arquivos. Imagens referenciadas: sete por página, contando o logo. Comparação final com referências específicas continua pendente, pois elas não foram fornecidas. Relatórios anteriores sobre ausência de assets nesses dois cases estão superados por esta atualização.

Arquivos modificados nesta etapa: os dois HTMLs, css/components.css, css/responsive.css, README.md e este relatório. Nenhum novo asset gerado.


## Imagens reais — Sinapse e Cervello

Inseridas seis imagens e o logo em cada case. Sinapse: fluxo, anotações e quatro modais. Cervello: atendimento, dashboards claro/escuro e três telas mobile. Imagens analisadas visualmente; a montagem de sites de terceiros da Sinapse foi preservada no repositório sem publicação por falta de contexto no texto. As composições e SVGs redundantes dos dashboards não foram adicionados para evitar repetição.

Os modais mantêm dimensões nativas; dashboards comparados em duas colunas e empilhados no mobile. Alt, dimensões, lazy loading, legendas e links para arquivos originais incluídos. Verificados caminhos dos 14 assets, diff sem erros de whitespace e ausência de overflow a 320px em ambos os cases. Nenhuma imagem carregada foi reportada quebrada no navegador. Revisão visual parcial da Sinapse em desktop e do Cervello em mobile; comparação final completa continua pendente.

Modificados: projects/sinapse/index.html, projects/cervello/index.html, css/components.css, css/responsive.css, README.md e este relatório. Faltam imagens do formulário Sinapse e a composição de screenshots da home.


## Composições da home

Hero com screenshots de SEBRAE, Sinapse e Cervello; quatro faixas com interfaces reais. Grid editorial com texto à esquerda e imagem à direita no desktop. Mobile em uma coluna, recortes contidos e apenas o modal de cálculo na faixa Sinapse. Nenhum asset criado, recolorido ou distorcido. CSS da home versionado na URL para atualizar o cache durante a prévia.

Referências home-destktop.png e home-mobile.png reabertas. Preservados o contraste entre texto e grandes interfaces, fundos suaves e sobreposição moderada. Diferenças intencionais: textos reais mais extensos; logos fornecidos; quarto projeto Iconatus; ausência das anotações decorativas; modais pequenos sem ampliação excessiva. CTA WhatsApp ainda depende do número real.

Primeira revisão: cache antigo impedia aplicação do grid, corrigido versionando URLs CSS. Segunda revisão: imagens do hero posicionadas antes dos princípios no mobile, conforme referência. Screenshots de revisão exibidos na conversa em 1280px, 320px e 1440px. Verificadas larguras 320, 768 e 1440 sem overflow horizontal; nenhum arquivo carregado reportado quebrado; 13 referências de imagem e caminhos locais verificados. Diff sem erros de whitespace. Comparação formal lado a lado e captura persistida ainda não realizadas; resultado geral permanece blocked pelas pendências registradas.

Arquivos alterados: index.html, css/layout.css, css/components.css, css/responsive.css, README.md e design-qa.md. A pendência anterior de imagens na home está resolvida.
