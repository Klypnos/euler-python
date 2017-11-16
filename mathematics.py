from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
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
