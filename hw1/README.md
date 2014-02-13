# RWET Homework #1

## ngram.py

```
$ ./ngram.py --help
usage: ngram.py [-h] [-n NUMBER] (-c | -t)

Extracts n-grams from standard input.

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        the number, n, of units in the n-grams
  -c, --characters      sets the unit to characters
  -t, --tokens          sets the unit to tokens
```

## hw1.py

```
$ ./hw1.py --help
usage: hw1.py [-h] [-i] -l LANGUAGE_MODEL [-p PROBABILITY] [-u] (-c | -t)

Morphs input text into the style of another.

optional arguments:
  -h, --help            show this help message and exit
  -i, --uniform_probability
                        whether to ignore the probability values when sampling
  -l LANGUAGE_MODEL, --language_model LANGUAGE_MODEL
                        the language model
  -p PROBABILITY, --probability PROBABILITY
                        the probability of mutating a unit
  -u, --use_original_context
                        fixes the original text as context for mutations
  -c, --characters      sets the unit to characters
  -t, --tokens          sets the unit to tokens
```
