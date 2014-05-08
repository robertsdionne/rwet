# RWET/final Project

Scripts:
* setup.sh: creates a virtualenv environment and installs the editdistance module
* run.sh: activates the virtualenv environment, preprocesses texts and generates poems.

Four programs:
* [distance.py](https://github.com/robertsdionne/rwet/tree/master/final#distancepy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/final#example)
* [pair.py](https://github.com/robertsdionne/rwet/tree/master/final#pairpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/final#example-1)
* [prepare_data.py](https://github.com/robertsdionne/rwet/tree/master/final#prepare_datapy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/final#example-2)
* [query.py](https://github.com/robertsdionne/rwet/tree/master/final#querypy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/final#example-3)
* [sentences.py](https://github.com/robertsdionne/rwet/tree/master/final#sentencespy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/final#example-4)

Generated poems:
* [poems](http://robertsdionne.github.io/rwet/final/)

## distance.py

Distance.py is the main program which takes as input a couplet from a source text and then blends
together each pair of words, one chosen from each line of the couplet, into a grid of new words to
make a poem. It uses word vector data from the [word2vec](https://code.google.com/p/word2vec/)
open source project to blend words together through vector addition.

```bash
$ ./distance.py --help
usage: distance.py [-h] [--number NUMBER] --vocabulary VOCABULARY --vectors
                   VECTORS [-p PROBABILITY] [--html]

Find the nearest words to sums of pairs of words from a couplet of an original
text.

optional arguments:
  -h, --help            show this help message and exit
  --number NUMBER       the number of similar words
  --vocabulary VOCABULARY
                        the input vocabulary text file
  --vectors VECTORS     the input numpy vector binary file
  -p PROBABILITY, --probability PROBABILITY
                        the probability parameter for the geometric
                        distribution for choosing words
  --html                whether to output html
```

### Example

```bash
$ cat | ./distance.py --vocabulary vocabulary.txt --vectors vectors.dat
Hello world.
Where are you?
```
```
Hello world.
Where are you?

      Hello world.
Where when when
are   meleon these
you?  yourself myself
```

## pair.py

Pair.py prints two randomly selected neighboring lines from the input file.

```bash
$ ./pair.py --help
usage: pair.py [-h]

Chooses two neighboring non-empty lines at random.

optional arguments:
  -h, --help  show this help message and exit
```

### Example

```bash
$ cat | ./pair.py 
One.
Two.
Three.
Four.
```
```
Three.
Four.
```

## prepare_data.py

Prepare_data.py reads in a word2vec vector database and outputs a text file representing the
vocabulary of the database with one word per line. It also outputs a numpy 2d array that stores the
vectors representing each word.

```bash
$ ./prepare_data.py --help
usage: prepare_data.py [-h] --input INPUT --vocabulary VOCABULARY --vectors
                       VECTORS

Converts word2vec data to a vocabulary text file and a numpy vector binary
file.

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         the word2vec data file
  --vocabulary VOCABULARY
                        the output vocabulary text file
  --vectors VECTORS     the output numpy vector binary file
```

### Example

```bash
$ ./prepare_data.py --input vectors.bin --vocabulary vocabulary.txt --vectors vectors.dat
```

## query.py

Query.py returns the words that most closely match the sum of the vectors of the words on each
input line.

```bash
$ ./query.py --help
usage: query.py [-h] [--number NUMBER] --vocabulary VOCABULARY --vectors
                VECTORS

Find the nearest words.

optional arguments:
  -h, --help            show this help message and exit
  --number NUMBER       the number of similar words
  --vocabulary VOCABULARY
                        the input vocabulary text file
  --vectors VECTORS     the input numpy vector binary file
```

### Example

```bash
$ ./query.py --vectors vectors.dat --vocabulary vocabulary.txt
red fruit
```
```
red fruit flowers yellow white green dried purple colored chocolate
```

## sentences.py

Sentences.py reads in a file and outputs each sentence from the file in order using TextBlob.

```bash
$ ./sentences.py --help
usage: sentences.py [-h]

Prints the sentences in the text on standard input.

optional arguments:
  -h, --help  show this help message and exit
```

### Example

```bash
$ cat | ./sentences.py
I am going to the store. Would you like to come with me? Okay.
```
```
I am going to the store.
Would you like to come with me?
Okay.
```
