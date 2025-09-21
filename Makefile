build:
	docker compose up --no-deps --build -d

down:
	docker compose down

run:
	docker compose up -d