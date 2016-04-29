# -*- coding: utf-8 -*-
from socket import *

HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()