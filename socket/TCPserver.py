# -*- coding: utf-8 -*-
from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024 # 1024字节 = 1kb
ADDR = (HOST, PORT)
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(6)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSock.accept()  # accept转接客户请求 空出主机再接受客户请求
    print '...connected from:', addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('%s' % (data))

tcpCliSock.close()
tcpSock.close()

