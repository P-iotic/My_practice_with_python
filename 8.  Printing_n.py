"""
P.iotic

Q: 10. Write a Python program that accepts an integer(n) and computes the value of
n+nn+nnn

For this program it is rather a simple stricky question. I used n as a string
input rather than an integer because of the fact with integers they would add
up but in this case the need to add up in the form of a string to be next to
one another first, then we can convert them into integer values and add up to
get the totals.
"""
n = input('Enter nth term: ')
n1 = n
n2 = n+n
n3 = n+n+n
total =int(n1)+int(n2)+int(n3)
print(n1,'+',n2,'+',n3)
print(total)

"""
Solution

a = int(input('Input an integer : '))
n1 = int( "%s" % a)
n2 = int( "%s%s" % (a,a))
n3 = int( "%s%s%s" % (a,a,a))
print(n1+n2+n3)
"""
