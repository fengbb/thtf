#-*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
import socket
from urllib.parse import urljoin
import http.cookiejar
import re
import chardet
url = 'http://www.meizitu.com'
def geturl(url):
    #reg = r'<a href=".*" .* title=".*">.*</a>' target=".*"
    #reg = r'<a href=".*" title=".*"'
    reg = r'<a href=".*"  target="_blank" title=".*"  >.*</a>'
    urlt = re.compile(reg)
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    pagedata = page.read()#.decode('gbk')
    fencoding=chardet.detect(pagedata)
    if fencoding['encoding'] == 'utf-8':
        pagedata1 = pagedata.decode('utf-8')
    elif  fencoding['encoding'] == 'gb2312':
        pagedata1 = pagedata.decode('gb2312')
    #print (pagedata)
    urllists = re.findall(urlt,pagedata)
    for urllist in urllists:
        print (urllist)
        #urllistvalue =
        print (urllist.split(' '))
       # print (type(urllist))

if __name__ == '__main__':
    geturl(url)


