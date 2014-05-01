#!/usr/bin/env python

import argparse
import json
import re
import sys


# extract the word from entries with a parenthetical numeric suffix,
#   e.g. 'ACCENT' from 'ACCENT(1)'
def extract_word(word):
  match = re.match('(.*)\\([0-9]+\\)', word)
  return match.group(1) if match else word


def main():
  commands = argparse.ArgumentParser(description = 'Converts cmudict to JSON format')
  commands.parse_args()

  # store word pronunciations into a dictionary for subsequent JSON output
  word_pronunciations = dict()
  for line in sys.stdin:

    # strip leading and trailing whitespace
    line = line.strip()

    # skip comments
    if line.startswith(';;;'):
      continue

    # split the line into tokens
    tokens = line.split()

    # extract the word from the first token
    word = extract_word(tokens[0]).lower()

    # extract the phonemes from the remaining tokens
    phonemes = tokens[1:]

    # add the phonemes to the list of pronunciations stored at word_pronunciations[word]
    word_pronunciations.setdefault(word, list()).append(phonemes)

  # print the word pronunciations as JSON
  print json.dumps(word_pronunciations, indent = 2, sort_keys = True)


if '__main__' == __name__:
  main()
