"""
P.iotic

Q: 17. Write a Python program to calculate the sum of three given numbers. If the
values are equal, return three times their sum.
"""
"""
My Solution
j = float(input('Enter a value: '))
k = float(input('Enter 2nd value: '))
l = float(input('Enter last value: '))

if j==k and k==l:
    sum=3*(j+k+l)
    print('Sum: ',sum)
else:
    print('Sum: ',(j+k+l))
"""

"""
strange enough I kind of understand whats going on with def, you doing calculations
that makes the program short.
"""

def sum_thrice(x, y,z):

    sum = x + y + z

    if x==y==z:
        sum = sum*3
    return sum
x = float(input('Enter a value(1st): '))
y = float(input('Enter a value(2nd): '))
z = float(input('Enter a value(3rd): '))
print(sum_thrice(x, y, z))
