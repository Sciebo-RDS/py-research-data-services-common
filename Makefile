test:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
	pip install .
	python -m pytest --cov=RDS --cov-report xml