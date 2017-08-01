#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
#filename special __one or more words charected __

# +++your code here+++
# Write functions and modify main() to call them

def ListSpecialFilesFullPath(directory):
  filenames = os.listdir(directory)
  listToString = ' '.join(filenames)
  special_files = re.findall(r'(\w*__\w+__[\w.]*)', listToString)

  print special_files
  if not special_files:
    print "No special files found"
    exit(0)

  fullPathSpecialFiles = []
  for file in special_files:
    fullPathSpecialFiles.append(os.path.abspath(os.path.join(directory, file)))

  return fullPathSpecialFiles

def ZipSpecialFiles(directory):
  special_files = ListSpecialFilesFullPath(directory)


# to dir is a full path
def CopyFiles(paths, toDir):

  if not os.path.exists(toDir):
    cmd = 'mkdir ' + toDir

  
  for filePath in paths:
    filename = os.path.basename(filePath)
    shutil.copy(filePath, os.path.join(toDir,filename))

def CopySpecialFiles(fromDir, toDir):
  print fromDir, toDir
  special_files = ListSpecialFilesFullPath(fromDir)

  if not special_files:
    print "No special files in " + fromDir

  CopyFiles(special_files, toDir)

def ZipSpecialFiles(directory, zipfile):
  special_files = ListSpecialFilesFullPath(directory)
  if not special_files:
    print "No files to zip"

  ZipFiles(special_files, zipfile)

def ZipFiles(paths, zipfile):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status != 0:
    print "command failed with status ", status
    sys.exit(status)



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  ListSpecialFilesFullPath(args[0])
  if len(todir) > 0:
    CopySpecialFiles(args[0], todir)

  if len(tozip) > 0:
    ZipSpecialFiles(args[0], tozip)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
