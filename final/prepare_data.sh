#/usr/bin/env bash

# make a temporary directory
mkdir -p temp

# if vectors.bin does not exist
if [ ! -e temp/word2vec/vectors.bin ]; then

  # checkout word2vec
  svn checkout http://word2vec.googlecode.com/svn/trunk/ temp/word2vec

  # build and train word2vec
  cd temp/word2vec
  head -n6 demo-word.sh | bash
  cd ../..
fi

# convert vectors.bin to numpy format
./prepare_data.py --input temp/word2vec/vectors.bin \
    --vocabulary vocabulary.txt --vectors vectors.dat
