.PHONY: install test format lint run

install:
	python3 -m venv venv && source venv/bin/activate && pip install .

test:
	source venv/bin/activate && python -m unittest discover tests

format:
	black .

lint:
	flake8 .

run:
	source venv/bin/activate && tasky
