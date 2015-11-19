# -*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
import socket
from urllib.parse import urljoin
import http.cookiejar
username='122727569@qq.com'
password='2911357'
url = 'https://passport.baidu.com/v2/?login&fr=old'
##enable cooklie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
values = {'username':username, 'password':password}
data = urllib.parse.urlencode(values).encode('utf-8')
#req = urllib.request.Request(url,data=b'hello world')
#req = urllib.request.Request(url,data)
opener = urllib.request.build_opener(handler)
req = opener.open(url,data)
page = req.read()
print (page)
#htmldata = page.read()#.decode('utf-8')
#print (htmldata)
print (cookie)
for ck in cookie:
    print (ck.name,':',ck.value)
#if not 'PHPSESSID' in [ck.name for ck in cookie]:
#    print ("Login failed with login=%s, passwd=%s" % (username,password))
#else:
#    print ("We are logged in !")
'''
req = urllib.request.Request('http://www.itoppay.com')
try:
    htmldata = urllib.request.urlopen(req)
    print (htmldata.read().decode('gbk'))
    
except urllib.error.HTTPError as e:
    print (e.code)
    print (e.read())
    
'''
