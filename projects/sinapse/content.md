# Sinapse Finance

Menos atrito para lidar com processos financeiros complexos.

## Contexto e meu papel

A Sinapse Finance oferecia terceirização de processos financeiros para pequenas e médias empresas. A tecnologia ajudava a tornar as operações mais rápidas, previsíveis e fáceis de acompanhar.

Como designer principal, trabalhei em duas frentes: uma plataforma de automações financeiras e a melhoria dos formulários usados para receber informações dos clientes. Atuei com uma segunda designer em transição do design gráfico para UX, em colaboração com PO, especialistas financeiros e desenvolvimento. Também produzi HTML e CSS para apoiar a entrega.

As duas iniciativas buscavam reduzir trabalho manual, mas tinham desafios e estágios diferentes.

## Dois problemas na mesma operação

### Dar visibilidade às automações

A Sinapse já integrava ERPs, gateways e outras APIs, mas os fluxos não tinham uma representação visual. Configurar, acompanhar e manter as automações dependia bastante da equipe interna.

Os usuários conheciam processos financeiros e ferramentas digitais. Queriam mais controle, transparência e agilidade. Meu desafio era transformar regras complexas em uma experiência que pudessem compreender e configurar.

### Entender o atrito dos formulários

Os formulários haviam sido criados para padronizar a entrada de dados. Na prática, muitos clientes preferiam enviar informações por outros canais ou pedir aos consultores da Sinapse que fizessem o preenchimento.

Em alguns casos, fornecedores também participavam, criando mais intermediários até a informação chegar à operação. A ferramenta acabava transferindo trabalho para a equipe que deveria ajudar.

Inicialmente, as reclamações pareciam relacionadas a bugs de uma implementação feita com pouco prazo. A investigação mostrou um problema mais amplo.

## Investigação

### Mapear antes de desenhar

Nas automações, comecei documentando os processos financeiros existentes: regras, condições, caminhos, erros e estados possíveis. Havia pouco espaço para mudar essas rotinas, então era importante representá-las com precisão.

Validei o mapeamento com o PO, especialistas financeiros e desenvolvedores seniores. Engenharia participou desde essa fase, discutindo possibilidades, restrições e custo técnico das alternativas.

Esse alinhamento ajudava a evitar que uma regra pouco compreendida fosse incorporada à interface e ao software.

### Observar o formulário em uso

O trabalho com formulários aconteceu em aproximadamente duas semanas, incluindo investigação, redesign e primeira avaliação após o lançamento.

Comecei com testes e conversas com desenvolvimento. Encontrei entradas inadequadas aceitas pelos campos, validações pouco claras e dados que poderiam causar problemas no processamento.

Depois, instrumentamos o fluxo para observar o uso real. O volume de acessos permitiu reunir evidências em poucos dias. Analisei gravações, organizei os problemas encontrados e conversei com consultores financeiros para entender o contexto das dificuldades.

## O que os dados mostraram

Em um período analisado após uma correção emergencial, o Hotjar registrou:

- **58%** de submissões concluídas com sucesso.
- **42%** das sessões com dificuldades de uso ou compreensão.
- **39%** de abandono.
- **17%** com ocorrência de bugs.

No Google Analytics, a taxa de rejeição era de **75,25%**, com tempo médio de **5min08s**.

As evidências indicavam que corrigir bugs não seria suficiente. Havia dúvidas sobre os campos, limites de upload desconhecidos, pouca prevenção de erros e um preenchimento demorado.

A investigação abriu uma questão de produto: quanto dessa coleta realmente precisava depender de um formulário?

## Decisões de design

### Automações organizadas em etapas

Explorei um diagrama com elementos arrastáveis e uma alternativa guiada por etapas. O diagrama oferecia liberdade, mas aumentava o número de combinações, estados e exceções que o desenvolvimento precisaria tratar.

Escolhi um fluxo linear, com cada etapa representada por um card. Configurações complexas foram divididas em tarefas menores, muitas vezes em modais. Cada automação também poderia ser monitorada, desabilitada e consultada por seu registro de erros.

A estrutura guiava a configuração dentro das regras que a Sinapse conseguia executar, equilibrando clareza para o usuário e viabilidade técnica.

### Formulários mais claros

No formulário, priorizei os atritos observados. Reescrevi os nomes dos campos, acrescentei orientações curtas e reorganizei as informações e sua hierarquia visual.

Os limites de tamanho dos arquivos passaram a aparecer junto ao upload. As mensagens de erro foram revistas para explicar o problema e indicar como corrigi-lo.

Esses ajustes ajudavam o usuário a prevenir erros e recuperar o preenchimento quando algo desse errado, com uma linguagem mais próxima do restante da plataforma.

## Caminhos além do preenchimento manual

Além da melhoria imediata, exploramos duas hipóteses para reduzir a dependência dos formulários.

A primeira era uma interface de conversa, possivelmente integrada ao WhatsApp, aproximando a coleta dos canais que os clientes já preferiam. Ela dependia de uma avaliação financeira e não chegou à prototipação.

A segunda era extrair dados de documentos, como notas fiscais, usando OCR e IA. Em 2022, havia uma dependência técnica importante; a discussão com desenvolvimento começou, mas não foi concluída durante minha participação.

As duas permaneceram como possibilidades de evolução do produto.

## Validação e ajustes

### Compreensão das automações

O acesso aos clientes era limitado. Além da validação interna com especialistas financeiros, recrutei pessoas acostumadas a softwares de produtividade para testar a interação.

Elas precisavam configurar uma automação completa a partir de uma instrução inicial. O fluxo linear foi compreendido, embora surgissem dificuldades ligadas ao conhecimento financeiro. Esses testes ajudavam a avaliar a mecânica da interface, mas não substituíam a validação com o público principal.

Também identifiquei dúvidas sobre a função de cada card. Acrescentei pequenos títulos descritivos, como “Encerrar”, para deixar o papel das etapas mais evidente e facilitar a leitura do fluxo.

### Formulário em produção

Sem acesso direto aos clientes para testes moderados, acompanhei o formulário pela telemetria. Em uma medição mais curta após o redesign:

- As submissões bem-sucedidas passaram de **58% para aproximadamente 65%**.
- A rejeição caiu de cerca de **75% para menos de 40%**.
- O tempo médio de preenchimento diminuiu.

Os sinais mostravam uma melhora da experiência existente. Ainda assim, reduzir a necessidade de digitar informações continuava sendo uma oportunidade importante.

## Resultados e limites

O formulário chegou a uma melhoria implementada e medida em um ciclo curto. A plataforma de automações teve um percurso mais longo: deixei o projeto com a solução completa aprovada pelo PO, desenvolvimento, especialistas financeiros e demais envolvidos, e com a implementação iniciada.

Como não acompanhei sua entrega completa, não tenho métricas de adoção ou impacto em produção das automações. O resultado dessa frente foi transformar processos mapeados em uma solução de interação validada internamente e considerada viável para desenvolvimento.

As principais restrições foram o acesso limitado aos usuários, a necessidade de respeitar processos existentes e a complexidade técnica das automações. No formulário, somava-se o prazo curto, enquanto eu trabalhava nas duas iniciativas.

## Aprendizados

Hoje, buscaria combinar mais cedo o acesso aos usuários e o espaço para pesquisa e validação. Também deixaria explícito, desde o início, o que cada teste permite concluir, especialmente quando os participantes não representam o público principal.

Os projetos reforçaram meu interesse por produtos B2B de produtividade. Neles, o design ajuda a decidir quais detalhes o usuário precisa compreender, quais o sistema pode assumir e quais etapas podem deixar de existir.
