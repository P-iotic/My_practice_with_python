"""
P.iotic

Q: 4. Write a Python program that calculates the area of a circle based on the radius entered by user.

Firstly do not mind my import statement, i mostly prefer using from rather
than import (still gets us to the same place.

You will underestimate maths at some point but its programs like this that
reminds me to go back to the basics and remember but memory is not so bad

Do not have much to say than there are other methods to get there.

1.
from math import pi

radius = float(input('Enter the circle raduis: '))

radius = pi*(radius**2)

print('Area of the circle:',str(radius))

2.
"""
import math

radius = float(input('Enter the circle radius: '))

print('Area of the circle: '+str(math.pi*(radius**2)))
