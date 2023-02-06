# wiki-audit

Generate useful information from a GitHub wiki.

### Installation

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install .
```

### Usage

To create a CSV of wiki pages and their images:

```
wiki-audit images https://github.com/user/repo/wiki > images.csv
```

To create a CSV of wiki pages and their links:

```
wiki-audit links https://github.com/user/repo/wiki > links.csv
```

### Contributing

To install necessary development dependencies:

```
pip install -e '.[test]'
```

To check source code formatting:

```
black --check .
flake8 .
```

