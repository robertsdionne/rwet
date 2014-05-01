#!/usr/bin/env python

import argparse
import re
import sys


def main():
  commands = argparse.ArgumentParser(
      description = 'Cleans up a source text by splitting on punctuation instead of original lines')
  commands.parse_args()
  
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
