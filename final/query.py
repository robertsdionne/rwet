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
  """A word vector database.
  """

  def __init__(self, words, vectors):
    """Saves the words and word vectors.
    """
    self.words = words
    self.word_set = set(words)
    self.vectors = vectors

  def sanitize(self, word):
    """Strips neighboring and intermeidate punctuation characters and turns the word to lowercase.
    """
    return re.sub(u'[^\\w\']', u'', word.lower())

  def words_to_vector(self, words):
    """Translates words into their word vectors, sums them and returns the normalized result.
    """
    words = map(lambda word: self.sanitize(word), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    result = self.vectors[indices].sum(axis = 0)
    length = numpy.linalg.norm(result)
    return result / length if length > 0 else result

  def nearest_n_words_to_vector(self, n, vector):
    """Queries for the n words with the most similar word vectors to vector using the dot product.
    """
    dot_products = numpy.dot(self.vectors, vector)
    indices = [t[0] for t in heapq.nlargest(n, enumerate(dot_products), operator.itemgetter(1))]
    return map(lambda index: self.words[index], indices)


def read_vocabulary(filename):
  """Reads a vocabulary text file, with one word per line, and returns the words as a list.
  """
  result = list()
  with open(filename) as file:
    for line in file:
      result.append(line.strip().decode('utf8'))
  return result


def read_vectors(filename):
  """Reads a numpy 2d array file and returns the array.
  """
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

    # strip and decode the line with utf8
    line = line.strip().decode('utf8').split()

    # find the nearest word to the sum of the word vectors of each word in the line
    nearest = word_vectors.nearest_n_words_to_vector(arguments.number,
      word_vectors.words_to_vector(line))
    print
    print (u' '.join(nearest)).encode('utf8')
    print


if '__main__' == __name__:
  main()
