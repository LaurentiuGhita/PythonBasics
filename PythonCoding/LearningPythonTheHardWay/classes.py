#!/usr/bin/env python

class MyClass(object):
	def __init__(self, inputStr, inputList):
		self.stringA = inputStr
		self.listOfIntes = inputList

	def printString(self):
		print self.stringA

	def printList(self):
		for integer in self.listOfIntes:
			print integer


def main():
	myObj = MyClass("cucu", [1, 3,4, 6])
	myObj.printString()
	myObj.printList()

if __name__ == '__main__':
	main()