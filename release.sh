# generate disribution package
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel

# upload distribution package
python3 -m pip install --user --upgrade twine
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

twine upload dist/*
