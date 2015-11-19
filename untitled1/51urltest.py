# -*- coding: utf-8 -*-
import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
def ungzip(data):
    try:
        print ('正在解压...')
        data = gzip.decompress(data)
        print ('解压完成！')
    except:
        print ('没有压缩，无需解压')
    return data
def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
def getOpener(head):
    cj = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(handler)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'static.zhihu.com',
    'DNT': '1'
}
url = 'https://login.taobao.com/member/login.jhtml'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)
#print (data.decode('gbk'))
#_xsrf = getXSRF(data.decode())
#url += 'login/email'
id = '18201131205'
password = 'fb2911357'
postDict = {
   # '_xsrf': _xsrf,
    'TPL_username': id,
    'TPL_password': password,
    #'rememberme': 'y'
    }
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)
print (data.decode('gbk'))
    
