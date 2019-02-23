# ass7.py
#
# write three functions
# the first function returns a list of all squares from 1 to any integer n
#     (uses a list comprehension)
# the second function returns the hamming distance between two strings
#     (takes two strings and returns the integer number of differences)
#     (throws a value error exception if the strings have different lengths)
# the third function converts a string of text to an encoded string
#     (the code replaces every character with its opposite in the alphabet)
#     (whitespace and punctuation are removed)
#     (the text is written in blocks of five letters with spaces in between)
# Usage:
#     % python ass7.py
#
# Helen Gao, 7-23-2018 by 11am


# this function uses list comprehension to return a list of all squares from 1 to any integer input n
def squares(N):

    # the list of squares consists of the square of every number from 1 to n+1
    # number*number computes the square of the number
    # n+1 is used as the upper bound since python's indexing is zero-based
    lst = [number*number for number in range(1, N+1)]

    # the previous list (made with comprehensions) is returned
    return lst


# this function returns the hamming distance between two strings
# it takes two strings and returns the integer number of differences
# it throws a value error exception if the string inputs have different lengths
def hamming_distance(str1, str2):

    # if the strings have different lengths
    if len(str1) != len(str2):

        # the function raises a value error and prints an error message
        raise ValueError('str1 and str2 must be the same length')

    # making string 1 lowercase since the instructions say to ignore case
    str1 = str1.lower()

    # also making string 2 lowercase so the cases of both strings match
    str2 = str2.lower()

    # creating a count of integers that starts at 0
    # this will count how many differences are between the strings
    count = 0

    # the loop lasts for the length of string 1
    # could also use the length of string 2 since the strings are the same length
    for i in range(len(str1)):

        # if the corresponding characters in the string don't agree
        if str1[i] != str2[i]:

            # increase the count by 1
            count = count + 1

    # return the count of the hamming distance
    return count


# this function converts a string of text to an encoded string
# the code replaces every character with its opposite in the alphabet
# whitespace and punctuation are removed and the coded text is converted to five-letter blocks
def encode(str):

    # the string is converted to lowercase for later encoding
    str = str.lower()

    # importing the string module to get whitespace and punctuation characters later
    import string

    # for every whitespace character
    for ch in string.whitespace:

        # replace the whitespace character in the string with an empty string
        str = str.replace(ch, '')

    # for every punctuation character
    for ch in string.punctuation:

        # replace the punctuation character in the string with an empty string
        str = str.replace(ch, '')

    # creating a new empty string
    newstring = ''

    # creating a count of characters in the new string starting at 0
    # this will later be used to find every fifth character
    count = 0

    # for every character in the original string
    for ch in str:

        # newstring adds a new character
        # string.ascii_lowercase.index(ch) finds the index of the character in the alphabet
        # then it adds one because python has zero-based indexing and -0 doesn't exist
        # that number is turned negative so the function can index from the end of the alphabet
        # the character that is the negative index in the alphabet of the original character is added to newstring
        newstring = newstring + string.ascii_lowercase[-(string.ascii_lowercase.index(ch)+1)]

        # count increases by 1 since a character was added to newstring
        count = count + 1

        # if the count is a multiple of five
        if count % 5 == 0:

            # a space is added to newstring to create five-letter blocks
            newstring = newstring + ' '

    # strip the trailing whitespace
    # this occurs if the string has a multiple of five characters
    # added this part after someone brought it up in joe's thursday section
    newstring = newstring.strip()

    # the encoded string is returned
    return newstring
