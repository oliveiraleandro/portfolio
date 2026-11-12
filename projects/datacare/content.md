# Como os analistas examinam e tratam dados no Datacare

Como único designer do Datacare, redesenhei ferramentas de análise de dados. Mais tarde, usei o Claude para testar como o design system orientava a criação de novas telas.

_O pipeline mostra onde os registros passam por validação e tratamento de duplicidades._

## O trabalho com os analistas

A Assesso reuniu em uma plataforma sua experiência no tratamento de dados brasileiros, como CPFs e endereços. Os analistas tinham dificuldade para examinar os registros e escolher a ferramenta adequada para cada problema.

Entrei no início de 2023. Trabalhei com os desenvolvedores e o líder de produto. Testei as propostas com analistas e com pessoas de fora da empresa, começando pela navegação.

## O espaço de uma tela de notebook

Os analistas usavam notebooks simples. Adotei 1366 × 768 pixels como referência e procurei manter os controles principais nos primeiros 668 pixels de altura. Escolhi um fundo cinza claro para as tabelas, considerando a iluminação do escritório.

_A busca do menu leva o analista à ferramenta desejada._

## Legibilidade das tabelas

Testei a interface em diferentes modos de cor para verificar se era possível distinguir textos, ícones e ações. Também avaliei o contraste e o tamanho das letras.

_A mesma tabela em quatro modos de cor._

## Entender os dados antes de tratá-los

No profiler, o analista examina uma amostra de conjuntos que podem chegar a bilhões de registros. Cada coluna mostra o que os valores representam, como CPFs ou telefones. Mantive os indicadores visíveis durante a rolagem para que o analista pudesse consultá-los enquanto examinava as linhas.

Escolhi gráficos de acordo com o conteúdo de cada coluna. Nos testes, mesmo quem tinha pouca experiência com dados conseguiu distinguir colunas pelos gráficos. A partir desse diagnóstico, o analista pode incluir uma ferramenta sugerida no pipeline, a sequência de tarefas que transforma os dados.

_Do diagnóstico à escolha de uma ferramenta de tratamento._

## Como a cor ajuda a reconhecer cada tarefa

Um pipeline podia reunir dezenas de tarefas. Nos testes, atribuir uma cor a cada uma dificultou reconhecer sua função. Passei a usar roxo para transformações e laranja para etapas que executavam outro pipeline. Cada tarefa também tinha nome e ícone. Nos testes seguintes, os participantes reconheceram as categorias com mais facilidade.

_Componentes usados no editor de pipelines._

## Um assistente para escolher ferramentas

Desenhei uma proposta de assistente de IA que resume os problemas encontrados nos dados e explica por que recomenda determinado tratamento. Parte dessa proposta ainda aguarda implementação.

## Do Figma ao guia de composição no Claude

No Figma, organizei os valores de cor e espaçamento em estilos e variáveis e criei componentes reutilizados em vários módulos, dos campos de entrada às tabelas. Conectei o Claude a essa biblioteca pelo MCP do Figma para prototipar o painel de lentes.

Com um pedido aberto, o Claude repetiu cards arredondados onde eu usaria listas ou tabelas expansíveis. Preencheu grandes áreas com cores claras e empurrou controles para baixo da primeira tela. No Datacare, costumo reservar a cor para indicar o significado de um elemento sobre um fundo neutro.

Criei no Claude um guia para a equipe de front-end consultar ao compor telas. Registrei quando evitar cards e como adaptar os espaçamentos. Acrescentei à biblioteca um cabeçalho que mostra como dar destaque à ação principal e onde posicionar a busca e os filtros.

Já comecei a usar o guia e sou seu principal usuário até aqui. Ainda estou avaliando o resultado da aplicação dessas regras nos protótipos.

_Cada lente responde a uma pergunta, como quais cadastros podem estar duplicados._

## O que o Claude percebeu em um teste sem áudio

Durante um teste, o participante parou para me perguntar quando deveria importar um dado e quando deveria criar um. Foi a conversa que me permitiu entender a dúvida.

Enviei ao Claude a gravação sem áudio para descobrir quais dificuldades ele perceberia só pelas interações. Na primeira análise, ele descreveu a interface como se o participante tivesse visto tudo de uma vez.

Pedi que mapeasse a interface e acompanhasse as ações na ordem em que ocorreram. Ainda precisei indicar o que a pessoa já tinha visto e precisava lembrar. Hoje, eu começaria a automação pela descrição das ações. Para interpretar uma hesitação, recorreria também ao que observei e ouvi durante o teste.

## Resultados no produto

Os analistas continuam a usar o profiler na preparação dos projetos. Por sugestão deles, acrescentei subtítulos às janelas de configuração para esclarecer a tarefa em andamento. A liderança também usou os protótipos em apresentações comerciais para mostrar os próximos passos da plataforma.

_No monitor, o analista consulta os arquivos gerados em cada etapa._

_Indicadores de execução com valores ilustrativos._
