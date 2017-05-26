#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('alagitpull/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# Base requirements
with open('requirements/base.txt') as f:
    install_reqs = [line for line in f.read().split('\n') if line]

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='alagitpull',
    version=version,
    description='Cleverly-named alabaster sub-theme for git-pull projects',
    long_description=readme,
    install_requires=install_reqs,
    author='Tony Narlock',
    author_email='tony@git-pull.com',
    url='https://alagitpull.git-pull.com',
    packages=['alagitpull'],
    include_package_data=True,
    entry_points={
        'sphinx_themes': [
            'alagitpull = alagitpull:get_path',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
