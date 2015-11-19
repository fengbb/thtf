# -*- coding: utf-8 -*-
import urllib
import urllib.request
#import 
#with urllib.request.urlopen('http://www.baidu.com/'+ str(num)) as f:
f = urllib.request.urlopen('http://www.baidu.com/'+ str())
a = f.readline()
print (a)
f.close()
#for i in f.readline().decode('utf-8'):
#print (i)
#    #print(f.read().decode('utf-8'))
#with urllib.request.urlopen('http://www.baidu.com/') as f:
#req = urllib.request("http://www.baidu.com/")
#res = urllib.request.urlopen("http://www.baidu.com/")
#html = res.read()
#res.close()
#html = unicode(html, "gb2312").encode("utf8")
#print (html)
