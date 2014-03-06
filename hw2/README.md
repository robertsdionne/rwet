# RWET Homework #2

## hw2.py

Hw2.py reads a text from standard input and generates a 7 stanza poem by attempting to connect as
many lines as possible by aligning lines with matching initial and terminal characters. It then
mutates each word in a line with a given probability so that the word's initial character matches
its prior neighbor's terminal character, and its terminal character matches its next neighbor's
initial character.

```bash
$ ./hw2.py --help
usage: hw2.py [-h] [-r] [-p PROBABILITY]

Generates stanzas from piecing together lines that start with the same sound
as the ending of the previous line. Then, substitutes some words in each line
with words that match the previous word's last letter and next word's first
letter.

optional arguments:
  -h, --help            show this help message and exit
  -r, --reverse         whether to reverse the substituted words before
                        planting them within a line
  -p PROBABILITY, --probability PROBABILITY
                        the probability of substituting a word
```
