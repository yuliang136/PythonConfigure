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

	# print type(GlobalVariable.ItemType)
	# print GlobalVariable.ItemType

	# print ItemName
	GlobalVariable.ItemNums = len(GlobalVariable.ItemName)			#获得数据列数

	# print 'ItemNums ' + str(GlobalVariable.ItemNums)

	# print ItemNums

	# print type(items)
	# for eachItem in items:
	# 	print eachItem

		# print type(f.readlines())
		# for line in f.readlines():
			# print (line.strip())
			# print type(f.readlines())
		
	
	# with codecs.open('csv_test.csv','r','utf-8') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		print row

# def WriteCSV():
# 	csvfile = file(GlobalVariable.CSVInPath,'wb')
# 	writer = csv.writer(csvfile)
# 	writer.writerow(['姓名','年龄','电话'])

# 	data = [('小河', '25', '1234567'),
# 			('小芳', '18', '789456')]
# 	writer.writerows(data)
# 	csvfile.close()

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
			strparts = len(fileName.split('.'))
			strExt = fileName.split('.')[1]

			# print strExt
			if strExt.lower() == 'csv' and strparts == 2:
				HandleOneFile(fileName)

def GetEachItemContent(x):
	strRtn = GlobalVariable.doubleTab
	# print x
	# 全部都用required
	strRtn += 'required '
	# 判断类型 Proto里用int32 string
	strLoadType = GlobalVariable.ItemType[x]
	# print type(strLoadType)
	# print strLoadType

	strType = ''
	if strLoadType == u'int':
		strType = u'int32'
	elif strLoadType == u'string':
		strType = u'string'
	elif strLoadType == u'float':
		strType = u'float'
			
	strRtn = strRtn + strType + ' '

	# 变量名字
	strLoadName = GlobalVariable.ItemName[x]
	strRtn = strRtn + strLoadName + ' '

	# 等号
	strRtn += '= '
	# 序号从0开始

	num = x + 1
	strRtn += str(num) + ';'

	return strRtn

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

def WriteFramework(filePath):

	#取出不含后缀名的文件名字
	fileSingleName = GetAbsoluteFileNameByFullPath(filePath)

	# print fileSingleName

	# print fileSingleName
	# print filePath

	f = open(filePath,'w')
	f.write('message ' + fileSingleName + '\n')
	f.write('{' + '\n')
	f.write(GlobalVariable.StringTab + 'message ' + fileSingleName + 'Item'+ '\n')
	f.write(GlobalVariable.StringTab + '{' + '\n')

	# 循环读出内容 写入文件.
	# 循环的次数之前会读入.
	# print ItemNums
	for i in range(GlobalVariable.ItemNums):
		# print str(i)
		eachItemContent = GetEachItemContent(i)
		# print eachItemContent
		f.write(eachItemContent + '\n')

	# print GlobalVariable.ItemNums

	f.write(GlobalVariable.StringTab + '};' + '\n')

	f.write('\n')

	f.write(GlobalVariable.StringTab + 'repeated ' + fileSingleName + 'Item items = 1;' + '\n')

	f.write('}')
	
	f.close()

# str.decode( 'utf-8' )

# 处理单个文件.
def HandleOneFile(filePath):
	print "Handle " + filePath + '......'
	
	LoadFile(filePath)

	#取出文件名 组合为file.proto
	# GlobalVariable.CSVData[0].strip('\r\n').split(',')

	fileSingleName = GetAbsoluteFileNameByFullPath(filePath)
	# print fileSingleName

	#组合输出proto路径
	protoFile = GlobalVariable.ProtoOutPath + fileSingleName + '.proto'
	# print protoFile
	WriteFramework(protoFile)


# 处理所有文件.
def HandleAllFiles(csvpath,protopath):
	# print csvpath
	# print protopath
	gci(csvpath)

def main ():

	# print ("脚本名: " + sys.argv[0]).decode('utf-8')
	GlobalVariable.CSVInPath = sys.argv[1]
	GlobalVariable.ProtoOutPath = sys.argv[2]

	HandleAllFiles(GlobalVariable.CSVInPath, GlobalVariable.ProtoOutPath)


if __name__ == '__main__':
    main()




