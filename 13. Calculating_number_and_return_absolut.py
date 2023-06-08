"""
P.iotic

Q: 16. Write a Python program to calculate the difference between a given number
and 17. If the number is greater than 17, return twice the absolute difference.

def...interesing there is a function from C++ that this reminds me of
"""

def difference(n):
    if n <=17:
        return 17-n
    else:
        return (n-17)*2

print(difference(22))
print(difference(14))
