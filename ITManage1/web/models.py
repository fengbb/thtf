#-*- coding:utf-8 -*-
##定义使用utf-8编码
#导入类库
from django.db import models
import django
from django.contrib.auth.models import User
import datetime
# Create your models here.
#定义IDC表
class IDC(models.Model):
    name = models.CharField(max_length=64,unique=True) ##unique=True,表字段中有重复的话，不能保存，也就是表字段不能重复
    # __unicode__() 方法可以进行任何处理来返回对一个对象的表示,方法未返回一个Unicode对象
    #返回name值
    # def __unicode__(self) python3 默认是str
    def __str__(self):
        return self.name
    #自己定义在admin后台中显示的名字
    class Meta:
        verbose_name = u'IDC'
        verbose_name_plural = u'IDC'
#定义部门表
class Department(models.Model):
    name = models.CharField(max_length=64,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'
#定义主机表
class Hosts(models.Model):
    hostname = models.CharField(max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField(unique=True) #定义ip地址字段
    #定义主机类型可选择类型
    system_type_choices = (
        ('windows','Windows'),
        ('linux','Linux/Unix')
    )
    idc = models.ForeignKey('IDC')  #外键，一对一字段，idc从IDC字段中选择
    system_type = models.CharField(choices=system_type_choices,max_length=32,default='linux') #choices=system_type_choices这个定义从system_type_choices着里面选择，default定义默认选择
    port = models.IntegerField(default=22) #定义端口字段，整形
    #models.BooleanField定义单选按钮，默认选择True，提示信息为help_text
    enabled = models.BooleanField(default=True,help_text=u'主机若不想被用户访问可以去掉此选项')
    #null=True 如果为True，空值将会被存储为NULL，默认为False,blank=True 如果为True，字段允许为空，默认不允许
    #null是针对数据库而言，如果null=True, 表示数据库的该字段可以为空。
    #blank是针对表单的，如果blank=True，表示你的表单填写该字段的时候可以不填
    memo = models.CharField(max_length=128,blank=True,null=True)
    #定义创建时间，auto_now_add=True自动添加当前时间
    #auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间
    #auto_now_add为添加时的时间，更新对象时不会有变动
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s(%s)' %(self.hostname,self.ip_addr)
    class Meta:
        verbose_name = u'主机'
        verbose_name_plural = u'主机'
#定义远程用户表
class HostUsers(models.Model):
    auth_method_choices = (('ssh-password',"SSH/Password"),('ssh-key',"SSH/KEY"))
    auth_method = models.CharField(choices=auth_method_choices,max_length=16,help_text=u'如果选择SSH/KEY，请确保你的私钥文件已在settings.py中指定')
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64,blank=True,null=True,help_text=u'如果auth_method选择的是SSH/KEY,那此处不需要填写..')
    memo = models.CharField(max_length=128,blank=True,null=True)
    def __str__(self):
        return '%s(%s)' %(self.username,self.password)
    class Meta:
        verbose_name = u'远程用户'
        verbose_name_plural = u'远程用户'
        #unique_together这个选项用于：当你需要通过两个字段保持唯一性时使用。比如假设你希望，一个Person的FirstName和LastName两者的组合必须是唯一的，那么需要这样设置：
        #unique_together = (("first_name", "last_name"),)
        unique_together = ('auth_method','password','username')
#定义主机与远程用户绑定表
class BindHosts(models.Model):
    host = models.ForeignKey('Hosts')
    host_user = models.ForeignKey('HostUsers')
    #定义多对多字段
    host_group = models.ManyToManyField('HostGroups')
    enabled = models.BooleanField(default=True)
    def __str__(self):
        return '%s(%s)' %(self.host.hostname,self.host_user.username)
    class Meta:
        unique_together = ("host","host_user")
        verbose_name = u'主机与远程用户绑定'
        verbose_name_plural = u'主机与远程用户绑定'
    def get_groups(self):
        return ",\n".join([g.name for g in self.host_group.all()])
class HostGroups(models.Model):
    name = models.CharField(max_length=64,unique=True)
    memo = models.CharField(max_length=128,blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组'
        verbose_name_plural = u'主机组'
#定义CrazyEye账户表
class UserProfile(models.Model):
    #定义一对一字段
    user = models.OneToOneField(User)
    name = models.CharField(unique=True,max_length=32)
    #定义外键，外键是一对多，就是一个部门可以有多个账户，一个账户只能有一个部门
    department = models.ForeignKey('Department',verbose_name=u'部门')
    host_groups = models.ManyToManyField('HostGroups',verbose_name=u'授权主机组')
    bind_hosts = models.ManyToManyField('BindHosts',verbose_name=u'授权主机')
    valid_begin_time = models.DateTimeField(default=django.utils.timezone.now)
    valid_end_time = models.DateTimeField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'CrazyEye账户'
        verbose_name_plural = u'CrazyEye账户'
#定义SessionTrack表
class SessionTrack(models.Model):
    data = models.DateTimeField(default=django.utils.timezone.now)
    closed = models.BooleanField(default=False)
    def __str__(self):
        return '%s' %self.id
#定义审计日志
class AuditLog(models.Model):
    session = models.ForeignKey(SessionTrack)
    user = models.ForeignKey('UserProfile')
    host = models.ForeignKey('BindHosts')
    action_choices = (
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'exception'),
    )
    action_type = models.IntegerField(choices=action_choices,default=0)
    cmd = models.TextField()
    memo = models.CharField(max_length=128,blank=True,null=True)
    date = models.DateTimeField()
    def __str__(self):
        return '%s-->%s@%s:%s' %(self.user.user.username,self.host.host_user.username,self.host.host.ip_addr,self.cmd)
    class Meta:
        verbose_name = u'审计日志'
        verbose_name_plural = u'审计日志'
#定义批量任务表
class TaskLog(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True,blank=True)
    task_type_choices = (('cmd',"CMD"),('file_send',"批量发送文件"),('file_get',"批量下载文件"))
    task_type = models.CharField(choices=task_type_choices,max_length=50)
    user = models.ForeignKey('UserProfile')
    hosts = models.ManyToManyField('BindHosts')
    cmd = models.TextField()
    expire_time = models.IntegerField(default=30)
    task_pid = models.IntegerField(default=0)
    note = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return "taskid:%s cmd:%s" % (self.id,self.cmd)
    class Meta:
        verbose_name = u'批量任务'
        verbose_name_plural = u'批量任务'
class TaskLogDetail(models.Model):
    child_of_task = models.ForeignKey('TaskLog')
    bind_host = models.ForeignKey('BindHosts')
    date = models.DateTimeField(auto_now_add=True)
    event_log = models.TextField()
    result_choices = (('success','success'),('failed','failed'),('unknown','unknown'))
    result = models.CharField(choices=result_choices,max_length=30,default='unknown')
    note = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return "child of:%s result:%s" % (self.child_of_task.id,self.result)
    class Meta:
        verbose_name = u'批量任务日志'
        verbose_name_plural = u'批量任务日志'
class Token(models.Model):
    user = models.ForeignKey(UserProfile)
    host = models.ForeignKey(BindHosts)
    token = models.CharField(max_length=64)
    date = models.DateTimeField(default=django.utils.timezone.now)
    expire = models.IntegerField(default=300)
    def __str__(self):
        return '%s : %s' % (self.host.host.ip_addr,self.token)


#test
class Test(models.Model):
    test = models.CharField(max_length=32)
    num = models.IntegerField()
    def __str__(self):
        return self.test








