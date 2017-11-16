"""

Question            : 50
Start Time          : 14.11.17 17:03
End Time            : 14.11.17 19:00
Total Time Spent    : 01:57
Complexity          :
Answer              :

"""
from math import sqrt
from itertools import count
from sys import exit
primes = []
def smallerPrimes(n):
    primeSum = 0
    curr = 2
    while primeSum < n:
        for j in range(2, int(sqrt(curr)) + 1):
            if curr % j == 0:
                break
        else:
            primeSum += curr
            primes.append(curr)
        curr += 1

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

smallerPrimes(1000000)
primeSum = sum(primes)
while 1:
    copySum = primeSum
    for i in range(len(primes)):
        for j in range(1, i):
            left = sum(primes[:i - j])
            right = sum(primes[-j:])
            truncatedSum = copySum - left - right
            if isPrime(truncatedSum):
                print truncatedSum
                exit()
