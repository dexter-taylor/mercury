#!/usr/bin/env python

# setuptools script for Mercury data management framework 

import codecs
import os
import re


from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


NAME = 'mercury'
VERSION = '0.8.3'
PACKAGES = find_packages(where='src')
DEPENDENCIES=['snap-micro',
              'docopt',
              'arrow',
              'Flask',
              'itsdangerous',
              'Jinja2',
              'kafka',
              'MarkupSafe',
              'PyYAML',
              'SQLAlchemy',
              'SQLAlchemy-Utils',
              'Werkzeug',
              'requests',
              'boto3',
              'botocore',
              'raven',
              'redis',
              'sh']

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mercury-toolkit',
    version=VERSION,
    author='Dexter Taylor',
    author_email='binarymachineshop@gmail.com',
    platforms=['any'],
    scripts=['scripts/kload',
             'scripts/k2olap',
             'scripts/seesv',
             'scripts/xlseer',
             'scripts/mkmap',
             'scripts/xfile',
             'scripts/ngst',
             'scripts/j2sqlgen',
             'scripts/bqex',
             'scripts/bqstream-x'],
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    test_suite='tests',
    description=('Mercury: a framework for fluid ETL and data management'),
    license='MIT',
    keywords='ETL data pipeline framework',
    url='http://github.com/binarymachines/mercury',
    long_description=read('README.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development'
    ]
)
