import math
"""

Question            : 3
Start Time          : 09.11.17 14:26
End Time            : 09.11.17 14:32
Total Time Spent    : 00:06
Complexity          : O( sqrt(n)*log(n) )
Answer              : 6857

"""
num = 600851475143
lastFactor = 1
for i in range(2, int(math.sqrt(600851475143)) ): # sqrt(n) complexity
    while num % i == 0: # log(n) complexity ex: 64 is divided by 2, 6 times log2(64) = 6
        lastFactor = i
        num /= i
print lastFactor
