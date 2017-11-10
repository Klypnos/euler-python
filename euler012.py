"""

Question            : 12
Start Time          : 10.11.17 01:01
End Time            : 10.11.17 01:06
Total Time Spent    : 00:05
Complexity          : O(n*sqrt(n))
Answer              : 76576500

"""
from math import sqrt
def numofFactors(n):
    count = 0
    for i in range(1, int(sqrt(n)) + 1): # divisor until sqrt is mirror of the rest, ex: sqrt(28) > 5 >> 1/28,2/14,4/7
        count = count + 1 if n % i == 0 else count
    return count*2

i = 0
inc = 1
while numofFactors(i) <= 500:
    i += inc
    inc += 1
print i
