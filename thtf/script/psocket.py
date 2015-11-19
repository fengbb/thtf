import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sc = s.connect(("www.baidu.com",80))

