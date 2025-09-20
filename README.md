Como vou fazer esse projeto:

1) Vou optar por usar OOP na API
2) Vou construir a API e Agentes em Conjunto
3) Vou construir um Agente com o Agno e outro com LangGraph
4) Vou usar o PostgreSQL como dados de Storage global e o SQLite como Memória

Stack:

Uv para gerenciar pacotes;
Uvunicorn com fastapi para o web server;
Docker para container;
Docker-first, ou seja, tudo em docker;

Condução:

Nesse readme vou trazer os seguintes tópicos: Desisões técnicas; Boas práticas; Como rodar em dev e deploy; O que pode melhorar e o que foi limitante; diferenças do Agno para o LangGraph.

Padrão:

Não vou seguir nenhum padrão, mas deixarei claro a necessidade do uso
