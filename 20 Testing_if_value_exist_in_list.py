"""
P.iotic

Q: 25. Write a Python program that checks whether a specified value is contained
within a group of values.

"""
"""
My solution, discovered you can search  for a value inside a list by using if-
statement using in 
data =[1,5,3,8]
number = int(input('Enter a number to be tested: '))

if number in data:
    print('True')
else:
    print('False')
"""
#Solution
def is_group(group_data, n):#group_data and n are variables
    for value in group_data:#looking at print you'll notice its talking about def
        if n == value:
            return True
    return False
print(is_group([1, 5, 8, 3], 3))
print(is_group([5, 8, 3], -1))
