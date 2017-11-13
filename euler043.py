"""

Question            : 43
Start Time          : 12.11.17 21:15
End Time            : 12.11.17 21:27
Total Time Spent    : 00:12
Complexity          : O(n!)
Answer              : 16695334890

"""
from itertools import permutations

def isSubstringDivisible(number):
    primes = [2,3,5,7,11,13,17]
    i = 1
    for prime in primes:
        if int(number[i:i + 3]) % prime != 0:
            return False
        i += 1
    return True



sum = 0
for perm in permutations(range(10),10):
    number =  reduce(lambda x,y: x + y, map(str, perm)) # list to string conversion
    if isSubstringDivisible(number):
        sum += int(number)
        #print int(number)
print sum
