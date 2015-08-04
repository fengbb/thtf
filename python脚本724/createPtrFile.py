#!/usr/bin/env python
import sys
import os
import re
import shutil
import time
dnsdomain = raw_input("please input a domain like 'test.com'not need 'www.':")
def createTmpFile():
	dnsinfo=os.popen('awk -F " " \'{print $1 } \' /tmp/test/dns.conf > /tmp/test/tmp/dnsname.txt')
	dnsip=os.popen('awk -F " " \'{print $4 }\' /tmp/test/dns.conf > /tmp/test/tmp/dnsip.txt')
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
                                                	if not head1:
                                                        	break
						 	with open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a') as writeptr2:
								writeptr2.write(head1+'\n')
					continue
		break
def writePtr(dnsdomain):
	ptrDir = '/tmp/test/PTR'
	#dnsdomain = raw_input("please input a domain like 'test.com' not have 'www.':")
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
	createTmpFile()
	createDirFile()
	writePtr(dnsdomain)
