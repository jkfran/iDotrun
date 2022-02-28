import sys
from setuptools import setup

# The importer relies heavily on glob recursive search capability.
# This was only introduced in Python 3.5:
# https://docs.python.org/3.6/whatsnew/3.5.html#glob
assert sys.version_info >= (3, 5), "dotrun requires Python 3.5 or newer"

extra_options = dict()

if sys.platform == "darwin":
    extra_options = dict(
        setup_requires=["py2app"],
        app=["canonicalwebteam/dotrun/__init__.py"],
        options={
            "py2app": {
                "argv_emulation": True,
                "packages": [
                    "ipdb",
                    "black",
                    "flake8",
                    "termcolor",
                    "virtualenv",
                    "nodeenv",
                ],
            }
        },
    )

setup(
    name="canonicalwebteam.dotrun",
    version="0.0.0",
    packages=["canonicalwebteam.dotrun"],
    install_requires=[
        "ipdb",
        "black",
        "flake8",
        "termcolor",
        "virtualenv",
        "nodeenv",
    ],
    entry_points={
        "console_scripts": ["idotrun = canonicalwebteam.dotrun:cli"]
    },
    **extra_options
)
