from setuptools import setup, find_packages

import os

install_requires = [
    "pyyaml",
    "flake8",
]

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read()

setup(
    name="adacore-style-checker",
    url="https://github.com/AdaCore/style_checker",
    author="AdaCore",
    author_email="info@adacore.com",
    description="AdaCore Style Checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="."),
    package_dir={"": "."},
    package_data={
        "asclib.checkers.typific": ["*.xml"],
        "etc": ["*"],
    },
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "style_checker = asclib.main:main"
        ],
    },
)
