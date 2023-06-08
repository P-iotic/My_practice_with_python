"""
P.iotic

Q: 26 Write a Python program to create a histogram from a given list of integers.
items is [2,3,6,5]
I didn't see it at first but because 
"""

def histogram(items):
    for n in items:#run 4 times
        output = ''
        times = n
        while(times>0):
            output += '*'
            times = times -1
        print(output)

histogram([2 ,3 ,6 ,5])
