#!/usr/bin/env python
import sys
import os
import re
import shutil
import time
while True:
	with open('/tmp/test/dns-test.conf','r') as dnsconfinfo:
                        dnsconf=dnsconfinfo.readlines()
                        for i in range(len(dnsconf)):
                                if dnsconf[i] == '\n':
                                        continue
                                else:
					dnsconf[i] = dnsconf[i].strip('\n')
					if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', dnsconf[i]) !=None:
						print dnsconf[i]
                                #        dnsname1=dnsname[i]
                                #        dnsnameresult.append(dnsname1)
	break
