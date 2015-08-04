#coding=utf-8 
#!/usr/bin/env python
import sys
import os
import re
import shutil
import time
#dnsdomain1 = os.popen('cat /tmp/test/dns-test.conf | grep NS |awk '{print $4}'| awk -F '.' '{print $2.$3}'') 
#dnsdomain = raw_input("please input a domain like 'test.com'not need 'www.':")
def getDomain():
    dnsdomain1=os.popen("cat /tmp/test/dns-test.conf | grep NS |awk '{print $4}'| awk -F '.' '{print $2}'").read().split()
    dnsdomain2=os.popen("cat dns-test.conf | grep NS |awk '{print $4}'| awk -F '.' '{print $3}'").read().split()
    for dnsdomain3,dnsdomain4 in zip(dnsdomain1,dnsdomain2):
        dnsdomain3 = dnsdomain3.strip('\n')
        dnsdomain4 = dnsdomain4.strip('\n')
        dnsdomain = dnsdomain3+'.'+dnsdomain4
    return dnsdomain
        
#####处理dns配置文件正向域，吧开头部分处理掉，只留正向解析部分，这样好处理正向域中的ip地址和域名头部
def createDnsTmpFile():
    dnsresult=list()
    while True:
        with open('/tmp/test/dns-test.conf','r') as dnsconfinfo:
            dnsconf=dnsconfinfo.readlines()
            for i in range(len(dnsconf)):
                if dnsconf[i] == '\n':
                    continue
                else:
                    dnsconf[i] = dnsconf[i]
                    if re.findall(r'\d+\.\d+\.\d+\.\d+', dnsconf[i]):
                        dnsconf1 = dnsconf[i]
                        dnsresult.append(dnsconf1)
            for i in range(len(dnsresult)):
                with open('/tmp/test/tmp/dnsconf.txt','a') as dnsresultinfo:
                    dnsresultinfo.write(dnsresult[i])
        break
#######处理dns正向域中的ip地址和域头部，分别写到俩个文件中，dnsname1.txt和dnsip1。dnsname和dnsip俩个文件是中间处理时生成的文件，如果在上面函数中没有处理文件中部的空格和换行的话，最后写的时候，空格后面的没有办法写进去，所有要处理文件中的空格
def createTmpFile():
    dnsinfo=os.popen('awk -F " " \'{print $1 } \' /tmp/test/tmp/dnsconf.txt > /tmp/test/tmp/dnsname.txt')
    dnsip=os.popen('awk -F " " \'{print $4 }\' /tmp/test/tmp/dnsconf.txt > /tmp/test/tmp/dnsip.txt')
    dnsnameresult=list()
    dnsipresult=list()
    time.sleep(2)
    while True:
        with open('/tmp/test/tmp/dnsname.txt','r') as dnsnameinfo:
            dnsname=dnsnameinfo.readlines()
            for i in range(len(dnsname)):
                if dnsname[i] == '\n':
                    continue
                else:
                    dnsname1=dnsname[i]
                    dnsnameresult.append(dnsname1)
        with open('/tmp/test/tmp/dnsip.txt','r') as dnsipinfo:
            dnsip=dnsipinfo.readlines()
            for i in range(len(dnsip)):
                if dnsip[i] == '\n':
                    continue
                else:
                    dnsip1=dnsip[i]
                    dnsipresult.append(dnsip1)
            for i in range(len(dnsnameresult)):
                with open('/tmp/test/tmp/dnsname1.txt','a') as writename:
                    writename.write(dnsnameresult[i])
            for i in range(len(dnsipresult)):
                with open('/tmp/test/tmp/dnsip1.txt','a') as writeip:
                    writeip.write(dnsipresult[i])
        break
####建立PTR文件夹和生成反向解析域文件，并且吧反向解析域的头部写好
def createDirFile():
    DIR='/tmp/test/PTR'
    if not os.path.exists(DIR):
    #       shutil.rmtree(DIR)
    #       os.makedirs(DIR)
        os.makedirs(DIR)
    #       continue
    else:
        shutil.rmtree(DIR)
        os.makedirs(DIR)
    while True:
        with open('/tmp/test/tmp/dnsip1.txt','r')  as ipinfo:
            ip=ipinfo.readlines()
            for ip1 in ip:
                ip1 = ip1.split('.')
                if len(ip1) <= 1:
                    continue
                if os.path.exists('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2])):
                    continue
                else:
                    with open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a') as writeptr1:
                        writeptr1.write('$ORIGIN'+'\t'+ip1[2]+'.'+ip1[1]+'.'+ip1[0]+'.'+'in-addr.arpa.'+'\n')
                    with open('/tmp/test/tmp/headinfo.txt') as head:
                        for head1 in head.readlines():
                            head1 = head1.strip('\n')
                            if not head1:
                                break
                            with open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a') as writeptr2:
                                writeptr2.write(head1+'\n')
                continue
        break
######在反向解析域文件中添加反向解析记录
def writePtr():
    dnsdomain=getDomain()
    ptrDir = '/tmp/test/PTR'
    while True:
        with  open('/tmp/test/tmp/dnsname1.txt','r') as nameinfo:
            name = nameinfo.readlines()
            #print name
            #print type(name)
        with open('/tmp/test/tmp/dnsip1.txt','r') as ipinfo:
            ip = ipinfo.readlines()
            for ip1,name1 in zip(ip,name):
                ip1 = ip1.split('.')
                if len(ip1) <= 1:
                    continue
                firstIp = ip1[0]
                secondIp = ip1[1]
                thirdIp = ip1[2]
                fourthIp = ip1[3].strip('\n')
                iplist = firstIp+'.'+secondIp+'.'+thirdIp
                files = os.listdir(ptrDir)
                name1 = name1.strip('\n')
                for ptrname in files:
                    if iplist in ptrname:
                        with open('/tmp/test/PTR/%s' % (ptrname),'a') as ptrname1:
                            ptrname1.write(fourthIp+'\t'+'IN'+'\t'+'PTR'+'\t'+name1+'.'+dnsdomain+'.'+'\n')
        break
if __name__ == '__main__':
    createDnsTmpFile()
    createTmpFile()
    createDirFile()
    writePtr()
