#!/usr/bin/env bash

source ../venv/bin/activate
echo "processing f1r"
cat data/L16+h-eva/f1r.P* | ./process_voynich.py | ./chunk_words.py --image f1r.png \
    -html -d cmudict07a.json -s lightinaugust.txt > f1r.html
echo "processing f39v"
cat data/L16+h-eva/f39v.P* | ./process_voynich.py | ./chunk_words.py --image f39v.png \
    -html -d cmudict07a.json -s rosettastone.txt > f39v.html
echo "processing f81r"
cat data/L16+h-eva/f81r.P* | ./process_voynich.py | ./chunk_words.py --image f81r.png \
    -html -d cmudict07a.json -s odyssey.txt > f81r.html
