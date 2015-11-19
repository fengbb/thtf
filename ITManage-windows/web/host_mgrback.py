#-*- coding:utf-8 -*-
##定义使用utf-8编码
__author__ = 'DN'

import json,subprocess
import paramiko,time,os,signal
import multiprocessing
from ITManage import settings
from django.db import transaction
from backend.utils import json_date_handler
from web import models
def valid_host_groups_back(request):
    #select_related()使用的场景，是获取实体的同时，能快速获取到它对应的外键关系实体。如果获取实体时没有使用select_related()，
    # 要引用该实体的外键关系，那么就会重新连接数据库去获取对应实体了。比如 作者Author 博客Blog 两个表，他们的关系 是一个作者Author有多个博客blog，；
    # 当我们想获取到一个作者的同时 直接引用该作者的所有博客时，常规做法是会进行两次数据库连接的，但使用了select_related()后，情况就有所变化了，
    # 它第一次连接数据库获取该作者的时候，该作者的所有博客被获取到了。
    print (request.user)
    user_groups = models.UserProfile.objects.get(user_id = request.user.id).user_groups.select_related()
    host_groups = []
    for u_group in user_groups:
        host_groups += u_group.host_groups.select_related()
    host_groups = list(set(host_groups))
    host_group_dic = {-1:[]}
    selected_g_id = None
    active_g_item = None
    for h_group in host_groups:
        hosts = models.BindHosts.objects.filter(host_group_id = h_group.id)
        host_nums = len(set([i.host.ip_add for i in hosts]))
        hosts = list(hosts)
        selected_group = request.GET.get('selected_group')
        if selected_group:
            if selected_group.isdigit():
                if h_group.id == int(selected_group):
                    host_group_dic[h_group.id] = [h_group, host_nums,hosts]
                    selected_g_id = h_group.id
                else:
                    host_group_dic[h_group.id] = [h_group,host_nums]
            elif selected_group == '-1':
                selected_g_id = -1
                host_group_dic[h_group.id] = [h_group,host_nums]
        else:
            host_group_dic[h_group.id] = [h_group,host_nums]

    return [host_group_dic,selected_g_id]


def valid_host_groups(request):
    print (request.user)
    host_group_dic = {-1:[]}
    print (host_group_dic)
    #return [ host_group_dic,selected_g_id]
def valid_host_list(request):
    user_groups = models.UserProfile.objects.get(user_id = request.user.id).user_groups.select_related()
    host_groups = []
    for u_group in user_groups:
        host_groups += u_group.host_groups.select_related()
    host_groups = list(set(host_groups))
    host_group_dic = {-1:[]}
    for h_group in host_groups:
        hosts = models.BindHosts.objects.filter(host_group_id=h_group.id)
        host_nums = len(set([i.host.ip_add for i in hosts]))
        hosts = list(hosts)

        host_group_dic[h_group.id] = [h_group,host_nums,hosts]
    return host_group_dic
class MultiTask(object):
    def __init__(self,task_type,request_ins):
        self.request = request_ins
        self.task_type = task_type
    def run(self):
        return self.parse_args()
    def parse_args(self):
        task_func = getattr(self,self.task_type)
        return task_func()
    def terminate_task(self):
        task_id = self.request.POST.get('task_id')
        assert task_id.isdigit()
        task_obj = models.TaskLog.objects.get(id=int(task_id))
        res_msg = ' '
        try:
            os.killpg(task_obj.task_pid,signal.SIGTERM)
            res_msg = 'Task %s has terminated!' % task_id
        except OSError as e:
            res_msg = "Error happened when tries to terminate task %s , err_msg[%s]" % (task_id,str(e))
        return res_msg
    def run_cmd(self):
        cmd = self.request.POST.get("cmd")
        host_ids = [int(i.split('host_')[-1]) for i in json.loads(self.request.POST.get("selected_hosts"))]
        task_expire_time = self.request.POST.get("expire_time")
        exec_hosts = models.BindHosts.objects.filter(id__in=host_ids)
        task_obj = self.create_task_log('cmd',exec_hosts,task_expire_time,cmd)
        p = subprocess.Popen(['python',
                              settings.MultiTaskScript,
                              '-task_type','cmd',
                              '-expire',task_expire_time,
                              '-uid',str(self.request.user.userprofile.id),
                              '-task',cmd,
                              '-task_id', str(task_obj.id)
							],preexec_fn=os.setsid)
        task_obj.task_pid = p.pid
        task_obj.save()
        return task_obj.id
    ##事务回滚
    @transaction.atomic
    def create_task_log(self,task_type,hosts,expire_time,content,note=None):
        task_log_obj = models.TaskLog(
            task_type = task_type,
            user = self.request.user.userprofile,
            cmd = content,
            expire_time = int(expire_time),
            note = note
        )
        task_log_obj.save()
        task_log_obj.hosts.add(*hosts)
        for h in hosts:
            task_log_detail_obj = models.TaskLogDetail(
                child_of_task_id = task_log_obj.id,
                bind_host_id = h.id,
                event_log = '',
                result = 'unknown'
            )
            task_log_detail_obj.save()
        return task_log_obj
    def file_get(self):
        return self.file_send()
    def file_send(self):
        params = json.loads(self.request.POST.get('params'))
        host_ids =[int(i.split('host_')[-1]) for i in params.get("selected_hosts")]
        task_expire_time = params.get("expire_time")
        exec_hosts = models.BindHosts.objects.filter(id__in=host_ids)
        task_type = self.request.POST.get('task_type')
        local_file_list = params.get('local_file_list')
        if task_type == 'file_send':
            content = "send local files %s to remote path [%s]" % (local_file_list,params.get('remote_file_path'))
        else:
            local_file_list = 'not_required'
            content = "download remote file [%s]" % params.get('remote_file_path')
        task_obj = self.create_task_log(task_type,exec_hosts,task_expire_time,content)
        if task_type == 'file_get':
            local_path = "%s%s%s%s" % (settings.BASE_DIR,settings.FileUploadDir,self.request.user.userprofile.id,task_obj.id)
            try:
                os.mkdir(local_path)
            except OSError as e:
                pass

            p = subprocess.Popen(['python',
                                  settings.MultiTaskScript,
                                  '-task_type',task_type,
                                  '-expire',task_expire_time,
                                  '-uid',str(self.request.user.userprofile.id),
                                  '-local',''.join('local_file_list'),
                                  '-remote',params.get('remote_file_path'),
                                  '-task_id',str(task_obj.id)
                                  ],preexec_fn=os.setsid)
            task_obj.task_pid = p.pid
            task_obj.save()
            return task_obj.id
    def get_task_result(self,detail=True):
        '''get multi run task result'''
        task_id = self.request.GET.get('task_id')
        log_dic = {
            'detail':{}
         }
        task_obj = models.TaskLog.objects.get(id=int(task_id))
        task_detail_obj_list = models.TaskLogDetail.objects.filter(child_of_task_id=task_obj.id)
        log_dic['summary'] = {
            'id':task_obj.id ,
            'start_time': task_obj.start_time,
            'end_time': task_obj.end_time,
            'task_type': task_obj.task_type,
            'host_num': task_obj.hosts.select_related().count(),
            'finished_num': task_detail_obj_list.filter(result='success').count(),
            'failed_num': task_detail_obj_list.filter(result='failed').count(),
            'unknown_num': task_detail_obj_list.filter(result='unknown').count(),
            'content': task_obj.cmd,
            'expire_time':task_obj.expire_time
        }
        if detail:
            for log in task_detail_obj_list:
                log_dic['detail'][log.id] = {
                    'date': log.date,
                    'bind_host_id':log.bind_host_id,
                    'host_id':log.bind_host.host.id,
                    'hostname':log.bind_host.host.hostname,
                    'ip_addr':log.bind_host.host.ip_addr,
                    'username':log.bind_host.host_user.username,
                    'system':log.bind_host.host.system_type,
                    'event_log':log.event_log,
                    'result':log.result,
                    'note':log.note
                }
            return json.dumps(log_dic,default=json_date_handler)





