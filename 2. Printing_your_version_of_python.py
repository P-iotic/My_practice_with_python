"""
P.iotic

Q: 2. Write a python program to find out what version of Python you are using.

The import sys module contains methods and variables for modifying many elements
of the Python Runtime Environment.
I am writing this for myself because i do not know yet what or how to use import sys
Hoping for a better reflect later on.

2 methods shown to me on W3resource as solution

1.
import sys

print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

2.(One below)
"""
import platform
print(platform.python_version())
