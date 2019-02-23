# ass6.py
#
# write three functions
# the first function parses an email address
#     (takes a string and returns a list of the components of the address)
#     (the first item in the list is the username)
#     (the second item in the list contains the steps needed to route the email)
# the second function determines whether a string of only parentheses consists of valid nested parentheses
#     (takes a string and returns a boolean)
# the third function determines whether a string of parentheses and other characters has valid nesting
#     (quotations and hash marks are ignored)
# Usage:
#     % python ass6.py
#
# Helen Gao, 7-18-2018 by 11am


# this function parses an email address in the form of a string and returns a list
# the list contains the username and the steps to route the email
def parse_email_address(str):

    # a new list is created by splitting the string at the @ symbol
    # this separates the username from the routing steps
    lst = str.split('@')

    # a second list is created by splitting the second component (index 1) of the earlier list
    # this list is split at the . so that the routing steps are separate
    lst2 = lst[1].split('.')

    # the second component (index 1) of the first list is replaced
    # lst2 is made backwards by using slicing (all of lst2 with a step or -1)
    lst[1] = lst2[::-1]

    # returns the final list of the parsed email address
    return lst


# this function determines whether a string of only parentheses consists of valid nested parentheses
# it takes a string of parentheses and returns a true/false boolean
def is_valid_parens(str):

    # every opening parenthesis needs a closing parenthesis and vice veresa
    # if the string is not a multiple of two that means there isn't even pairing of parentheses
    if len(str) % 2 == 1:

        # without an even number of parentheses the string cannot have valid nesting
        # thus the function returns false
        return False

    # if the string has no characters
    if len(str) == 0:

        # the function returns true
        return True

    # if the first character of the string is ) } or ]
    # meaning that it's a closing parenthesis
    # since opening parentheses must come before closing ones the first character can't be a closing parenthesis
    if str[0] in ')}]':

        # the function returns false
        return False

    # if the last character of the string is ( { or [
    # meaning that it's an opening parenthesis
    # since opening parentheses must be followed by closing ones the last character can't be an opening parenthesis
    if str[-1] in '({[':

        # the function returns false
        return False

    # creating a dictionary of matching parentheses
    # opening parentheses are keys and closing parentheses are values
    parentheses = {'(': ')', '{': '}', '[': ']'}

    # creating an empty list
    lst = []

    # for every character in the given string
    for ch in str:

        # if the character is an opening parenthesis
        if ch in '({[':

            #the opening parenthesis is added to the list
            lst.append(ch)

        # if the character isn't an opening parenthesis
        else:

            # the last character in the list is popped off
            # this returns as the variable open_parenthesis
            open_parenthesis = lst.pop()

            # if the open parenthesis doesn't match the character
            # this refers to the dictionary of matching parentheses
            if parentheses[open_parenthesis] != ch:

                # the function returns false
                # since a closing parenthesis should match the most recently opened parenthesis
                return False

    # if the final list has a length of 0
    # meaning that all parentheses matched and the last open parenthesis has been closed
    if len(lst) == 0:

        # the function returns true
        return True

    # if the final list doesn't have a length of 0
    # meaning that the open parentheses haven't been closed
    else:

        # the function returns false
        return False


# this function determines whether a string of parentheses and other characters has valid nesting
# it takes a string and returns a true/false boolean
# quotations and hash marks are ignored
# this reuses a lot of is_valid_parens
def is_valid(str):

    # the first condition of an even string has been removed
    # since with the addition of other characters there is no need for an even number of total characters

    # if the string has no characters
    if len(str) == 0:

        # the function returns true
        return True

    # if the first character of the string is ) } or ]
    # meaning that it's a closing parenthesis
    # since opening parentheses must come before closing ones the first character can't be a closing parenthesis
    if str[0] in ')}]':

        # the function returns false
        return False

    # if the last character of the string is ( { or [
    # meaning that it's an opening parenthesis
    # since opening parentheses must be followed by closing ones the last character can't be an opening parenthesis
    if str[-1] in '({[':

        # the function returns false
        return False

    # creating a dictionary of matching parentheses
    # opening parentheses are keys and closing parentheses are values
    parentheses = {'(': ')', '{': '}', '[': ']'}

    # creating an empty list
    lst = []

    # for every character in the given string
    for ch in str:

        # if the character is an opening parenthesis
        if ch in '({[':

            # the opening parenthesis is added to the list
            lst.append(ch)

        # if the character is a closing parenthesis
        elif ch in ')}]':

            # the last character in the list is popped off
            # this returns as the variable open_parenthesis
            open_parenthesis = lst.pop()

            # if the open parenthesis doesn't match the character
            # this refers to the dictionary of matching parentheses
            if parentheses[open_parenthesis] != ch:

                # the function returns false
                # since a closing parenthesis should match the most recently opened parenthesis
                return False

    # if the final list has a length of 0
    # meaning that all parentheses matched and the last open parenthesis has been closed
    if len(lst) == 0:

        # the function returns true
        return True

    # if the final list doesn't have a length of 0
    # meaning that the open parentheses haven't been closed
    else:

        # the function returns false
        return False
