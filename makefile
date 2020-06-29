build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist pzsql.egg-info build __pycache__

release:
	twine upload dist/* --non-interactive --config-file config.pypirc
