# how to distribute:
- clone the project from github.
- install with additional dependencies:
```
pip install -e .[dev]
```
- build: 
```
python -m build
```
- upload:
``` 
twine upload -r pypi dist/*
```

# how to document
- install with additional dependencies
```
pip install -e .[doc]
```
- build
```
.\docs\make html
```

- auto sphinx:
```tw
sphinx-autobuild docs/source docs/build/html
```