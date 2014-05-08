# RWET Midterm Project

Scripts:
* setup.sh: creates a virtualenv environment and installs the editdistance module
* run.sh: activates the virtualenv environment, preprocesses texts and generates poems.

Four programs:
* [distance.py](https://github.com/robertsdionne/rwet/tree/master/midterm#cleanup_textpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example)
* [pair.py](https://github.com/robertsdionne/rwet/tree/master/midterm#cmudict_to_jsonpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example-1)
* [prepare_data.py](https://github.com/robertsdionne/rwet/tree/master/midterm#process_voynichpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example-2)
* [query.py](https://github.com/robertsdionne/rwet/tree/master/midterm#translatepy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example-3)
* [sentences.py](https://github.com/robertsdionne/rwet/tree/master/midterm#translatepy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#translatepy)

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

Cmudict_to_json.py reads a cmudict specification from standard for word pronunciations from standard
input and outputs equivalent JSON to standard output.

```bash
$ ./pair.py --help
usage: pair.py [-h]

Chooses two neighboring non-empty lines at random.

optional arguments:
  -h, --help  show this help message and exit
```

### Example

```bash
$ ./cmudict_to_json.py 
;;; this is a comment
WHATEVER W HH AE0 T EH1 V ER0
```
```json
{
  "whatever": [
    [
      "W", 
      "HH", 
      "AE0", 
      "T", 
      "EH1", 
      "V", 
      "ER0"
    ]
  ]
}
```

## prepare_data.py

Process_voynich.py reads a Voynich manuscript transcription from standard input and extracts one
transcription for each line to print to standard output, translating all special markers into
spaces.

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
$ ./process_voynich.py 
<f1r.P1.1;H>       fachys.ykal.ar.ataiin.shol.shory.cth!res.y.kor.sholdy!-
<f1r.P1.1;C>       fachys.ykal.ar.ataiin.shol.shory.cthorys.y.kor.sholdy!-
#
<f1r.P1.2;H>       sory.ckhar.o!r.y.kair.chtaiin.shar.are.cthar.cthar.dan!-
<f1r.P1.2;C>       sory.ckhar.o.r.y.kain.shtaiin.shar.ar*.cthar.cthar.dan!-
```
```bash
fachys ykal ar ataiin shol shory cth res y kor sholdy  
sory ckhar o r y kair chtaiin shar are cthar cthar dan
```

## translate.py

Translate.py reads from standard input an ancient untranslated manuscript and prints to standard
output a rhythmically plausible translation into English based on syllabic analysis. In addition to
the ancient manuscript, the program reads a dictionary of pronunciations from the --dictionary
argument and a source text providing possible translations from the --source argument. The output
may be either text or HTML formatted.

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
$ ./translate.py --dictionary temp/cmudict07a.json --source temp/odyssey.txt
fachys ykal ar ataiin shol shory cth res y kor sholdy  
sory ckhar o r y kair chtaiin shar are cthar cthar dan
```
```bash
fachys ykal ar ataiin shol shory cth res y kor sholdy
ULYSSES ORDERED THEM ABOUT AND MADE THEM DO THEIR WORK QUICKLY, (10)

sory ckhar o r y kair chtaiin shar are cthar cthar dan
AND THE BOWLS IN WHICH HE WAS MIXING WINE FELL FROM HIS HANDS, (6)
```

## sentences.py

```bash
$ ./sentences.py --help
usage: sentences.py [-h]

Prints the sentences in the text on standard input.

optional arguments:
  -h, --help  show this help message and exit
```
