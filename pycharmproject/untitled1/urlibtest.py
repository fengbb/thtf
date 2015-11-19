# -*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
import socket
from urllib.parse import urljoin
import http.cookiejar

####3.0版本中已经将urllib2、urlparse、和robotparser并入了urllib中，并且修改urllib模块

####urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。如果想在程序中明确控制 Proxy，而不受环境变量的影响，可以使用下面的方式
'''
#enable_proxy = True
enable_proxy = False
proxy_handler = urllib.request.ProxyHandler({"http": '111.166.203.101:8118'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm','123.123.212.123','user','password')
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(urllib.request.HTTPHandler,proxy_handler)
    f = opener.open('http://www.baidu.com')
    a = f.read()
    print (a)
    #opener = urllib.request.urlopen()
else:
    opener = urllib.request.build_opener(urllib.request.HTTPHandler,null_proxy_handler)
    f = opener.open('http://www.baidu.com')
    a = f.read()
#    print(type(a))
#    for i in a:
    print(a)
#urllib.request.install_opener(opener)

'''
#1 urllib.request
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# url：可以是字符串，也可以是Request对象。
# data：发送给服务器的额外数据。现在只有http请求才会使用此参数，当提供了此参数时http请求会发送POST而不是GET,做自动登录的时候可以发送用户名和密码给服务器。
# time：可选的超时。
# ca*：https有关的参数。
# urlopen返回一个类文件对象,可以像文件一样操作,有如下方法:
#read() , readline() , readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
# info()：返回一个对象，表示远程服务器返回的头信息。
# getcode()：返回Http状态码，如果是http请求，200表示请求成功完成;404表示网址未找到。
# geturl()：返回请求的url地址。
# 1.1列子
#req = urllib.request.Request('http://news.163.com/photoview/00AP0001/96529.html#p=B1FLPGCJ00AP0001')
req = urllib.request.Request('http://pic.meizitu.com/wp-content/uploads/2015a/08/23/01.jpg')
htmldata1 = urllib.request.urlopen(req)
htmldata = urllib.request.urlopen('http://www.qq.com')
print (htmldata.info())
print (htmldata.getcode())
print (htmldata.geturl())
print ('#############')
print (htmldata1.info())
print (htmldata1.getcode())
print (htmldata1.geturl())
#i = input()
#1.2打印网页信息
#print (htmldata.read()) #urlopen 返回bytes 类型
#print (htmldata.read().decode('utf-8')) #decode解码，解码的('utf-8')要和网页编码一致（也就是网页的编码），要不打印出来会乱码
'''
#1.3 发送给服务器的额外数据
req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',
                             data=b'This data is passed to stdin of the CGI')
with urllib.request.urlopen(req) as f:
    #print(f.read().decode('utf-8'))
##使用的cgi脚本如下
#!/usr/bin/env python
#import sys
#data = sys.stdin.read()
#print('Content-type: text-plain\n\nGot Data: "%s"' % data)

##put 发送
DATA=b'some data'
req = urllib.request.Request(url='http://localhost:80', data=DATA,method='PUT')
with urllib.request.urlopen(req) as f:
    pass
print(f.status)
print(f.reason)

###install_opener和build_opener这两个方法通常都是在一起用,也有时候build_opener单独使用来得到OpenerDirector对象。　　
#　　install_opener实例化会得到OpenerDirector 对象用来赋予全局变量opener。如果想用这个opener来调用urlopen，那么就必须实例化得到OpenerDirector；这样就可以简单的调用OpenerDirector.open()来代替urlopen()。
#　　build_opener实例化也会得到OpenerDirector对象，其中参数handlers可以被BaseHandler或他的子类实例化。
#2 request
##request对外提供的接口是urlopen方法，该方法可以接受一个纯粹的字符串形式的url(注释部分，也可以接受一个Request对象(注意是大写)。当你传递的是字符串的时候，request中会有相关底层方法把你的字符串封装为一个Request对象。
#最后把request方法传递给opener中的open方法，open方法中会采用你声明的handler或者默认handler进行具体的URL请求处理。
req = urllib.request.Request("http://www.baidu.com")
data = urllib.request.urlopen(req)
for d in data.readlines():
    print(str(d,encoding = "utf-8"))
    '''
#3 发送header 如果网站有防盗连接，要自己构造header，要不会报错
# [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'),  
#                                    ('Connection', 'keep-alive'),  
#                                    ('Cache-Control', 'no-cache'),  
#                                    ('Accept-Language:', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),  
#                                    ('Accept-Encoding', 'gzip, deflate'),  
#                                    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]  
   
'''
url = 'http://www.baidu.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
req = urllib.request.Request(url,headers=headers)
htmldata = urllib.request.urlopen(req)
print (htmldata.read().decode("utf-8"))
'''
#4 http错误
'''
req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print (e.code)
    #print (e.read().decode('utf-8'))
'''
#5 异常处理
'''
req = Request('http://www.gogle.com/')
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print("good!")
    print(response.read().decode("utf-8"))
'''
#6 异常处理2
'''
req = Request("http://www.baidu.com")
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print("The server couldn\'t fulfill the request.")
        print('Error code: ', e.code)
    else:
        print("good!")
        print(response.read().decode("utf-8"))
'''
#7 HTTP 认证
##当需要Authentication的时候，服务器发送一个头（同时还有401代码）请求Authentication。它详细指明了一个Authentication和一个域。这个头看起来像：
#客户端然后就会用包含在头中的正确的帐户和密码重新请求这个域。这是“基本验证”。为了简化这个过程，我们可以创建一个
#HTTPBasicAuthHandler和opener的实例来使用这个handler。

#HTTPBasicAuthHandler用一个叫做密码管理的对象来处理url和用户名和密码的域的映射。如果你知道域是什么（从服务器发送的authentication 头中），那你就可以使用一个HTTPPasswordMgr。多

#数情况下人们不在乎域是什么。那样使用HTTPPasswordMgrWithDefaultRealm就很方便。它允许你为一个url具体指定用户名和密码。这将会在你没有为一个特殊的域提供一个可供选择的密码锁时提供给你。

#我们通过提供None作为add_password方法域的参数指出 这一点。

#最高级别的url是需要authentication的第一个url。比你传递给.add_password()的url更深的url同样也会匹配。
'''
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://www.163.com/"
password_mgr.add_password(None, top_level_url, '15353531182@163.com', '2911357')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
a_url = "http://www.163.com/"
x = opener.open(a_url)
print(x.read(100))
print(x.info())

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

a = urllib.request.urlopen(a_url).read(120000).decode('gb2312')
print(a)
print(urllib.request.urlopen(a_url).info())
'''
'''
#8 使用代理
proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
a = urllib.request.urlopen("http://g.cn").read().decode("utf8")
print(a)
'''
'''
#9 超时
timeout = 2
socket.setdefaulttimeout(timeout)

# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.baidu.com/')
a = urllib.request.urlopen(req).read()
print(a)
'''
'''
#10 urlparse
#通过Python所带的urlparse模块，我们能够轻松地把URL分解成元件(scheme(协议), netloc(网址), path(路径), parameters(参数), query, fragment)
#之后，还能将这些元件重新组装成一个URL。当我们处理HTML 文档的时候，这项功能是非常方便的
#函数urlparse(urlstring [, default_scheme [, allow_fragments]])的作用是将URL分解成不同的组成部分，它从urlstring中取得URL，并返回元组 (scheme, netloc, path, parameters, query, fragment)。
#注意，返回的这个元组非常有用，例如可以用来确定网络协议(HTTP、FTP等等 )、服务器地址、文件路径，等等。
#函数urlunparse(tuple)的作用是将URL的组件装配成一个URL，它接收元组(scheme, netloc, path, parameters, query, fragment)后，
#会重新组成一个具有正确格式的URL，以便供Python的其他HTML解析模块使用。
#函数urljoin(base, url [, allow_fragments]) 的作用是拼接URL，它以第一个参数作为其基地址，然后与第二个参数中的相对地址相结合组成一个绝对URL地址。
#函数urljoin在通过为URL基地址 附加新的文件名的方式来处理同一位置处的若干文件的时候格外有用。需要注意的是，如果基地址并非以字符/结尾的话，那么URL基地址最右边部分就会被这个 相对路径所替换。
#比如，URL的基地址为Http://www.testpage.com/pub，URL的相对地址为test.html，那么两者将合 并成http://www.testpage.com/test.html，而非http://www.testpage.com/pub /test.html。
#如果希望在该路径中保留末端目录，应确保URL基地址以字符/结尾。
#
o = urllib.request.urlparse('http://www.meizitu.com/a/4748.html')
print (o)
##函数使用例子
URLscheme = "http"
URLlocation = "www.python.org"
URLpath = "lib/module-urlparse.html"
modList = ("urllib", "urllib2", \
"httplib", "cgilib")
#将地址解析成组件
print ("用Google搜索python时地址栏中URL的解析结果")
parsedTuple = urllib.request.urlparse("http://www.google.com/search?hl=en&q=python&btnG=Google+Search")
print (parsedTuple)
#将组件反解析成URL
print ("反解析python文档页面的URL")
unparsedURL = urllib.request.urlunparse( \
    (URLscheme, URLlocation, URLpath, '', '', ''))
print ("\t" + unparsedURL)
#将路径和新文件组成一个新的URL
print ("\n利用拼接方式添加更多python文档页面的URL")
for mod in modList:
    newURL = urllib.request.urljoin(unparsedURL, "module-%s.html" % (mod))
    print ("\t" + newURL)
#通过为路径添加一个子路径来组成一个新的URL
print ("\n通过拼接子路径来生成Python文档页面的URL")
newURL = urllib.request.urljoin(unparsedURL,"module-urllib2/request-objects.html")
print ("\t" + newURL)
'''

# 11 cookes
#参考链接http://cuiqingcai.com/968.html
#Cookie用于服务器实现会话，用户登录及相关功能时进行状态管理
#Set-Cookie：session=8345234;expires=Sun，15-Nov-2013 15:00:00 GMT；path=/；domain=baidu.com
#expires是cookie的生存周期，path是cookie的有效路径，domain是cookie的有效域.
#路径"path"用于设置可以读取一个cookie的最顶层的目录．
#将cookie的路径设置为你的网页最顶层的目录可以让该该目录下的所有网页都能访问该cookie．
#方法：在你的cookie中加入path=/; 如果你只想让"food" 目录中的网页可以使用该cookie，则你加入path=/food;.
#domain：有些网站有许多小的域名，例如百度可能还在"news.baidu.com" "zhidao.baidu.com" 和"v.baidu.com" 域名下有网页．
#如果想让"baidu.com"下的所有机器都可以读取该cookie，必须在cookie中加入 "domain=.baidu.com" ．
#用户浏览器会存储Cookie直到过期，浏览器会向符合path和domain的服务器发送类似以下内容的HTTP请求报头：
#这个模块主要提供了这几个对象，CookieJar，FileCookieJar，MozillaCookieJar,LWPCookieJar
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
httpcookie = opener.open('http://www.baidu.com')
print ('##')
print (httpcookie)
##Cookie实例的集合，Cookie实例有name,value,path,expires等属性：
for ck in cookie:
    print (ck.name,':',ck.value)
##也可以将cookie捕捉到文件中
#FileCookieJar(filename)
#创建FileCookieJar实例，检索cookie信息并将信息存储到文件中，filename是文件名
#创建与Mozilla cookies.txt文件兼容的FileCookieJar实例。
#LWPCookieJar(filename)
#创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例。
##不指定路径的话保存到当前脚本目录下
filename = 'baiducookiejar.txt'
url = 'http://www.baidu.com'
FileCookieJar = http.cookiejar.MozillaCookieJar(filename)
FileCookieJar.save()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(FileCookieJar))
opener.open(url)
FileCookieJar.save(ignore_discard=True, ignore_expires=True)
##由此可见，ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
#ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入，
#在这里，我们将这两个全部设置为True。
print (open(filename).read())
readfilename = "baiducookiejar.txt"
MozillaCookieJarFile = http.cookiejar.MozillaCookieJar(readfilename)
print (MozillaCookieJarFile)
MozillaCookieJarFile.load('baiducookiejar.txt',ignore_discard=True, ignore_expires=True)
print (MozillaCookieJarFile)











