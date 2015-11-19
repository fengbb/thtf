#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
from django.contrib import admin
from web import models
#测试
class MyAdminSite(admin.AdminSite):
    site_header = 'TEST ADMIN site'
admin_site = MyAdminSite(name="TEST_ADMIN")
admin_site.register(models.BindHosts)
