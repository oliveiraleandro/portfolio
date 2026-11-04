# Portfólio — Leandro Oliveira

Portfólio de Product/UX Design com home e cases de SEBRAE, Sinapse Finance, Cervello BPMS e Iconatus (CAP). Site estático e responsivo em português brasileiro e inglês americano.

## Ferramentas utilizadas

- HTML5, CSS3 e JavaScript puro, sem frameworks. Um gerador Python atualiza as páginas inglesas durante a manutenção; a hospedagem serve os HTMLs prontos.
- OpenAI Codex (aplicativo desktop), com assistência do modelo de IA **GPT-6** nesta sessão de desenvolvimento.
- Navegador integrado do Codex para revisão visual e verificações de responsividade.
- Python 3 para o servidor local e verificações de arquivos; não é necessário no site publicado.
- Ícones SVG Lucide (ISC) na abertura e WhatsApp do Simple Icons 16.0.0 (CC0).

## Visualizar localmente

Na raiz do projeto:

```sh
python3 -m http.server 8000
```

Abra [localhost:8000](http://localhost:8000/).

A versão inglesa está em [localhost:8000/en/](http://localhost:8000/en/). Cada case possui sua página correspondente em `/en/projects/`. O seletor mantém a página e, com JavaScript, a âncora atual. Não há redirecionamento automático por idioma do navegador.

## Atualizar conteúdo e traduções

1. Edite os HTMLs em português nos caminhos originais; eles também definem a estrutura compartilhada das versões inglesas.
2. Atualize `translations/en-US.json`: cada texto original tem sua tradução, incluindo descrições de imagens e metadados. Nomes de marcas e termos já ingleses aparecem explicitamente no catálogo.
   Consulte o glossário e os critérios de revisão em [translations/README.md](translations/README.md).
3. Execute `python3 scripts/build_locales.py`. A geração falha se faltar uma tradução, antes de escrever qualquer página.
4. Confira com `python3 scripts/build_locales.py --check` e `python3 scripts/test_locales.py`.

Não edite os HTMLs de `en/` diretamente: eles são gerados. Inclua os HTMLs gerados na publicação, junto dos arquivos originais. Estilos, scripts e imagens são compartilhados; as capturas dos produtos permanecem no idioma original.

## Referência e manutenção

Consulte [DOCUMENTACAO.md](DOCUMENTACAO.md) para estrutura, conteúdo, decisões visuais, manutenção e pendências. O histórico de revisão está em [design-qa.md](design-qa.md).

O site está preparado para hospedagem estática, incluindo GitHub Pages. A publicação e a configuração do domínio ainda precisam ser confirmadas.

## Rodapé compartilhado

O rodapé compacto tem uma única fonte em `templates/footer.html`, com estilos
isolados em `css/footer.css`. Edite esses arquivos, não os rodapés de cada página.
O template preserva o botão de WhatsApp, a frase caligráfica e a assinatura.
As traduções usam o catálogo existente; os caminhos de imagens são calculados
para cada página. O HTML é gerado previamente, sem framework ou carregamento
adicional no navegador.

```sh
python3 scripts/build_footer.py
python3 scripts/build_footer.py --check
```

O segundo comando falha se algum rodapé divergir do template. A geração de
idiomas também aplica o template antes de traduzir. O comando independente
permite atualizar apenas os rodapés sem regenerar o conteúdo dos cases.
Páginas sem rodapé, como a timeline visual, continuam sem ele.

As capturas em `review-screenshots/footer/` registram a referência visual em
1440 e 390 px, em português e inglês, na home e em um case. Ao alterar estilos
compartilhados, compare o resultado com essas referências: botão e frase na mesma
linha no desktop, empilhados no celular, assinatura logo abaixo. As fontes
caligráficas são do sistema; a comparação deve usar o mesmo navegador e sistema
operacional. O template evita divergência de conteúdo, mas a revisão visual ainda
é necessária para mudanças em CSS ou fontes.
