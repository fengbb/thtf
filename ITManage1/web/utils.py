#-*- coding:utf-8 -*-
__author__ = 'DN'
from ITManage import settings
import os,tempfile,zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from web import models
import django
from django.db.models import Count
#from backend import utils
import random,json,datetime,time
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import os

def handle_upload_file(request,file_obj):
    upload_dir = '%s%s%s' %(settings.BASE_DIR,settings.FileUploadDir,request.user.userprofile.id)
    if not os.path.isdir(upload_dir):
        os.mkdir(upload_dir)
    with open('%s%s' % (upload_dir,file_obj.name),'wb') as destination:
        #返回一个上传文件的分块生成器。如multiple_chunks()返回True,必须在循环中使用chrunks()来代替read()。
        # 一般情况下直接使用chunks()就行。
        for chunk in file_obj.chunks():
            destination.write(chunk)
def send_file(request):
    filename = __file__
    ##python3 没有file用open代替
    wrapper = FileWrapper(open(filename))
    response = HttpResponse(wrapper,content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response
def send_zipfile(request,task_id,file_path):
    zip_file_name = 'task_id_%s_file' % task_id
    archive = zipfile.ZipFile(zip_file_name,'w',zipfile.ZIP_DEFLATED)
    file_list = os.listdir(file_path)
    for filename in file_list:
        archive.write('%s/%s' % (file_path,filename))
    archive.close()
    wrapper = FileWrapper(open(zip_file_name))
    response = HttpResponse(wrapper,content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s.zip' % zip_file_name
    response['Content-Length'] = os.path.getsize(zip_file_name)
    return response
class Token(object):
    def __init__(self,request):
        self.request = request
        self.token_type = request.POST.get('token_type')
        self.token = {'token':None}
    def generate(self):
        func = getattr(self,self.token_type)
        return func()
    def host_token(self):
        bind_host_id = self.request.POST.get('bind_host_id')
        host_obj = models.BindHosts.objects.get(id=int(bind_host_id))
        latest_token_obj = models.Token.objects.filter(host_id = int(bind_host_id),user_id=self.request.user.userprofile.id).last()
        token_gen_flag = False
        if latest_token_obj:
            token_gen_time_stamp = time.mktime(latest_token_obj.date.timetuple())
            current_time = time.mktime(django.utils.timezone.now().timetuple())
            if current_time - token_gen_time_stamp > latest_token_obj.expire:
                #定义过期标签
                token_gen_flag = True
        else:
            token_gen_flag = True
        if token_gen_flag:
            token = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890',6))
            models.Token.objects.create(
                user = self.request.user.userprofile,
                host = host_obj,
                token = token
            )
        else:
            token = latest_token_obj.token
        self.token['token'] = token
        return json.dumps(self.token)
def get_all_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=django.utils.timezone.now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id',None))
    return User.objects.filter(id__in=uid_list)
class Dashboard(object):
    def __init__(self,request):
        self.request = request
    def get(self):
        data_type = self.request.GET.get("data_type")
        #assert的作用是现计算表达式 expression ，如果其值为假（即为0），
        # 那么它先向stderr打印一条出错信息，然后通过调用 abort 来终止程序运行。
        assert data_type is not None
        func = getattr(self,data_type)
        return func()
    def get_online_users(self):
        return get_all_logged_in_users().values('userprofile__name','userprofile__department__name','last_login','userprofile__id')
    def get_online_hosts(self):
        return models.SessionTrack.objects.filter(auditlog__action_type=1,closed=0).values('auditlog__host__host__hostname',
                                                                                           'auditlog__user__name',
                                                                                           'auditlog__host__host__ip_addr',
                                                                                           'auditlog__host__host__id',
                                                                                           'auditlog__host__host_user__username',
                                                                                           'auditlog__session',
                                                                                           'id','date')
def dashboard_summary(request):
    data_dic = {
        'user_login_statistics':[],
        'recent_active_users':[],
        'recent_active_users_cmd_count':[],
        'summary':{}
    }
    data_dic['user_login_statistics'] = list(models.AuditLog.objects.filter(action_type=1).extra({"login_date":"date(date)"}).values_list('login_date').annotate(count=Count('pk')))
    #data_dic['user_login_statistics'] = list(models.AuditLog.objects.filter(action_type=1).extra({"login_date":"date(date"}).values_list('login_date').annotate(count=Count('pk')))
    days_before_7 = django.utils.timezone.now() +django.utils.timezone.timedelta(days=-7)
    recent_active_users = models.AuditLog.objects.filter(date__gt = days_before_7,action_type=1).values('user','user__name').annotate(Count('user'))
    recent_active_users_cmd_count = models.AuditLog.objects.filter(date__gt = days_before_7,action_type=0).values('user','user__name').annotate(Count('cmd'))
    data_dic['recent_active_users'] = list(recent_active_users)
    data_dic['recent_active_users_cmd_count'] = list(recent_active_users_cmd_count)
    data_dic['summary']['total_servers'] = models.Hosts.objects.count()
    data_dic['summary']['total_users'] = models.UserProfile.objects.count()
    data_dic['summary']['current_logging_users'] = get_all_logged_in_users().count()
    current_connected_hosts = models.SessionTrack.objects.filter(closed=0).count()
    data_dic['summary']['current_connected_hosts'] = current_connected_hosts
    return data_dic
def recent_accssed_hosts(request):
    days_before_14 = django.utils.timezone.now()+django.utils.timezone.timedelta(days=-14)
    recent_logins = models.AuditLog.objects.filter(date__gt = days_before_14,user_id=request.user.userprofile.id,action_type=1).order_by('date')
    unique_bindhost_ids = set([i[0] for i in recent_logins.values_list('host_id')])
    recent_login_hosts = []
    for h_id in unique_bindhost_ids:
        recent_login_hosts.append(recent_logins.filter(host_id=h_id).latest('date'))
    return set(recent_login_hosts)









