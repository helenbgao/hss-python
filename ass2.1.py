#ass2.1.py
#
#function that takes string s (with less than 70 characters) as a parameter and prints it with enough leading spaces so that the last letter of the string ends up in the 70th column
#usage: ???
#   %python ass2.1.py string s
#
#Helen Gao, 7-2-2018 by 9:59am

def right_justify(s): #creating a function named right_justify with s as a parameter
    print(' '*(70-len(s))+s) #printing (70 - the length of the string s) spaces to produce enough spaces and then concatenating it with the actual string s so that the whole string is 70 characters long and the last letter of s is in the 70th column of the display. forgot to use parentheses at first. fixed it upon remembering that pemdas existed

right_justify('hello!') #test case 1

right_justify('i would like some points, please!') #test case 2

right_justify(':)') #test case 3