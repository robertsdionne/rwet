#!/usr/bin/env python


import argparse
import json
import sys


def normalize_dictionary_of_counts(dictionary_of_counts):
  total_count = 0.0
  for count in dictionary_of_counts.itervalues():
    total_count += count
  return {key: count / total_count for key, count in dictionary_of_counts.iteritems()}


def main():
  commands = argparse.ArgumentParser(description = 'Extracts n-grams from standard input.')
  commands.add_argument('-n', '--number', dest = 'number', type = int, default = 2,
      help = 'the number, n, of units in the n-grams')
  unit_group = commands.add_mutually_exclusive_group(required = True)
  unit_group.add_argument('-c', '--characters', action = 'store_true',
      help = 'sets the unit to characters')
  unit_group.add_argument('-t', '--tokens', action = 'store_true',
      help = 'sets the unit to tokens')

  arguments = commands.parse_args()

  if arguments.characters:
    delimiter = ''
  else:
    delimiter = ' '

  ngrams = {}
  for i in xrange(1, arguments.number + 1):
    ngrams[i] = {}
  for line in sys.stdin:
    if arguments.characters:
      units = line.strip()
    else:
      units = line.strip().split()
    for i in xrange(1, arguments.number + 1):
      igrams = ngrams[i]
      for j in xrange(0, len(units) - i + 1):
        if i > 1:
          prefix = delimiter.join(units[j:j + i - 1])
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
  ngrams[1] = normalize_dictionary_of_counts(ngrams[1])
  for i in xrange(2, arguments.number + 1):
    for key, value in ngrams[i].iteritems():
      ngrams[i][key] = normalize_dictionary_of_counts(ngrams[i][key])
  print json.dumps(ngrams, indent = 2, sort_keys = True)


if '__main__' == __name__:
  main()
