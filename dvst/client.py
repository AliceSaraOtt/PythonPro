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
    data = []
    who = raw_input('请下注：龙-1 虎-2 平-3：')
    money = raw_input('下注金额：')
    client.send(who + '-' + money) # 发送下注信息
    data = client.recv(bufsize) # 接受赌博结果
    data = data.split('-')
    print '龙:%s 虎:%s 余额:%s' % (data[0],data[1],data[2])
    #client.send('%s\r\n' % data)
client.close()


