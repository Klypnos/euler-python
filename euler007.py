import math
"""

Question            : 7
Start Time          : 09.11.17 22:32
End Time            : 09.11.17 22:43
Total Time Spent    : 00:11
Complexity          : O(n*sqrt(n))
Answer              : 104743

"""
def nthPrime(num):
    i = 0
    curr = 2
    while i < num:
        cond = True
        for j in range(2, int(math.sqrt(curr)) + 1):
            if curr % j == 0: #no prime
                cond = False
                break
        if cond:
            i += 1
        curr += 1
    return curr - 1

print nthPrime(10001)
