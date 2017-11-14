"""

Question            : 45
Start Time          : 13.11.17 15.07
End Time            : 13.11.17 15:19
Total Time Spent    : 00:12
Complexity          : O(n)
Answer              : 1533776805

"""
from itertools import count, imap
from math import sqrt

def triangle(n):
    return n * (n + 1) / 2

def triangletoN(number):
    return int((sqrt(8 * number + 1) - 1) / 2)

def isTriangle(number):
    return triangle(triangletoN(number)) == number

def pentagonal(n):
    return n * (3 * n - 1) / 2

def pentagonaltoN(penta): # p(n) = (3*n*n - n)/2
    return int( (sqrt(penta * 24 + 1) + 1 ) / 6 )

def isPentagonal(number):
    return pentagonal(pentagonaltoN(number)) == number

def hexagonal(n):
    return n * (2 * n - 1)

for i, val in enumerate(imap( hexagonal, count(144))):
    if isPentagonal(val) and isTriangle(val):
        print val
        break
