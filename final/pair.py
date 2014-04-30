#!/usr/bin/env python

import random
import sys


def main():
  lines = map(lambda line: line.strip(), sys.stdin.readlines())
  lines = filter(lambda line: len(line) > 0, lines)
  choice = random.randrange(len(lines) - 1)
  for line in lines[choice : choice + 2]:
    print line


if '__main__' == __name__:
  main()
