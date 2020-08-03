install:
	pip install -r requirements.txt | grep -v 'already satisfied' || true

install-dev:
	pip install -r requirements_dev.txt | grep -v 'already satisfied' || true

test: install install-dev
	pip install .
	python -m pytest --cov=RDS --cov-report xml

build:
	python setup.py build

sdist:
	python setup.py sdist

clean:
	rm -r dist src/*.egg-info build .coverage coverage.xml .pytest_cache