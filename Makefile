# Refaz os containers e força o build das imagens
build:
	docker compose up --no-deps --build -d

# Remove os containers
stop:
	docker compose down

# Sobe os containers
run:
	docker compose up -d

# Ativa o monitoramento do container em desenvolvimento
watch:
	docker compose logs -f