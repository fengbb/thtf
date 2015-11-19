#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
import time
def json_date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d %T")
def json_date_to_stamp(obj):
    if hasattr(obj,'isoformat'):
        return time.mktime(obj.timetuple()) *1000
