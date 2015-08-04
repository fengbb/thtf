#coding=utf-8 
#!/usr/bin/env python
import sys
import os
import random
import time
def createCaiPiao():
	blueBall=list()
#	randomshu = random.randint(1,33)
#	caipiao.append(randomshu)
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
	blueBall =  blueBall
	blueBall.sort()
	with open('/tmp/random/result.txt','a') as result:
		result.write('篮球：')
		for result1 in blueBall:
			result1 =  str(result1)
			result.write(result1+' ')
		result.write('\n')
	redBall = str(random.randint(1,17))
	with open('/tmp/random/result.txt','a') as result:
		result.write('红球：'+redBall+'\n')
if __name__ == '__main__':
	for i in xrange(1000000):
		createCaiPiao()	
