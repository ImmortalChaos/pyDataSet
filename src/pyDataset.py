# -*- coding: utf-8 -*-
import configparser
import os

def isShowInfo(keyname) :
	return keyname=="TITLE" or keyname=="DESCRIPTION" or keyname=="CREATE_DATE"

class DataSet:
	def __init__(self) :
		self.dataSetInfo = configparser.ConfigParser()
		data_filpath = os.path.join(os.path.dirname(__file__), 'dataset.dat')
		self.dataSetInfo.read(data_filpath)

	def getInfo(self, dataname) :
		dskeys = list(self.dataSetInfo[dataname.upper()].keys())
		outtext = ""
		for k in dskeys :
			k = k.upper()
			if not isShowInfo(k) :
				continue
			if outtext is not "" :
				outtext += os.linesep
			outtext+=k+"="+self.dataSetInfo[dataname.upper()][k]

		return outtext


	def getKeys(self) :
		return self.dataSetInfo.sections()

	def loadData(self, dataname) :
		return self.dataSetInfo[dataname.upper()]['CREATE_DATE']

	def printKeys(self) :
		sectionCount = 0
		for section in self.dataSetInfo.sections():
			sectionCount+=1
			print(section)

		return sectionCount

if __name__ == "__main__":
	ds = DataSet()
	ds.printKeys()
