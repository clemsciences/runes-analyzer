#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

# To upload this file to PyPI you must build it then upload it:
# python setup.py sdist bdist_wheel  # build in 'dist' folder
# python-m twine upload dist/*  # 'twine' must be installed: 'pip install twine'

import io
import os
from setuptools import find_packages, setup

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = []
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name='runesanalyzer',
    version='1.0.4',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    url='https://github.com/clemsciences/runes-analyzer',
    license="License :: OSI Approved :: MIT License",
    author='Clément Besnier',
    author_email='clemsciences@gmail.com',
    description='Gathers different kinds of runic inscriptions',
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=DEPENDENCIES,
    keywords=["runes", "corpus"],
    zip_safe=True,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing",
    ],

)
