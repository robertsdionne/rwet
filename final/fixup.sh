for item in $(ls reading*); do
  ./distance3.py --vectors vectors_big.dat --vocabulary vocabulary_big.txt --number 100 --probability 0.1 < $item > $item.html
done
