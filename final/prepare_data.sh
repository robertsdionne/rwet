#/usr/bin/env bash

mkdir -p temp

if [ ! -e vectors.bin ]; then
  svn checkout http://word2vec.googlecode.com/svn/trunk/ temp/word2vec
  cd temp/word2vec
  head -n6 demo-word.sh | bash
  cd ../..
fi

./prepare_data.py --input temp/word2vec/vectors.bin \
    --vocabulary vocabulary.txt --vectors vectors.dat
