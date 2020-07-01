build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist tlksql.egg-info build __pycache__

package:
	rm -rf dist tlksql.egg-info build __pycache__
	python3 setup.py sdist bdist_wheel

release:
	twine upload dist/* --non-interactive --config-file config.pypirc
