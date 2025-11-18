lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=python_project_scripts --cov-report=xml --cov-report=term-missing

install:
	uv sync