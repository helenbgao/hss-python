# interlace.py
#
# a program that finds words that can be decomposed into two legal words by taking every other letter
# the program takes a filename for a text file on the command line
# Usage:
#     % python interlace.py sys.argv[1] (provided that sys.argv[1] is a text file in the same directory as interlace.py)
# note: went to joe's thursday section where we all wrote/discussed this program together
#
# Helen Gao, 7-30-2018 by 11am

# import the sys library so that python can run command line arguments
import sys

# creating an empty dictionary
# this will later hold all the words in the text file
words = {}

# creating an empty list
# this will later hold the triples of words
triples = []

# the program opens sys.argv[1] for reading
with open(sys.argv[1], "r") as file:

    # for every line in the file of words
    for line in file:

        # the word is stripped of whitespace so that it only contains characters
        line = line.strip()

        # the word is added as a key to the dictionary of words
        # the values for the keys are all 1 since the values don't really matter
        words[line] = 1

# for every word in the dictionary of words
for word in words:

    # first is set to the odd decomposition of the word
    # this uses slicing with a step of 2
    first = word[::2]

    # second is set to the even decomposition of the word
    # this uses slicing starting at position 1 with a step of 2
    second = word[1::2]

    # if both the first and second decomposition are valid words in the dictionary
    if first in words and second in words:

        # the original word, odd decomposition, and even decomposition are added to the list of triples as a tuple
        triples.append((word, first, second))

# the list of triples are sorted alphabetically
# this is necessary because the earlier for loop used words from the dictionary of words
# since dictionaries are unordered the words may not have stayed in alphabetical order
triples.sort()

# print the length of the list of triples
print(len(triples))

# print the first 10 word triples in the list
print(triples[:10])
