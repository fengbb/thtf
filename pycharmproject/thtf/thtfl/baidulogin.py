#-*- coding: utf-8 -*-
###登录百度
import urllib
import urllib.parse
import urllib.request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin
import http.cookiejar
import re
####login_url 定义登录网页的url
login_url = 'https://passport.baidu.com/v2/api/?login'     ###

####定义数据提交采用的方法
method = 'post'
#定义登录时传给服务器的数据，就是用户名和密码，不同网站的前面参数不同，自己在对应网站查看具体参数
'''
login_data = {
        #'用户名': 'xxxxxxx'
        'TPL_username': '18201131205',
        #'密码': 'xxxxxxxxxx',
        'TPL_password_2': 'fb2911357',
        'tpl': 'pp',
        'u': 'https://passport.baidu.com/',
        'mem_pass': 'on',
        'charset': 'UTF-8',
        'token': 'b84d8ffbfebf560f4fd03b9039802076',
        'staticpage': 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
        'isPhone': 'false',
        'callback': 'parent.bd__pcbs__xbyww4'
    }
    '''
login_data = {
            #'staticpage': 'http://tieba.baidu.com/tb/static-common/html/pass/v3Jump.html',
            #'charset':	'GBK',
            #'token': 'b84d8ffbfebf560f4fd03b9039802076',
            #'tpl': 'pp',
            #'apiver': 'v3',
            #'tt': '1441787284623',
            #'safeflg': '0',
            #'u': 'http://tieba.baidu.com/',
            #'isPhone': 'false',
            #'detect': '1',
            #'gid': '57E51E3-B9AA-4030-9B36-21306D825720',
            #'quick_user': '0',
            #'logintype': 'basicLogin',
            #'logLoginType': 'pc_loginBasic',
            #'loginmerge': 'true',
            'username': '15523520182',
            'password': '2911357',
            #'mem_pass': 'on',
            #'rsakey': '8jIlHAUYFHCabRsSCyds82SL8uXpZi36',
            #'crypttype': '12',
            #'ppui_logintime': '19594',
            #'callback': 'parent.bd__pcbs__6l0ncm'
}

header = [
        ('host', 'www.baidu.com'),  ### headers 里面可以指定host，域名
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        ('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
        #('Connection', 'keep-alive'),
        ( 'User-Agent', 'Mozilla/5.0 ( Windows NT 6.1; WOW64; X11; Ubuntu; Linux x86_64; rv:40.0 ) Gecko/20100101 Firefox/40.0'),
        #('Referer','https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F')  ####y有些网站有防盗链接，加referer，可以在网站header里面看的见
                 ]

######定义cookie数据，存放在当前目录下cookies.dat中
data = {
        'cookie_file_path': './taobao_cookies.dat'
    }
####定义一个空字典，用来存放登录的一些信息
connection_info = {}
###定义正则匹配
ref = r'src="(.+?)"'
##LWPCookieJar(filename)
#创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例。
connection_info['cookie'] = http.cookiejar.LWPCookieJar()
try:
    ###试着从文件读cookie信息
    connection_info['cookie'].revert(login_data['cookie_file_path'])
    #print (connection_info['cookie'])
    print (ok)
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
qurl = '''https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=false'''
request = urllib.request.Request(qurl, connection_info['post_data'])
#####使用全局opener打开网页
##和urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)一样
### url：可以是字符串，也可以是Request对象。
conn = opener.open(request)
print (conn.read().decode('GBK'))
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
#tb_url = 'http://tieba.baidu.com/'
#tbdata = urllib.request.urlopen(tb_url)
#print (tbdata.read().decode('GBK'))