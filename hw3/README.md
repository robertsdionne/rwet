# RWET Homework #3

Two programs:
* [hw3.py](https://github.com/robertsdionne/rwet/tree/master/hw3#hw3py)
    * [example](https://github.com/robertsdionne/rwet/tree/master/hw3#example)
* [ngram.py](https://github.com/robertsdionne/rwet/tree/master/hw3#ngrampy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/hw3#example-1)

## hw3.py

Hw2.py reads a text from standard input and generates a text by attempting to connect as
many lines as possible by aligning lines with matching initial and terminal characters. It then
mutates each word in a line with a given probability so that the word's initial character matches
its prior neighbor's terminal character, its terminal character matches its next neighbor's
initial character and with a language model drawn from an input text.

```bash
$ ./hw3.py --help
usage: hw3.py [-h] -l LANGUAGE_MODEL [-p PROBABILITY] [-r]

Generates stanzas from piecing together lines that start with the same sound
as the ending of the previous line. Then, substitutes some words mutated with a language model
into each line with words that match the previous word's last letter and next word's first letter.

optional arguments:
  -h, --help            show this help message and exit
  -l LANGUAGE_MODEL, --language_model LANGUAGE_MODEL
                        the language model
  -p PROBABILITY, --probability PROBABILITY
                        the probability of substituting a word
  -r, --reverse         whether to reverse the substituted words before
                        planting them within a line
```

### Example

```bash
$ ./hw3.py -p 1 -l onomotopoeia5grams.json  < lightinaugust.txt | head
```
```
in neigel lying gnew with horshu until lrmm men nidh have eudoia and deffat to of field,
down.
no woman,
not th hair rewroo of place.
enemies.
She laughed,
dumping god dishes sf food da all latt the floor.
recalcitrant,
the eudoia and das student temtety-c crime epoit the e-haw ways of Yoknapatawpha County,
young.
```

## ngram.py

Ngram.py examines standard input and prints a JSON structure to standard output that
contains n-gram statistics for the input text. The user chooses a value for n, and the program
calculates statistics for unigrams, bigrams, ..., up to n-grams. The user may select whether to
gather statistics on units of characters or tokens. The program serves as an
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
