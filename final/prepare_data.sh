#/usr/bin/env bash

if [ ! -e GoogleNews-vectors-negative300.bin.gz ]; then
  # curl TODO(robertsdionne): figure out correct URL
  ln -s ~/Downloads/GoogleNews-vectors-negative300.bin.gz GoogleNews-vectors-negative300.bin.gz
fi

if [ ! -e GoogleNews-vectors-negative300.bin ]; then
  gunzip -c GoogleNews-vectors-negative300.bin.gz > GoogleNews-vectors-negative300.bin
fi

# ./prepare_data.py --input GoogleNews-vectors-negative300.bin \
#     --vocabulary vocabulary_big.txt --vectors vectors_big.dat

./prepare_data.py --input vectors.bin --vocabulary vocabulary.txt --vectors vectors.dat
