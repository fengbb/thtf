#!/usr/bin/env python
import sys
import os
import re
dnsinfo=os.popen('awk -F " " \'{print $1 } \' /tmp/test/dns.conf > dnsname.txt')
dnsip=os.popen('awk -F " " \'{print $4 }\' /tmp/test/dns.conf | awk -F "." \'{print $4 }\' > dnsip.txt')
#os.popen('sleep\(5\)')
dnsnameinfo = open('/tmp/test/dnsname.txt','r')
dnsipinfo = open('/tmp/test/dnsip.txt','r')
#dnsptr = open('/tmp/test/named.10.2.64.zone1','a')
#result = list()
#result1 = list()
#for dnsname in open('/tmp/test/dnsname.txt'):
#	dnsname = dnsnameinfo.readline()
#	print dnsname
#	result.append(dnsname)
for dnsip,dnsname in zip(dnsipinfo.readlines(),dnsnameinfo.readlines()):
	for dnsip1 in dnsip.splitlines():
		#print dnsip1
		dnsip1=dnsip1.rstrip()+'\n'
		#print dnsip1
		#print type(dnsip1)
	for dnsname1 in dnsname.splitlines():
                #print dnsip1
                dnsname1=dnsname1.rstrip()+'\n'
                #print dnsip1
                #print type(dnsip1)
	open('/tmp/test/named.10.2.64.zone1','a').write(dnsip1 + dnsname1 + '\n')
#	print dnsip,dnsname
#while True:
#	dnsname=dnsnameinfo.readlines()
#	dnsname1=dnsname.replace(" ","").replace("\t","").strip()
#	print dnsname1
#	dnsip=dnsipinfo.readlines() #.strip(' ').lstrip('\n')
#	dnsip1=dnsip.replace(" ","").replace("\t","").strip()
#	print dnsip1
#	if not (dnsname1 and dnsip1):
#		break
#	open('/tmp/test/named.10.2.64.zone1','a').write(dnsip1 + dnsname1 + '\n')
	#dnsname = dnsname.strip('\n')
#	print (dnsname,dnsip)
#	dnsptr.write(dnsip + dnsname)
#	dnsptr.write(dnsname)
#	dnsptr.write("\n")
dnsnameinfo.close()
dnsipinfo.close()
#open('/tmp/test/named.10.2.64.zone1','w').write('%s' % '\t'.join(result+result1))
