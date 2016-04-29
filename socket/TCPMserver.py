# -*- coding: utf-8 -*-
from socket import *
import threading
import time

HOST = ''
PORT = 8888
BUFSIZ = 1024 # 1024字节 = 1kb
ADDR = (HOST, PORT)
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(6)

def m(tcpCliSock, addr):
    print '...connected from:', addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('%s' % (data))

while True:
    time.sleep(0.1)
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSock.accept()  # accept转接客户请求 空出主机再接受客户请求
    t = threading.Thread(target=m,args=(tcpCliSock, addr))
    #t.setDaemon(True)
    t.start()

tcpCliSock.close()
tcpSock.close()

