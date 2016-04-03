#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='lotube-crawler',
  version='1.0',
  description='LOTube video crawler',
  author='lotube',
  url='https://github.com/zurfyx',
  packages=[
    'lotube_crawler',
    'lotube_crawler.base',
    'lotube_crawler.extractor',
  ],
  install_requires=[
    'requests',
  ],
)
