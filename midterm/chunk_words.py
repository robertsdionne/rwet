#!/usr/bin/env python

import collections
import itertools
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
  ('b', ['B']),
  ('c', ['S']),
  ('d', ['D']),
  ('e', ['EH0']),
  ('f', ['F']),
  ('g', ['G']),
  ('h', ['HH']),
  ('i', ['IH0']),
  ('j', ['JH']),
  ('k', ['K']),
  ('l', ['L']),
  ('m', ['M']),
  ('n', ['N']),
  ('o', ['OW0']),
  ('p', ['P']),
  ('q', ['K']),
  ('r', ['R']),
  ('s', ['S']),
  ('t', ['T']),
  ('u', ['AH']),
  ('v', ['V']),
  ('w', ['W']),
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


def main():
  for line in sys.stdin:
    line = line.strip()
    print line, ' '.join(chunk_word(line))


if '__main__' == __name__:
  main()
