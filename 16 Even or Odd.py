"""
P.iotic

Q: 21. Write a Python program that determines whether a given number
(accepted from the user) is even or odd, and prints an appropriate
message to the user.
"""

def guess_number(num, x):
    num = int(input('Enter a number: '))

    if num %2==0:
        x="Even"
        return num
    x="Odd"
    return num
print(x)
