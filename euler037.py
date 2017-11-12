"""

Question            : 37
Start Time          : 12.11.17 18:22
End Time            : 12.11.17 18:38
Total Time Spent    : 00:16
Complexity          : O(n*sqrt(n)*d) d: average number of digits
Answer              : 748317

"""
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isTruncatablePrime(n):
    digits = str(n)
    numbersStr = list()
    for i in range(len(digits)):
        numbersStr.append(digits[i:])
        numbersStr.append(digits[:i+1])
    numbers = map(int,numbersStr[1:])
    for val in numbers:
        if not isPrime(val):
            return False
    return True

sum = 0
count = 0
i = 10
while count < 11:
    if isTruncatablePrime(i):
        sum += i
        count += 1
    i += 1
print sum
