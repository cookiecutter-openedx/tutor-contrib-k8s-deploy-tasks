# -------------------------------------------------------------------------
# build a package for PyPi
# -------------------------------------------------------------------------
SHELL := /bin/bash

ifeq ($(OS),Windows_NT)
    PYTHON := python.exe
    ACTIVATE_VENV := venv\Scripts\activate
else
    PYTHON := python3.11
    ACTIVATE_VENV := source venv/bin/activate
endif
PIP := $(PYTHON) -m pip


.PHONY: build requirements deps-update deps-init

analyze:
	cloc . --exclude-ext=svg,json,zip --vcs=git

init:
	npm install
	$(PYTHON) -m venv venv && \
	$(ACTIVATE_VENV) && \
	$(PIP) install --upgrade pip && \
	$(PIP) install -r requirements.txt


build:
	python3.11 -m pip install --upgrade setuptools wheel twine
	python3.11 -m pip install --upgrade build

	if [ -d "./build" ]; then sudo rm -r build; fi
	if [ -d "./dist" ]; then sudo rm -r dist; fi
	if [ -d "./tutork8s_deploy_tasks.egg-info" ]; then sudo rm -r tutork8s_deploy_tasks.egg-info; fi

	python3.11 -m build --sdist ./
	python3.11 -m build --wheel ./

	python3.11 -m pip install --upgrade twine
	twine check dist/*

release-github:
	git commit -m "fix: force a new release" --allow-empty && git push

# -------------------------------------------------------------------------
# upload to PyPi Test
# https:// ?????
# -------------------------------------------------------------------------
release-test:
	make build
	twine upload --verbose --skip-existing --repository testpypi dist/*


# -------------------------------------------------------------------------
# upload to PyPi
# https://pypi.org/project/django-memberpress-client/
# -------------------------------------------------------------------------
release-prod:
	make build
	twine upload --verbose --skip-existing dist/*