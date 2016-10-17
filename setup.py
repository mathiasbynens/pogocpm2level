#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
	name = 'pogocpm2level',
	packages = ['pogocpm2level'],
	version = '1.0.1',
	download_url = 'https://github.com/mathiasbynens/pogocpm2level/tarball/v1.0.1',
	description = 'Easily calculate the level of a given Pokémon in Pokémon GO based on its total CP multiplier value.',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Software Development :: Libraries',
	],
	author = 'Mathias Bynens',
	author_email = 'mathias@qiwi.be',
	license='MIT',
	url = 'https://github.com/mathiasbynens/pogocpm2level',
	keywords = ['pogo', 'pokemon go', 'cpm'],
	test_suite='nose.collector',
	tests_require=['nose'],
)
