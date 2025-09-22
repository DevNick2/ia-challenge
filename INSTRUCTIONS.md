# Sua missão, caso decida aceitar

O objetivo deste desafio é avaliar sua capacidade de projetar e construir um sistema de
agentes de IA multifuncional utilizando nosso stack principal. Queremos ver na prática suas
habilidades em arquitetura de backend, sua capacidade de integrar diferentes capacidades
de IA e seu entendimento sobre como conectar agentes a ferramentas externas.

## Cenário
Imagine que estamos expandindo os workflows de automação da Ferramenta. Precisamos de
um sistema de agentes capaz de realizar duas tarefas distintas como parte de um fluxo de
trabalho maior:

1. Criar um ativo visual: Gerar uma imagem a partir de um prompt (ex: criar um
banner para um post de blog).
2. Executar uma ação em um sistema externo: Interagir com uma ferramenta de
produtividade para gerenciar o andamento de uma tarefa (ex: mover um card no
Trello de "Em Progresso" para "Revisão").

Sua missão é projetar e construir o protótipo de um sistema que demonstre essas duas
capacidades.
- [X] Stack principal construida sobre o Agno
- [X] Exposição de um agente pela AGUI
- [X] Prontidão para depoloy
- [X] Criar um ativo visual;
- [X] Executar uma ação em sistema externo;

## Tarefas técnicas:

- [X] Criar a estrutura inicial com o UV;
- [X] Criar a configuração Docker (Dockerfile e compose.yml) para Desenvolvimento e Produção;
- [X] Criar o makefile para operar a aplicação;
- [X] Criar a estrutura de agentes;
- [X] Criar o agente de gerar a imagem;
- [X] Criar o agente de executar a ação em serviço externo com o MCP;
- [X] Criar o workflow do github actions;
- [X] Expor um Agente ao AGUI
- [X] Implementar um front end que use conecte ao agente