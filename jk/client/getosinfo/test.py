#!/usr/bin/env python
#-*- coding: utf-8
import urllib2,urllib
req_header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept':'text/html;q=0.9,*/*;q=0.8',
	'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding':'gzip',
	'Connection':'close',
	'Referer':None #עÒÈ¹û²»ÄץȡµĻ°£¬ÕÀ¿ÉÔèץȡÍվµÄost
 }
postdata = {'Data': 'Bao'}
data = urllib.urlencode(postdata)
req = urllib2.Request('http://192.168.0.208:8000/api/test',data,req_header)
response = urllib2.urlopen(req)
htmldata = response.read()
print (htmldata)
