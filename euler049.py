"""

Question            : 49
Start Time          : 13.11.17 17:42
End Time            : 13.11.17 18:39
Total Time Spent    : 00:57
Complexity          : O(n^3)
Answer              : 296962999629

"""
from math import sqrt
primes = list()
def fourDigitPrimes():
    curr = 1000
    while curr < 10000:
        cond = True
        for j in range(2, int(sqrt(curr)) + 1):
            if curr % j == 0: #no prime
                cond = False
                break
        if cond:
            primes.append(curr)
        curr += 1

def isPermutation(a, b):
    return sorted(str(a)) == sorted(str(b))

fourDigitPrimes()
for i, ithPrime in enumerate(primes):
    for j, jthPrime in enumerate(primes[i + 1:]):
        nextPrime = 2 * jthPrime - ithPrime
        if isPermutation(ithPrime,jthPrime) and isPermutation(ithPrime,nextPrime) and nextPrime in primes:
            print ithPrime, jthPrime, nextPrime
