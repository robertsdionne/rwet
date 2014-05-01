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

  def __init__(self, words, vectors):
    """TODO(robertsdionne): describe
    """
    self.words = words
    self.word_set = set(words)
    self.vectors = vectors

  def sanitize(self, word):
    return re.sub(u'[^\\w\']', u'', word.lower())

  def words_to_vector(self, words):
    """TODO(robertsdionne): describe
    """
    words = map(lambda word: self.sanitize(word), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    result = self.vectors[indices].sum(axis = 0)
    length = numpy.linalg.norm(result)
    return result / length if length > 0 else result

  def nearest_n_words_to_vector(self, n, vector):
    dot_products = numpy.dot(self.vectors, vector)
    indices = [t[0] for t in heapq.nlargest(n, enumerate(dot_products), operator.itemgetter(1))]
    return map(lambda index: self.words[index], indices)


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
  arguments = commands.parse_args()

  word_vectors = Words(read_vocabulary(arguments.vocabulary), read_vectors(arguments.vectors))

  for line in sys.stdin:
    line = line.strip().decode('utf8').split()
    nearest = word_vectors.nearest_n_words_to_vector(arguments.number,
      word_vectors.words_to_vector(line))
    print
    print (u' '.join(nearest)).encode('utf8')
    print


if '__main__' == __name__:
  main()
