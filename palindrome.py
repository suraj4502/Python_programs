''' A palindrome is a word, phrase, number, or other sequence of characters which reads
    the same backward as forward. For example, "racecar" and "level" are palindromes,
    while "hello" and "world" are not. '''


def is_palindrome(s):
    s =s.lower() # converting to lowercase
    s = ''.join(c for c in s if c.isalnum()) # Remove all non-alphanumeric characters
    if s == s[::-1] :
        print("The given string is a palindrome.")
    else :
        print("The given word is not a palindrome.")


# is_palindrome('racecar')


# c='my0string'
# print(c.isalnum())
