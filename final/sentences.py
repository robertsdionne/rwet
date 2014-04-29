#!/usr/bin/env python

import sys
import textblob

def main():
  text = u' '.join(sys.stdin.read().decode('utf8').split())
  blob = textblob.TextBlob(text)
  for sentence in blob.sentences:
    print sentence


if '__main__' == __name__:
  main()
