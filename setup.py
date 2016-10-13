#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
	name = 'pogocpm2level',
	packages = ['pogocpm2level'],
	version = '1.0.0',
	download_url = 'https://github.com/mathiasbynens/pogocpm2level/tarball/v1.0.1',
	description = 'Easily calculate the level of a given Pokémon in Pokémon GO based on its total CP multiplier value.',
	author = 'Mathias Bynens',
	author_email = 'mathias@qiwi.be',
	license='MIT',
	url = 'https://github.com/mathiasbynens/pogocpm2level',
	keywords = ['pogo', 'pokemon go', 'cpm'],
	classifiers = [],
	test_suite='nose.collector',
	tests_require=['nose'],
)
