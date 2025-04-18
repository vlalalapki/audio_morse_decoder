install:
	pip install -r requirements.txt

format:
	black .
	ruff --fix .

check:
	ruff .
	mypy .
