#!/usr/bin/env python

import argparse
from hw1 import MarkovCharacterMutator
import json
import random
import re
import sys


S = 7 # number of stanzas
N = 14 # maximum number of lines per stanza


class FlowingGenerator(object):

  def __init__(self, lines_per_stanza, mutator, probability, reverse, stanzas):
    self.lines_per_stanza = lines_per_stanza
    self.mutator = mutator
    self.probability = probability
    self.reverse = reverse
    self.stanzas = stanzas
    self.starts_with = dict()
    self.word_starts_and_ends_with = dict()

  def feed(self, text):
    words = self.tokenize(text)
    for word in words:
      if self.reverse:
        word = self.sanitize_word(word[::-1]) # reverse the word
      else:
        word = self.sanitize_word(word)
      if len(word) > 0:
        word = self.mutator.feed(word)
        first_letter, last_letter = word[0], word[-1]
        self.word_starts_and_ends_with[first_letter + last_letter] = word
    if len(words) > 0:
      first_word = self.sanitize_word(words[0])
      if len(first_word) > 0:
        first_letter = first_word[0]
        self.starts_with.setdefault(first_letter, set()).add(text)

  def generate(self):
    s = 0
    while s < self.stanzas:
      first_letter = random.choice(self.starts_with.keys())
      previous_line = None
      n = 0
      while first_letter in self.starts_with:
        if len(self.starts_with[first_letter]) is 0:
          break
        line = random.choice([x for x in self.starts_with[first_letter]])
        self.starts_with[first_letter].remove(line)
        original_words = line.split()
        words = filter(lambda w: len(self.sanitize_word(w)) > 0, original_words[:])
        for i in xrange(1, len(words) - 1, 2):
          if random.random() < self.probability:
            previous_word = words[i - 1]
            word = words[i]
            next_word = words[i + 1]
            previous_last_letter = previous_word[-1]
            next_first_letter = next_word[0]
            if previous_last_letter + next_first_letter in self.word_starts_and_ends_with:
              words[i] = self.word_starts_and_ends_with[previous_last_letter + next_first_letter]
        line = ' '.join(words)
        print line.encode('utf8')
        last_word = self.sanitize_word(original_words[-1])
        first_letter = last_word[-1]
        n += 1
      print
      s += 1

  def sanitize_word(self, word):
    return re.sub('[^\w\'-]', '', word).lower()

  def tokenize(self, text):
    return text.split()


def main():
  commands = argparse.ArgumentParser(description = 'Generates stanzas from piecing together '
    'lines that start with the same sound as the ending of the previous line. Then, substitutes '
    'some words in each line with words that match the previous word\'s last letter and next '
    'word\'s first letter.')
  commands.add_argument('-l', '--language_model', required = True, help = 'the language model')
  commands.add_argument('-p', '--probability', type = float, default = 0.25,
      help = 'the probability of substituting a word')
  commands.add_argument('-r', '--reverse', action = 'store_true',
    help = 'whether to reverse the substituted words before planting them within a line')

  arguments = commands.parse_args()

  mutator = MarkovCharacterMutator(arguments.language_model, 0.5, False, False)
  mutator.prepare()
  generator = FlowingGenerator(N, mutator, arguments.probability, arguments.reverse, S)
  for line in sys.stdin:
    generator.feed(line.decode('utf8').strip())
  generator.generate()

if '__main__' == __name__:
  main()
