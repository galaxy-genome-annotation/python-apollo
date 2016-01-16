# http://bugs.python.org/issue15881#msg170215
from setuptools import setup, find_packages

setup(
    name="apollo",
    version='1.0',
    description="WebApollo API library",
    author="Eric Rasche",
    author_email="esr@tamu.edu",
    install_requires=['requests>=2.4.3'],
    packages=find_packages(),
    license='MIT',
    platforms="Posix; MacOS X; Windows",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"
    ])
