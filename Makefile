create_env:
	python -m venv .venv_morse
	source .venv_morse/bin/activate && pip install -r requirements.txt

mlflow:
	cd mlflow_server
	sh mlflow_run.sh

format:
	black .
	ruff --fix .

check:
	ruff .
	mypy .

