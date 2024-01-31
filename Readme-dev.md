# how to distribute:


- build: 
```
python -m build
```

- upload:
``` 
twine upload -r pypi dist/*
```

# how to document
- build
```
.\docs\make html
```

- auto sphinx:
```
sphinx-autobuild docs/source docs/build/html
```