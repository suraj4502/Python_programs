"""
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams of each other, as are "anagram" and "nag a ram".
"""

def anagram(s1,s2):
    return sorted(s1)== sorted(s2)




print(sorted('listen'))
print(sorted('silent'))
print(anagram('listen','silent'))