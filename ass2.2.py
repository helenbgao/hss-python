#ass2.2.py
#
#making functions that take arguments such as 'spam' to print twice and then four times
#usage: ???
#   %python ass2.2.py f (function objects), v (values)
#
#Helen Gao, 7-2-2018 by 9:59am

def do_twice(f): #part a of the assignment. function do_twice will call a function twice and print_spam prints 'spam', so do_twice(print_spam) prints spam twice
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)

def do_twice(f, v): #part b of the assignment. modified the function do_twice to take two arguments (f, for function object, and v, for value) instead of the previous one (f)
   f(v) #call function f with the value v as an argument
   f(v) #does above again so that function f is called twice

def print_twice(bruce): #part c of the assignment. copied the definition of print_twice() from page 21 of the textbook
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam') #part d of the assignment. used the versio of do_twice from part b to call print_twice as the first argument (function object) and spam as the second argument (value) to print spam four times

def do_four(f, v): #part e of the assignment. defined the function do_four that continued to use f for function object and v for value as arguments
    do_twice(f, v) #used the do_twice function so that do_four called do_twice two times, totalling four calls of the function object f
    do_twice(f, v)

#only printed spam when the instructions said to test (part a) or use (part d) a function. part a was 2 spams, and part d was 4, totalling 6 spams. didn't test do_four function because we weren't told to; wasn't really sure if we were supposed to