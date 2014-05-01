#!/usr/bin/env python

import argparse
import bisect
import json
import random
import sys


class MarkovMutator(object):
  """MarkovMutators mutate a sequence of units using a collection of n-gram statistics.
  """

  def __init__(self,
      delimiter, language_model_filename, probability, uniform_probability, use_original_context):
    self.delimiter = delimiter
    self.language_model = dict()
    self.language_model_filename = language_model_filename
    self.probability = probability
    self.uniform_probability = uniform_probability
    self.use_original_context = use_original_context

  def accumulate(self, iterable):
      """Return running totals.

      For example,
        accumulate([1, 2, 3, 4, 5]) --> [1, 3, 6, 10, 15].

      Implementation is from http://docs.python.org/3.2/library/itertools.html#itertools.accumulate.
      """
      it = iter(iterable)
      total = next(it)
      yield total
      for element in it:
          total = total + element
          yield total

  def mutate_line(self, units):
    """Mutates a line composed of units by, with probability self.probability, changing a letter to
    better match the n-gram statistics from the language model.
    """
    mutated_line = list(units)
    if self.use_original_context:
      context = list(units)
    else:
      context = mutated_line
    max_n = max([int(key) for key in self.language_model])
    for i in xrange(len(units)):
      if random.random() < self.probability:
        n = min(max_n, i + 1)
        prefix = self.delimiter.join(context[i - n + 1:i])
        suffix = context[i]
        mutated_line[i] = self.mutate_unit(n, prefix, suffix)
    return self.delimiter.join(mutated_line)

  def mutate_unit(self, n, prefix, suffix):
    """Mutates a given unit.
    """
    if u' ' == suffix or u'\t' == suffix:
      return suffix
    ngrams = self.language_model[str(n)]
    if n > 1:
      distribution = ngrams.get(prefix)
    else:
      distribution = ngrams
    if not distribution:
      return self.mutate_unit(n - 1, prefix[1:], suffix)
    else:
      sample = self.sample_from_distribution(distribution)
      if u' ' != sample and u'\t' != sample:
        return sample
      else:
        return suffix

  def prepare(self):
    """Loads the language model file into a Python dictionary.
    """
    with open(self.language_model_filename) as language_model_file:
      self.language_model = json.load(language_model_file)

  def sample_from_distribution(self, distribution):
    """Sample a value from a dictionary representing probabilities of values.
    """
    units, probabilities = zip(*distribution.iteritems())
    if self.uniform_probability:
      probabilities = [1.0 / len(probabilities) for p in probabilities]
    cumulative_probabilities = list(self.accumulate(probabilities))
    index = bisect.bisect_left(cumulative_probabilities, random.random())
    return units[index]

  def tokenize(self, text):
    """Tokenize a line of text.
    """
    return text.split()


class MarkovCharacterMutator(MarkovMutator):
  """A MarkovMutator that mutates a sequence of characters using n-gram statistics on characters.
  """
  
  def __init__(self,
      language_model_filename, probability, uniform_probability, use_original_context):
    super(MarkovCharacterMutator, self).__init__(
        u'', language_model_filename, probability, uniform_probability, use_original_context)

  def feed(self, text):
    """Prints a mutated sequence of characters.
    """
    return self.mutate_line(text)


class MarkovTokenMutator(MarkovMutator):
  """A MarkovMutator that mutates a sequence of tokens using n-gram statistics on tokens.
  """

  def __init__(self,
      language_model_filename, probability, uniform_probability, use_original_context):
    super(MarkovCharacterMutator, self).__init__(
        u' ', language_model_filename, probability, uniform_probability, use_original_context)

  def feed(self, text):
    """Prints a mutated sequence of tokens.
    """
    return self.mutate_line(self.tokenize(text))


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
    mutator = MarkovCharacterMutator(arguments.language_model,
        arguments.probability, arguments.uniform_probability, arguments.use_original_context)
  else:
    mutator = MarkovTokenMutator(arguments.language_model,
        arguments.probability, arguments.uniform_probability, arguments.use_original_context)

  mutator.prepare()

  for line in sys.stdin:
    print mutator.feed(line.decode('utf8').strip()).encode('utf8')


if '__main__' == __name__:
  main()
