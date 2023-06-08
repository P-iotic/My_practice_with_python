"""
P.iotic

Q: Write a Python program to test whether a passed letter is a vowel or not.

vowels are a,e,i,o,u

I have an idea of what def, how t=the variable and sum is initialated but still
not found when it comes to linking it to the answer.
Just saw that in print, I can create a input to test whether it is or isn't a vowel
so me understanding it is that is_vowel is tested against all_vowels, to see
if it contains any of the char values mentioned there.
"""

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel(input('Enter a letter to test: ')))
print(is_vowel('e'))
