# ass5.py
#
# write three programs
# the first program strips all comments from a given line
#     (taking a string and returning a string without comments, but leaving #'s if they're in quotations)
# the second program finds the longest ascending sequence in a list of numbers
#     (returns a list containing the position of the start of the sequence and the length of the sequence)
# the third program finds all words whose reverse are also in the list, in order of appearange
#     (returns a list of lowercase words that are candidates)
# Usage:
#     % python ass5.py line (a line for the strip_line function)
#     % python ass5.py lst (a list for the longest_subsequence function)
#     % python ass5.py lst (a list for the find_reversals function)
#
# Helen Gao, 7-16-2018 by 11am


# a function that strips comments from a given line
# takes a string and returns a string
# removes all comments while leaving #'s in the strings
# went to joe's thursday section where we all worked on/discussed this strip_line function
def strip_line(line):

    # the first character in a line won't be a quote so the condition inquote begins as false
    inquote = False

    # the open quote starts off as a default value
    open_quote = ""

    # string will be returned later but for now it starts off empty
    string = ""

    # this for loop runs for all the characters in the given line
    for ch in line:

        # if the character is in a quote
        if inquote == True:

            # if the character is the open_quote
            if ch == open_quote:

                # the quotation must be closed now meaning that inquote becomes false
                inquote = False

                # the character can be added to the string
                string = string + ch

            # if the character does not close the quotation
            else:

                # the character can be added to the string regardless of whether it is a # since we are still in a quote
                string = string + ch

        # if the character is not inside of a quote
        else:

            # if the character is a #
            if ch == "#":

                # return only the characters before the # so that the comment is removed
                return string

            # if the character starts a quote
            elif ch == "'":

                # inquote is now true since the quotation started a quote
                inquote = True

                # open_quote stores the quotation that started the quote
                open_quote = ch

                # the character can be added to the string
                string = string + ch

            # inquote is now true since the quotation started a quote
            elif ch == '"':

                # inquote is now true since the quotation started a quote
                inquote = True

                # open_quote stores the quotation that started the quote
                open_quote = ch

                # the character can be added to the string
                string = string + ch
            # if the character is not in a quote nor a quotation nor a #
            else:

                # the character can be added to the string
                string = string + ch

    # returns the final result of the string with comments removed
    return string


# this function takes lst as an argument for a list
# it then returns a list containing the position and length of the longest subsequence
def longest_subsequence(lst):

    # if the list is empty
    if len(lst) < 1:

        # the function returns the list and its length to avoid crashing
        return [lst, len(lst)]

    # if the list contains elements
    else:

        # the longest subsequence is set to be the first item in the list
        longest = [lst[0]]

        # the current subsequence is also set to be the first item in the list
        current = [lst[0]]

        # for the numbers in the rest of the list
        for number in lst[1:]:

            # if the number is greater than the last number in the current subsequence
            # meaning that it can be added to an ascending sequence
            if number > current[-1]:

                # add the number to the current subsequence
                current.append(number)

                # if the current subsequence is longer than the longest subsequence
                if len(current) > len(longest):

                    # the longest subsequence is redefined as the current subsequence
                    longest = current

            # if the number is equal to or less than the last number in the current subsequence
            else:

                # the current subsequence starts at the number
                current = [lst[lst.index(number)]]

        # return the final result
        # use the index function to find the position in the list of the first number in the longest subsequence
        # also return the length of the longest subsequence and put the two values into a list
        return [lst.index(longest[0]), len(longest)]


# this function finds all the reversals in a given list
# it only returns the first instance of a reversal
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
    return(reversals)