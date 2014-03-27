#!/usr/bin/env python

import argparse
import editdistance
import collections
import itertools
import json
import re
import sys


PARSE = collections.OrderedDict([
  ('ooooooooo', ['UW0']),
  ('eeee', ['IY0']),
  ('iiii', ['AY0']),
  ('eee', ['IY0']),
  ('hhh', ['HH']),
  ('iii', ['AY0']),
  ('rrr', ['R']),
  ('aa', ['AA0']),
  ('ay', ['AY0']),
  ('ch', ['CH']),
  ('dd', ['D']),
  ('ee', ['IY0']),
  ('er', ['ER0']),
  ('ey', ['EY0']),
  ('ii', ['AY0']),
  ('hh', ['HH']),
  ('ll', ['LL']),
  ('oo', ['UW0']),
  ('oy', ['OY0']),
  ('ph', ['F']),
  ('qk', ['K']),
  ('rr', ['R']),
  ('sh', ['SH']),
  ('th', ['TH']),
  ('yy', ['EY0']),
  ('a', ['AE0']),
  ('b', ['B']),
  ('c', ['S']),
  ('d', ['D']),
  ('e', ['EH0']),
  ('f', ['F']),
  ('g', ['G']),
  ('h', ['HH']),
  ('i', ['IH0']),
  ('j', ['JH']),
  ('k', ['K']),
  ('l', ['L']),
  ('m', ['M']),
  ('n', ['N']),
  ('o', ['OW0']),
  ('p', ['P']),
  ('q', ['K']),
  ('r', ['R']),
  ('s', ['S']),
  ('t', ['T']),
  ('u', ['AH']),
  ('v', ['V']),
  ('w', ['W']),
  ('x', ['K', 'S']),
  ('y', ['EY0']),
  ('z', ['Z'])
])


def chunk_word(pronunciations, word):
  word = re.sub('[^\w\']', '', word).lower()
  if pronunciations.has_key(word):
    return pronunciations[word][0]
  result = []
  chunk_found = False
  for chunk, phonemes in PARSE.iteritems():
    if word.startswith(chunk):
      result.extend(phonemes)
      word = word[len(chunk):]
      chunk_found = True
      break
  if chunk_found and word:
    result.extend(chunk_word(pronunciations, word))
  if not chunk_found:
    result.append('?')
  return result


def transform_phoneme(phoneme):
  match = re.match('.*([0-9])', phoneme)
  return 'V' if match else 'C'


def word_cadence(phonemes):
  def remove_duplicates(phoneme):
    if 'C' == phoneme:
      if remove_duplicates.previous_phoneme_was_vowel:
        remove_duplicates.previous_phoneme_was_vowel = False
        return True
      else:
        return False
    else:
      remove_duplicates.previous_phoneme_was_vowel = True
      return True
  remove_duplicates.previous_phoneme_was_vowel = True
  return ''.join(filter(remove_duplicates, map(transform_phoneme, phonemes)))


def choose(source_lines, pronunciations, target_line_cadence):
  prioritized = list()
  for line in source_lines:
    words = line.split()
    cadences = list()
    for word in words:
      cadence = word_cadence(chunk_word(pronunciations, word))
      cadences.append(cadence)
    line_cadence = ' '.join(cadences)
    edit_distance = editdistance.eval(target_line_cadence, line_cadence)
    prioritized.append((edit_distance, line, line_cadence))
  sorted_priority = min(prioritized)
  return sorted_priority[1], sorted_priority[2], sorted_priority[0]


def main():
  commands = argparse.ArgumentParser(
      description = 'Decompose words into their phonemes')
  commands.add_argument(
      '-d', '--dictionary', required = True, help = 'the pronunciation dictionary')
  commands.add_argument('--html', action = 'store_true', help = 'output to html')
  commands.add_argument('-i', '--image', help = 'the html image to precede the text')
  commands.add_argument('-s', '--source', help = 'the source text')
  commands.add_argument('--api_key', help = 'the api key')
  commands.add_argument('--api_secret', help = 'the api secret')
  commands.add_argument('--oath_access_token', help = 'the oauth access token')
  commands.add_argument('--oath_access_token_secret', help = 'the oauth access token secret')
  arguments = commands.parse_args()

  with open(arguments.dictionary) as dictionary_file:
    pronunciations = json.load(dictionary_file)

  with open(arguments.source) as source_file:
    source_lines = list()
    for line in source_file:
      line = line.strip()
      source_lines.append(line)

  if arguments.html:
    print '''
<html>
  <head>
    <meta charset="utf-8">
    <style type="text/css">
      @font-face {
        font-family: 'EVA Hand 1';
        src: url('EVA1.ttf');
      }
      @font-face {
        font-family: 'Ubuntu Mono';
        src: url('Ubuntu-M.ttf');
      }
      body {
        font-family: 'Ubuntu Mono';
      }
      div {
        padding-left: 1em;
      }
    </style>
  </head>
  <body>
    %s
    <div style="padding-left: 5em;">
''' % ('<div><img src="%s" style="width: 45em;" /></div>' % arguments.image if arguments.image else '')

  for line in sys.stdin:
    line = line.strip()
    words = line.split()
    cadences = [word_cadence(chunk_word(pronunciations, word)) for word in words]
    line_cadence = ' '.join(cadences)
    choice, choice_cadence, priority = choose(source_lines, pronunciations, line_cadence)
    line = re.sub('\\s+', ' ', line)
    choice = re.sub('\\s+', ' ', choice)
    if arguments.html:
      print '      <p>'
      print '        <span style="font-family: \'EVA Hand 1\';"><b>%s</b></span> <br />' % line
      print '        <span>%s</span> <br />' % line
      print '        <span><b>%s</b></span> <br />' % choice.upper()
      print '      </p>'
    else:
      print line
      print choice.upper(), '(%s)' % priority
      print

  if arguments.html:
    print '''
    </div>
  </body>
</html>
'''


if '__main__' == __name__:
  main()
