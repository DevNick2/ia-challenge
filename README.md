Como vou fazer esse projeto:

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
- [X] Criar a configuração Docker (Dockerfile e compose.yml) para Desenvolvimento e Produção;
- [X] Criar o makefile para operar a aplicação;
- [X] Criar a estrutura de agentes;
- [X] Criar o agente de gerar a imagem;
- [X] Criar o agente de executar a ação em serviço externo com o MCP;
- [ ] Criar a estrutura de API;
- [ ] Criar uma rota de Post para a geração da imagem;
- [ ] Criar uma rota de Post para executar o workflow de ação;
- [ ] Criar o workflow do github actions
- [ ] Documentar o processo de uso do modelo de geração de imagens do gpt-5

### Requisitos e Setup para o EC2:
O OS para esse setup é Ubuntu 20~
Não vou entrar no mérito dos recursos da instância e sim nos requisitos para a aplicação rodar.

São 3 passos de forma objetiva:

1) Configurar a chave ssh para o github:
```bash
ssh-keygen -t ed25519 -C "jeannicolasav@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

ssh-keygen -t rsa-sha2-256
```

2) Configurar as dependências para funcionar;
```bash
sudo apt-get update
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
# /bin/bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl start docker  
sudo docker run hello-world
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
docker ps
sudo systemctl enable docker
docker --version
```
3) Instalar o projeto e adicionar o arquivo env:
```bash
$ git clone {github_project}

cd github_project

# Cria o arquivo .env.production
# pode ser com echo
# ou vim .env.production
# use o .env.example como base para as variaveis

docker compose -f devops/compose.yml up --no-deps --build -d
```

### Implantação e Deploy de Versões
A esteira dessa aplicação é feita baseada em versões com o git one-flow.

Para subir essa aplicação em produção é necessário algumas etapas:

1) Configurar o EC2 para que tenha o básico para rodar a aplicação (Vide seão sobre Pré requisitos para Produção);
2) Configurar as variáveis de ambiente no github actions para o EC2 e a chave;
3) Os deploys são feitos por versão e com trigger ao invés de fazer por PR ou Push (optei por isso pois para deploys em PRD normalmente faço double check antes de subir.) por tanto deve haver uma versão pronta para fazer isso;
