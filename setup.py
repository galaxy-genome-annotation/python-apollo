#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()


setup(
    name="apollo",
    version='2.0',
    description="WebApollo API library",
    long_description=readme,
    author="E Rasche",
    author_email="hxr@hx42.org",
    url='https://github.com/erasche/python-apollo',
    packages=['apollo'],
    install_requires=['requests>=2.4.3'],
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
