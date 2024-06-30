fmt:
	black .
	ruff check . --fix

style:
	black --check .
	ruff check .

test:
	python run_tests.py