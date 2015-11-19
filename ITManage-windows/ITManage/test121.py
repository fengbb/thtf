# -*- coding: utf-8 -*-
import os
import re
import shutil
import time
#import tqdm
#源文件目录
Source_Path = 'E:\\test'
#目的文件目录
Objective_Path = 'E:\\test1'

def chageFile():
	for Source_File_List in os.listdir(Source_Path):
		#time.sleep(0.1)
		Count_File_Number = len(os.listdir(Source_Path))
		Count_Finish_File_Number = 1
		#把文件名全部转换成大写
		Finish_Source_File_List = Source_File_List.upper()
		#获取到文件的第一个字母,并转换成大写
		Path_First_Character = Finish_Source_File_List[0]
		#获取子目录全称
		if '-' in Finish_Source_File_List:
			Path_All_Character = Finish_Source_File_List.split('-')[0]
		#获取目的文件夹的全路径
		Final_Path = Objective_Path + '\\' + Path_First_Character + '\\' + Path_All_Character
		#创建目的文件夹的全路径，如果没有就创建
		isExists = os.path.exists(Final_Path)
		if not isExists:
			print("%s 文件夹创建成功" % (Final_Path))
			os.makedirs(Final_Path)
		else:
			print("%s 目录已存在" % (Final_Path))
		#获取目的文件的全路径
		#Final_File = Final_Path + '\\' + Finish_Source_File_List
		#判断文件名中是否含有空格
		if re.search(r"\s+",Finish_Source_File_List):
			Final_File = Final_Path + '\\' + Finish_Source_File_List.replace(' ','')
			if os.path.exists(Final_File):
				print("正在删除文件 %s" % (Final_File))
				os.remove(Final_File)
		else:
			Final_File = Final_Path + '\\' + Finish_Source_File_List
			if os.path.exists(Final_File):
				print("正在删除文件 %s" % (Final_File))
				os.remove(Final_File)


		#准备开始拷贝文件
		#如果目的地目的文件存在则删除
#		if os.path.exists(Final_File):
#			print("正在删除文件 %s" % (Final_File))
#			os.remove(Final_File)
		#获取源文件的全路径
		Source_File_Path = Source_Path + '\\' + Source_File_List
		print("正在拷贝第%s个文件" % (Count_Finish_File_Number))
		print("还剩%s个文件" % (Count_File_Number-Count_Finish_File_Number))
		print("正在拷贝文件 ==》%s" % (Final_File))
		shutil.move(Source_File_Path, Final_File)
		print("文件 %s 拷贝完成" % (Final_File))
#		print("正在删除文件 ==》 %s" % (Source_File_Path))
#		os.remove(Source_File_Path)
		print("源文件 %s 已经删除" % (Source_File_Path))
		Count_Finish_File_Number = Count_Finish_File_Number+1

if __name__ == '__main__':
	chageFile()