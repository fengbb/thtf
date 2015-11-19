#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from jkl.models import Host,HostGroup,TestPost

# Create your views here.
try:
    import json
except ImportError as e:
    import simplejson as json
#@csrf_exempt
def collect(request):
    req = request
    if req.POST:
        vendor = req.POST.get('Product_Name') #6
        #sn = req.POST.get('Serial_Number')
        product = req.POST.get('Manufacturer') #14
        cpu_model = req.POST.get('Model_Name') #13
        cpu_num = req.POST.get('Cpu_Cores') #5
        cpu_vendor = req.POST.get('Vendor_Id') #2
        memory_part_number = req.POST.get('Part_Number')#8
        #memory_manufacturer = req.POST.get('Manufacturer')
        memory_size = req.POST.get('size') #12
        #device_mode = req.POST.get('Device_Model')
        #device_version = req.POST.get('Firmware_Version')
        #device_sn = req.POST.get('Serial_Number')#11
        device_size = req.POST.get('User_Capacity') #4
        osver = req.POST.get('os_version') #7
        hostname = req.POST.get('os_name') #1
        os_release = req.POST.get('os_release') #9
        ipaddres = req.POST.get('Ipaddr') #3
        #print (ipaddres)
        mac = req.POST.get('Mac')
        #link = req.POST.get('Link')
        #mask = req.POST.get('Mask')
        #device = req.POST.get('Device') #10
        #sn=sn,device_sn=device_sn,
        ##将数据保存到数据库
        host = Host.objects.create(hostname=hostname,product=product,cpu_num=cpu_num,
                            cpu_model=cpu_model,cpu_vendor=cpu_vendor,memory_part_number=memory_part_number,
                           memory_size=memory_size,device_size=device_size,
                            osver=osver,os_release=os_release,vendor=vendor,ipaddr=ipaddres)
        return HttpResponse('ok') #如果插入成功，返回'ok'
    else:
        return HttpResponse('no post data')
###测试传送数据到数据库
def postdata(request):
        req = request
        if req.POST:
            test = TestPost.objects.create(post_name=req.POST.get('Data'))
            return HttpResponse('ok')

def gethosts(request):
    d = []
    hostgroups = HostGroup.objects.all()
    for hg in hostgroups:
        print (hg.name)
        ret_hg = {'hostgroup':hg.name,'members':[]}
        members = hg.members.all()
        print ('#####')
        print (members)
        print ('@@@@@@')
        for h in members:
            ret_h = {'hostname': h.hostname, 'ipaddr': h.ipaddr}
            ret_hg['members'].append(ret_h)
        d.append(ret_hg)
    ret = {'status':0, 'data':d, 'message':'ok'}
    return HttpResponse(json.dumps(ret))



