# -------------------------------------------------------------------------
# build a package for PyPi
# -------------------------------------------------------------------------
.PHONY: build requirements deps-update deps-init

report:
	cloc $(git ls-files)


build:
	python3 -m pip install --upgrade setuptools wheel twine
	python3 -m pip install --upgrade build

	if [ -d "./build" ]; then sudo rm -r build; fi
	if [ -d "./dist" ]; then sudo rm -r dist; fi
	if [ -d "./tutork8s_deploy_tasks.egg-info" ]; then sudo rm -r tutork8s_deploy_tasks.egg-info; fi

	python3 -m build --sdist ./
	python3 -m build --wheel ./

	python3 -m pip install --upgrade twine
	twine check dist/*


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