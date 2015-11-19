#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
import sys
basedir = '/'.join(__file__.split("/")[:-2])
sys.path.append(basedir)
from backend import main
if __name__ == '__main__':
    main.call(sys.argv[1:])
