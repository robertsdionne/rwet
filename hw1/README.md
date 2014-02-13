# RWET Homework #1

Two programs:
* [ngram.py](https://github.com/robertsdionne/rwet/tree/master/hw1#ngrampy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/hw1#example)
* [hw1.py](https://github.com/robertsdionne/rwet/tree/master/hw1#hw1py)
    * [example](https://github.com/robertsdionne/rwet/tree/master/hw1#example-1)

## ngram.py

Ngram.py examines standard input and prints a JSON structure to standard output that
contains n-gram statistics for the input text. The user chooses a value for n, and the program
calculates statistics for unigrams, bigrams, ..., up to n-grams. The program serves as an
intermediate step in homework #1 by enabling the user to save n-gram statistics for use with the
hw1.py script.

```bash
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

```bash
$ echo 'scooby dooby doo' | ./ngrams.py -n 2 -c > bigrams.json
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

```bash
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

```bash
$ echo 'whoa, who are you to judge me? what mood!' | ./hw1.py -l bigrams.json -c > reading.txt
$ cat reading.txt
woby, wby aoe dou to jucgy mec dhay moob!
```
