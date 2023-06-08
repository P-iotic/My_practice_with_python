"""
P.iotoc

Q: 3. Write a Python program to display the current date and time.

import datetime imports the datetime module which supplies classes for manipulating
dates and times.

Once again, It has hit me out of the game with my lack of knowledge for the datetime module
shakky but will get there slowly, brick by brick

now =... creats a datetime object for the current date and time

I do not see it yet but that last dot reminds me of Excel in getting the current date
but thats because we did excercises on that.

The last print, from it I get i better-ish understanding from the % now. In a way for
example if you using float to display a value with certain number of decimals you say %0.2f
which the 0 indicates the value and .2 says 2 decimal places right?
Though i am not yet clear on the f. I tried going through python website on brushing
my understanding but it all seemed out of planet except the ones i made myself familiar
with.
%Y-%m-%d %H-%M-%S 
2023-05-20 22:16:02
"""
import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
