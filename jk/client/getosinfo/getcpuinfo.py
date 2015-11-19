#!/usr/bin/env python
#-*- coding: utf-8 -*-
from subprocess import PIPE,Popen
import re
def getCpuInfo():
	p = Popen(['cat', '/proc/cpuinfo'],shell=False,stdout=PIPE)
	stdout, stderr = p.communicate()
	#print (stdout.strip())
	return stdout.strip()
def parserCpuInfo(cpudata):
	pd = {}
	model_name = re.compile(r'.*model name\s+:\s(.*)')
	vendor_id = re.compile(r'vendor_id\s+:(.*)')
    	#cpu_cores = re.compile(r'cpu cores\s+:\s([\d]+)')
    	cpu_cores = re.compile(r'cpu cores\s+:\s(.*)')
    	lines = [line for line in cpudata.split('\n')]
    	for line in lines:
        	model = re.match(model_name,line)
        	vendor = re.match(vendor_id,line)
        	cores = re.match(cpu_cores,line)
		#print (model,vendor,cores)
        	if model:
            		pd['Model_Name'] = model.groups()[0].strip()
			#print (model.groups()[0].strip())
        	if vendor:
            		pd['Vendor_Id'] = vendor.groups()[0].strip()
        	if cores:
            		pd['Cpu_Cores'] = cores.groups()[0].strip()
        	else:
			pass
            	#	pd['Cpu_Cores'] = int('1')
    	return pd
if __name__ == '__main__':
	cpudata = getCpuInfo()
	print parserCpuInfo(cpudata)
