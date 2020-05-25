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

# numbergram

A small script for solving the Countdown number game

```bash
python3 numbergram.py [-h] numbers numbers numbers numbers numbers numbers [target]
```

So for example `python3 numbergram.py 75 50 100 25 6 8 243` will give the output:

```
(((((50-6)*100)/25)+75)-8) = 243.0
(((((50-6)*100)/25)-8)+75) = 243.0
(((((50-6)/25)*100)+75)-8) = 243.0
(((((50-6)/25)*100)-8)+75) = 243.0
(((((50*25)+100)-6)/8)+75) = 243.0
(((((50*25)-6)+100)/8)+75) = 243.0
(((((100*25)+50)-6)/8)-75) = 243.0
(((((100*25)-75)/50)-8)*6) = 243.0
(((((100*25)-6)+50)/8)-75) = 243.0
(((((100/50)+25)-6)*8)+75) = 243.0
(((((100/50)-6)+25)*8)+75) = 243.0
(((((25*50)+100)-6)/8)+75) = 243.0
(((((25*50)-6)+100)/8)+75) = 243.0
(((((25*100)+50)-6)/8)-75) = 243.0
(((((25*100)-75)/50)-8)*6) = 243.0
(((((25*100)-6)+50)/8)-75) = 243.0
```

If a target is ommitted then all operations between the 6 numbers using -, +, / and * will be printed.

Numbers should be between 1 and 100, and the target should be between 100 and 999 inclusive. It will try to calculate anthing you give it, but they might lay outside the rules for Countdown.