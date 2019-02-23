# palindrome.py
#
# writing a program that takes a command line argument holding the name of a text file that opens the file and prints all the palindromes
# Usage:
#   % python palindrome.py sys.argv[1] (sys.argv[1] is a text file in the same directory as palindrome.py)
#
# Helen Gao, by 10:59am on 7-11-2018
import sys #importing the sys library so that python can run command line arguments
if len(sys.argv) < 2: #this is the look before you leap concept discussed in class. if less than two arguments are provided, the program will deal with it gracefully by printing the proper usage (rather than displaying an error message)
    print('Usage: python', sys.argv[0], "<text file>") #printing the usage. sys.argv[0] refers to this program (palindrome.py)
else: #if there are two or more arguments (it is okay to have more than two arguments since the extras will be ignored) then the program will run properly
    file = open(sys.argv[1]) #the variable file opens sys.argv[1] (sys.argv[1] refers to the text file that is the argument after the sys.argv[0], the program)
    for line in file: #going through all the lines in the opened text file
        line = line.strip() #stripping the whitespace from each line so that it only contains characters
        if line[::] == line[::-1]: #if the whole word (used slicing) read forward is the same as the whole word read backwards (used slicing again but with a step of -1 so that the string would be backwards) then the word fits the definition of a palindrome so the function will print the verified palindromic line
            print(line) #print the lines that are palindromes
