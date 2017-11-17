"""

Question            : 60
Start Time          : 17.11.17 14:07
End Time            : 17.11.17 16:00
Total Time Spent    : 01:53
Complexity          : O(n*n*k) k: prime pair array length
Answer              : 26033

"""
import mathematics
import numpy as np
from collections import defaultdict
sample = 9999
digit = len(str(sample))
primes = mathematics.sieve((10 ** digit) * sample)
set_primes = set(primes)

prime_families = []
for i, val in enumerate(primes):
    if val > sample:
        break
    prime_families.append([val])
#print prime_families
print "Preprocessing ends."

for i, prime_pairs in enumerate(prime_families):
    for prime2 in primes[:len(prime_families)]:
        for prime_pair in prime_pairs:
            first = int(''.join([str(prime2), str(prime_pair)]))
            second = int(''.join([str(prime_pair), str(prime2)]))
            if first not in set_primes or second not in set_primes:
                #print first, second, first is set_primes
                break
        else:
            prime_families[i].append(prime2)

for prime_family in prime_families:
    if len(prime_family) >= 5:
        print prime_family, sum(prime_family)
