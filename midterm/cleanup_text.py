#!/usr/bin/env python

import argparse
import re
import sys


def main():
  lines = sys.stdin.readlines()
  text = ''.join(lines)
  text = re.sub('\n', ' ', text)
  text = re.sub('\\.\\s+', '.\n', text)
  text = re.sub('\\!\\s+', '!\n', text)
  text = re.sub('\\?\\s+', '?\n', text)
  text = re.sub(',\\s+', ',\n', text)
  text = re.sub('-\\s+', '-\n', text)
  text = re.sub(':\\s+', ':\n', text)
  text = re.sub(';\\s+', ';\n', text)
  print text


if '__main__' == __name__:
  main()
