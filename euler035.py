"""

Question            : 35
Start Time          : 12.11.17 17:53
End Time            :
Total Time Spent    :
Complexity          :
Answer              :

"""
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isCircularPrime(n):
    numberofDigits = len(str(n))
    digits = map(int, str(n))
    digits.extend(digits) #twice the digits to ease circulation
    for i in range(numberofDigits):
            num = 0
            multiplier = 10 ** (numberofDigits - 1)
            for j in range(numberofDigits):
                num += digits[i+j] * multiplier
                multiplier /= 10
            if not isPrime(num):
                return False
    return True
count = 0
for i in range(0,1000000):
    if isCircularPrime(i):
        count += 1
print count
