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

A versão inglesa está temporariamente suspensa. As rotas `/en/` e `/en/projects/` estão desabilitadas, e o seletor de idioma foi removido.

## Atualizar conteúdo e traduções

Edite apenas os HTMLs em português. O catálogo de traduções está congelado; `scripts/build_locales.py` não gera nem modifica arquivos enquanto `ENGLISH_ENABLED = False`.

Os HTMLs ingleses anteriores estão preservados em `translations/suspended-en/`, com extensão `.html.disabled`. Para retomar o inglês, restaure esses arquivos em `en/`, reative o gerador, restaure os seletores de idioma nas páginas portuguesas e revise o catálogo antes de gerar as páginas.

Confira a suspensão com `python3 scripts/test_locales.py`.

## Referência e manutenção

Consulte [DOCUMENTACAO.md](DOCUMENTACAO.md) para estrutura, conteúdo, decisões visuais, manutenção e pendências. O histórico de revisão está em [design-qa.md](design-qa.md).

## Publicação enxuta no GitHub Pages

`bash scripts/prepare_publish.sh` prepara `dist/` copiando os HTMLs prontos,
CSS, JavaScript e imagens de `assets/`, `public/` e `projects/`.
Não instala dependências, compila código nem executa geradores de conteúdo.
A pasta é recriada a cada execução e não é versionada.

Capturas de revisão continuam em `review-screenshots/`; referências, documentação,
scripts, traduções suspensas, PDF de apresentação e arquivos temporários também
permanecem no repositório, mas ficam fora da publicação. As imagens da timeline
em `public/` são conteúdo do site e continuam publicadas.

O workflow `.github/workflows/pages.yml` publica somente `dist/`. Para ativá-lo,
envie os arquivos ao GitHub e selecione **Settings → Pages → Source → GitHub Actions**
em vez da publicação direta da branch. Depois execute **Publish static portfolio**
na aba Actions se necessário. A configuração atual não é alterada por preparar
os arquivos localmente. Domínio personalizado não está configurado.

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
