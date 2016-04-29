# -*- coding: utf-8 -*-
# 创建SocketServerTCP服务器：
import SocketServer, random as r
from SocketServer import StreamRequestHandler as SRH
from time import ctime, sleep

def bet(who, money, left):
    res = []  # 返回龙，虎，和余额
    dragon = r.randint(1, 13)
    sleep(0.1)
    targer = r.randint(1, 13)

    if who == '1':  # 押龙
        if dragon > targer:
            left += money
        else:
            left -= money
    elif who == '2':  # 押虎
        if dragon < targer:
            left += money
        else:
            left -= money
    elif who == '3':
        if dragon == targer:
            left = money * 16
        else:
            left -= money
    res.append(dragon)
    res.append(targer)
    res.append(left)
    res = [str(v) for v in res]
    return '-'.join(res)

host = '127.0.0.1'
port = 9999
addr = (host, port)

class Servers(SRH):
    def handle(self):
        print 'got connection from ', self.client_address
        self.wfile.write('欢迎光临云顶山庄')
        left = 1000
        while True:
            data = self.request.recv(1024)
            data = data.split('-') # 分解下注信息
            res = bet(data[0], int(data[1]), int(left))  # 调用赌博函数
            left = res[res.rfind('-') + 1:] # 调整余额
            self.request.send(res)

print 'server is running....'
server = SocketServer.ThreadingTCPServer(addr, Servers)
server.serve_forever()
