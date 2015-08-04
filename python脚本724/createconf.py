#!/usr/bin/env python
import sys
import os
import re
import shutil
import time
pidfile = 'pid file = /var/run/rsyncd.pid'
port = 'port = 873'
address = 'address = 192.168.31.3'
uid = 'uid = root'
gid = 'gid = root'
usechroot = 'use chroot = yes'
readonly = 'read only = yes'
hostallow = 'hosts allow = *'
maxconnections = 'max connections = 5'
motdfile = 'motd file = /etc/rsyncd.motd'
logformat = 'log format = %t %a %m %f %b'
syslogfacility = 'syslog facility = local3'
timeout = 'timeout = 300'
projectname = '[svn]'
projectpath = 'path= /svn'
projectreadonly = 'read only = false'
projectlist = 'list = yes'
projectignoreerr = 'ignore errors'
projectauth = 'auth users = root'
projectsecrets = 'secrets file = /etc/rsyncd.secrets'
def writeRsyncConf():
    pidfile1 = raw_input("please input where do you what save your pid like(\033[1;32;40mpid file = /var/run/rsyncd.pid)(y set default\033[0m)")
    if pidfile1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(pidfile+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(pidfile1+'\n')
    port1 = raw_input("please input port like(\033[1;32;40mport = 873)(y set default\033[0m)")
    if  port1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(port+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(port1+'\n')
    address1 = raw_input("please input address like(\033[1;32;40maddress = 192.168.31.4)(y set default\033[0m)")
    if  address1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(address+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(address1+'\n')
    uid1 = raw_input("please input uid like(\033[1;32;40muid = root)(y set default\033[0m)")
    if uid1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(uid+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(uid1+'\n')
    gid1 = raw_input("please input gid like(\033[1;32;40mgid = root)(y set default\033[0m)")
    if gid1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(gid+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(gid1+'\n')
    usechroot1 = raw_input("please input if  can change root dir like(\033[1;32;40muse chroot = yes)(y set default\033[0m)")
    if usechroot1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(usechroot+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(usechroot1+'\n')
    readonly1 = raw_input("please input if readonly  like(\033[1;32;40mread only = yes)(y set default\033[0m)")
    if readonly1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(readonly+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(readonly1+'\n')
    hostallow1 = raw_input("please input allow host  like(\033[1;32;40mhosts allow = 192.168.0.1)(y set default\033[0m)")
    if hostallow1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(hostallow+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(hostallow1+'\n')
    maxconnections1 = raw_input("please input max connections  like(\033[1;32;40mmax connections = 5)(y set default\033[0m)")
    if maxconnections1 == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(maxconnections+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(maxconnections1+'\n')
    motdfile1 = raw_input("please input motd file  like(\033[1;32;40mmotd file = /etc/rsyncd.motd)(y set default\033[0m)")
    if motdfile1  == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(motdfile+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(motdfile1+'\n')
    logformat1 = raw_input("please input format log  like(\033[1;32;40mlog format = %t %a %m %f %b)(y set default\033[0m)")
    if logformat1  == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(logformat+'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(logformat1+'\n')
    syslogfacility1 = raw_input("please input sys log level  like(\033[1;32;40msyslog facility = local3)(y set default\033[0m)")
    if syslogfacility1  == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(syslogfacility +'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(syslogfacility1+'\n')
    timeout1 = raw_input("please input time out  like(\033[1;32;40mtimeout = 300)(y set default\033[0m)")
    if timeout1  == 'y':
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(timeout +'\n')
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write(timeout1+'\n')
def createProject():
    while True:
        print ("start creat project info")
        projectname1 = raw_input("please input project name  like(\033[1;32;40m[svn])(y set default\033[0m)")
        if  projectname1  == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectname +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectname1+'\n')
        projectpath1 = raw_input("please input project path  like(\033[1;32;40mpath= /svn)(y set default\033[0m)")
        if  projectpath1  == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectpath +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectpath1+'\n')
        projectreadonly1 = raw_input("please input if project is read only like(\033[1;32;40mread only = false)(y set default\033[0m)")
        if  projectreadonly1  == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectreadonly +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectreadonly1+'\n')
        projectlist1 = raw_input("please input if project can list like(\033[1;32;40mlist = yes)(y set default\033[0m)")
        if  projectlist1  == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectlist +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectlist1+'\n')
        projectignoreerr1 = raw_input("please input if project ignore errors like(\033[1;32;40mignore errors)(y set default\033[0m)")
        if  projectignoreerr1  == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectignoreerr +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectignoreerr1+'\n')
        projectauth1 = raw_input("please input project auth users  like(\033[1;32;40mauth users = root)(y set default\033[0m)")
        if  projectauth1   == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectauth +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectauth1 +'\n')
        projectsecrets1 = raw_input("please input project secrets path  like(\033[1;32;40msecrets file = /etc/rsyncd.secrets)(y set default\033[0m)")
        if  projectsecrets1   == 'y':
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectsecrets +'\n')
        else:
            with open('/etc/rsyncd.conf','a') as rsynconf:
                rsynconf.write(projectsecrets1 +'\n')
        otherproject = raw_input("one project have done, \033[1;32;40mcreate other input y quit input n(y or n\033[0m)")
        if otherproject == 'y':
            continue
        if otherproject == 'n':
            break
            
def createRsyncConf():
    if os.path.exists('/etc/rsyncd.conf'):
        input = raw_input("rsyncconf file have exist do you what create new or add project?(\033[1;32;40my=create new a=add project other exit\033[0m)")
        if input == 'y':
            os.system('echo "#"  > /etc/rsyncd.conf ')
            writeRsyncConf()
	    createProject()
            ###write func()
	if input == 'a':
	    createProject()
	    ####write projectfun()
        else:
            print ("exit")
    else:
        with open('/etc/rsyncd.conf','a') as rsynconf:
            rsynconf.write('#### '+'\n')
            writeRsyncConf()
	    createProject()

if __name__ == '__main__':
    createRsyncConf()
