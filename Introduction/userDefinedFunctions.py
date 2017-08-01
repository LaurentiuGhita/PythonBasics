#!/usr/bin/env python

import sys

def repeat(s, exclaim):
    result = s * 3 # can also use s + s + s slower
    if exclaim:
        result += '!!!'
    return result


def main():
    print sys.argv
    print repeat('Yay', False)
    print repeat('Who hoo', True)

if __name__ == '__main__':
    main()
