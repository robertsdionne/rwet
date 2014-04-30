#/usr/bin/env bash

mkdir -p temp

if [ ! -e GoogleNews-vectors-negative300.bin.gz ]; then
  # curl TODO(robertsdionne): figure out correct URL
  ln -s ~/Downloads/GoogleNews-vectors-negative300.bin.gz temp/GoogleNews-vectors-negative300.bin.gz
fi

if [ ! -e GoogleNews-vectors-negative300.bin ]; then
  gunzip -c temp/GoogleNews-vectors-negative300.bin.gz > temp/GoogleNews-vectors-negative300.bin
fi

./prepare_data.py --input temp/GoogleNews-vectors-negative300.bin \
    --vocabulary vocabulary_big.txt --vectors vectors_big.dat
