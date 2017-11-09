"""

Question            : 10
Start Time          : 09.11.17 23:15
End Time            : 09.11.17 23:42
Total Time Spent    : 00:27
Complexity          : O( sqrt(n) * log(log(n)) )
Answer              : 142913828922

"""
"""
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range( 2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2,2000000):
    if isPrime(i):
        sum += i
print sum
"""
from math import sqrt
n = 2000001
numbers = [True] * n
#print numbers

for i in range(2, int(sqrt(n)) + 1 ): #sieve
    if numbers[i]:
        for j in range(i*i,n,i):
            numbers[j] = False
print reduce(lambda x,y: x+y, [i for i,x in enumerate(numbers) if x ] ) - 1
# 1 is minused because first two elements are also counted as prime which are 0 and 1
# prime harmonic series are asymptotic to loglogn
