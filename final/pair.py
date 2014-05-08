#!/usr/bin/env python

import argparse
import random
import sys


def main():
  arguments = argparse.ArgumentParser(help = 'Chooses two neighboring non-empty lines at random.')

  # read and strip all lines into a list
  lines = map(lambda line: line.strip(), sys.stdin.readlines())

  # remove empty lines from the list
  lines = filter(lambda line: len(line) > 0, lines)

  # choose a random pair of lines and print them
  choice = random.randrange(len(lines) - 1)
  for line in lines[choice : choice + 2]:
    print line


if '__main__' == __name__:
  main()
