#!/usr/bin/env python
# coding=utf-8

from unittest import TestCase

from pogocpm2level import cpm2level

class TestCalculation(TestCase):

	def test_scenario_1(self):
		self.assertEqual(cpm2level(0.095), 1.0)

	def test_scenario_2(self):
		self.assertEqual(cpm2level(0.703), 27.5)

	def test_scenario_3(self):
		self.assertEqual(cpm2level(0.491), 13.5)

	def test_scenario_4(self):
		self.assertEqual(cpm2level(0.738), 31.0)

	def test_scenario_5(self):
		self.assertEqual(cpm2level(0.741), 31.5)
