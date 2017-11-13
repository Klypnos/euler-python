"""

Question            : 41
Start Time          : 12.11.17 19:35
End Time            : 12.11.17 19:48
Total Time Spent    : 00:13
Complexity          : O(n!)
Answer              : 7652413

"""
from itertools import permutations
from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# 8! 9! permutations are not possible because 8*9/2 = 36 and 9*10/2= 45 both are divisible by 3.
max = 0
for i in range(7,-1,-1):
    condition = False
    for perm in permutations(range(1, i + 1), i):
        number =  int(reduce(lambda x,y: x + y, map(str, perm))) # list to int conversion
        if isPrime(number):
            condition = True
            max = number
    if condition:
        break
print max
