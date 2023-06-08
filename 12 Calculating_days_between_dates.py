"""
P.iotic

Q: 14. Write a Python program to calculate the number of days between 2 dates 

I didn't have an idea where to start, tried a few methods but they didn't add up
so i looked at the solution and only the year, month,day variable, last 4 came
directly from the solution.

Once again new introduction to datetime
"""

from datetime import date

year = int(input('Enter starting year: '))
month = int(input('Enter starting month: '))
day = int(input('Enter starting day: '))
year2 =int(input('Enter ending year: '))
month2 = int(input('Enter ending month: '))
day2 = int(input('Enter ending day: '))
f_date = date(year, month, day)
l_date = date(year2, month2, day2)
delta = l_date - f_date
print(delta.days,'Days apart')
