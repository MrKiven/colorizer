# -*- coding: utf-8 -*-

"""
The formatter for ANSI colored console output is heavily based on Pygments
terminal colorizing code.
"""

from setuptools import setup

VERSION = "0.1.1"


setup(
    name='colorizer-py',
    version=VERSION,
    url="https://github.com/MrKiven/colorizer",
    license="MIT",
    author="MrKiven",
    author_email="kiven.mr@gmail.com",
    description=__doc__.strip('\n'),
    scripts=[],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.3',
        # 'Programming Language :: Python :: 2.4',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
    ]
)
