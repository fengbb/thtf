#coding=utf-8 
#!/usr/bin/env python
import sys
import os
import re
import shutil
import time
def inputDnsconfFile():
    input = True
    while input:
        global dnsconffile
	dnsconffile= raw_input("please input where is dnsconf file like(\033[1;32;40m/var/test/dns-test.conf\033[0m)")
        if not dnsconffile.strip():
            continue
        else:
            return  dnsconffile
            input = False
def inputDnsptrFile():
    input = True
    while input:
        global dnsptrfile
	dnsptrfile= raw_input("please input where is dnsptr file like(\033[1;32;40m/var/test/headinfo.txt\033[0m)")
        if not dnsptrfile.strip():
            continue
        else:
            return  dnsptrfile
            finput = False
def inputDnstmpDir():
    input = True
    while input:
        global dnstmpdir
	dnstmpdir= raw_input("please input where is dnsconf file like(\033[1;32;40m/var/test/tmpdir\033[0m)")
	if not os.path.exists(dnstmpdir):
    #       shutil.rmtree(DIR)
    #       os.makedirs(DIR)
        os.makedirs(dnstmpdir)
    #       continue
    else:
        shutil.rmtree(dnstmpdir)
        os.makedirs(dnstmpdir)
        if not dnstmpdir.strip():
            continue
        else:
            return  dnstmpdir
            input = False
def inputDnsptrDir():
    input = True
    while input:
        global dnsptrdir
	dnsptrdir= raw_input("please input where is dnsconf file like(\033[1;32;40m/var/test/ptr\033[0m)")
        if not dnsptrdir.strip():
            continue
        else:
            return  dnsptrdir
            input = False
        
#####获取域名
def getDomain(dnsconffile):
    dnsdomain1=os.popen("cat %s  | grep NS |awk '{print $4}'| awk -F '.' '{print $2}'" % (dnsconffile)).read().split()
    dnsdomain2=os.popen("cat %s | grep NS |awk '{print $4}'| awk -F '.' '{print $3}'" % (dnsconffile)).read().split()
    for dnsdomain3,dnsdomain4 in zip(dnsdomain1,dnsdomain2):
        dnsdomain3 = dnsdomain3.strip('\n')
        dnsdomain4 = dnsdomain4.strip('\n')
        dnsdomain = dnsdomain3+'.'+dnsdomain4
    return dnsdomain
#####处理dns配置文件正向域，吧开头部分处理掉，只留正向解析部分，这样好处理正向域中的ip地址和域名头部
def createDnsTmpFile(dnsconffile,dnstmpdir):
    dnsresult=list()
    while True:
        with open('%s' % (dnsconffile),'r') as dnsconfinfo:
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
                with open('%s/dnsconf.txt' % (dnstmpdir),'a') as dnsresultinfo:
                    dnsresultinfo.write(dnsresult[i])
        break
#######处理dns正向域中的ip地址和域头部，分别写到俩个文件中，dnsname1.txt和dnsip1。dnsname和dnsip俩个文件是中间处理时生成的文件，如果在上面函数中没有处理文件中部的空格和换行的话，最后写的时候，空格后面的没有办法写进去，所有要处理文件中的空格
def createTmpFile(dnstmpdir):
    dnsinfo=os.popen('awk -F " " \'{print $1 } \' %s/dnsconf.txt > %s/dnsname.txt' % (dnstmpdir,dnstmpdir))
    dnsip=os.popen('awk -F " " \'{print $4 }\' %s/dnsconf.txt > %s/dnsip.txt' % (dnstmpdir,dnstmpdir)) 
    dnsnameresult=list()
    dnsipresult=list()
    time.sleep(2)
    while True:
        with open('%s/dnsname.txt' % (dnstmpdir),'r') as dnsnameinfo:
            dnsname=dnsnameinfo.readlines()
            for i in range(len(dnsname)):
                if dnsname[i] == '\n':
                    continue
                else:
                    dnsname1=dnsname[i]
                    dnsnameresult.append(dnsname1)
        with open('%s/dnsip.txt' % (dnstmpdir),'r') as dnsipinfo:
            dnsip=dnsipinfo.readlines()
            for i in range(len(dnsip)):
                if dnsip[i] == '\n':
                    continue
                else:
                    dnsip1=dnsip[i]
                    dnsipresult.append(dnsip1)
            for i in range(len(dnsnameresult)):
                with open('%s/dnsname1.txt' % (dnstmpdir),'a') as writename:
                    writename.write(dnsnameresult[i])
            for i in range(len(dnsipresult)):
                with open('%s/dnsip1.txt' % (dnstmpdir),'a') as writeip:
                    writeip.write(dnsipresult[i])
        break
####建立PTR文件夹和生成反向解析域文件，并且吧反向解析域的头部写好
def createDirFile(dnsptrdir,dnstmpdir):
    #DIR='/tmp/test/PTR'
    if not os.path.exists(dnsptrdir):
    #       shutil.rmtree(DIR)
    #       os.makedirs(DIR)
        os.makedirs(dnsptrdir)
    #       continue
    else:
        shutil.rmtree(dnsptrdir)
        os.makedirs(dnsptrdir)
    while True:
        with open('%s/dnsip1.txt' % (dnstmpdir),'r')  as ipinfo:
            ip=ipinfo.readlines()
            for ip1 in ip:
                ip1 = ip1.split('.')
                if len(ip1) <= 1:
                    continue
                if os.path.exists('%s/named.%s.%s.%s.zone' % (dnsptrdir,ip1[0],ip1[1],ip1[2])):
                    continue
                else:
                    with open('%s/named.%s.%s.%s.zone' % (dnsptrdir,ip1[0],ip1[1],ip1[2]),'a') as writeptr1:
                        writeptr1.write('$ORIGIN'+'\t'+ip1[2]+'.'+ip1[1]+'.'+ip1[0]+'.'+'in-addr.arpa.'+'\n')
                    with open('%s' % (dnsptrfile), 'r') as head:
                        for head1 in head.readlines():
                            head1 = head1.strip('\n')
                            if not head1:
                                break
                            with open('%s/named.%s.%s.%s.zone' % (dnsptrdir,ip1[0],ip1[1],ip1[2]),'a') as writeptr2:
                                writeptr2.write(head1+'\n')
                continue
        break
######在反向解析域文件中添加反向解析记录
def writePtr(dnsptrdir,dnstmpdir,dnsconffile):
    dnsdomain=getDomain(dnsconffile)
    #ptrDir = '/tmp/test/PTR'
    while True:
        with  open('%s/dnsname1.txt' % (dnstmpdir),'r') as nameinfo:
            name = nameinfo.readlines()
            #print name
            #print type(name)
        with open('%s/dnsip1.txt' % (dnstmpdir),'r') as ipinfo:
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
                files = os.listdir(dnsptrdir)
                name1 = name1.strip('\n')
                for ptrname in files:
                    if iplist in ptrname:
                        with open('%s/%s' % (dnsptrdir,ptrname),'a') as ptrname1:
                            ptrname1.write(fourthIp+'\t'+'IN'+'\t'+'PTR'+'\t'+name1+'.'+dnsdomain+'.'+'\n')
        break
if __name__ == '__main__':
    inputDnsconfFile()
    inputDnsptrFile()
    inputDnstmpDir()
    inputDnsptrDir()
    createDnsTmpFile(dnsconffile,dnstmpdir)
    createTmpFile(dnstmpdir)
    createDirFile(dnsptrdir,dnstmpdir)
    writePtr(dnsptrdir,dnstmpdir,dnsconffile)
