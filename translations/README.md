# Guia editorial — português brasileiro e inglês americano

O catálogo `en-US.json` contém os textos originais como chaves e as versões inglesas como valores. Ele cobre a home e os quatro cases, incluindo títulos, descrições para compartilhamento, navegação, legendas e alternativas de imagens. Os rótulos do seletor são mantidos no gerador.

## Voz e fidelidade

- Usar inglês americano, primeira pessoa e frases diretas, preservando a autoria individual e a colaboração descritas no português.
- Adaptar construções literais quando necessário, sem ampliar responsabilidades, resultados ou escopo.
- Preservar estimativas, datas, percentuais, duração dos projetos e limitações da pesquisa. Usar ponto decimal: `75,25%` → `75.25%`.
- Diferenciar validação interna, conversas informais, testes com participantes e resultados em produção. Não transformar feedback qualitativo em impacto mensurado.
- Manter marcas, nomes de produtos e siglas reconhecidas. Traduzir os termos ao redor, sem inventar nomes oficiais em inglês.
- Usar títulos em sentence case; as tags seguem a capitalização já adotada no portfólio.
- Preservar o conteúdo factual das imagens originais. Traduzir suas legendas e alternativas, sem tratar os números das interfaces como métricas do projeto.

## Glossário

| Português / contexto | Inglês adotado |
| --- | --- |
| Case | Case study |
| Página inicial / home | Home page; Home em rótulos curtos |
| Design System | Design system no texto; Design System na tag |
| Validação com usuários | Evaluating designs with users, conforme a frase |
| Chamado de suporte | Support ticket; ticket após estabelecer o contexto |
| Solicitação | Request |
| Gestor | Manager |
| Consultor | Consultant |
| Corretor de imóveis | Real estate agent; agent após estabelecer o contexto |
| Captação de imóveis | Property sourcing; sourcing activity |
| Acompanhamento de negócios (CAP) | Follow-ups |
| Visitas recentes (CAP) | Recent visits; não substituir por page views |
| Precificação | Pricing |
| Valorização do imóvel | Property appreciation |
| Vocação econômica (SEBRAE) | Economic strength |
| Nível de efetividade (SEBRAE) | Effectiveness level |
| Automação financeira | Financial automation |
| Taxa de rejeição | Bounce rate |
| Abandono | Abandonment; manter distinto de bounce rate |
| Preenchimento manual | Manual data entry |
| Arquitetura de informação | Information architecture |
| Visualização de dados | Data visualization |
| Responsividade | Responsive design |

## Revisão realizada em 24/09/2026

Revisadas as 360 entradas do catálogo. Foram ajustadas 25 traduções para naturalidade, consistência e fidelidade ao original. Entre as correções: “multiple user roles” voltou a “multiple users”, “recent views” passou a “recent visits” e descrições de validação foram reformuladas para evitar a expressão ambígua “user validation”.

As ressalvas sobre ausência de métricas, período curto de medição e implementação incompleta permanecem nos cases. As telas dos produtos continuam em seu idioma original.

## Atualização

Edite o catálogo, execute `python3 scripts/build_locales.py` e confira o texto completo no HTML gerado. Alguns parágrafos possuem trechos separados por ênfases ou quebras de linha; a tradução precisa funcionar na frase montada. Não edite os arquivos de `en/` diretamente.

Valide a geração com `python3 scripts/build_locales.py --check` e as rotas com `python3 scripts/test_locales.py`.
