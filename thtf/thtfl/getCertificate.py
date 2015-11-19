#-*- coding: utf-8 -*-
#http://www.2cto.com/kf/201406/306115.html
from socket import socket
from OpenSSL.SSL import Connection, Context, SSLv3_METHOD, TLSv1_1_METHOD, WantReadError
sslcontext = Context(SSLv3_METHOD)
sslcontext.set_timeout(30)
#ip = '119.75.218.70'
yuming = 'www.itoppay.com'
s = socket()
s.connect(('www.itoppay.com',443))
c = Connection(sslcontext,s)
c.set_connect_state()
print ("%s try to handshake" % (yuming))
c.do_handshake()
cert = c.get_peer_certificate()
####颁发者
print ("issuer:", cert.get_issuer())
###使用者
print ("subject:" ,cert.get_subject())
#print (cert.get_extension())
print (cert.get_extension_count())
###有效期到
print (cert.get_notAfter())
###有效期从
print (cert.get_notBefore())
pubkey = cert.get_pubkey()
print (pubkey.type())

print (cert.get_pubkey())
print (cert.get_serial_number())
print (cert.get_signature_algorithm())
print (cert.get_version)
#print (cert._get_boundary_time())
#print (cert.__getattribute__())
c.shutdown()
s.close()
