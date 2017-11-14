"""

Question            : 47
Start Time          : 13.11.17 16:11
End Time            : 13.11.17 17:20
Total Time Spent    : 01:09
Complexity          : ~O(nlogn)
Answer              : 134043

"""
from itertools import count
from math import sqrt

primes = {}
def nthPrime(num):
    if num in primes:
        return primes[num]
    if len(primes) > 2:
        i = len(primes) - 1
        curr = primes[len(primes) - 1]
    else:
        i = 0
        curr = 2
    while i < num:
        cond = True
        for j in range(2, int(sqrt(curr)) + 1):
            if curr % j == 0: #no prime
                cond = False
                break
        if cond:
            primes[i] = curr
            i += 1
        curr += 1
    return curr - 1

def findFactors(n):
    factors = set()
    i = 0
    while n != 1:
        if i not in primes:
            nthPrime( len(primes) * 2)
        while n % primes[i] == 0:
            n = n / primes[i]
            if primes[i] not in factors:
                factors.add(i)
        i += 1
    return len(factors)

nthPrime(100)
consecutives = 0
for i in iter(count(4)):
    if findFactors(i) == 4:
        consecutives += 1
    else:
        consecutives = 0
    if consecutives == 4:
        print i - 3
        break
