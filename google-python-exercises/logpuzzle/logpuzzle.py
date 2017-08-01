#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def myComp(url):
  match = re.search(r'\S+/\S+-(\w+).', url)
  lastPart = match.group(1)
  return lastPart

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++

  urlStart = filename.index('_') + 1
  hostUrl = filename[urlStart:]
  print hostUrl

  if not os.path.exists(filename):
    print 'Filename', filename, "does not exist"
    sys.exit(1)

  try:
    f = open(filename, 'rU')
    text = f.read()
    url_matches = re.findall(r'GET\s(\S*puzzle\S*)\s', text)
    if not url_matches:
      print "No matches found"
      return

    prependUrl = "http://" + hostUrl
    fullUrlList = [prependUrl + fileUrl for fileUrl in url_matches]

    # get rid of duplicates
    dictionary = {}
    for url in fullUrlList:
      dictionary[url] = 1
      
    uniqueUrls = dictionary.keys()
    uniqueUrlsSorted = sorted(uniqueUrls, key=myComp)

    return uniqueUrlsSorted
  except IOError:
    sys.stderr.write("Problem reading:" + filename)

  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  index = 0
  for img_url in img_urls:
    local_name = "img%d" %index
    print "Retrieving " + img_url
    urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))
    index += 1

  ouputHtml = os.path.join(dest_dir, 'index.html')
  output = open(ouputHtml, 'w')
  output.write('<html><body>\n')

  for i in range(index):
    entry = '<img src="img%d">' %i
    output.write(entry)

  output.write('</body></html>\n')
  print "\n".join(img_urls)


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
