#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
import os,sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ITManage.settings")
base_dir = '/'.join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
sys.path.append(base_dir)

from web import models
