#!/usr/bin/env python

import sys
import re

def GetData(arguments):
	'''
		Check if arguments are ok
		arguments serverIp and port to listen/connect
		returns (error, ip, port)
	'''
	gotIpAddress = False
	gotPort = False
	ipaddr = ''
	port = 0
	errorCode = 0

	while gotIpAddress != True:
		if len(arguments) < 2:	
			print "Please specify ip"
			ipaddr = raw_input()
		else:
			ipaddr = sys.argv[1]


		valid = CheckIfValidIpv2(ipaddr)
		if valid:
			gotIpAddress = True

	while gotPort != True:
		if len(arguments) < 3:
			print "Please specify port"
			port = raw_input()
		else:
			port = sys.argv[2]

		valid = CheckIfPortValid(port)
		if valid:
			gotPort = True

	return (errorCode, ipaddr, port)

def CheckIfValidIpv2(ipaddr):
	match = re.search(r'[\d]+\.[\d]+\.[\d]+.[\d]+', ipaddr)
	if not match:
		print "Invalid ip address "
		return False
	return True

def CheckIfPortValid(port):
	match = re.search(r'[\d]+', port)
	if match:
		if int(port) >= 4000 and int(port) <= 8000:
			return True
		else:
			print "Port must be an integer between 4000 and 8000"
			return False
	else:
		print "Invalid format"
	return false



