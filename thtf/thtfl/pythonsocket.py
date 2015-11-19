#-*- coding=: utf-8 -*-
import socket
import sys
#首先要创建一个Socket， socket的socket的函数可以实现
# 1 创建一个socket,
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 上面代码使用了下面俩个属性来创建Socket
# 地址族：socket.AF_INET(IPv4)
# 类型：socket.SOCK_STREAM 使用TCP传输控制协议,socket.SOCK_DGRAM 使用UDP传输控制协议
# 2 错误处理
try:
    s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. error code:' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print ('Socket Created')
# 3 连接到服务器， 连接到服务器需要服务器地址和端口号
# 连接到服务器之前，我们需要知道它的IP地址，在Python中，获取IP地址很简单的：
try:
    s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. error code:' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print ('Socket Created')
host = 'www.tvican.com'
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
print ('Ip address of ' + host + ' is ' + remote_ip)
# 4 我们已经有IP 地址了，接下来需要制定要连接的端口
try:
    s3 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. error code:' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print ('Socket Created')
host1 = 'www.tvican.com'
port = 80
try:
    remote_ip = socket.gethostbyname(host1)
except socket.gaierror as e:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
print ('Ip address of ' + host + ' is ' + remote_ip)
s3.connect((remote_ip,port))
print ('Socket Connected to ' + host + ' is ' + ' on ip ' + remote_ip)
#使用 SOCK_STREAM/TCP 套接字才有“连接”的概念。连接意味着可靠的数据流通讯机制，可以同时有多个数据流。可以想象成一个数据互不干扰的管道。另外一个重要的提示是：数据包的发送和接收是有顺序的。
# 其他一些 Socket 如 UDP、ICMP 和 ARP 没有“连接”的概念，它们是无连接通讯，意味着你可从任何人或者给任何人发送和接收数据包。
#5 连接创建后，接下来就是往服务器上发送数据
try:
    s4 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. error code:' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print ('Socket Created')
host2 = 'www.tvican.com'
port = 80
try:
    remote_ip = socket.gethostbyname(host1)
except socket.gaierror as e:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
print ('Ip address of ' + host + ' is ' + remote_ip)
s4.connect((remote_ip,port))
print ('Socket Connected to ' + host + ' is ' + ' on ip ' + remote_ip)
message = "GET / HTTP/1.1\r\n\r\n"
try:
    s4.sendall(message.encode()) #python3 send 数据必须是bytes
except socket.error:
    print ('send failed')
    sys.exit()
print ('Message send successfully')
#6 数据发送完后就是接收数据， recv 函数接收数据
try:
    s5 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. error code:' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print ('Socket Created')
host3 = 'www.tvican.com'
port = 80
try:
    remote_ip = socket.gethostbyname(host3)
except socket.gaierror as e:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
print ('Ip address of ' + host + ' is ' + remote_ip)
s5.connect((remote_ip,port))
print ('Socket Connected to ' + host + ' is ' + ' on ip ' + remote_ip)
message = "GET / HTTP/1.1\r\n\r\n"
try:
    s5.sendall(message.encode()) #python3 send 数据必须是bytes
except socket.error:
    print ('send failed')
    sys.exit()
print ('Message send successfully')
reply = s5.recv(4096).decode()
print (reply)
s5.close()











