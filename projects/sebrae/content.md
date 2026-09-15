# Ecossistema de Inovação SEBRAE

Uma plataforma para aplicar uma metodologia complexa com mais clareza no dia a dia.

## Contexto e desafio

O SEBRAE Paraná havia desenvolvido uma metodologia para avaliar e fortalecer ecossistemas de inovação nos municípios. O método era abrangente, mas sua aplicação dependia de formulários, planilhas e documentos espalhados em diferentes arquivos.

Isso dificultava a colaboração, o acompanhamento das avaliações e a produção de relatórios. Treinar novos consultores também era trabalhoso, porque o conhecimento necessário nem sempre estava acessível durante a operação.

Meu papel foi entender a metodologia, organizar a experiência e desenhar uma plataforma para consultores e gestores. O desafio era facilitar o trabalho preservando a profundidade do método.

## Entendendo o trabalho de cada pessoa

Comecei estudando o manual de aproximadamente 150 páginas, conversando com a equipe do SEBRAE e analisando seus arquivos e processos. Queria entender tanto as informações necessárias quanto a maneira como eram usadas.

Identifiquei dois perfis principais:

- **Consultores:** entrevistavam os atores dos ecossistemas e preenchiam as avaliações. Eram os usuários mais frequentes.
- **Gestores:** acompanhavam o trabalho, consultavam relatórios e observavam a evolução dos ambientes de inovação.

Mapear a jornada do consultor ajudou a reconhecer uma oportunidade: mesmo com uma metodologia complexa, era possível organizar o trabalho cotidiano em uma sequência clara.

## Da metodologia ao fluxo de trabalho

A operação seguia um caminho relativamente previsível: selecionar ou criar uma avaliação, coletar informações, preencher os dados e chegar ao cálculo da pontuação.

Organizei a interface em torno dessa sequência, deixando uma ação principal evidente em cada contexto. As tarefas operacionais ganharam destaque, enquanto as explicações metodológicas ficaram disponíveis conforme a necessidade.

A expectativa era que os consultores ganhassem familiaridade com o uso. Por isso, conteúdos extensos não precisavam disputar atenção com as ações diárias. Dashboards e análises tinham maior relevância para os gestores e receberam menos destaque no fluxo de preenchimento.

Essa organização permitia avançar com rapidez e consultar os detalhes do método sempre que surgisse uma dúvida.

## Validando a estrutura

Antes de trabalhar o acabamento visual, criei wireframes e os validei com o Product Owner. O foco era verificar se a navegação fazia sentido, se as etapas estavam completas e se havia informação suficiente para orientar a implementação.

Não surgiram mudanças estruturais significativas, e avancei para um protótipo mais detalhado. Validar essa base cedo ajudou a evitar revisões maiores quando as telas já estivessem prontas.

Também preservei representações conhecidas pela equipe, como os gráficos de radar. Eles faziam parte da linguagem da metodologia e ajudavam as pessoas a reconhecer os resultados na nova ferramenta.

## Ajuda disponível na hora certa

Na apresentação ao SEBRAE, o principal pedido foi incluir mais explicações sobre a metodologia dentro da plataforma. Era uma necessidade importante, especialmente para consultores menos experientes.

Ampliei o conteúdo disponível sob demanda. O modal de **nível de efetividade**, por exemplo, passou a explicar o conceito com mais profundidade, mantendo a tela principal concentrada na tarefa.

Essa solução aproximava o conhecimento do momento de uso. O consultor podia seguir com o preenchimento e abrir uma explicação quando precisasse, sem depender da busca em documentos separados.

## O que aprendemos nos testes

Testamos a solução com pessoas não especialistas e com especialistas do SEBRAE. Cada grupo ajudou a observar uma parte diferente da experiência.

Os não especialistas revelaram pontos com contraste insuficiente e termos difíceis de compreender. Corrigimos os problemas visuais e revisamos parte da terminologia para tornar a interface mais acessível.

Os especialistas reconheceram a metodologia e demonstraram familiaridade com a proposta. Ao mesmo tempo, os testes revelaram o principal atrito do projeto: o catálogo de projetos.

### O catálogo e a rotina dos consultores

A plataforma organizava cada avaliação como um projeto. Essa estrutura ajudava o SEBRAE a acompanhar iniciativas, registrar seu histórico e observar a evolução dos ecossistemas.

Os consultores, porém, pensavam no trabalho a partir das atividades: coletar dados, produzir uma avaliação e entregar informações aos gestores. Criar um projeto independente para cada avaliação não era uma organização natural para eles.

Como essa estrutura atendia a uma necessidade institucional importante, havia pouca margem para removê-la. Propus uma carga inicial de projetos no banco de dados, para que o primeiro acesso já trouxesse exemplos reais.

Esses registros serviriam de referência para nomear projetos, organizar avaliações e entender o nível de detalhe esperado. A proposta ajudava a reduzir o esforço de aprendizado, embora não resolvesse por completo a diferença entre a estrutura institucional e a forma de trabalhar dos consultores.

## Colaboração com desenvolvimento

A equipe técnica definiu o uso de um sistema de design baseado em Material Design. Trabalhei dentro dessa base para manter os princípios de organização e clareza da solução.

Os desenvolvedores não participaram da descoberta nem da apresentação inicial ao cliente. Antes da implementação, apresentei o protótipo em reuniões com a equipe e o Product Owner, explicando os fluxos e os motivos das decisões.

Não houve pedidos relevantes de mudança por limitações técnicas. Nas revisões, a implementação ficou muito próxima do protótipo, preservando as escolhas construídas durante o processo.

## Resultados

A plataforma reuniu em um só ambiente informações e atividades que antes dependiam de arquivos separados e consolidação manual.

Os consultores passaram a ter o processo de avaliação e as orientações necessárias no mesmo sistema. Os gestores ganharam acesso direto a dados atuais e históricos, em tempo real, reduzindo a dependência de relatórios preparados pelos consultores.

O retorno qualitativo do SEBRAE foi muito positivo. O líder do projeto destacou a fidelidade da representação digital da metodologia, um dos principais objetivos do trabalho.

O projeto também previa que a solução desenvolvida no Paraná pudesse apoiar a adoção do método por outras unidades do SEBRAE no país.

## O que eu faria diferente

Hoje, exploraria mais alternativas para o catálogo. A ideia seria preservar a organização por projetos na gestão e nos dados, aproximando o início da experiência das atividades que os consultores já reconheciam.

O principal aprendizado foi entender que digitalizar um processo exige escolher quais partes de sua estrutura precisam aparecer para cada pessoa. Essa escolha pode facilitar o trabalho sem perder o rigor necessário ao negócio.
