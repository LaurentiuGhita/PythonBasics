#!/usr/bin/env python

from SocketServer import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST='127.0.0.1'
PORT= 7089
ADDR = (HOST, PORT)

class MyRequestHandler(SRH): ## derive from SRH
	def handle(self): # override handle
		print "... conntected from: ", self.client_address
		self.wfile.write('[%s] %s' %(ctime(), 
			self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection'
tcpServ.serve_forever()