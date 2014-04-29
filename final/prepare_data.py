#!/usr/bin/env python

import argparse
import numpy
import sklearn.preprocessing
import struct
import sys


def read_word2vec_data(filename):
  """Reads word2vec formatted data into a list of words and a numpy 2darray.
  """
  with open(filename) as file:

    # Read the word count and vector dimension from the first line of the file.
    word_count, dimension = (long(x) for x in file.readline().split())

    # Create variables to store the data.
    words = list()
    vectors = numpy.ndarray(shape = (word_count, dimension), dtype = numpy.float32)

    # For each word, add it to the words list and add its vector to the numpy array.
    for i in xrange(word_count):
      letters = list()

      # Read the next bytes up to a space character as the next word.
      while True:
        letter = file.read(1)

        # Break at end-of-file or after reading a space character.
        if '' == letter or ' ' == letter:
          break
        letters.append(letter)

      # Save the word to the vocabulary list.
      word = ''.join(letters)
      words.append(word)

      # Read and normalize the vector before saving it to the numpy array.
      vector = numpy.ndarray(shape = (1, dimension), dtype = numpy.float32)
      vector[:] = struct.unpack('f' * dimension, file.read(4 * dimension))
      vectors[i] = sklearn.preprocessing.normalize(vector, norm = 'l2')
    return words, vectors


def write_vocabulary(vocabulary, filename):
  """Writes a list of words to a text file.
  """
  with open(filename, 'w') as file:
    for word in vocabulary:
      file.write(word.strip())
      file.write('\n')


def write_vectors(vectors, filename):
  """Writes a numpy 2darray to a binary file.
  """
  with open(filename, 'w') as file:
    numpy.save(file, vectors)


def main():
  commands = argparse.ArgumentParser(description = 'Converts word2vec data to a vocabulary text '
      'file and a numpy vector binary file.')
  commands.add_argument('--input', required = True, help = 'the word2vec data file')
  commands.add_argument('--vocabulary', required = True, help = 'the output vocabulary text file')
  commands.add_argument('--vectors', required = True, help = 'the output numpy vector binary file')
  arguments = commands.parse_args()

  vocabulary, vectors = read_word2vec_data(arguments.input)
  write_vocabulary(vocabulary, arguments.vocabulary)
  write_vectors(vectors, arguments.vectors)


if '__main__' == __name__:
  main()
