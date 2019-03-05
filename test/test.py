# -*- coding: utf-8 -*-
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from sample import *

class sampleTest(unittest.TestCase):
	def test_number_sum(self):
		self.assertEqual(number_sum(3,5), 8)

if __name__ == '__main__':
	unittest.main()

