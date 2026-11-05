# Revisão do hero editorial

final result: passed

## Escopo e evidências

Abertura da home baseada na primeira proposta escolhida pelo usuário.

- Referência visual em `/Users/leandro/.codex/generated_images/01a1a8e8-809c-7041-a521-134a55491282/exec-fcc82f76-af1c-4fac-a8af-c8fa7adabf1a.png`.
- Implementação em `http://127.0.0.1:8766/`.
- Comparação normalizada em `/tmp/hero-editorial-comparison.png`, referência acima e implementação abaixo, ambas com 1440 px de largura.
- Captura desktop em `/tmp/hero-editorial-desktop.png`.
- Captura mobile em `/tmp/hero-editorial-mobile.png`.

## Achados e correções

A primeira comparação mostrou tipografia e faixa de princípios menores que a proposta. Foram ampliados o título, o parágrafo e os princípios e recalibrados os espaços verticais. A segunda comparação confirmou a hierarquia, a quebra do título em duas linhas e a altura total próximas da referência. Nenhum P0, P1 ou P2 pendente no escopo revisado.

## Superfícies verificadas

- Tipografia usa as famílias já presentes no site, com título responsivo, texto legível e conteúdo HTML selecionável.
- Layout preserva a régua horizontal do cabeçalho e dos cases. Os princípios ocupam três colunas no desktop e uma coluna no celular.
- Cores combinam a superfície creme com texto azul-escuro e marca-texto amarelo. O cabeçalho mantém as cores atuais do projeto.
- O pincel foi gerado por ImageGen e salvo em `assets/hero-highlight.png`, com transparência e margens externas aparadas. Os ícones reutilizam os assets vetoriais existentes.
- O conteúdo português foi preservado. A tradução inglesa foi remontada para enfatizar “the people”, com a frase completa revisada.
- Home verificada a 1440 px e 390 px. Inglês verificado a 320 px, sem transbordamento horizontal ou imagens quebradas. Console sem erros na home.
- Geração dos dez HTMLs conferida, cinco testes de localização aprovados e diff sem erros de whitespace.

## Limites e refinamentos

A textura do pincel é uma nova imagem na mesma direção da referência. A tipografia rasterizada da proposta tem pequenas diferenças de renderização frente às fontes reais. Essas diferenças são P3. A captura mobile foi feita antes da calibração final da escala desktop, e a revisão posterior em inglês a 320 px confirmou o comportamento das regras responsivas.
