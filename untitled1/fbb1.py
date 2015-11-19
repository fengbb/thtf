#encoding:UTF-8  
import urllib.request
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#              'Accept':'text/html;q=0.9,*/*;q=0.8',
#              'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#              'Accept-Encoding':'gzip',
#              'Connection':'close',
#              'Referer':None,
#              }
def getdata():  
    url="http://www.meizitu.com/"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url,headers=headers)
    
    #data=urllib.request.urlopen(req).read().decode('gbk').encode(encoding='utf-8').decode('utf-8')
    data=urllib.request.urlopen(req).read().decode('gb18030').encode(encoding='gbk').decode('gbk')
    #data1 = data.de
    #print (data.encoding)
    print (data)
    #for i in data.split('\n'):
        #print (i)
        #print ('###########')
    #print(data)  
  
getdata()
