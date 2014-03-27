#!/usr/bin/env bash

# exit on error
set -e

source ../venv/bin/activate

echo "processing f1r"
cat data/L16+h-eva/f1r.P* | ./process_voynich.py | ./translate.py --image image/f1r.png \
    --html -d cmudict07a.json -s lightinaugust.txt > f1r.html
cat data/L16+h-eva/f1r.P* | ./process_voynich.py | ./translate.py -d cmudict07a.json \
    -s lightinaugust.txt > f1r.txt

echo "processing f39v"
cat data/L16+h-eva/f39v.P* | ./process_voynich.py | ./translate.py --image image/f39v.png \
    --html -d cmudict07a.json -s rosettastone.txt > f39v.html
cat data/L16+h-eva/f39v.P* | ./process_voynich.py | ./translate.py -d cmudict07a.json \
    -s rosettastone.txt > f39v.txt

echo "processing f81r"
cat data/L16+h-eva/f81r.P* | ./process_voynich.py | ./translate.py --image image/f81r.png \
    --html -d cmudict07a.json -s odyssey.txt > f81r.html
cat data/L16+h-eva/f81r.P* | ./process_voynich.py | ./translate.py -d cmudict07a.json \
    -s odyssey.txt > f81r.txt
