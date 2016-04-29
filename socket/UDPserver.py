# -*- coding: utf-8 -*-
from socket import *

HOST = ''
PORT = 21588
BUFSIZ = 1024 # 1024字节 = 1kb
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print '等待数据'
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(data,addr)
    print '成功接受数据并返回到：',addr

udpSerSock.close()