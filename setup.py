#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='YOUR_APP_NAME',
    version='0.1.0',
    description='YOUR DESCRIPTION',
    author='AUTHOR',
    author_email='AUTHOR@COMPANY.COM',
    url='https://github.com/COMPANY/REPO',
    packages=find_packages(exclude=['tests']),
    install_requires=['django', 'DEPENDENCY_ONE', 'DEPENDENCY_TWO']
)
