#! /usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='makes anagrams from letters')
parser.add_argument('letters', nargs=1, metavar='letters', help='The letters to anagram.')
parser.add_argument('--use-all', help='Whether the anagrams have to use all the letters', action='store_true')

args = parser.parse_args()

def onlycontains(word, letters, lettercount):
    otherletters = False

    otherlettercount = {}
    
    for letter in word:
        if letter not in letters:
            otherletters = True
            break

        if letter in otherlettercount:
            otherlettercount[letter] += 1
        else:
            otherlettercount[letter] = 1

    for letter in otherlettercount:
        if otherlettercount[letter] > lettercount[letter]:
            otherletters = True
            break
    
    return not otherletters

def makewordlist(letters, max_length, lettercount):
    words = []
    with open('wordlist.txt', 'r') as wordlistfile:
        for word in wordlistfile:
            word = word.strip('\r\n')
            if len(word) <= max_length and onlycontains(word, letters, lettercount):
                words.append(word)
    return words

def makeanagrams(letters, use_all):
    lettercount = {}

    for letter in letters:
        if letter in lettercount:
            lettercount[letter] += 1
        else:
            lettercount[letter] = 1

    wordlist = makewordlist(set(letters), len(letters), lettercount)

    if use_all:
        wordlist = [word for word in filter(lambda word: len(word) == len(letters), wordlist)]

    wordlist.sort(key=len)

    return wordlist

if __name__ == '__main__':
    letters = args.letters[0]
    use_all = args.use_all

    wordlist = makeanagrams(letters, use_all)
        
    print(wordlist)

    
