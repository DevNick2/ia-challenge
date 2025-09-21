Como vou fazer esse projeto:

1) Vou optar por usar OOP na API
2) Vou construir a API e Agentes em Conjunto
3) Vou construir os Agentes com o Agno
4) Vou usar o PostgreSQL como dados de Storage global e o SQLite como Memória
5) Os deploys usam o github actions

Stack:

Uv para gerenciar pacotes;
Uvicorn com fastapi para o web server;
Docker para container;
Docker-first, ou seja, tudo em docker;

Condução:

Nesse readme vou trazer os seguintes tópicos:
  - Desisões técnicas;
  - Boas práticas;
  - Como rodar em dev e deploy;
  - O que pode melhorar e o que foi limitante;

Padrão:

Não vou seguir nenhum padrão, mas deixarei claro a necessidade do uso

Passos:

- [X] Criar a estrutura inicial com o UV;
- [ ] Criar a configuração Docker (Dockerfile e compose.yml) para Desenvolvimento e Produção;
- [X] Criar o makefile para operar a aplicação;
- [ ] Criar a estrutura de agentes;
- [X] Criar o agente de gerar a imagem;
- [ ] Criar o agente de executar a ação em serviço externo com o MCP;
- [ ] Criar a estrutura de API;
- [ ] Criar uma rota de Post para a geração da imagem;
- [ ] Criar uma rota de Post para executar o workflow de ação;
- [ ] Criar o workflow do github actions
- [ ] Documentar o processo de uso do modelo de geração de imagens do gpt-5