__author__ = 'DN'
# -*- coding: utf8 -*-
__author__ = 'Administrator'
import sys
import requests
#from bs4 import BeautifulSoup
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept':'text/html;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-cn',
           'Accept-Charset':'utf-8,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding':'gzip',
           'Connection':'close',
           }
To_Encoding='gb18030'
#网页地址GBK
#url_list='http://www.163.com'
#网页地址UTF-8
url_list='http://www.baidu.com'
#超时。你可以告诉requests在经过以 timeout 参数设定的秒数时间之后停止等待响应:
Time_Out_Secend = 3
#是否重定向
Allow_To_Redirects = 'True'
r = requests.get(url_list,headers = Headers,timeout = Time_Out_Secend,allow_redirects = Allow_To_Redirects)
print (type(r.content))
#网页编码
Html_Encodining = r.encoding
#print(r.text.dcode(Html_Encodining,'ignore').encod(To_Encoding))
print(Html_Encodining)
#print(r.content.decode(Html_Encodining,'ignore').encode(To_Encoding))
#print(r.content.decode(Html_Encodining,'ignore').encode(To_Encoding))
#print(r.text)
print (type(r.content.decode()))
print (r.content.decode(Html_Encodining,'ignore').encode('GB18030','ignore'))
#print (r.content.decode(Html_Encodining).encode(''))
#print(r.content.decode(Html_Encodining).encode())


#print(r.text)
