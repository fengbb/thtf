#-*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin
import http.cookiejar
import re

####http://www.cnblogs.com/skyme/p/3436545.html
class Login:
    _login_url = 'http://home.51cto.com/index.php?s=/Index/doLogin'
    _method = 'post'
    #2458478557
    _login_data = {
        'email':'122727569@qq.com',
        #'email':'2458478557@qq.com',
        'passwd':'fb2911357',
    }
    _headers = [
        ('host','home.51cto.com'),
        ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'),
        ('Referer','http://home.51cto.com/index.php?s=/Index/index/reback/http%253A%252F%252Fwww.51cto.com%252F/')
    ]
    _data = {
        'cookie_file_path': './51cto_cookies.dat'
    }
    _re = r'src="(.+?)"'
    _version = '0.1'
    _connection_info = {}
    def __init__(self):
        ##LWPCookieJar(filename)
        #创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例。
        self._connection_info['cookie'] = http.cookiejar.LWPCookieJar()
        try:
            self._connection_info['cookie'].revert(self._login_data['cookie_file_path'])
        except Exception as e:
            pass
            #print (e)
        self._connection_info['cookie_processor'] = urllib.request.HTTPCookieProcessor(self._connection_info['cookie'])
        self._connection_info['post_data'] = urllib.parse.urlencode(self._login_data).encode()
    def open(self):
        opener = urllib.request.build_opener(self._connection_info['cookie_processor'])
        opener.addheaders = self._headers
        urllib.request.install_opener(opener)
        request = urllib.request.Request(self._login_url,self._connection_info['post_data'])
        conn = opener.open(request)
        #print (conn.read().decode())
        if (conn.geturl() == self._login_url):
            self._connection_info['cookie'].save(self._data['cookie_file_path'])
        else:
            pass
        #print ()
        partner = re.compile(self._re)
        match = partner.findall(conn.read().decode())
        for item in match:
            try:
                opener.open(item)
            except urllib.error.HTTPError as e:
                pass
                #print (e.code)
            print (item)
        ####下载豆领取
        url = 'http://down.51cto.com/download.php'
        #url = 'http://down.51cto.com/credits'
        #data = {'do':'getfreecredits','t':random.random()}
        data = {'do':'getfreecredits','t':''}
        login51cto = opener.open(url, urllib.parse.urlencode(data).encode())
        html = opener.open(url, urllib.parse.urlencode(data).encode())
        #print (html.read())
        #print (login51cto.getcode())
        ######无忧币领取
        url = 'http://home.51cto.com/index.php?s=/Home/toSign'
        data = {'s':''}
        loginwuyou = opener.open(url, urllib.parse.urlencode(data).encode())
        #print (loginwuyou.getcode())
if __name__ == '__main__':
    login_51cto = Login()
    login_51cto.open()

