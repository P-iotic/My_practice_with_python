"""
P.iotic

Q: 12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.

My first, being introduced to the calender module
Below in directl the solution i retrieved from w3resource
"""
import calendar

y = int(input("Input the year : "))
m = int(input("Input the month : "))

print('')
print(calendar.month(y, m))
