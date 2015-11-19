#-*- coding: utf-8 -*-
import paramiko
def sshConnect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.40.204',22,'root','Abcd1234')
    stdin,stdout,stderr = client.exec_command('uname -a')
    for line in stdout:
        print ('...' + line.strip('\n'))
    client.close()
def ptyConnect():
    t = paramiko.Transport('192.168.40.204',22)
    t.connect(username='root',password='Abcd1234')
    chan = t.open_session()
    chan.settimeout(60)
    chan.get_pty()
    chan.invoke_shell()
    chan.send('ifconfig')
    print (chan.recv(65535))
if __name__ == '__main__':
    sshConnect()
    ptyConnect()
