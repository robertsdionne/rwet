#/usr/bin/env bash

mkdir -p temp

if [ ! -e !/Downloads/GoogleNews-vectors-negative300.bin.gz ]; then
  echo 'Download GoogleNews-vectors-negative300.bin.gz from here:'
  echo 'https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing'
  exit
fi

if [ ! -e GoogleNews-vectors-negative300.bin.gz ]; then
  ln -s ~/Downloads/GoogleNews-vectors-negative300.bin.gz temp/GoogleNews-vectors-negative300.bin.gz
fi

if [ ! -e GoogleNews-vectors-negative300.bin ]; then
  gunzip -c temp/GoogleNews-vectors-negative300.bin.gz > temp/GoogleNews-vectors-negative300.bin
fi

./prepare_data.py --input temp/GoogleNews-vectors-negative300.bin \
    --vocabulary vocabulary_big.txt --vectors vectors_big.dat
