#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
subpackages = [x.replace('/', '.') for x in glob.glob('arrow/commands/*') if not x.endswith('.py') and not x.endswith('.pyc')] + \
    [x.replace('/', '.') for x in glob.glob('apollo/*') if not x.endswith('.py') and not x.endswith('.pyc')] + ['arrow.commands']

setup(
    name="apollo",
    version='3.1',
    description="Apollo API library",
    long_description=readme,
    author="Helena Rasche;Anthony Bretaudeau",
    author_email="hxr@hx42.org",
    url='https://github.com/galaxy-genome-annotation/python-apollo',
    packages=['apollo', 'arrow'] + subpackages,
    entry_points='''
        [console_scripts]
        arrow=arrow.cli:arrow
    ''',
    install_requires=['requests', 'biopython', 'cachetools', 'click>=6.7', 'wrapt', 'pyyaml', 'decorator'],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ])
