"""

Question            : 27
Start Time          : 12.11.17 01:20
End Time            : 12.11.17 01:43
Total Time Spent    : 00:23
Complexity          : O(a*b*sqrt(n)*l) l: average number of primes for an (a,b) tuple
Answer              : -59231

"""
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

maxN = 0
maxA = 0
maxB = 0
for a in range(-999,1000):
    for b in range(1001):
        if isPrime(b) and isPrime(a+b+1) and isPrime(4+2*a+b):
            n = 3
            while isPrime(n**2 + a*n + b):
                n += 1
            if n > maxN:
                maxN = n
                maxA = a
                maxB = b
                #print maxA, maxB, n
print maxA * maxB
