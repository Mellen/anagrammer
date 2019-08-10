# anagrammer

A small script for generating anagrams

wordlist.txt was downloaded from http://www.mieliestronk.com/corncob_lowercase.txt

## usage

```bash
python3 anagrammer.py [-h] [--use-all] letters
```

So for example `python3 anagrammer.py letters` will give the output

```python
['re', 'eel', 'els', 'ere', 'est', 'lee', 'let', 'see', 'set', 'tee', 'eels', 'else', 'erst', 'leer', 'lees', 'lest', 'lets', 'reel', 'rest', 'seer', 'stet', 'tees', 'test', 'tree', 'ester', 'leers', 'reels', 'reset', 'sleet', 'steel', 'steer', 'terse', 'trees', 'letter', 'retest', 'setter', 'settle', 'street', 'tester', 'letters', 'settler', 'trestle']
```

and `python3 anagrammer.py letters --use-all` will give the output

```python
['letters', 'settler', 'trestle']
```