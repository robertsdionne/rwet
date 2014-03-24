#!/usr/bin/env python

import re
import sys


def remove_comments(line):
  line = re.sub('{.*?}', '', line)
  line = re.sub('\\*', '', line)
  line = re.sub('!', ' ', line)
  line = re.sub('%', ' ', line)
  line = re.sub('-', ' ', line)
  line = re.sub('=', ' ', line)
  line = re.sub('\\.', ' ', line)
  line = re.sub(',', ' ', line)
  return line


def parse_line(line):
  match = re.match('<(.*)\.(.*)\.(.*);(.*)>\s+(.*)', line)
  if match:
    return (match.group(1),
      match.group(2), match.group(3), match.group(4), remove_comments(match.group(5)))
  else:
    return None, None, None, None, None


def main():
  lines = sys.stdin.readlines()
  processed_lines = list()
  for line in lines:
    line = line.strip()
    if '#' == line[0]:
      continue
    page_locator, unit_locator, line_number, transcriber_code, line = parse_line(line)
    if 'H' == transcriber_code and line:
      processed_lines.append(line)
  output = '\n'.join(processed_lines)
# cleaned_output = re.sub('\s+', '\n', output)
  print output


if '__main__' == __name__:
  main()
