"""

Question            : 51
Start Time          : 16.11.17 11:56
End Time            : 16.11.17 13:34
Total Time Spent    : 01:40
Complexity          : n * log(n) * log(n)
Answer              : 121313

"""
import mathematics
from itertools import permutations
from collections import defaultdict
import sys

digits = defaultdict(set)
def calculate_digit_permutations(n):
    for i in range(1, n):
        which_digits = [1] * i
        which_digits.extend([0] * (n - i))
        for perm in permutations(which_digits, n):
            #if not perm[0]:
            digits[n].add(perm)
    digits[n] = list(digits[n])

def n_prime_digit_family(number, which_digits):
    indices = [i for i, value in enumerate(which_digits) if value]
    number = mathematics.int_to_list(number)
    count = 0
    family = []
    for i in reversed(range(10)):
        for ind in indices:
            number[ind] = i
        if mathematics.list_to_int(number) in primes:
            family.append(mathematics.list_to_int(number))
            count += 1
    return (count, family)

primes = set(mathematics.sieve_between(10000,1000000))
calculate_digit_permutations(5)
calculate_digit_permutations(6)

maxTuple = (0, [])
for prime in primes:
    number_of_digits = len(str(prime))
    for perm in digits[number_of_digits]:
        result = n_prime_digit_family(prime, perm)
        if result[0] == 8:
            print result
            sys.exit()
