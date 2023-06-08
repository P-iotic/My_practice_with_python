"""
P.iotic

Q: 3. Write a Python Program that accepts a sequence of comma separated numbers
form the user and generates a list and a tuple of those numbers.

while at first sight it looked fair but it has dribbled me to a point which i
will check out the solution but before that let me explain what I had tried doing

so I made an input value for the your to enter the sequence, that is the input
I created a for loop because i want to run for the length of sequences
e.g. let us say that the sequence had 23,0,6 meaning the length is 6
the loop should run 6 times, inside the for loop I create a if statement to
check if there are commas that exist. If True then i say continue,
which means replacing the comma with an empty space which while testing it works
but the issue then becomes of me telling the program to display the answers
in a sequence.

1. is my attempted solution followed by the solution
"""
"""
sequences=input('Enter a sequence: ')

for k in range(len(sequences)):
    if sequences[k]==',':
        continue
    sequences = list(sequences)
    print(sequences[k], end='')
"""
values = input("Enter comma seperated numbers : ")

list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
"""
When I saw the input, I felt it was a good start but wow did it not go all wrong
after there. List = value.split(',') its my first seeing you can use the spilt to isolate
the numbers from the , by the output but also see it tells the program that everything
befor the comma should be stored as a single item, basically grouping them in the
exact way we want it to be. The tuple change from list I understand now
"""
