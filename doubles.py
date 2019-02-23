# doubles.py
#
# write a program that produces a sorted list of word pairs where both words are in the word list
# the first word has a double letter and the second word is obtained from the first by removing a set of double letters.
# Usage:
#     % python doubles.py sys.argv[1] (provided that sys.argv[1] is a text file in the same directory as doubles.py)
#
# Helen Gao, 7-18-2018 by 11am


# import the sys library so that python can run command line arguments
import sys

# creating an empty dictionary called file
# this will later store all the words in sys.argv[1] so that they can be quickly searched
file = {}

# creating an empty list called lst1
# this will later store all the words that have double letters
lst1 = []

# creating an empty list called lst1
# this will later store all the words with removed double letters
lst2 = []

# creating an empty list called final
# this will contain the final list of word pairs
final = []

# if two arguments are not provided
# the program will print the proper usage rather than displaying an error message
if len(sys.argv) != 2:

    # print the proper usage
    print('Usage: python', sys.argv[0], "<filename>")

# if the arguments are provided properly
else:

    # try to do the following
    try:

        # opens the file sys.argv[1] for reading as words for trimming
        with open(sys.argv[1], "r") as words:

            # creating a variable n that starts at -1
            # this will be used later as a counter
            n = -1

            # for every line in the file or words
            for line in words:

                # the line is stripped of whitespace so that it only contains characters
                line = line.strip()

                # this creates an entry in the dictionary
                # line is the key and n+1 is the value
                # this way the dictionary matches words in the file to their corresponding positions in the file
                # the positions don't really matter in the end though
                # this was really just to get all the words in a dictionary so they could be easily searched
                file[line] = n + 1

                # the counter n increases by 1 so the loop can start over
                n = n + 1

            # opens the file sys.argv[1] for reading as words for trimming
            with open(sys.argv[1], "r") as words:

                # for every word in the file of words
                for word in words:

                    # the word is stripped of whitespace so that it only contains characters
                    word = word.strip()

                    # a new list called lst is created
                    # the first item in lst is the first character of word
                    lst = [word[0]]

                    # this for loop repeats from the second character of the word until the end of the word
                    # it will fill lst1 with the words containing double letters
                    # it will fill lst2 with the words with double letters removed
                    for i in range (1, len(word)):

                        # if the character at position i is in the list
                        # this means that there is a double letter
                        if word[i] in lst:

                            # newword is created by slicing word
                            # by slicing word at (i-1) and (i+1) the new word will not have the double letter that is word[i]
                            newword = word[:(i-1)] + word[(i+1):]

                            # the new word is added to lst2
                            # this way the positions of word and newword match up in the two lists
                            lst2.append(newword)

                            # the original word is added to lst1
                            # this way the positions of word and newword match up in the two lists
                            lst1.append(word)

                        # if the character at position i is not in the list
                        # this means that there is no double letter
                        else:

                            # the last character in the list is popped so that the list is empty again
                            lst.pop()

                            # the current character at word[i] is added to the list
                            # this way when the loop is repeated the current character will be compared to for double letters
                            lst.append(word[i])

        # this for loop repeats for the length of lst2
        # it will fill final with the appropriate word pairs
        for i in range(len(lst2)):

            # if the word at position i of lst2 is in the dictionary of words
            if lst2[i] in file:

                # the word qualifies as part of a word pair
                # a list containing the words at position i of both lst1 and lst2 is added to final
                final.append([lst1[i], lst2[i]])

        # the program prints the length of the final list of word pairs
        print(len(final))

        # the program prints the first ten word pairs from the final list
        print(final[:10])

    # in the case of a FileNotFound error
    except FileNotFoundError:

        # print an error message saying that the file was not found
        print('File', sys.argv[1], 'was not found')

    # in the case of another error
    except:

        # print an error message saying that the program could not read the file
        print('Could not read the file')