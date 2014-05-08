#/usr/bin/env bash

# make a temporary directory
mkdir -p temp

# if the .gz archive does not exist
if [ ! -e ~/Downloads/GoogleNews-vectors-negative300.bin.gz ]; then

  # prompt user to download the .gz archive
  echo 'Download GoogleNews-vectors-negative300.bin.gz from here:'
  echo 'https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing'
  exit
fi

# if the .gz archive does not exist in the temporary directory
if [ ! -e temp/GoogleNews-vectors-negative300.bin.gz ]; then

  # link the .gz archive to the temporary directory
  ln -s ~/Downloads/GoogleNews-vectors-negative300.bin.gz temp/GoogleNews-vectors-negative300.bin.gz
fi

# if the .bin vectors file does not exist
if [ ! -e GoogleNews-vectors-negative300.bin ]; then

  # unzip the .gz archive
  gunzip -c temp/GoogleNews-vectors-negative300.bin.gz > temp/GoogleNews-vectors-negative300.bin
fi

# convert the .bin file to numpy format
./prepare_data.py --input temp/GoogleNews-vectors-negative300.bin \
    --vocabulary vocabulary_big.txt --vectors vectors_big.dat
