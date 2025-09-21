build:
	docker compose up --no-deps --build --watch

down:
	docker compose down

run:
	docker compose up --watch