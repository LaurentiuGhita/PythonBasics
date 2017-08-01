#!/usr/bin/env python

from socket import *
import sys
import re

import addressCheck

def ConnectClient(ipaddr, port):
	serverAddress = (ipaddr, int(port))
	maxMsgSize = 1024

	tcpClientSocket = socket(AF_INET, SOCK_STREAM)
	tcpClientSocket.connect(serverAddress)

	while True:
		data = raw_input('>')
		if not data:
			break

		tcpClientSocket.send(data)
		receivedData = tcpClientSocket.recv(maxMsgSize)
		if not receivedData:
			print "No response from server exiting ... "
			break
		else:
			print "Received from server: ", receivedData 

	tcpClientSocket.close()


def main():
	(error, ip, port) = addressCheck.GetData(sys.argv)
	if error == 0:
		ConnectClient(ip, port)

if __name__ == '__main__':
	main()