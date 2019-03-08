# -*- coding: utf-8 -*-
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import pandas as pd
from pyDataset import *

class pyDataSetTest(unittest.TestCase):
	def setUp(self) :
		self.ds = DataSet()

	def test_splitConfigArgumentToken(self) :
		self.assertEqual(splitConfigArgumentToken(None), None)
		self.assertEqual(splitConfigArgumentToken(""), "")
		self.assertEqual(splitConfigArgumentToken("Text"), "Text")
		self.assertEqual(splitConfigArgumentToken("연도|STR, 월|STR"), [["연도","STR"], ["월","STR"]])
		self.assertEqual(splitConfigArgumentToken("연도|STR"), [["연도","STR"]])

	def test_aprintKeys(self) :
		self.assertEqual(self.ds.printKeys(), 2)

	def test_getInfo(self) :
		answer = "TITLE=전국 신규 민간 아파트 분양가격 동향" + os.linesep
		answer+= "DESCRIPTION=주택분양보증을 받아 분양한 전체 민간 신규아파트 분양가격 동향" + os.linesep
		answer+= "CREATE_DATE=2019-01-18"
		self.assertEqual(self.ds.getInfo('Average price of korean a lot-solid apartment'), answer)

	def test_getKeys(self) :
		dsk = self.ds.getKeys()
		self.assertEqual(dsk[0], "SAMPLE DATA")
		self.assertEqual(dsk[1], "AVERAGE PRICE OF KOREAN A LOT-SOLID APARTMENT")

	def test_loadData(self) :
		data = self.ds.loadData('Sample Data')
		print(data.head())
		self.assertEqual(isinstance(data, pd.core.frame.DataFrame), True);

if __name__ == '__main__':
	unittest.main()

