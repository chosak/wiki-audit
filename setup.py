from setuptools import setup


VERSION = "0.1"


setup(
    name="wiki_audit",
    version=VERSION,
    install_requires=[
        "beautifulsoup4",
        "click",
        "httpx",
    ],
    extras_require={
        "test": [
            "black",
            "flake8",
        ],
    },
    entry_points="""
        [console_scripts]
        wiki-audit=wiki_audit:main
    """,
)
