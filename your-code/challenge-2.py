"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import string
import random
characters = list(string.ascii_lowercase) + list(range(10))

def stringGenerator(l):
    return "".join(str(random.choice(characters)) for i in range(l))

def n_strings(n, a, b):
    if a <= b:
        r = [stringGenerator(random.choice(range(a,b))) if a < b else stringGenerator(a) for i in range(n) ]
        return r
    else:
        print('Incorrect min and max string lengths. Try again.')

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(n_strings(int(n), int(a), int(b)))
