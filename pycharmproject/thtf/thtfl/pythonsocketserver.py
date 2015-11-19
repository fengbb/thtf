#-*- coding: utf-8 -*-
# socket 服务器端编程主要包括下面几点
#1 打开socket
#2 绑定到一个地址端口
#3 侦听进来的连接
#4 接受数据
#5 读写数据
import socket
import sys
HOST = ''
PORT = 9999
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. error code:' + str(msg[0]) + ', error message: ' + msg[1])
    sys.exit()
print ('Socket created')
try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print('Bind failed. Erroe code:' + str(msg[0]) + 'Message' + msg[1])
    sys.exit()
print ('Socket bind commplete')
#绑定 Socket 之后就可以开始侦听连接，我们需要将 Socket 变成侦听模式。socket 的 listen 函数用于实现侦听模式：
s.listen(10)
print ('Socket now listening')
#listen 函数所需的参数成为 backlog，用来控制程序忙时可保持等待状态的连接数。这里我们传递的是 10，意味着如果已经有 10 个连接在等待处理，
# 那么第 11 个连接将会被拒绝。当检查了 socket_accept 后这个会更加清晰。
# 接受连接
### 这样的话接受连接后立即关闭，没有什么用，连接建立后一般会有大量事情需要处理，因此我们给客户端
conn, addr = s.accept()
print ('Connected with' + addr[0] + ':' + str(addr[1]))
#


