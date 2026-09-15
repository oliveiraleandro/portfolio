# CAP — Redesign de uma plataforma imobiliária

Uma experiência mais clara e consistente para o trabalho dos corretores, no desktop e no celular.

## Contexto e desafio

O CAP é uma plataforma B2B que reúne imóveis, ofertas, proprietários, histórico de preços e dados de mercado. Seu objetivo é apoiar corretores na pesquisa, captação, acompanhamento e precificação de imóveis.

Quando entrei no projeto, o produto precisava de um redesign completo. O cliente considerava a aparência pouco adequada a um público profissional, e a estrutura de tabelas extensas, abas e modais dificultava o uso no celular.

Havia uma condição importante: nenhuma funcionalidade poderia ser removida. Eu podia reorganizar informações e mudar interações, mas precisava preservar todas as capacidades existentes.

## Meu papel

Eu já havia trabalhado com o cliente e fui chamado para redesenhar uma área de outro produto, voltado a gestores de imobiliárias. A entrega foi bem recebida e abriu espaço para o redesign completo do CAP.

Durante aproximadamente três meses, fui o único designer do projeto. Trabalhei diretamente com o fundador e os desenvolvedores, que tinham bastante experiência no mercado imobiliário. Não havia PM ou PO formal, e o fundador participava ativamente das decisões.

Minha atuação envolveu mapear a plataforma, pesquisar referências, conversar com corretores, redesenhar as jornadas e organizar os componentes para implementação.

## Conhecendo o produto

Com acesso ao ambiente de desenvolvimento, percorri as telas e fiz um inventário de conteúdos, funcionalidades e caminhos de navegação. Como o escopo cobria todo o produto, esse levantamento era essencial para reorganizá-lo sem deixar recursos para trás.

Encontrei três problemas principais:

- **Estrutura pouco preparada para mobile:** tabelas largas e fluxos com muitos níveis seriam difíceis de usar em telas pequenas.
- **Home subutilizada:** a página inicial funcionava quase como um menu, com pouca informação sobre o trabalho em andamento.
- **Falta de consistência visual:** famílias tipográficas, ícones, cores e ilustrações variavam entre as áreas.

A percepção de uma aparência infantil vinha dessa combinação. O redesign precisava criar uma linguagem visual mais coesa e uma organização adequada à rotina profissional.

## Referências e contexto de uso

Como muitas plataformas imobiliárias B2B eram fechadas, ampliei a pesquisa para produtos como ZAP, QuintoAndar e Zillow, além do Captei, mais próximo do contexto do CAP. Observei busca, listagem, densidade de informação e apresentação dos imóveis.

Mantive algumas cores da identidade anterior, mas reduzi a quantidade usada em cada tela. As ilustrações deram espaço a fotografias, fundos simples e gradientes discretos. Também organizei uma escala tipográfica menor e mais consistente.

Conversei com dois corretores para entender a rotina fora do escritório. Eles confirmaram que passavam muitas horas na rua em dias de visita, reforçando a importância de uma versão mobile útil no trabalho.

As conversas também trouxeram dificuldades de precificação e qualificação de leads. O papel do CAP era oferecer informações melhores para apoiar o julgamento do corretor. Essa definição ajudou a manter as propostas dentro do alcance do produto.

## Uma home para retomar o trabalho

Propus trazer **captações recentes** e **acompanhamentos recentes** para a página inicial. Captações eram imóveis que o corretor buscava incluir na carteira; acompanhamentos representavam negócios em andamento.

A ideia surgiu do mapeamento das jornadas, como uma hipótese de design. Ao mostrar atividades atuais, a home poderia ajudar o corretor a continuar seu trabalho com menos navegação.

Ela passou, assim, a reunir acessos aos módulos e pontos de continuidade da operação. Ainda vejo espaço para aprofundar essa direção e aproximar a entrada na plataforma das tarefas mais frequentes.

## Encontrando a direção visual

Comecei pelo desktop, com esboços simples, e avancei rapidamente para protótipos detalhados e interativos. O fundador preferia explorar as propostas por conta própria, e esse formato ajudava na avaliação.

A primeira direção foi validada com o cliente e um corretor. Depois, consolidei os padrões visuais e desenvolvi as versões mobile.

Essa sequência permitiu encontrar a linguagem do produto antes de formalizar o sistema de componentes. A base resultante apoiou tanto as adaptações para celular quanto a entrega ao desenvolvimento.

## Da tabela ao card no celular

No desktop, mantive a listagem de imóveis em tabela, útil para comparar, ordenar e consultar muitos dados ao mesmo tempo. No celular, transformei cada linha em um card para evitar a rolagem em dois sentidos.

A mudança também exigiu rever a hierarquia. Na tabela, as visitas recentes apareciam na última coluna. No card, ganharam destaque logo no início, por funcionarem como um sinal indireto de atividade do imóvel.

Usei a cor secundária e maior peso tipográfico para esse dado. As demais informações receberam uma apresentação mais compacta, com acesso aos detalhes na tela seguinte.

O card seguia a sequência **atividade recente → resumo do imóvel → ação principal**. No final, um botão com a cor primária ocupava toda a largura. A adaptação preservava o conteúdo e reorganizava sua leitura para o novo espaço.

## Detalhes do imóvel: uma solução negociada

A visão detalhada foi a tela mais difícil do projeto. Ela reunia muitas informações em abas e modais. Minha primeira proposta mobile organizava o conteúdo em uma sequência sem abas, mas o cliente preferiu manter a estrutura existente.

A alternativa também tinha uma desvantagem: criava uma página bastante longa. Mantive as abas e trabalhei seu comportamento no celular, diferenciando melhor os estados ativos e inativos e deixando todas acessíveis sem rolagem horizontal adicional.

Foi uma solução de compromisso que preservou a navegação solicitada e reduziu parte das dificuldades em telas pequenas.

## Precificação como apoio à decisão

A área de precificação já tinha informações importantes, mas elas apareciam principalmente em tabelas. Reorganizei a apresentação para facilitar a leitura e a interpretação.

Os diferentes conceitos de preço receberam cores, ícones e tratamentos próprios. Os valores atuais ganharam destaque, enquanto o histórico passou a aparecer em uma série temporal, com indicadores de tendência e evolução. Também criei comparações com imóveis da região.

Essa foi uma das áreas mais bem recebidas pelo cliente. Na validação, o corretor demonstrou interesse no histórico e nas tendências, mas também perguntou sobre a precisão dos dados.

O feedback mostrou como uma apresentação mais clara aumenta a expectativa de confiança na informação. Questionei o cliente sobre estados de ausência ou incerteza e recebi a orientação de que dados incertos não seriam exibidos. A qualidade dessas informações continuava dependendo das áreas de negócio e tecnologia.

## Requisitos de negócio e densidade visual

Durante a validação, descobri que o cabeçalho precisava mostrar de forma persistente os limites de proprietários e imóveis, ligados ao modelo de cobrança. Também acrescentei um contador para tornar mais visível a quantidade de imóveis em acompanhamento.

Esses requisitos foram incorporados à hierarquia das telas. No desktop, mantive uma densidade relativamente alta, usando agrupamentos, cards, divisores e tipografia para organizar o volume de informações.

No mobile, os mesmos conteúdos precisavam de outra ordem e distribuição de destaque. Esse cuidado permitia manter as funcionalidades e adaptar a experiência a cada contexto.

## Validação e implementação

O cliente avaliava os protótipos interativos no próprio ritmo. Também apresentei parte do trabalho a um corretor externo que não usava o CAP. Ele considerou a navegação e a apresentação profissionais, mas reforçou a preocupação com a confiabilidade dos dados.

Depois da validação visual, organizei componentes, variantes e padrões reutilizáveis. A entrega aconteceu pelo Figma, sem uma reunião formal de passagem. A experiência do time em front-end facilitou a reprodução das interfaces, e as partes que acompanhei ficaram próximas do protótipo.

## Resultados e aprendizados

O redesign cobriu toda a plataforma, estabeleceu uma linguagem visual consistente e reorganizou informações importantes para o trabalho dos corretores. A versão mobile recebeu soluções próprias, especialmente na listagem e nos detalhes dos imóveis.

Não houve uma etapa estruturada de medição. Sugeri acompanhar métricas, mas isso não avançou naquele momento e estava fora do orçamento e do escopo contratado. Os resultados observados foram qualitativos, com destaque para a boa recepção da área de precificação.

Essa área representa bem minha contribuição: tornar os dados existentes mais compreensíveis e úteis para a decisão. Com mais tempo, aprofundaria a home e acompanharia o uso após a implementação para entender quais mudanças melhoraram a rotina dos corretores.
