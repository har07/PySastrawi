# AGENTS.md — PySastrawi

## Setup & install

```bash
pip install -e .
```

No external dependencies — pure stdlib + `re`.

## Running tests

Uses `unittest` — `nosetests` (referenced in `.travis.yml`) doesn't support Python 3.12+:

```bash
python -m unittest discover tests -p '*_test*.py' -v
```

Run a single test module:
```bash
python -m unittest tests/UnitTests/Stemmer/stemmer_test.py -v
```

Test framework is `unittest` (`assertEqual`, not the long-deprecated and now-removed `assertEquals`).

## Target Python version

`python_requires='>=3.8'` in `setup.py`. No external dependencies — pure stdlib + `re`.

## Package layout

- Source lives under `src/`; `setup.py` maps it via `package_dir={'': 'src'}`.
- Top-level package: `Sastrawi` → subpackages: `Dictionary`, `Morphology`, `Stemmer`, `StopWordRemover`.
- All `__init__.py` files are empty. Import with full dotted paths, e.g.:
  ```python
  from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
  ```

## Architecture

- **StemmerFactory** creates a `CachedStemmer` wrapping a `Stemmer` backed by an `ArrayDictionary` loaded from `data/kata-dasar.txt`.
- **Stemmer** splits text on spaces, handles plurals (dash-separated), and delegates singular stemming to a `Context` pipeline of visitors (suffix removal, prefix disambiguation).
- **Disambiguator** prefix rules live in `Morphology/Disambiguator/`. Rules 22 and 33 are intentionally absent — not a bug.
- **StopWordRemover** is standalone; not coupled to stemming.

## Data files

The base-word dictionary is at `src/Sastrawi/Stemmer/data/kata-dasar.txt`. It is shipped with the package via `package_data`. The `StemmerFactory` locates it relative to its own `__file__`.

## Visual Studio cruft

`Sastrawi.sln`, `*.pyproj`, and `*.vs/` are Visual Studio artifacts from the original development environment. Ignore them — there is no Python build integration.

## Release

`release.sh` uses `setuptools` + `wheel` + `twine`. Not needed during normal development.
