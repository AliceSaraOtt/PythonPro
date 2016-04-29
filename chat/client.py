# -*- coding: utf-8 -*-
from socket import *
import time,random as r

host = '127.0.0.1'
port = 9999
bufsize = 1024
addr = (host,port)
client = socket(AF_INET,SOCK_STREAM)
client.connect(addr)
print client.recv(bufsize) # 接受欢迎信息

while True:
    data = client.recv(1024)
    if data:
        print data
    time.sleep(1)
    #client.send('%s\r\n' % data)

print '要结束了'
client.close()