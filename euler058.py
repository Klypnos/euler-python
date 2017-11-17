"""

Question            : 58
Start Time          : 17.11.17 12:00
End Time            : 17.11.17 12:58
Total Time Spent    : 00:58
Complexity          : O(n*sqrt(n))
Answer              : 26241

"""
import mathematics

number_of_primes, count, ratio, start, increase = 0, 1, 1.0, 1, 2

while ratio > 0.1:
    count += 4
    for _ in range(4):
        start += increase
        if mathematics.is_prime(start):
            number_of_primes += 1
    increase += 2
    ratio = number_of_primes / float(count)
print increase - 1
