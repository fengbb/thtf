__author__ = 'DN'
import sys
count = len(open('D:\\pycharmproject\\jk\\jkl\\number.txt','rU').readlines())
print(count)
squared = [x ** 2 for x in range(9)]
sqdEvens = [x ** 2 for x in range(9) if not x % 2]
print (squared,)
print (sqdEvens,)
print (sys.platform)
print (1+2*4)
'''
s = input('please input a word:')
i = 0
while len(s) > i:
    print(s[i])
    i += 1
s = input('please input a word:')
for i in s:
    print (i)

listinput = input('please input five number:')
l = [ x for x in listinput.split() ]
sum = 0
i = 0
while len(l) > i:
    print (int(l[i]))
    sum = sum + int(l[i])
    i += 1
print (sum)
listinput = input('please input five number:')
l = [x for x in listinput.split()]
sum = 0
i = 1
for i in range(len(l)):
    sum = sum + int(l[i])
print (sum)

a = True
while a:
    i = input('please in put a number(1-100):')
    if 1 <= int(i) <= 100:
        print (i)
        a = False
    else:
        print ("false in put")
        continue
'''

