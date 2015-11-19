#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'
from web import models
from django.forms import ModelForm
from django import forms

class UserProfileForm(ModelForm):

    class Meta:
        models = models.UserProfile
        fields = ['name','department','valid_end_time']
        #fields = ['name','valid_begin_time','valid_end_time']
class RegistrationFrom(forms.Form):
    #label 用于字段在表单的显示，如果不设置那么显示的就是字段的名称了
    #initial初始化，用于指定字段的值当在一个未绑定表单中渲染字段时
    #widget 字段的小部件,改变字段的构造参数
    # 如title=forms.CharField(label=u'标题', widget=forms.TextInput(attrs={'size':'40'}))
    username = forms.CharField(label="Username",max_length=32,required=True)
    #
    name = forms.CharField(label="Real Nae",max_length=32,widget=forms.TextInput(attrs={'class' : 'btn-success'}))
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput)