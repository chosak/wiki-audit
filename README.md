# wiki-audit

Extract all images embedded or linked in a GitHub wiki.

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

```
wiki-audit https://github.com/user/repo/wiki > out.csv
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

