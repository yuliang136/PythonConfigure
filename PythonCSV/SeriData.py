# -*- coding: utf-8 -*-
# coding: utf-8
# 序列化数据

import csv
import codecs
import GlobalVariable
import sys
import os;

def LoadFile(filePath):
	with codecs.open(filePath, 'r', 'utf8') as f:
		GlobalVariable.CSVData = f.readlines()

	GlobalVariable.ItemName = GlobalVariable.CSVData[0].strip('\r\n').split(',')
	GlobalVariable.ItemType = GlobalVariable.CSVData[2].strip('\r\n').split(',')
	GlobalVariable.ItemNums = len(GlobalVariable.ItemName)			#获得数据列数
	GlobalVariable.ItemRows = len(GlobalVariable.CSVData)			#获得数据表行数 Rows.


def gci(dirpath):
# 遍历filepath下所有文件 包括子目录.
	files = os.listdir(dirpath)
	for fi in files:
		fi_d = os.path.join(dirpath,fi);
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			fileName =  os.path.join(dirpath,fi_d)

			# 取得后缀名字 进行判断是否是csv.
			strpartsLen = len(fileName.split('.'))
			strExt = fileName.split('.')[strpartsLen-1]

			# print strExt
			if strExt.lower() == 'csv':
				HandleOneFile(fileName)

# 获得不含文件扩展名的 绝对文件名字
def GetAbsoluteFileNameByFullPath(filePath):
	fileparts = filePath.split('\\')
	# print fileparts

	#取出最后一个file.csv
	fileSingleName = fileparts[len(fileparts) - 1]
	# print fileSingleName

	#取出文件name file.
	fileparts = fileSingleName.split('.')
	fileSingleName = fileparts[0]
	return fileSingleName

# 数据解析类. 使用CSV生成bytes二进制文件.
class DataParser:
	
	def __init__(self, csv_file_path, pb2Module, pbDataFilePath,pb2ModuleDir):
		self.csv_file_path = csv_file_path
		self.pb2Module = pb2Module
		self.pbDataFilePath = pbDataFilePath
		self.pb2ModuleDir = pb2ModuleDir
		self.ModuleName = self.pb2Module.split('_')[0]
		# print self.csv_file_path
		# print self.pb2Module
		# print self.pbDataFilePath 
	
	def LoadFile(self):
		with codecs.open(self.csv_file_path, 'r', 'utf8') as f:
			self.CSVData = f.readlines()

		# 第一行为名字.
		# 第二行为类型.
		# 第三行为注释.
		self.ItemName = self.CSVData[0].strip('\r\n').split(',')
		self.ItemType = self.CSVData[1].strip('\r\n').split(',')
		self.ItemNums = len(self.ItemName)			#获得数据列数
		self.ItemRows = len(self.CSVData)			#获得数据表行数 Rows.

		# print self.CSVData
		# print self.ItemName
		# print self.ItemType
		# print self.ItemNums
		# print self.ItemRows

	def LoadModule(self):
		# 加载模块
		from sys import path
		path.append(self.pb2ModuleDir)		
		import_string = 'import ' + self.pb2Module
		# print import_string
		exec import_string
		self._module = sys.modules[self.pb2Module]
		# print self._module

	def GetValue(self,itemType,itemValue):
		itemRtn = 0

 		if itemType == 'int':

 			if itemValue == '':
 				itemRtn = int('0')
 			else:
 				itemRtn = int(itemValue)

 		elif itemType == 'string':
 			if itemValue == '':
 				itemRtn = ''
 			else:
 				itemRtn = itemValue

 		elif itemType == 'float':
 			if itemValue == '':
 				itemRtn = float('0')
 			else:
 				itemRtn = float(itemValue)
 			
 		return itemRtn

 	def Write2File(self, writeData):
 		f = open(self.pbDataFilePath, 'wb')
		f.write(writeData.SerializeToString())
		f.close()
 		


	# 解析数据.
	def Parse(self):
		self.LoadFile()
		self.LoadModule()

		messageItem = getattr(self._module, self.ModuleName)()

		# print messageItem
		# print type(messageItem)

		# 循环遍历没有数据. 要减去前三排数据.
		for x in range(3,self.ItemRows):
			# print x
			# print self.CSVData[x]

			# 实例化一个item变量.
			item = messageItem.items.add()

			rowField = self.CSVData[x].strip('\r\n').split(',')

			# print rowField
			# 用','断开字符串.
			# 再遍历列数.
			for column in xrange(0,self.ItemNums):
				# print column
				strValue = rowField[column]
				# print 'strValue : ', strValue

				# 取得值.
				ItemValue = self.GetValue(self.ItemType[column], strValue)
				# print 'ItemValue :', ItemValue

				# 取得字符串字段名.
				ItemFieldName = self.ItemName[column]
				# print 'ItemFieldName :', ItemFieldName

				setattr(item,ItemFieldName,ItemValue)

		

		# print messageItem.items[0].Name
		self.Write2File(messageItem)



		

# 处理单个文件.
def HandleOneFile(filePath):
	# print filePath
	# LoadFile(filePath)

	#取出文件名 组合为file.proto
	# GlobalVariable.CSVData[0].strip('\r\n').split(',')

	# print filePath
	print "Handle " + filePath + '......'


	fileName = os.path.basename(filePath);
	# print fileName

	fileNameNoExt = os.path.splitext(fileName)[0]

	# print fileNameNoExt

	csvFilePath = filePath
	pb2FileModule = fileNameNoExt + '_pb2'
	pbDataFilePath = GlobalVariable.ProtoDataPath + fileNameNoExt + '.bytes'

	# print csvFilePath
	# print pb2FileModule
	# print pbDataFilePath

	dataHandle = DataParser(csvFilePath,pb2FileModule,pbDataFilePath,GlobalVariable.PythonClassOutPath)
	dataHandle.Parse()


# 处理所有文件.
def HandleAllFiles():
	# print csvpath
	# print protopath
	gci(GlobalVariable.CSVInPath)

def main ():


	# GlobalVariable.ProtoGenEXE = sys.argv[1]
	# # -i:%ProtoPath%Creature.proto -o:%CSharpPath%Creature.cs
	# # print sys.argv[1]

	GlobalVariable.CSVInPath = sys.argv[1]
	GlobalVariable.PythonClassOutPath = sys.argv[2]
	GlobalVariable.ProtoDataPath = sys.argv[3]

	# print GlobalVariable.CSVInPath
	# print GlobalVariable.PythonClassOutPath
	# print GlobalVariable.ProtoDataPath

	# GlobalVariable.CsharpOutPath = sys.argv[3]
	# GlobalVariable.PythonClassOutPath = sys.argv[4]
	# GlobalVariable.ProtocEXE = sys.argv[5]
	
	HandleAllFiles()

	# print GlobalVariable.ProtoGenEXE

	# 传入ProtoFiles 目录.
	# 传入CSharpClass 目录.

	# Protogen执行路径.
	# os.system(GlobalVariable.ProtoGenEXE)

	# proto目录路径





if __name__ == '__main__':
    main()




