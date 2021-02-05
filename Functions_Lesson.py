##Computers and Python
##Functions

#Four reasons to use functions
#1. Orginize programs by grouping chunks of code.
#2. Reuse code in multiple places.
#3. Improves readability and testing.
#4. 

#For the following function..
#argument: (3,4)
#parameter: (a, b)
#results: 7

def add_two(a, b):
    x = a + b
    return x

add_two(3, 4)

import math 

def pythag(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

print(pythag (3,4))

def tax(subtotal):
    finaltotal = subtotal * 1.15
    return finaltotal

print(tax(10))

import statistics as stat

def averagemark(*args):
    x = sum(args)/len(args)
    return x

print(averagemark(1,2,3,4,5,6,7,8))
