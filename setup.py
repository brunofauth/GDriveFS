#!/usr/bin/env python

import os
from pathlib import Path
import setuptools

import gdrivefs

REPO_ROOT = Path(os.path.dirname(__file__))


with open(REPO_ROOT / 'README.rst') as f:
      long_description = f.read()

with open(REPO_ROOT / 'requirements.txt') as f:
      install_requires = [line.strip() for line in f.readlines() if line]


setuptools.setup(
    name='gdrivefs',
    version=gdrivefs.__version__,
    description="A complete FUSE adapter for Google Drive.",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Topic :: System :: Filesystems',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Utilities'
    ],
    keywords='google-drive google drive fuse filesystem',
    author='Dustin Oprea',
    author_email='myselfasunder@gmail.com',
    url='https://github.com/dsoprea/GDriveFS',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={'gdrivefs': ['resources/client_secrets.json']},
    zip_safe=False,
    install_requires=install_requires,
    entry_points={"console_scripts": [
        "gdfs=gdrivefs.scripts.gdfs:main",
        "gdfstool=gdrivefs.scripts.gdfstool:main",
        "gdfsdumpentry=gdrivefs.scripts.gdfsdumpentry:main",
    ]}
)
