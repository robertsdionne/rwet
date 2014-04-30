#!/usr/bin/env python

import argparse
import heapq
import json
import numpy
import operator
import random
import re
import sklearn.preprocessing
import sys


class Words(object):
  """TODO(robertsdionne): describe
  """

  def __init__(self, multiply, probability, uniform, words, vectors):
    """TODO(robertsdionne): describe
    """
    self.multiply = multiply
    self.probability = probability
    self.uniform = uniform
    self.words = words
    self.word_set = set(words)
    self.vectors = vectors

  def sanitize(self, word):
    return re.sub('[^\\w\']', '', word.lower())

  def choose(self, choices):
    # if self.uniform:
    #   return random.choice(choices)
    # else:
    index = min(numpy.random.geometric(self.probability) - 1, len(choices) - 1)
    return choices[index]

  def word_to_vector(self, word):
    """TODO(robertsdionne): describe
    """
    word = self.sanitize(word)
    if word not in self.word_set:
      return numpy.zeros(self.vectors.shape[1])
    index = self.words.index(word)
    return self.vectors[index]

  def words_to_vectors(self, words):
    """TODO(robertsdionne): describe
    """
    words = map(lambda word: self.sanitize(word), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    return self.vectors[indices]

  def words_to_vector(self, words):
    """TODO(robertsdionne): describe
    """
    words = map(lambda word: self.sanitize(word), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    if self.multiply:
      result = self.vectors[indices].prod(axis = 0)
    else:
      result = self.vectors[indices].sum(axis = 0)
    length = numpy.linalg.norm(result)
    return result / length if length > 0 else result

  def nearest_n_words_to_vector(self, n, vector):
    dot_products = numpy.dot(self.vectors, vector)
    indices = [t[0] for t in heapq.nlargest(n, enumerate(dot_products), operator.itemgetter(1))]
    return map(lambda index: self.words[index], indices)

  def nearest_n_words_to_word(self, n, word):
    if self.sanitize(word) not in self.word_set:
      return [word]
    return self.nearest_n_words_to_vector(n, self.word_to_vector(word))

  def nearest_n_words_to_words(self, n, original_words):
    stop_words = set(map(lambda word: self.sanitize(word), original_words)) - self.word_set
    words = filter(lambda word: self.sanitize(word) in self.word_set, original_words)
    vectors = self.words_to_vectors(words)
    dot_products = numpy.dot(self.vectors, vectors.T)
    result = list()
    i = 0
    for original_word in original_words:
      entry = dict()
      entry['original_word'] = [original_word]
      if self.sanitize(original_word) in stop_words:
        entry['alternate_words'] = [original_word]
      else:
        indices = [t[0] for t in heapq.nlargest(
            n, enumerate(dot_products[:, i]), operator.itemgetter(1))]
        entry['alternate_words'] = map(lambda index: self.words[index], indices)
        i += 1
      result.append(entry)
    return result


def read_vocabulary(filename):
  result = list()
  with open(filename) as file:
    for line in file:
      result.append(line.strip().decode('utf8'))
  return result


def read_vectors(filename):
  with open(filename) as file:
    vectors = numpy.load(file)
  return vectors


def main():
  commands = argparse.ArgumentParser(description = 'Find the nearest words.')
  commands.add_argument('--number', type = int, default = 10, help = 'the number of similar words')
  commands.add_argument('--vocabulary', required = True, help = 'the input vocabulary text file')
  commands.add_argument('--vectors', required = True, help = 'the input numpy vector binary file')
  commands.add_argument('-p', '--probability', type = float, default = 0.3,
      help = 'the probability parameter for the geometric distribution for choosing words')
  commands.add_argument('--multiply', action = 'store_true', help = 'whether to multiply vectors')
  commands.add_argument('--uniform', action = 'store_true', help = 'whether to sample uniformly')
  arguments = commands.parse_args()

  word_vectors = Words(arguments.multiply, arguments.probability, arguments.uniform,
      read_vocabulary(arguments.vocabulary), read_vectors(arguments.vectors))

  line0 = sys.stdin.readline().strip().decode('utf8').split()
  line1 = sys.stdin.readline().strip().decode('utf8').split()

  print ' '.join(line0)
  print ' '.join(line1)
  print

  print '\t',
  for word0 in line0:
    print word0,
  for word1 in line1:
    print
    print '%s\t' % word1,
    for word0 in line0:
      print word_vectors.choose(word_vectors.nearest_n_words_to_vector(arguments.number,
          word_vectors.words_to_vector([word0, word1]))[2:]),

  # for line in sys.stdin:
  #   line = line.strip().decode('utf8')
  #   words = line.split()
  #   print json.dumps(word_vectors.nearest_n_words_to_words(arguments.number, words))


if '__main__' == __name__:
  main()
