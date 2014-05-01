#!/usr/bin/env python


import argparse
import bisect
import json
import random
import sys


# from http://docs.python.org/3.2/library/itertools.html#itertools.accumulate
def accumulate(iterable):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total = total + element
        yield total


def sample_from_distribution(distribution, uniform_probability):
  units, probabilities = zip(*distribution.iteritems())
  if uniform_probability:
    probabilities = [1.0 / len(probabilities) for p in probabilities]
  cumulative_probabilities = list(accumulate(probabilities))
  index = bisect.bisect_left(cumulative_probabilities, random.random())
  return units[index]


def mutate_unit(language_model, n, uniform_probability, prefix, suffix):
  if ' ' == suffix or '\t' == suffix:
    return suffix
  ngrams = language_model[str(n)]
  if n > 1:
    distribution = ngrams.get(prefix)
  else:
    distribution = ngrams
  if not distribution:
    return mutate_unit(language_model, n - 1, uniform_probability, prefix[1:], suffix)
  else:
    sample = sample_from_distribution(distribution, uniform_probability)
    if ' ' != sample and '\t' != sample:
      return sample
    else:
      return suffix


def mutate_line(
    language_model, probability, use_original_context, uniform_probability, delimiter, units):
  mutated_line = list(units)
  if use_original_context:
    context = list(units)
  else:
    context = mutated_line
  max_n = max([int(key) for key in language_model])
  for i in xrange(len(units)):
    if random.random() < probability:
      n = min(max_n, i + 1)
      prefix = delimiter.join(context[i - n + 1:i])
      suffix = context[i]
      mutated_line[i] = mutate_unit(language_model, n, uniform_probability, prefix, suffix)
  return delimiter.join(mutated_line)


def main():
  commands = argparse.ArgumentParser(description = 'Morphs input text into the style of another.')
  commands.add_argument('-i', '--uniform_probability', action = 'store_true',
      help = 'whether to ignore the probability values when sampling')
  commands.add_argument('-l', '--language_model', required = True, help = 'the language model')
  commands.add_argument('-p', '--probability', type = float, default = 0.5,
      help = 'the probability of mutating a unit')
  commands.add_argument('-u', '--use_original_context', action = 'store_true',
      help = 'fixes the original text as context for mutations')
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

  language_model_file = open(arguments.language_model)
  language_model = json.load(language_model_file)

  for line in sys.stdin:
    if arguments.characters:
      units = line.decode('utf8').strip()
    else:
      units = line.decode('utf8').strip().split()
    print mutate_line(language_model, arguments.probability,
        arguments.use_original_context, arguments.uniform_probability, delimiter, units)


if '__main__' == __name__:
  main()
