#coding=utf-8
from django.db import models
# Create your models here.
class User(models.Model):
    username = models.CharField(u'用户名',max_length=30)
    password = models.CharField(u'用户密码',max_length=100)
    email = models.EmailField(u'电子邮箱')
    def __unicode__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理'
