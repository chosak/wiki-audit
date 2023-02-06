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

To dump a list of wiki pages and their images:

```
wiki-audit images https://github.com/user/repo/wiki > images.csv
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

