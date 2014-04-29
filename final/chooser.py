#!/usr/bin/env python

import argparse
import json
import numpy
import random
import sys


def main():
  commands = argparse.ArgumentParser(description = 'Chooses words.')
  commands.add_argument('-p', '--probability', type = float, default = 0.5,
      help = 'the probability parameter to a geometric distribution')
  arguments = commands.parse_args()
  for line in sys.stdin:
    line = json.loads(line)
    words = list()
    for entry in line:
      index = min(numpy.random.geometric(arguments.probability), len(entry['alternate_words']) - 1)
      choice = entry['alternate_words'][index]
      words.append(choice)
    print ' '.join(words)


if '__main__' == __name__:
  main()
