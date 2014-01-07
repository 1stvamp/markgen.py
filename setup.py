"""Installer for markgen
"""

from setuptools import setup, find_packages

setup(
    name='markgen',
    description='Python library for the programmatic generation of markdown text',
    long_description=open('README.rst').read(),
    provides=['markgen'],
    version='0.9.5',
    author='Wes Mason',
    author_email='wes@1stvamp.org',
    url='https://github.com/1stvamp/markgen.py',
    packages=find_packages(exclude=['markgen_tests']),
    license='BSD'
)
