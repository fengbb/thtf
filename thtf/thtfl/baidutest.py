#-*- coding: utf-8 -*-
###登录百度
import urllib
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
from urllib.parse import urljoin
import http.cookiejar
import socket
import ssl
import re
####login_url 定义登录网页的url
login_url = 'https://passport.baidu.com/v2/?login'     ###

####定义数据提交采用的方法
method = 'post'
#定义登录时传给服务器的数据，就是用户名和密码，不同网站的前面参数不同，自己在对应网站查看具体参数
login_data = {
        #'用户名': 'xxxxxxx'
        'username': '15523520182',
        #'密码': 'xxxxxxxxxx',
        'password': '2911357',
        'tpl': 'pp',
        'u': 'https://passport.baidu.com/',
        'mem_pass': 'on',
        'charset': 'UTF-8',
        'token': 'b84d8ffbfebf560f4fd03b9039802076',
        'staticpage': 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
        'isPhone': 'false',
        'callback': 'parent.bd__pcbs__xbyww4'
    }

header = [
        ('host', 'passport.baidu.com'),  ### headers 里面可以指定host，域名
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        ('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
        ('Connection', 'keep-alive'),
        ( 'User-Agent', 'Mozilla/5.0 ( Windows NT 6.1; WOW64; X11; Ubuntu; Linux x86_64; rv:40.0 ) Gecko/20100101 Firefox/40.0'),
        ('Referer','https://passport.baidu.com/v2/?login')  ####y有些网站有防盗链接，加referer，可以在网站header里面看的见
                 ]

######定义cookie数据，存放在当前目录下cookies.dat中
data = {
        'cookie_file_path': './baidu_cookies.dat'
    }
####定义一个空字典，用来存放登录的一些信息
connection_info = {}
###定义正则匹配
ref = r'src="(.+?)"'
##LWPCookieJar(filename)
#创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例。
sockbaidu = ssl.wrap_socket(socket.socket())
sockbaidu.connect(('passport.baidu.com', 443))
data = '''\
POST /?login HTTP/1.1
Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*
Referer: https://passport.baidu.com/?login&tpl=mn
Accept-Language: zh-CN
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Alexa Toolbar; BOIE9;ZHCN)
Content-Type: application/x-www-form-urlencoded
Host: passport.baidu.com
Content-Length: 243
Connection: Keep-Alive
Cache-Control: no-cache
tpl_ok=&next_target=&tpl=mn&skip_ok=&aid=&need_pay=&need_coin=&pay_method=&u=http%3A%2F%2Fwww.baidu.com%2F&return_method=get&more_param=&return_type=&psp_tt=0&password=itianda&safeflg=0&isphone=tpl&username=itiandatest1&verifycode=&mem_pass=on\
'''
sockbaidu.sendall(data.encode())
recv_data = sockbaidu.recv(8192)
sockbaidu.close()
print (recv_data)
'''
connection_info['cookie'] = http.cookiejar.LWPCookieJar()
try:
    ###试着从文件读cookie信息
    connection_info['cookie'].revert(login_data['cookie_file_path'])
    #print (connection_info['cookie'])
except Exception as e:
    pass
    print (e)
print (connection_info['cookie'])
###利用urllib库的HTTPCookieProcessor对象创建cookie处理器
connection_info['cookie_processor'] = urllib.request.HTTPCookieProcessor(connection_info['cookie'])
###构建postdata
connection_info['post_data'] = urllib.parse.urlencode(login_data).encode()
#############################          opener的概念            #########################################################################
####当你获取一个URL你使用一个opener(一个urllib2.OpenerDirector的实例)。在前面，我们都是使用的默认的opener，也就是urlopen。
#####它是一个特殊的opener，可以理解成opener的一个特殊实例，传入的参数仅仅是url，data，timeout。
##### 如果我们需要用到Cookie，只用这个opener是不能达到目的的，所以我们需要创建更一般的opener来实现对Cookie的设置。
#通过cookie处理器来实例化opener
opener = urllib.request.build_opener(connection_info['cookie_processor'])
#####给opener添加heasers
opener.addheaders = header
####install_opener 用来创建（全局）默认opener。这个表示调用urlopen将使用你安装的opener
urllib.request.install_opener(opener)
####构建request对象
request = urllib.request.Request(login_url, connection_info['post_data'])
#####使用全局opener打开网页
##和urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)一样
### url：可以是字符串，也可以是Request对象。
conn = opener.open(request)
print (conn.read())
print (conn.geturl())
if (conn.geturl() == login_url) :
    connection_info['cookie'].save(data['cookie_file_path'])
else:
    pass
partner = re.compile(ref)
match = partner.findall(conn.read().decode())
for item in match:
        try:
            opener.open(item)
        except urllib.error.HTTPError as e:
            pass
            print (e.code)
        print (item)
tb_url = 'http://tieba.baidu.com/'
tbdata = urllib.request.urlopen(tb_url)
print (tbdata.read().decode('GBK'))
'''
