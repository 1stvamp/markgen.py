"""Installer for markgen
"""

from setuptools import setup, find_packages

setup(
    name='markgen',
    description='Python library for the programmatic generation of markdown text',
    long_description=open('README.rst').read(),
    provides=['markgen'],
    version='0.9.0',
    author='Wes Mason',
    author_email='wes@1stvamp.org',
    url='https://github.com/1stvamp/markgen.py',
    packages=find_packages(exclude=['ez_setup']),
    package_data={'': 'markgen_test_doc.md'},
    include_package_data=True,
    license='BSD'
)
