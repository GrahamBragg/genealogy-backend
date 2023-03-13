black:
	poetry run black .

install:
	poetry install

build:
	poetry build

buildd:
	docker build -t genealogy-backend:latest .

clean:
	rm -rf dist

update:
	poetry update

publish:
	poetry publish --build

run:
	poetry run uvicorn app.main:app --reload --host localhost --port 8080

up:
	docker compose up -d

down:
	docker compose down