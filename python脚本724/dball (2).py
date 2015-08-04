#coding=utf-8 
#!/usr/bin/env python
import sys
import os
import random
import time
def createCaiPiao():
    blueBall = list()
    redBall = list()
    while True:
        blueNum = random.randint(1,33)
        if not  blueBall:
             blueBall.append(blueNum)
        if blueNum in  blueBall:
            continue
        else:
             blueBall.append(blueNum)
        if len(blueBall) == 6:
            break   
    blueBall1 =  blueBall
    blueBall2 = sorted(blueBall1)
    #with open('/tmp/random/resultblue.txt','a') as result:
    #    for result1 in blueBall2:
    #        result1 = str(result1)
    #        result.write(result1+' ')
    while True:
        redNum = random.randint(1,16)
        if not redBall:
             redBall.append(redNum)
        if len(redBall) == 1:
            break
    redBall1 = redBall
    blueBall2.extend(redBall1)
    #print blueBall2
    with open('/tmp/random/resultall.txt','a') as result:
        for result1 in blueBall2:
            result1 = str(result1)
            result.write(result1+' ')
        result.write('\n')
def cfall():
    allresult = list()
    result2 = list()
    with open('/tmp/random/resultall.txt','r') as result:
        result1 = result.read().split('\n')
        #result1 = result1.strip('\n')
        #print result1
        #print type(result1)
        sl = list(set(result1))
        result = []
        for i in sl:
            c=0
            for j in result1:
                if i == j:
                    c += 1
            result.append([i,c])
        print result
        #for i in range(len(result1)):
        #    #print result1[i]
        #    if result1[i] == ' ':
        #        continue
        #    if result1[i] == '\n':
        #        continue
        #    else:
        #        result2=result1[i]
                #print result2
               # print type(result2)
        #        allresult.append(result2)
        #print allresult
def getblue():
    allresult = list()
    dic = {}
    with open('/tmp/random/resultblue.txt','r') as result:
    #result1 = result.readlines()
        result1 = result.read().split(' ')
        #print result1
        for i in range(len(result1)):
            #print result1[i]
            if result1[i] == '':
                continue
            if result1[i] == '\n':
                continue
            else:
                result2=result1[i]
                #print result2
                allresult.append(result2)
        #print allresult
                #d = {k:a.count(k) for k in set(allresult)}
        for item in allresult:
            dic[item] = dic.get(item,0) + 1
        print (dic)
        #print sorted(dic.items(), key=lampda d:d[1])
        #print allresult
def getred():
    allresult = list()
    dic = {}
    with open('/tmp/random/resultred.txt','r') as result:
    #result1 = result.readlines()
        result1 = result.read().split(' ')
        #print result1
        for i in range(len(result1)):
            #print result1[i]
            if result1[i] == '':
                continue
            if result1[i] == '\n':
                continue
            else:
                result2=result1[i]
                #print result2
                allresult.append(result2)
        #print allresult
                #d = {k:a.count(k) for k in set(allresult)}
        for item in allresult:
            dic[item] = dic.get(item,0) + 1
        print (dic)
        #print allresult
if __name__ == '__main__':
    for i in xrange(100):
        createCaiPiao() 
    #getblue()
    #getred()
    #cfall()
