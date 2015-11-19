#-*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import re
def login_cnblogs(url,name,pwd):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent,'Referer':'http://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fwww.cnblogs.com%2F',
             'Host':'passport.cnblogs.com',
             }
    params = {'input1':'用户名',
              'input2':'密码',
              "__EVENTVALIDATION":"T4jJDhgvFjFBQNgiVYyDK3EgsFlKJOoFlVl+rT8Bl9/kyxPzken5iSNmJ3bqm/IVGl08V2SKOduZ253w9ye422joQs9BNH0avopAw+PXNB7vIiTGcbY+T13szW4tJNSHC5AQ2FLKeBM5ACQY9U+vFDvGabmIUCU+8JQOGATrSWA=",
              "__VIEWSTATE":"Tlt+sjRg6zyHvlxKsLS0HWueoH5dzbb/dtqBc5DeoXgdeq7yxCGIVRG0U5tirvJrMizK/pyeKAAApMgobbT8NLdzQV75jYf4TC1pZ0P5lFTt9nVmaL4i7Ber05k+xDs8A1WmPPmxRNpgNUy4UNlZCLXv+0h/8WcatTyVLiE9XRo=",
              "btnLogin":"登  录",
              "txtReturnUrl":"http://home.cnblogs.com/"
        }
    ##设置cookie
    params = urllib.parse.urlencode(params).encode()
    url_hi = "http://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fwww.cnblogs.com%2F"
    cookie = http.cookiejar.CookieJar()   ###声明一个CookieJar对象实例来保存cookie
    cj = urllib.request.HTTPCookieProcessor(cookie)   ###利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
    ##设置登录参数
    #postdata =urllib.parse.urlencode().encode()
    ##生产请求
    request = urllib.request.Request('http://passport.cnblogs.com/login.aspx',params)
    ###登录 使用cookie登录
    opener = urllib.request.build_opener(cj)
    f = opener.open(request)
    if(200==f.getcode()):
        print ("登录成功")
    else:
        print ("登录失败")
    hi_html = opener.open(url)
    #print (hi_html.read().decode('utf-8','ignore'))
    return hi_html
if __name__=='__main__':
    name = 'oxiaobao'
    pwd = 'fb*@#2911357'
    url = 'http://www.cnblogs.com/'
    h = login_cnblogs(url,name,pwd)
    print (h.read().decode('gbk','ignore').encode('utf-8').decode('utf-8'))
