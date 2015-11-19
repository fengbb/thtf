#encoding:UTF-8  
import urllib.request
url = "http://www.itoppay.com/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
req = urllib.request.Request(url,headers=headers)
f = urllib.request.urlopen(req)
print (f.info())
contype = f.headers['Content-Type']
print (contype)
pos = contype.find('=')
if -1 != pos:
   contype = contype[pos+1:len(contype)]
print (contype)
#my = MyHTMLParser()
#data = f.read().decode(contype,'ignore')
#<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
#<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
