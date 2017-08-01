#!/usr/bin/env python

from socket import *
from time import ctime
import sys
import re

import addressCheck

def RunServer(ipaddr, port):
	addressTuple = (ipaddr, int(port))
	buffSize = 1024

	tcpSrvSocket = socket(AF_INET, SOCK_STREAM)
	tcpSrvSocket.bind(addressTuple)
	tcpSrvSocket.listen(5)

	try:
		while True:
			print "Waiting for connection ..."
			tcpClientSocket, clientAddr = tcpSrvSocket.accept()
			print "New connection from: ", clientAddr

			while True:
				receivedData = tcpClientSocket.recv(buffSize)
				
				if not receivedData:
					break
				tcpClientSocket.send('[%s] %s' % (ctime(), receivedData))

			tcpClientSocket.close()

	except KeyboardInterrupt:
		print "Received keyboard interrupt, shutting down .. "
		tcpSrvSocket.close()
	except EOFError:
		print "Shutting down ... "
		tcpSrvSocket.close()

def main():

	(error, ip, port) = addressCheck.GetData(sys.argv)
	if error == 0:
		RunServer(ip, port)

if __name__ == '__main__':
	main()