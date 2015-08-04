#!/usr/bin/env python
import sys
import os
import re
dnsinfo=os.popen('awk -F " " \'{print $1 } \' /tmp/test/dns.conf > dnsname.txt')
dnsip=os.popen('awk -F " " \'{print $4 }\' /tmp/test/dns.conf > dnsip.txt')
#with open('/tmp/test/dnsname.txt','r') as dnsnameinfo:
#with open('/tmp/test/dnsip.txt','r') as dnsipinfo
dnsnameresult=list()
dnsipresult=list()
while True:
	with open('/tmp/test/dnsname.txt','r') as dnsnameinfo:
		dnsname=dnsnameinfo.readlines()
		for i in range(len(dnsname)):
			if dnsname[i] == '\n':
				continue
			else:
				dnsname1=dnsname[i]
				dnsnameresult.append(dnsname1)
			#print dnsname1
#	print dnsnameresult
	with open('/tmp/test/dnsip.txt','r') as dnsipinfo:
		dnsip=dnsipinfo.readlines()
		for i in range(len(dnsip)):
                	if dnsip[i] == '\n':
                        	continue
                	else:
                        	dnsip1=dnsip[i]
                        	dnsipresult.append(dnsip1)
	
#	print dnsipresult
	#for dnsip2,dnsname2 in zip(dnsipresult.readline().strip('/n'),dnsnameinfo.readline().strip('/n')):
	#	print dnsip2,dnsname2
	for i in range(len(dnsnameresult)):
		open('/tmp/test/dnsname1.txt','a').write(dnsnameresult[i])
	for i in range(len(dnsipresult)):
                open('/tmp/test/dnsip1.txt','a').write(dnsipresult[i])
	break
#	if not (dnsname1 and dnsip1):
#		break
#	open('/tmp/test/named.10.2.64.zone1','a').write(dnsip1 + dnsname1 + '\n')
	#dnsname = dnsname.strip('\n')
#	print (dnsname,dnsip)
#	dnsptr.write(dnsip + dnsname)
#	dnsptr.write(dnsname)
#	dnsptr.write("\n")
#open('/tmp/test/named.10.2.64.zone1','w').write('%s' % '\t'.join(result+result1))
