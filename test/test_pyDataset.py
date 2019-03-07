# -*- coding: utf-8 -*-
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from pyDataset import *

class pyDataSetTest(unittest.TestCase):
	def setUp(self) :
		self.ds = DataSet()

	def test_aprintKeys(self) :
		self.assertEqual(self.ds.printKeys(), 1)

	def test_getInfo(self) :
		answer = "TITLE=전국 신규 민간 아파트 분양가격 동향" + os.linesep
		answer+= "DESCRIPTION=주택분양보증을 받아 분양한 전체 민간 신규아파트 분양가격 동향" + os.linesep
		answer+= "CREATE_DATE=2019-01-18"
		self.assertEqual(self.ds.getInfo('Average price of korean a lot-solid apartment'), answer)

	def test_getKeys(self) :
		dsk = self.ds.getKeys()
		self.assertEqual(dsk[0], "AVERAGE PRICE OF KOREAN A LOT-SOLID APARTMENT")

	def test_loadData(self) :
		self.assertEqual(self.ds.loadData('Average price of korean a lot-solid apartment'), "2019-01-18");

if __name__ == '__main__':
	unittest.main()

