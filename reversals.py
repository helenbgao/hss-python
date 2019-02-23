# reversals.py
#
# write a program that uses the find_reversals function to find all the reversals in a file from the command line
# the function read_dictionary opens the file, reads and trims each line and places them into a list of all the words
# Usage:
#     % python reversals.py sys.argv[1] (provided that sys.argv[1] is a text file in the same directory as reversals.py)
#
# Helen Gao, 7-16-2018 by 11am


# import the sys library so that python can run command line arguments
import sys


# this function is the same as the one from ass5
# it finds all the reversals in a given list while only returning the first instance of a reversal
def find_reversals(lst):

    # make everything in the list lowercase
    lst = [char.lower() for char in lst]

    # create a new list for the reversals
    reversals = []

    # for every word in the list
    for word in lst:

        # if the reverse of the word is found in the list
        # slice the list so that the function only searches from the word itself to the end of the list
        # this way only the first instance of a word will count
        if word[::-1] in lst[lst.index(word):]:

            # add the word to the list of reversals
            reversals.append(word)

    # return the final list of reversals
    return reversals


# this function opens a file, reads and trims each line of the file, and places them into a list of all the words
def read_dictionary(filename):

    # opens the file for reading as words for trimming
    with open(filename, "r") as words:

        # creates a new list to hold the trimmed words
        lst = []

        # for every line in the file of words
        for line in words:

            # the line is stripped of whitespace so that it only contains characters
            line = line.strip()

            # the stripped line is added to the list
            lst.append(line)

    # return the final list of trimmed words
    return lst


# if two arguments are not provided, the program will print proper usage rather than displaying an error message
if len(sys.argv) != 2:

    # print the proper usage
    print('Usage: python', sys.argv[0], "<text file>")

# if the arguments are provided properly
else:

    # try to do the following
    try:

        # run find_reversals on read_dictionary on sys.argv[1]
        # so that the function finds all the reversals in the given file and calls that reversals
        reversals = find_reversals(read_dictionary(sys.argv[1]))

        # only print the first 10 reversals in sys.argv[1]
        print(reversals[:10])

    # in the case of a FileNotFound error
    except FileNotFoundError:

        # print an error message saying that the file was not found
        print('File', sys.argv[1], 'was not found')

    # in the case of another error
    except:

        # print an error message saying that the function could not read the file
        print('Could not read the file')