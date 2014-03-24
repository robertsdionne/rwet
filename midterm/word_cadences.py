#!/usr/bin/env python

import json
import re
import sys


def transform_phoneme(phoneme):
  match = re.match('.*([0-9])', phoneme)
  return 'V' if match else 'C'


def word_cadence(phonemes):
  def remove_duplicates(phoneme):
    if 'C' == phoneme:
      if remove_duplicates.previous_phoneme_was_vowel:
        remove_duplicates.previous_phoneme_was_vowel = False
        return True
      else:
        return False
    else:
      remove_duplicates.previous_phoneme_was_vowel = True
      return True
  remove_duplicates.previous_phoneme_was_vowel = True
  return ''.join(filter(remove_duplicates, map(transform_phoneme, phonemes)))


def main():
  words_by_cadence = dict()
  for line in sys.stdin:
    line = line.strip()
    if line.startswith(';;;'):
      continue
    tokens = line.split()
    word = tokens[0]
    phonemes = tokens[1:]
    cadence = word_cadence(phonemes)
    words_by_cadence.setdefault(cadence, []).append(word)
  print json.dumps(words_by_cadence, indent = 2, sort_keys = True)

if '__main__' == __name__:
  main()
