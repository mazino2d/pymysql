PY = python3

build:
	$(PY) setup.py sdist bdist_wheel

clean:
	rm -rf dist *.egg-info build **/**/__pycache__ **/__pycache__

package:
	rm -rf dist tlksql.egg-info build __pycache__
	$(PY) setup.py sdist bdist_wheel

install:
	@pip3 uninstall zcommon4py -y
	$(PY) setup.py install

release:
	rm -rf dist tlksql.egg-info build __pycache__
	$(PY) setup.py sdist bdist_wheel
	twine upload dist/* --non-interactive --config-file config.pypirc
