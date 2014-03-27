#!/usr/bin/env bash

# exit on error
set -e

# activate virtualenv
source ../venv/bin/activate


echo "cleaning dependencies"
mkdir -p temp
./cmudict_to_json.py < text/cmudict/cmudict.0.7a > temp/cmudict07a.json
./cleanup_text.py < text/lightinaugust.txt > temp/lightinaugust.txt
./cleanup_text.py < text/rosettastone.txt > temp/rosettastone.txt
./cleanup_text.py < text/pg1727.txt > temp/odyssey.txt


echo "generating f1r.html"
cat text/L16+h-eva/f1r.P* | ./process_voynich.py | ./translate.py --image image/f1r.png \
    --html -d temp/cmudict07a.json -s temp/lightinaugust.txt > f1r.html

echo "generating f1r.txt"
cat text/L16+h-eva/f1r.P* | ./process_voynich.py | ./translate.py -d temp/cmudict07a.json \
    -s temp/lightinaugust.txt > f1r.txt


echo "generating f39v.html"
cat text/L16+h-eva/f39v.P* | ./process_voynich.py | ./translate.py --image image/f39v.png \
    --html -d temp/cmudict07a.json -s temp/rosettastone.txt > f39v.html

echo "generating f39v.txt"
cat text/L16+h-eva/f39v.P* | ./process_voynich.py | ./translate.py -d temp/cmudict07a.json \
    -s temp/rosettastone.txt > f39v.txt


echo "generating f81r.html"
cat text/L16+h-eva/f81r.P* | ./process_voynich.py | ./translate.py --image image/f81r.png \
    --html -d temp/cmudict07a.json -s temp/odyssey.txt > f81r.html

echo "generating f81r.txt"
cat text/L16+h-eva/f81r.P* | ./process_voynich.py | ./translate.py -d temp/cmudict07a.json \
    -s temp/odyssey.txt > f81r.txt
