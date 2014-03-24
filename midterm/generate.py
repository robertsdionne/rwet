#!/usr/bin/env python

import collections
import json
import random
import re
import sys


PARSE = collections.OrderedDict([
  ('ooooooooo', ['UW0']),
  ('eeee', ['IY0']),
  ('iiii', ['AY0']),
  ('eee', ['IY0']),
  ('hhh', ['HH']),
  ('iii', ['AY0']),
  ('rrr', ['R']),
  ('aa', ['AA0']),
  ('ay', ['AY0']),
  ('ch', ['CH']),
  ('dd', ['D']),
  ('ee', ['IY0']),
  ('er', ['ER0']),
  ('ey', ['EY0']),
  ('ii', ['AY0']),
  ('hh', ['HH']),
  ('ll', ['LL']),
  ('oo', ['UW0']),
  ('oy', ['OY0']),
  ('ph', ['F']),
  ('qk', ['K']),
  ('rr', ['R']),
  ('sh', ['SH']),
  ('th', ['TH']),
  ('yy', ['EY0']),
  ('a', ['AE0']),
  ('c', ['S']),
  ('d', ['D']),
  ('e', ['EH0']),
  ('f', ['F']),
  ('g', ['G']),
  ('h', ['HH']),
  ('k', ['K']),
  ('l', ['L']),
  ('m', ['M']),
  ('n', ['N']),
  ('o', ['OW0']),
  ('p', ['P']),
  ('q', ['K']),
  ('r', ['R']),
  ('i', ['IH0']),
  ('s', ['S']),
  ('t', ['T']),
  ('v', ['V']),
  ('x', ['K', 'S']),
  ('y', ['EY0']),
  ('z', ['Z'])
])


def chunk_word(word):
  result = []
  chunk_found = False
  for chunk, phonemes in PARSE.iteritems():
    if word.startswith(chunk):
      result.extend(phonemes)
      word = word[len(chunk):]
      chunk_found = True
      break
  if chunk_found and word:
    result.extend(chunk_word(word))
  if not chunk_found:
    result.append('?')
  return result



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
  for line in sys.stdin:
    line = line.strip()
    words = line.split()
    with open('naturalcadences.txt') as file:
      words_by_cadence = json.load(file)
    choices = []
    for word in words:
      cadence = word_cadence(chunk_word(word))
      choice = random.choice(words_by_cadence.get(cadence, ['?']))
      choices.append(choice)
    print ' '.join(words)
    print ' '.join(choices)
    print



if '__main__' == __name__:
  main()
