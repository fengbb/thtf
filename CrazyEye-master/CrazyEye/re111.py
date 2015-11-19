#_*_coding:utf-8_*_
__author__ = 'DN'
import re

str = u

p = re.compile('<h2 .*>(.*)</h2>')
match = p.findall(str)
for item in match:
    print (match)
#print(p.match(str).groups())
