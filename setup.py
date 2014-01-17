# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

version = open(os.path.join("version.txt")).read().strip()

setup(
    name='bodleian.recipe.fedoracommons',
    version=version,
    description="zc.buildout to configure a fedora commons instance",
    long_description=open(os.path.join("README.md")).read() + "#n" +
                     open(os.path.join("docs", "CHANGES.rst")).read() + "#n" +
                     open(os.path.join("docs", "CONTRIBUTORS.rst")).read(),
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='',
    author='Calvin Butcher',
    author_email='calvin(dot)butcher-at-bodleian.ox.ac.uk',
    url='https://github.com/BDLSS/bodleian.recipe.fedoracommons.git',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'hexagonit.recipe.download',
    ],
    entry_points={
        'zc.buildout': ['default = bodleian.recipe.fedoracommons:Recipe']
    },
)

