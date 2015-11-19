#!/usr/bin/env python
#自己写的使用paramiko的ssh-key连接其他主机
import paramiko
hostname='192.168.40.203'
port=22
username='root'
pkey='/ITManage-master/var/rsa_key/id_rsa'
print (paramiko.pkey.get_name())
key=paramiko.RSAKey.from_private_key_file(pkey)
s=paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname,port,username,pkey=key)
stdin,stdout,stderr=s.exec_command('hostname')
print (stdout.read())
