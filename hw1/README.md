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

### Example

```
$ echo scooby dooby doo | ./ngrams.py -n 2 -c > bigrams.json
$ cat bigrams.json 
```
```json
{
  "1": {
    " ": 0.125, 
    "b": 0.125, 
    "c": 0.0625, 
    "d": 0.125, 
    "o": 0.375, 
    "s": 0.0625, 
    "y": 0.125
  }, 
  "2": {
    " ": {
      "d": 1.0
    }, 
    "b": {
      "y": 1.0
    }, 
    "c": {
      "o": 1.0
    }, 
    "d": {
      "o": 1.0
    }, 
    "o": {
      "b": 0.4, 
      "o": 0.6
    }, 
    "s": {
      "c": 1.0
    }, 
    "y": {
      " ": 1.0
    }
  }
}
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

### Example

```
$ echo whoa, who are you to judge me? what mood! | ./hw1.py -l bigrams.json -c > reading.txt
$ cat reading.txt
woby, wby aoe dou to jucgy mec dhay moob!
```
