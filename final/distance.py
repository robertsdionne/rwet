#!/usr/bin/env python

import argparse
import heapq
import json
import numpy
import operator
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

  def word_to_vector(self, word):
    """TODO(robertsdionne): describe
    """
    word = word.lower()
    index = self.words.index(word)
    return self.vectors[index]

  def words_to_vectors(self, words):
    """TODO(robertsdionne): describe
    """
    words = map(lambda word: word.lower(), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    return self.vectors[indices]

  def nearest_n_words_to_word(self, n, word):
    if word.lower() not in self.word_set:
      return [word]
    vector = self.word_to_vector(word)
    dot_products = numpy.dot(self.vectors, vector)
    indices = [t[0] for t in heapq.nlargest(n, enumerate(dot_products), operator.itemgetter(1))]
    return map(lambda index: self.words[index], indices)

  def nearest_n_words_to_words(self, n, words):
    stop_words = set(map(lambda word: word.lower(), words)) - self.word_set
    words = filter(lambda word: word.lower() in self.word_set, words)
    vectors = self.words_to_vectors(words)
    dot_products = numpy.dot(self.vectors, vectors.T)
    result = dict()
    for i in xrange(len(words)):
      indices = [t[0] for t in heapq.nlargest(
          n, enumerate(dot_products[:, i]), operator.itemgetter(1))]
      result[words[i]] = map(lambda index: self.words[index], indices)
    for stop_word in stop_words:
      result[stop_word] = [stop_word]
    return result


def read_vocabulary(filename):
  result = list()
  with open(filename) as file:
    for line in file:
      result.append(line.strip())
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
    line = line.strip()
    words = line.split()
    print json.dumps(word_vectors.nearest_n_words_to_words(arguments.number, words))


if '__main__' == __name__:
  main()
