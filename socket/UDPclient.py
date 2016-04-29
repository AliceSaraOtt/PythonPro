# -*- coding: utf-8 -*-
from socket import *

HOST = 'localhost'
PORT = 21588
BUFSIZ = 1024 # 1024字节 = 1kb
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCliSock.close()