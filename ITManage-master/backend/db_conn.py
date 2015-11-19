#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
import sys,os
basedir = '/'.join(__file__.split("/")[:-2])
sys.path.append(basedir)

sys.path.append('%s/ITManage' %basedir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ITManage.settings'
import django
django.setup()


