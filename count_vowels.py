def count_vowels(s):
    count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            count += 1
    return count

def count_vowels_1(s):
    return sum(1 for c in s if c in 'aeiouAEIOU')



print(count_vowels("mystringae"))
print(count_vowels_1("mystringae"))