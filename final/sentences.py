#!/usr/bin/env python

import argparse
import sys
import textblob

def main():
  arguments = argparse.ArgumentParser(help = 'Prints the sentences in the text on standard input.')
  text = u' '.join(sys.stdin.read().decode('utf8').split())
  blob = textblob.TextBlob(text)
  for sentence in blob.sentences:
    print sentence


if '__main__' == __name__:
  main()
