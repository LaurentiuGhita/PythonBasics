#!/usr/bin/env python

from socket import *

tcpSock = socket(AF_INET, SOCK_STREAM)
udpSock = socket(AF_INET, SOCK_DGRAM)

address = ("", 7074)

tcpSock.bind(address)
tcpSock.listen(5)

while True:
	print "doing shit"