from math import sqrt
import numpy as np

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#sieve of eratosthenes find all primes (1,n)
def sieve(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(2, int(sqrt(n))):
        for j in range(i * i, n, i):
            primes[j] = False
    return [i for i, value in enumerate(primes) if value]
"""
def np_sieve(n):
    primes = np.ones(n, dtype=bool)
    #print primes
    #print primes, type(primes)
    primes[0], primes[1] = False, False
    for i in range(2, int(sqrt(n))): #
        for j in range(i * i, n, i):
            primes[j] = False
    size = np.sum(primes)
    prime_indices = np.empty(size, dtype=np.int32)
    #print size, np.size(prime_indices)
    index = 0
    #print primes
    for i, value in enumerate(primes):
        if value:
            prime_indices[index] = i
            index += 1
    #print index
    return prime_indices
sieve(10000000)
"""
#sieve of eratosthenes find all primes (m, n)
def sieve_between(m, n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(2, int(sqrt(n))): #
        for j in range(i * i, n, i):
            primes[j] = False
    return [i for i, value in enumerate(primes) if value and i >= m]

def int_to_list(number):
    return map(int,[i for i in str(number)])

def list_to_int(digits):
    sum = 0
    for i, val in enumerate(reversed(digits)):
        sum += val * (10**i)
    return sum

def is_palindrome(number):
    stringed = str(number)
    length = len(stringed)
    for i in range(length / 2):
        if stringed[i] != stringed[length - i - 1]:
            return False
    return True

def reverse_int(number):
    stringed = str(number)[::-1]
    return int(stringed)
