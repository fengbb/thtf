#-*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin
import http.cookiejar
import os, sys, socket, re
#获取登陆token
login_tokenStr = '''bdPass.api.params.login_token='(.*?)';'''
login_tokenObj = re.compile(login_tokenStr,re.DOTALL)
class Baidu(object):
    def __init__(self,user = '', psw = ''):
        self.user = user
        self.psw  = psw
        if not user or not psw :
            print ("Plz enter enter 3 params:user,psw,blog")
            sys.exit(0)
        if not os.path.exists(self.user):
            os.mkdir(self.user)
        self.cookiename = 'baidu%s.coockie' % (self.user)
        self.token = ''
        self.allCount  = 0
        self.pageSize  = 10
        self.totalpage = 0
        self.logined = False
        self.cj = http.cookiejar.LWPCookieJar()
        try:
            self.cj.revert(self.cookiename)
            self.logined = True
            print ("OK")
        except Exception as e:
            print (e)
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent','Opera/9.23')]
        urllib.request.install_opener(self.opener)
        socket.setdefaulttimeout(30)
    #登陆百度
    def login(self):
        #如果没有获取到cookie，就模拟登陆
        if not self.logined:
            print ("logon to baidu ...")
            #第一次先访问一下，目的是为了先保存一个cookie下来
            qurl = '''https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=false'''
            r = self.opener.open(qurl)
            self.cj.save(self.cookiename)
            #第二次访问，目的是为了获取token
            qurl = '''https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=false'''
            r = self.opener.open(qurl)
            rsp = r.read()
            #print (rsp)
            self.cj.save(self.cookiename)
            #通过正则表达式获取token
            matched_objs = login_tokenObj.findall(rsp)
            if matched_objs:
                self.token = matched_objs[0]
                print ('token =', self.token)
                #然后用token模拟登陆
                post_data = urllib.urlencode({'username':self.user,
                                              'password':self.psw,
                                              'token':self.token,
                                              'charset':'UTF-8',
                                              'callback':'parent.bd__pcbs__ohm3b7',
                                              'isPhone':'false',
                                              'mem_pass':'on',
                                              'loginType':'basicLogin',
                                              'safeflg':'0',
                                              'staticpage':'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
                                              'tpl':'pp',
                                              'u':'https://passport.baidu.com/',
                                              'verifycode':'',
                                            })
                #path = 'http://passport.baidu.com/?login'
                #path = 'http://passport.baidu.com/v2/api/?login'
                path = 'https://passport.baidu.com/v2/?login'
                self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
                self.opener.addheaders = [('User-agent','Opera/9.23')]
                urllib.request.install_opener(self.opener)
                headers = {
                  "Accept": "image/gif, */*",
                  "Referer": "https://passport.baidu.com/v2/?login",
                  "Accept-Language": "zh-cn",
                  "Content-Type": "application/x-www-form-urlencoded",
                  "Accept-Encoding": "gzip, deflate",
                  "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                  "Host": "passport.baidu.com",
                  "Connection": "Keep-Alive",
                  "Cache-Control": "no-cache"
                }
                req = urllib.request.Request(path,
                                post_data,
                                headers=headers,
                                )
                rsp = self.opener.open(req).read()
                print (rsp)
                #print rsp
                self.cj.save(self.cookiename)
                #for login test
                #qurl = '''http://hi.baidu.com/pub/show/createtext'''
                #rsp = self.opener.open(qurl).read()
                #file_object = open('login.txt', 'w')
                #file_object.write(rsp)
                #file_object.close()
            else:
                print ("Login Fail")
                sys.exit(0)
def main():
    user = '18201131205'       #你的百度登录名
    psw  = '2911357'  #你的百度登陆密码,不输入用户名和密码，得不到私有的文章
    #blog = "http://hi.baidu.com/zhourunsheng" #你自己的百度博客链接
    baidu = Baidu(user,psw)
    baidu.login()
    #baidu.getTotalPage()
    #baidu.dlownloadall()
if __name__ == '__main__':
    main()
