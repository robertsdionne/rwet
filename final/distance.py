#!/usr/bin/env python

import argparse
import heapq
import json
import numpy
import operator
import random
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
    if word not in self.word_set:
      return numpy.zeros(self.vectors.shape[1])
    index = self.words.index(word)
    return self.vectors[index]

  def words_to_vectors(self, words):
    """TODO(robertsdionne): describe
    """
    words = map(lambda word: word.lower(), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    return self.vectors[indices]

  def words_to_vector(self, words):
    """TODO(robertsdionne): describe
    """
    words = map(lambda word: word.lower(), words)
    indices = [self.words.index(word) for word in words if word in self.word_set]
    result = self.vectors[indices].sum(axis = 0)
    return result / numpy.linalg.norm(result)

  def nearest_n_words_to_vector(self, n, vector):
    dot_products = numpy.dot(self.vectors, vector)
    indices = [t[0] for t in heapq.nlargest(n, enumerate(dot_products), operator.itemgetter(1))]
    return map(lambda index: self.words[index], indices)

  def nearest_n_words_to_word(self, n, word):
    if word.lower() not in self.word_set:
      return [word]
    return self.nearest_n_words_to_vector(n, self.word_to_vector(word))

  def nearest_n_words_to_words(self, n, original_words):
    stop_words = set(map(lambda word: word.lower(), original_words)) - self.word_set
    words = filter(lambda word: word.lower() in self.word_set, original_words)
    vectors = self.words_to_vectors(words)
    dot_products = numpy.dot(self.vectors, vectors.T)
    result = list()
    i = 0
    for original_word in original_words:
      entry = dict()
      entry['original_word'] = [original_word]
      if original_word.lower() in stop_words:
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


def choose(choices):
  index = min(numpy.random.geometric(0.3) - 1, len(choices) - 1)
  return choices[index]


def main():
  commands = argparse.ArgumentParser(description = 'Find the nearest words.')
  commands.add_argument('--number', type = int, default = 10, help = 'the number of similar words')
  commands.add_argument('--vocabulary', required = True, help = 'the input vocabulary text file')
  commands.add_argument('--vectors', required = True, help = 'the input numpy vector binary file')
  arguments = commands.parse_args()

  word_vectors = Words(read_vocabulary(arguments.vocabulary), read_vectors(arguments.vectors))

  # the cat in the hat
  # ate too much today

  line0 = sys.stdin.readline().strip().decode('utf8').split()
  line1 = sys.stdin.readline().strip().decode('utf8').split()

  print '\t',
  for word0 in line0:
    print word0,
  for word1 in line1:
    print
    print '%s: ' % word1,
    for word0 in line0:
      print word0, word1
      # vector0 = word_vectors.word_to_vector(word0)
      # vector1 = word_vectors.word_to_vector(word1)
      # vector01 = vector0 - vector1
      # vector01 = vector01 / numpy.linalg.norm(vector01)
      print choose(word_vectors.nearest_n_words_to_vector(arguments.number,
          word_vectors.words_to_vector([word0, word1]))),

  # for line in sys.stdin:
  #   line = line.strip().decode('utf8')
  #   words = line.split()
  #   print json.dumps(word_vectors.nearest_n_words_to_words(arguments.number, words))


if '__main__' == __name__:
  main()
