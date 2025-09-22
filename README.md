# IA Challenge
Uma aplicação com Python e Agno para criar agentes que sejam capazes de gerar imagem e executar ações em serviços externos com MCP.

### Como fazer funcionar:
O arquivo Makefile possui todos os comandos para rodar o projeto, porém só roda em ambiente linux

Pré-requisitos:
- Docker
- Api Keys da Anthropic e OpenAI, use o .env.example como base
- Github Actions com as Chaves configuras, ver em .github/workflows/deploy.yml - Apenas quando colocar na esteira
- uv como gerenciador de pacotes e uvicorn para a api

Para rodar basta fazer o seguinte:
- uv sync
- make run ou docker compose up -d
- a porta configurada é 3000

### Decisões Técnicas:

Não optei por usar uma arquitetura robusta em função do tempo, porém em uma aplicação para produção ou um MVP que tenha propósito seria bom aderir, tenho afinidade com DDD, para esse caso inclusive é muito bom.
Além disso optei por utilizar algumas ferramentas extras:
- UV para gerenciar pacotes do python;
- Uvicorn para gerenciar os endpoints;
- Postgres como banco de dados;
- Os modelos da Anthropic (Claude Opus 4) e da OpenAi (GPT-5 mini);
- Nginx para expor a aplicação;
- Preparo para Github actions com workflow de deploy automatizado baseado em versões;
- Preparo para usar em um AWS EC2;

Não optei por usar Times de agentes em função do tempo, o Agno é um framework do qual tinha pouco conhecimento por tanto optei por fazer agentes individuais em função do tempo.
Optei por usar o Copilot KIT para gera as interfaces e conectar aos agentes pelo protocolo.

### O que pode melhorar:

Existem vários pontos a melhorar se pensar na aplicação para esse mesmo objetivo, deixo alguns pontos aqui:
- Automação de deploy com AWS Vault para gerenciar as variaveis de ambiente;
- Automação de deploy com ECS e Fargate (Com o script docker é facil de implementar);
- Melhoria de design da API adicionando um DDD, DI (Dependency Injection), Singleton Pattern dentre outros padrões;
- Banco de dados para uso de memória do Agente pode ser um Redis por ser mais rápido porém é um pouco limitante em relação a espaço, ainda assim teria mais velocidade para os agentes;

### Requisitos e Setup para o EC2:
O OS para esse setup é Ubuntu 20~
Não vou entrar no mérito dos recursos da instância e sim nos requisitos para a aplicação rodar.

São 3 passos de forma objetiva:

1) Configurar a chave ssh para o github:
```bash
ssh-keygen -t ed25519 -C "email_do_github"
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

1) Configurar o EC2 para que tenha o básico para rodar a aplicação (Requisitos e Setup para o EC2);
2) Configurar as variáveis de ambiente no github actions para o EC2 e a chave;
3) Os deploys são feitos por versão e com trigger ao invés de fazer por PR ou Push (optei por isso pois para deploys em PRD normalmente faço double check antes de subir.) por tanto deve haver uma versão pronta para fazer isso;
