# ass4.py
#
# writing a library of functions: the first to determine whether a given character is a vowel; the second to determine whether a given word contains all five vowels; the third to determine if every character in a given word is a vowel; the fourth to determine if a word is a palindrome
# Usage:
#   % python ass4.py calling the routines below from the test program ass4_test.py
#
# Jeff Parker, July 2018:                   Initial skeleton
# Helen Gao, by 10:59am on 7-11-2018        Implementation

# Is the character ch a vowel?
def is_vowel(ch): #defining a function is_vowel that takes ch (any given character) as a parameter and tests whether it is one of the vowels aeiou
    if ch in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'): #if the given character is in the provided list of vowels then return true
        return True
    else: #if the given character is not in the list of vowels then return false
        return False

# Does the word have all vowels: aeiou
def has_all_vowels(word): #defining a function has_all_vowels that takes word (any given word) as a parameter and tests whether it contains all the vowels (aeiou)
    word = word.lower() #making the word lowercase so that searching for the vowels can be done with only the five lowercase vowels rather than 5 lowercase and 5 uppercase letters
    if 'a' in word: #first searching the word for the letter a
        if 'e' in word: #then searching for e
            if 'i' in word: #then searching for i
                if 'o' in word: #then searching for o
                    if 'u' in word: #then searching for u
                        return True #if the word has passed all the above tests (that is, it contains all five vowels aeiou), the function returns true
                    else: #if the function has aeio but not u it returns false
                        return False
                else: #if the function does not contain the vowel o then it returns false
                    return False
            else: #if the function does not contain the vowel i then it returns false
                return False
        else: #if the function does not contain the vowel e then it returns false
            return False
    else: #if the function does not contain the vowel a then it returns false
        return False

# Is every character in the word a vowel?
def is_all_vowels(word): #defining a function is_all_vowels that takes word (any given word) as a parameter and tests whether every character in word is a vowel
    word = word.lower() #making the word lowercase so that only the five lowercase vowels need to be stripped, rather than 5 lowercase and 5 uppercase letters
    word = word.strip('a') #removing every instance of the letter a from the word
    word = word.strip('e') #removing every instance of the letter e from the word
    word = word.strip('i') #removing every instance of the letter i from the word
    word = word.strip('o') #removing every instance of the letter o from the word
    word = word.strip('u') #removing every instance of the letter u from the word
    if len(word) == 0: #if the word was made up entirely of vowels, it should have a length of 0 now that it has been stripped of all vowels
        return True #if word does indeed have length 0 now, then the function returns true
    else: #if the word was not composed entirely of vowels, its length is longer than 0 due to the remaining consonants so the function returns false
        return False


# Is the word a palindrome, like radar or Ada?
def is_palindrome(word): #defining a function is_palindrome that takes word (any given word) as a parameter and tests whether it is a palindrome (is the same forwards and backwards)
    word = word.lower() #making the word lowercase so that capitals won't interfere with reading the word backwards and forwards
    if word[::] == word[::-1]: #if the whole word (used slicing) read forward is the same as the whole word read backwards (used slicing again but with a step of -1 so that the string would be backwards) then the word fits the definition of a palindrome so the function returns true
        return True
    else: #if the whole word is not the same read forwards and backwards then it is not a palindrome so the function returns false
        return False

#the following are tests that were included in the skeleton. i left them in the code
print('My name is', __name__)
if __name__ == '__main__':
    print(is_vowel('a'), 'a')
    print(is_vowel('z'), 'z')

    s = 'vexatious'
    print(has_all_vowels(s), s)
    s = 'vaxen'
    print(has_all_vowels(s), s)

    s = 'aie'
    print(is_all_vowels(s), s)
    s = 'kite'
    print(is_all_vowels(s), s)

    s = 'radar'
    print(is_palindrome(s), s)
    s = 'rdarr'
    print(is_palindrome(s), s)
