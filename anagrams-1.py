# anagrams.py
#
# a program that finds all the words in a text file for sets of anagrams and prints the 10 largest sets
# this algorithm runs in under two seconds
# Usage:
#     % python anagrams.py sys.argv[1] (provided that sys.argv[1] is a text file in the same directory as anagrams.py)
#
# Helen Gao, 8-6-2018 by 11am
# note: went to joe's thursday section where we all discussed and worked on this assignment


# importing the system library so that python can run on the command line
import sys

# creating an empty dictionary
# this will later hold all the words in the text file
words = {}

# creating an empty dictionary
# this will later hold all the anagrams
anagrams = {}

# creating an empty list
# this will later hold all the anagrams and the numbers
results = []

# the program opens sys.argv[1] for reading as file
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

    # the variable key is set to the alphabetically sorted version of the word
    # the sorted function returns a list
    # that list is joined with empty strings to make the word a string
    key = ''.join(sorted(word))

    # if the key is already in the dictionary of anagrams
    if key in anagrams:

        # the word is appended as a value for the sorted key
        anagrams[key].append(word)

    # if the key is not already in the dictionary of anagrams
    else:

        # the key becomes a key in the dictionary
        # the value becomes a list with the word as the first item
        anagrams[key] = [word]

# for every key in the dictionary of anagrams
for key in anagrams:

    # if there are 2 or more items in the list
    # meaning that the words are anagrams
    if len(anagrams[key]) >= 2:

        # the length of the list and the list itself are appended to the list of results as a tuple
        results.append([len(anagrams[key]), anagrams[key]])

# the sort function sorts the list in reverse numerical order so that lists with more anagrams are at the beginning
results.sort(reverse = True)

# print the first ten items in the final list
print(results[:10])
