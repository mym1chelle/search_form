run:
	poetry run uvicorn app.main:app --reload

test:
	poetry run pytest

lint:
	poetry run flake8 app

test-cov:
	poetry run pytest --cov=app --cov-report xml

install:
	poetry install