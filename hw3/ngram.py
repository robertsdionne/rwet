#!/usr/bin/env python


import argparse
import json
import sys


class LanguageModel(object):

  def __init__(self, delimiter, number):
    self.delimiter = delimiter
    self.ngrams = dict()
    self.number = number

  def count(self, units):
    for i in xrange(1, self.number + 1):
      igrams = self.ngrams.setdefault(i, dict())
      for j in xrange(len(units) - i + 1):
        if i > 1:
          prefix = self.delimiter.join(units[j:j + i - 1])
          suffix = units[j + i - 1]
          if not prefix in igrams:
            igrams[prefix] = {}
          if not suffix in igrams[prefix]:
            igrams[prefix][suffix] = 1
          else:
            igrams[prefix][suffix] += 1
        else:
          suffix = units[j]
          if not suffix in igrams:
            igrams[suffix] = 1
          else:
            igrams[suffix] += 1

  def generate(self):
    self.ngrams[1] = self.normalize_dictionary_of_counts(self.ngrams[1])
    for i in xrange(2, self.number + 1):
      for key, value in self.ngrams[i].iteritems():
        self.ngrams[i][key] = self.normalize_dictionary_of_counts(self.ngrams[i][key])
    print json.dumps(self.ngrams, indent = 2, sort_keys = True)

  def normalize_dictionary_of_counts(self, dictionary_of_counts):
    total_count = 0.0
    for count in dictionary_of_counts.itervalues():
      total_count += count
    return {key: count / total_count for key, count in dictionary_of_counts.iteritems()}

  def tokenize(self, text):
    return text.split()


class CharacterLanguageModel(LanguageModel):

  def __init__(self, number):
    super(CharacterLanguageModel, self).__init__('', number)

  def feed(self, text):
    self.count(text)


class TokenLanguageModel(LanguageModel):

  def __init__(self, number):
    super(TokenLanguageModel, self).__init__(' ', number)

  def feed(self, text):
    self.count(self.tokenize(text))


def main():
  commands = argparse.ArgumentParser(description = 'Extracts n-grams from standard input.')
  commands.add_argument('-n', '--number', type = int, default = 2,
      help = 'the number, n, of units in the n-grams')
  unit_group = commands.add_mutually_exclusive_group(required = True)
  unit_group.add_argument('-c', '--characters', action = 'store_true',
      help = 'sets the unit to characters')
  unit_group.add_argument('-t', '--tokens', action = 'store_true',
      help = 'sets the unit to tokens')

  arguments = commands.parse_args()

  if arguments.characters:
    language_model = CharacterLanguageModel(arguments.number)
  else:
    language_model = TokenLanguageModel(arguments.number)

  for line in sys.stdin:
    language_model.feed(line.decode('utf8').strip())  
  language_model.generate()


if '__main__' == __name__:
  main()
