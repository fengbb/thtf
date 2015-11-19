#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
import os
import re
path = "D:\\test"
#使用os.walk遍历目录，这个方法返回的是一个三元tupple(dirpath, dirnames, filenames),
for i in os.walk(path):
    #print(i)
    #print (i[2])
    if len(i[2]):
        #使用for循环操作文件名
        for a in i[2]:
            b = a.split(".")[0].upper()
            if re.search(r"\s+",b):
                #print (i[0],b)
                filename = '%s\%s.%s' % (i[0],b.strip(),a.split(".")[1])
                filename1 = '%s\%s.%s' % (i[0],b,a.split(".")[1])
                #print (filename)
                if os.path.exists(filename):
                    os.remove(filename1)
                else:
                    os.rename(filename1,filename)