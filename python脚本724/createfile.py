#!/usr/bin/env python
import sys
import os
import re
import shutil
#dnsdomain = raw_input("please input a domain like 'test.com' not have 'www.':")
#with open('/tmp/test/dnsname1.txt','r') as:
#with open('/tmp/test/dnsip1.txt','r')  as:
#dnsptr = open('/tmp/test/named.10.2.64.zone1','a')
DIR='/tmp/test/PTR'
if not os.path.exists(DIR):
#	shutil.rmtree(DIR)
#	os.makedirs(DIR)
	os.makedirs(DIR)
#	continue
#else:
#	os.makedirs(DIR)	

while True:
#	with open('/tmp/test/dnsname1.txt','r') as nameinfo: 
#		name=nameinfo.readline().strip('\n')
#		if not name:
#			break
	#for name in nameinfo.readline():
	#	name=name.strip('\n')
	with open('/tmp/test/dnsip1.txt','r')  as ipinfo:
		ip=ipinfo.readlines()
		for ip1 in ip:
			ip1 = ip1.split('.')
			if len(ip1) <= 1:
				continue
			if os.path.exists('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2])):
#				with open('/tmp/test/dnsname1.txt','r') as nameinfo:
#                			name=nameinfo.readline().strip('\n')
#                			if not name:
#                        			break
#				open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a').write(ip1[3]+'\t'+'IN'+'\t'+'PTR'+'\t'+name+'.'+dnsdomain+'.'+'\n')
				continue
			else:
				open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a').write('$ORIGIN'+'\t'+ip1[2]+'.'+ip1[1]+'.'+ip1[0]+'.'+'in-addr.arpa.'+'\n')
				with open('/tmp/test/tmp/headinfo.txt') as head:
                                        for head1 in head.readlines():
                                        	if not head1:
                                                	break
						#else:
                                       		open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a').write(head1+'\n')
#			 	with open('/tmp/test/dnsname1.txt','r') as nameinfo:
#                                	for name in nameinfo.readline():
#						name=name.strip('/n')
#                                 		if not name:
#                                        		break
#                                		open('/tmp/test/PTR/named.%s.%s.%s.zone' % (ip1[0],ip1[1],ip1[2]),'a').write(ip1[3]+'\t'+'IN'+'\t'+'PTR'+'\t'+name+'.'+dnsdomain+'.'+'\n')
			continue
	#for ip in ipinfo.readline():
	#	ip=ip.strip('\n')
#	open('/tmp/test/named.10.2.64.zone1','a').write(ip+'\t'+'IN'+'\t'+'PTR'+'\t'+name+'.'+dnsdomain+'.'+'\n')
	break
#nameinfo.close()
#ipinfo.close()
