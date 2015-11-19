__author__ = 'DN'
#encoding:UTF-8
import urllib.request

def getdata():
    url="http://www.meizitu.com/"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url,headers=headers)

    #data=urllib.request.urlopen(req).read().decode('gbk').encode(encoding='utf-8').decode('utf-8')
    print (type(urllib.request.urlopen(req).read()))
    #data=urllib.request.urlopen(req).read().decode('gb18030').encode(encoding='utf-8').decode('utf-8')
    #print (data.encoding)
    #print (data)
    '''
    for i in data.split('\n'):
        print (i)
    #print(data)'''

getdata()

