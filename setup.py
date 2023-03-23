#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Python bindings to the Syncthing REST interface, targeting v0.14.44"""


from pathlib import Path

from setuptools import setup


with open(Path(__file__).parent.joinpath('README.md'),
          encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='syncthing2',
    version='2.4.5',
    author='Blake VandeMerwe',
    author_email='blakev@null.net',
    description='Python bindings to the Syncthing REST interface, targeting v0.14.44',
    long_description=long_description,
    url='https://github.com/blakev/python-syncthing',
    license='The MIT License',
    install_requires=[
        'python-dateutil>=2.8.1,<=2.8.2',
        'requests>=2.24.0,<3'
    ],
    extras_require={
        'dev': [
            'sphinx',
            'sphinxcontrib-napoleon',
            'sphinx_rtd_theme'
        ]
    },
    packages=[
        'syncthing'
    ],
    package_dir={
        'syncthing': 'syncthing'
    },
    include_package_data=True,
    zip_safe=True,
    keywords='syncthing,sync,rest,backup,api',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Archiving :: Mirroring'
    ],
    data_files=[('README.md', ['README.md'])],
)
