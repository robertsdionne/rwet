#!/usr/bin/env python

import argparse
import json
import random
import re
import sys


S = 7
N = 14


def sanitize_word(word):
  return re.sub('[^\w\'-]', '', word).lower()


def main():
  commands = argparse.ArgumentParser(description = 'Generates stanzas from piecing together '
    'lines that start with the same sound as the ending of the previous line. Then, substitutes '
    'some words in each line with words that match the previous word\'s last letter and next '
    'word\'s first letter.')
  commands.add_argument('-r', '--reverse', action = 'store_true',
    help = 'whether to reverse the substituted words before planting them within a line')
  commands.add_argument('-p', '--probability', type = float, default = 0.25,
      help = 'the probability of substituting a word')

  arguments = commands.parse_args()

  starts_with = dict()
  word_starts_and_ends_with = dict()
  for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
      if arguments.reverse:
        word = sanitize_word(word[::-1]) # reverse the word
      else:
        word = sanitize_word(word)
      if len(word) > 0:
        first_letter, last_letter = word[0], word[-1]
        word_starts_and_ends_with[first_letter + last_letter] = word
    if len(words) > 0:
      first_word = sanitize_word(words[0])
      if len(first_word) > 0:
        first_letter = first_word[0]
        if first_letter not in starts_with:
          starts_with[first_letter] = set()
        starts_with[first_letter].add(line)
  s = 0
  while s < S:
    first_letter = random.choice(starts_with.keys())
    previous_line = None
    n = 0
    while first_letter in starts_with and n < N:
      if len(starts_with[first_letter]) is 0:
        break
      line = random.choice(list(starts_with[first_letter]))
      starts_with[first_letter].remove(line)
      original_words = line.split()
      words = original_words[:]
      for i in xrange(1, len(words) - 1, 2):
        if random.random() < arguments.probability:
          previous_word = sanitize_word(words[i - 1])
          word = sanitize_word(words[i])
          next_word = sanitize_word(words[i + 1])
          previous_last_letter = previous_word[-1]
          next_first_letter = next_word[0]
          if previous_last_letter + next_first_letter in word_starts_and_ends_with:
            words[i] = word_starts_and_ends_with[previous_last_letter + next_first_letter]
      line = ' '.join(words)
      print line
      last_word = sanitize_word(original_words[-1])
      first_letter = last_word[-1]
      n += 1
    print
    s += 1


if '__main__' == __name__:
  main()
