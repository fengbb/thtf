#!/usr/bin/env python
import sys
import os
dnsinfo=os.popen('cat /tmp/test/dns-test.conf').read()
dnsinfo1=dnsinfo.split('\n')
print dnsinfo1
for dnsinfo2 in dnsinfo1:
	dnsinfo2=dnsinfo1.split('\t')
	if len(rootused2) <= 1:     #chu li zi fu chuang chang du bu yi yang qing kuang
                continue
	print dnsinfo2
