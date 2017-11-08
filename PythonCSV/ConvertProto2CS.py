# -*- coding: utf-8 -*-
# coding: utf-8

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

def gci(dirpath):
# 遍历filepath下所有文件 包括子目录.
	files = os.listdir(dirpath)
	for fi in files:
		fi_d = os.path.join(dirpath,fi);
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			fileName =  os.path.join(dirpath,fi_d)
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

# 处理单个文件.
def HandleOneFile(filePath):
	# print filePath
	# LoadFile(filePath)

	#取出文件名 组合为file.proto
	# GlobalVariable.CSVData[0].strip('\r\n').split(',')

	# print filePath
	print "Handle " + filePath + '......'

	fileSingleName = GetAbsoluteFileNameByFullPath(filePath)
	# print fileSingleName
	#组合输出proto路径
	cSharpFile = GlobalVariable.CsharpOutPath + fileSingleName + '.cs'
	# print cSharpFile
	
	#组合为执行字符串.

	strCSEXE = GlobalVariable.ProtoGenEXE + ' ' + '-i:' + filePath + ' ' + '-o:' + cSharpFile

	# print 生成CS类.
	os.system(strCSEXE)

	# 生成Python解释类.
	strPythonEXE = GlobalVariable.ProtocEXE + ' ' + '-I=' + \
					GlobalVariable.ProtoOutPath + ' ' + '--python_out=' +  GlobalVariable.PythonClassOutPath + \
					' ' + GlobalVariable.ProtoOutPath + fileSingleName + '.proto'

	# print strPythonEXE
	os.system(strPythonEXE)

# 处理所有文件.
def HandleAllFiles(protoPath,csharpPath):
	# print csvpath
	# print protopath
	gci(protoPath)

def main ():


	GlobalVariable.ProtoGenEXE = sys.argv[1]
	# -i:%ProtoPath%Creature.proto -o:%CSharpPath%Creature.cs
	# print sys.argv[1]

	GlobalVariable.ProtoOutPath = sys.argv[2]
	GlobalVariable.CsharpOutPath = sys.argv[3]
	GlobalVariable.PythonClassOutPath = sys.argv[4]
	GlobalVariable.ProtocEXE = sys.argv[5]
	
	HandleAllFiles(GlobalVariable.ProtoOutPath,GlobalVariable.CsharpOutPath)

	# print GlobalVariable.ProtoGenEXE

	# 传入ProtoFiles 目录.
	# 传入CSharpClass 目录.

	# Protogen执行路径.
	# os.system(GlobalVariable.ProtoGenEXE)

	# proto目录路径





if __name__ == '__main__':
    main()




