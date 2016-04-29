# -*- coding: utf-8 -*-
# 创建SocketServerTCP服务器：
import SocketServer, random as r,threading
from SocketServer import StreamRequestHandler as SRH
from time import ctime, sleep

host = '127.0.0.1'
port = 9999
addr = (host, port)

class Servers(SRH):
    user = []
    def handle(self):
        self.user.append(self.request)
        print 'got connection from ', self.client_address
        #self.wfile.write('welcome to 925')
        while True:
            msg = raw_input('大喇叭：')
            for u in self.user:
                u.send(msg)

print 'server is running....'
server = SocketServer.ThreadingTCPServer(addr, Servers)
server.serve_forever()
#server_thread = threading.Thread(target=server.serve_forever)
# Exit the server thread when the main thread terminates
#server_thread.daemon = True
#server_thread.start()
