# -*- coding: utf-8 -*-
import configparser
import pandas as pd
import matplotlib.font_manager as fm
import matplotlib as mpl
import os

def _isShowInfo(keyname) :
	return keyname=="TITLE" or keyname=="DESCRIPTION" or keyname=="CREATE_DATE"

def _StringtoNumber(text) :
	if "." in text :
		return float(text)
	return int(text)

def splitConfigArgumentToken(txt) :
	if txt==None or txt=="" :
		return txt

	lines = txt.split(",")
	if len(lines)==1 : # String
		rt = txt.split("|")
		if len(rt)==1 :
			return txt

	result = []
	for l in lines :
		result.append(l.strip().split("|"))

	return result

class DataSet:
	def __init__(self) :
		self.dataSetInfo = configparser.ConfigParser()
		data_filpath = os.path.join(os.path.dirname(__file__), 'dataset.dat')
		self.dataSetInfo.read(data_filpath)
		self.rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

	def _doTransformColumnType(self, p) :
		vparams = splitConfigArgumentToken(p)
		for vparam in vparams:
			if vparam[1]=="STR" :
				self.data[vparam[0]] = self.data[vparam[0]].astype(str)

	def _doTransformAddColumn(self, p) :
		vparams = splitConfigArgumentToken(p)
		for vparam in vparams:
			if vparam[1]=="to_numeric" :
				self.data[vparam[0]] = pd.to_numeric(self.data[vparam[2]], errors='coerce')
			elif vparam[1]=="mul" :
				self.data[vparam[0]] = self.data[vparam[2]]*_StringtoNumber(vparam[3])

	def _doTransformDeleteColumn(self, p) :
		vparams = splitConfigArgumentToken(p)
		if isinstance(vparams, str) :
			self.data = self.data.drop([vparams], axis=1)

	def _doTransformationDatas(self, cfg) :
		skeys = list(cfg)
		for k in skeys :
			if k == "column_type" :
				self._doTransformColumnType(cfg["COLUMN_TYPE"])
			elif k == "add_column" :
				self._doTransformAddColumn(cfg["ADD_COLUMN"])
			elif k == "delete_column" :
				self._doTransformDeleteColumn(cfg["DELETE_COLUMN"])

	def enableMatplotlibCustomFont(self, font_filename='NanumBarunGothic') : # pragma: no cover
		'''change font for Matplotlib.
		If you use Korean characters, you need to set the font so that you can see the correct characters.
		This method tested UbunutOS and MacOS.'''
		fontpaths = ['/usr/share/fonts/truetype/nanum/'+font_filename+'.ttf', '/Library/Fonts/'+font_filename+'.ttf', os.path.join(self.rootPath, font_filename+'.ttf')]
		for fontpath in fontpaths :
			if os.path.exists(fontpath) :
				fm.FontProperties(fname=fontpath, size=9)
				mpl.font_manager._rebuild()
				mpl.pyplot.rc('font', family=font_filename)
				return True
		return False

	def getInfo(self, dataname) :
		dskeys = list(self.dataSetInfo[dataname.upper()].keys())
		outtext = ""
		for k in dskeys :
			k = k.upper()
			if not _isShowInfo(k) :
				continue
			if outtext is not "" :
				outtext += os.linesep
			outtext+=k+"="+self.dataSetInfo[dataname.upper()][k]

		return outtext

	def getKeys(self) :
		return self.dataSetInfo.sections()

	def loadData(self, dataname, useTransform=True) :
		newData = self.dataSetInfo[dataname.upper()]
		data_filename = newData['ID'].lower() + newData['VERSION'].lower() + "." + newData['FILE_TYPE'].lower()
		data_filepath = os.path.join(self.rootPath, 'data', data_filename)
		self.data = pd.read_csv(data_filepath, encoding=newData['ENCODING'])
		if useTransform :
			self._doTransformationDatas(newData)
		return self.data

	def printKeys(self) :
		sectionCount = 0
		for section in self.dataSetInfo.sections():
			sectionCount+=1
			print(section)

		return sectionCount
