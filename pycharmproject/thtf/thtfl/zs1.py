import ssl
import socket
import pprint
from ssl import SSLSocket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.settimeout(1)
ssl_sock = ssl.wrap_socket(s,
                                ca_certs="C:\cacert.pem",
                                cert_reqs=ssl.CERT_REQUIRED)
#wrappedSocket = ssl.SSLSocket.getpeercert(binary_form=False)
ssl_sock.connect(('www.verisign.com', 443))
response = False
pprint.pprint(ssl_sock.getpeercert())
#    der_cert = wrappedSocket.getpeercert(False)
#    der_cert_bin = wrappedSocket.getpeercert(True)
#    print(der_cert)
#    print ('##########')
#    print(der_cert_bin)
#    print ('##########')
#    pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
#    print(pem_cert)
ssl_sock.close()
