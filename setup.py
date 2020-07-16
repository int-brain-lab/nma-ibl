#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='nma-ibl',
    version='0.1.0',
    description='Toolkits to access data in IBL public database',
    author='Vathes',
    author_email='support@vathes.com',
    packages=find_packages(exclude=[]),
    install_requires=['datajoint>=0.12', 'seaborn>=0.10.0'],
)
