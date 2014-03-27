# RWET Midterm Project

Four programs:
* [cleanup_text.py](https://github.com/robertsdionne/rwet/tree/master/midterm#cleanup_textpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example)
* [cmudict_to_json.py](https://github.com/robertsdionne/rwet/tree/master/midterm#cmudict_to_jsonpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example-1)
* [process_voynich.py](https://github.com/robertsdionne/rwet/tree/master/midterm#process_voynichpy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example-2)
* [translate.py](https://github.com/robertsdionne/rwet/tree/master/midterm#translatepy)
    * [example](https://github.com/robertsdionne/rwet/tree/master/midterm#example-3)

Three generated poems:
* [f1r_lightinaugust](http://robertsdionne.github.io/rwet/midterm/f1r_lightinaugust.html)
* [f39v_rosettastone](http://robertsdionne.github.io/rwet/midterm/f39v_rosettastone.html)
* [f81r_odyssey](http://robertsdionne.github.io/rwet/midterm/f81r_odyssey.html)

## cleanup_text.py

Cleanup_text.py reads a text from standard input, joins all lines together and then splits newlines
after punctuation such as period (.), exclamation (!), question (?), comma (,), dash (-), colon (:)
and semicolon (;), before printing the modified text to standard output.

```bash
$ ./cleanup_text.py --help
usage: cleanup_text.py [-h]

Cleans up a source text by splitting on punctuation instead of original lines

optional arguments:
  -h, --help  show this help message and exit
```

### Example

```bash
$ echo 'What time. Such food.' | ./cleanup_text.py
```
```
What time.
Such food.
```

## cmudict_to_json.py

Cmudict_to_json.py reads a cmudict specification from standard for word pronunciations from standard
input and outputs equivalent JSON to standard output.

```bash
$ ./cmudict_to_json.py --help
usage: cmudict_to_json.py [-h]

Converts cmudict to JSON format

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

## process_voynich.py

Process_voynich.py reads a Voynich manuscript transcription from standard input and extracts one
transcription for each line to print to standard output, translating all special markers into
spaces.

```bash
$ ./process_voynich.py --help
usage: process_voynich.py [-h]

Reads a single transcription from Voynich manuscript data files

optional arguments:
  -h, --help  show this help message and exit
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
$ ./translate.py --help
usage: translate.py [-h] -d DICTIONARY [--html] [-i IMAGE] [-s SOURCE]

Translates a manuscript into rhythmically plausible lines from source text

optional arguments:
  -h, --help            show this help message and exit
  -d DICTIONARY, --dictionary DICTIONARY
                        the pronunciation dictionary
  --html                output to html
  -i IMAGE, --image IMAGE
                        the html image to precede the text
  -s SOURCE, --source SOURCE
                        the source text
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
