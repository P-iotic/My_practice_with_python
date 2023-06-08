"""
P.iotic

Q: 8. Write a Python program to display the first and last colors from the
following list.

For this solution, I am not sure if this is right but I put the colors in
a list and used print to display the first and last color by calling them out in []
Not sure how else i would tackle it but I would have put it in a for loop and used the last value of the
loop to initial the last color.
"""
color_list = ["Red","Green","White","Black"]
print('First colour\t :',color_list[0],'\nLast colour\t :',color_list[3])
"""
Solution

color_list = ["Red","Green","White","Black"]
print("%s %s"%(color_list[0],color_list[-1]))

While do not seem to be far off, checking this out, beginning to see the
importance of trying out % because it looks to make things simple. The [-1] is
interesting because for a moment I had forgotten that you can do it backwards.
"""
