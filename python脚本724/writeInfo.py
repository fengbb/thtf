#!/usr/bin/env python
import sys
import os
import re
ptrDir = '/tmp/test/PTR'
dnsdomain = raw_input("please input a domain like 'test.com' not have 'www.':")
#nameinfo = open('/tmp/test/dnsname1.txt','r') 
while True:
	with  open('/tmp/test/dnsname1.txt','r') as nameinfo:
		name = nameinfo.readlines()
		#print name
		#print type(name)
	with open('/tmp/test/dnsip1.txt','r') as ipinfo:
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
		#	print name1
		#	print type(name1)
			for ptrname in files:
				if iplist in ptrname:
					with open('/tmp/test/PTR/%s' % (ptrname),'a') as ptrname1:
						ptrname1.write(fourthIp+'\t'+'IN'+'\t'+'PTR'+'\t'+name1+'.'+dnsdomain+'.'+'\n')
				#print ptrname
	break
