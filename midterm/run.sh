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


echo "generating f1r_lightinaugust.html"
cat text/L16+h-eva/f1r.P* | ./process_voynich.py | ./translate.py --image image/f1r.png \
    --html -d temp/cmudict07a.json -s temp/lightinaugust.txt > f1r_lightinaugust.html

echo "generating f1r_lightinaugust.txt"
cat text/L16+h-eva/f1r.P* | ./process_voynich.py | ./translate.py -d temp/cmudict07a.json \
    -s temp/lightinaugust.txt > f1r_lightinaugust.txt


echo "generating f39v_rosettastone.html"
cat text/L16+h-eva/f39v.P* | ./process_voynich.py | ./translate.py --image image/f39v.png \
    --html -d temp/cmudict07a.json -s temp/rosettastone.txt > f39v_rosettastone.html

echo "generating f39v_rosettastone.txt"
cat text/L16+h-eva/f39v.P* | ./process_voynich.py | ./translate.py -d temp/cmudict07a.json \
    -s temp/rosettastone.txt > f39v_rosettastone.txt


echo "generating f81r_odyssey.html"
cat text/L16+h-eva/f81r.P* | ./process_voynich.py | ./translate.py --image image/f81r.png \
    --html -d temp/cmudict07a.json -s temp/odyssey.txt > f81r_odyssey.html

echo "generating f81r_odyssey.txt"
cat text/L16+h-eva/f81r.P* | ./process_voynich.py | ./translate.py -d temp/cmudict07a.json \
    -s temp/odyssey.txt > f81r_odyssey.txt
