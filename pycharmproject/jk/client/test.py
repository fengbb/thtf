#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
import urllib

values = {
	'Vendor_Id': 'GenuineIntel',
	'Model_Name':  'Intel(R) Xeon(R) CPU           X5650  @ 2.67GHz',
	'Cpu_Cores': '4',
	'User_Capacity':  '107,374,182,400 bytes',
	'Part_Number': 'Not Specified',
	'Manufacturer': 'Not Specified',
	'Size': '4 MB',
	'Serial_Number': 'VMware-42 02 d4 07 f6 7c 03 5c-76 20 10 09 a2 e7 60 b0',
	'Product_Name':  'VMware Virtual Platform',
	'manufacturer':  'VMware, Inc.',
	'os_version': 'centos 6.6',
	'os_name': 'localhost.localdomain',
	'os_release': '2.6.32-504.30.3.el6.x86_64',
	'Device': 'eth0',
	'Link': 'Local',
	'Mac':  '00:50:56:82:48:AD',
	'Ipaddr': '127.0.0.1',
	'Mask': '255.0.0.0'
}
data = urllib.urlencode(values)
req = urllib2.Request('http://www.testpost.com:8000/api/test',data)
response = urllib2.urlopen(req)
html = response.read()
print (html)
