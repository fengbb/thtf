#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib,urllib2
from getcpuinfo  import *
from getdiskinfo  import *
from getdmiinfo  import *
from gethostinfo  import *
from  getipinfo  import *
from getmemoryinfo  import *
def getHostTotal():
	ld = []
	cpuinfo = parserCpuInfo(getCpuInfo())
	diskinfo = parserDiskInfo(getDiskInfo())
	for i in parserMemInfo(getMemInfo()):
		meminfo = i
	productinfo = parserDMI(getDMI())
	hostinfo = getHostInfo()
	ipaddr = parserIpaddr(getIpaddr())
	for i in ipaddr:
		print ('###')
		print (i)
		print ('@@@@')
		ip = i
	for k in cpuinfo.iteritems():
		ld.append(k)
	for i in diskinfo.iteritems():
		ld.append(i)
	for j in meminfo.iteritems():
		ld.append(j)
	for v in productinfo.iteritems():
		ld.append(v)
	for x in hostinfo.iteritems():
		ld.append(x)
	for y in ip.iteritems():
		ld.append(y)
	return ld
def parserHostTotal(hostdata):
	pg = {}
	for i in hostdata:
		print i
		pg[i[0]] = i[1]
	return pg
def urlPost(postdata):
	data = urllib.urlencode(postdata)
	try:
		req = urllib2.Request('http://192.168.0.208:8000/api/collect',data)
		response = urllib2.urlopen(req)
		print (response.read())
	except urllib2.HTTPError, e:
		if e.getcode() == 500:
			print (e.read())
		else:
			return response.read()
if __name__ == '__main__':
	hostdata = getHostTotal()
	postdata = parserHostTotal(hostdata)
	#print (postdata)
	print (urlPost(postdata))
