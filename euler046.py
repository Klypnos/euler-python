"""

Question            : 46
Start Time          : 13.11.17 15:32
End Time            : 13.11.17 15:50
Total Time Spent    : 00:18
Complexity          : O(n*m*logm*k) m is the input to nthPrime function, k is the order of square number in 2*k*k k=(1,~) set
Answer              :

"""
from itertools import imap, count
from math import sqrt

def nthPrime(num):
    i = 0
    curr = 2
    while i < num:
        cond = True
        for j in range(2, int(sqrt(curr)) + 1):
            if curr % j == 0: #no prime
                cond = False
                break
        if cond:
            i += 1
        curr += 1
    return curr - 1

def isPrime(n):
    if n < 2:
        return False
    for i in range( 2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def doesSupportConjecture(num):
    for prime in imap(nthPrime, count(1)):
        for number in iter(count(1)):
            square = number * number * 2
            #print prime, square
            if square + prime > num:
                break
            elif square + prime == num:
                return True
        if prime > num:
            return False

for i in iter(count(3, 2)):
    if not isPrime(i) and not doesSupportConjecture(i):
        print i
        break
