"""
P.iotic

Q: 7. Write a Python program that accepts a filename from the user and prints the
extension of the file.

Input to get the type of extension provided by the user. List takes the whole
string input and separates it into 2 parts that way it is easier to use in
part 2 inside of print.
"""
extension = input('Enter filename: ')

list = extension.split('.')

print('Extensio of file: ',list[1])

"""
Solution
filename = input('Enter filename: ')
f_extns = filename.split(".")
print("The extension of the file is : "+repr(f_extns[-1]))
"""
