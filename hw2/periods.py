#!/usr/bin/env python

import re
import sys


def main():
  for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if len(words) > 0:
      print '%s.' % line
    else:
      print line


if '__main__' == __name__:
  main()
