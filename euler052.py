"""

Question            : 52
Start Time          : 16.11.17 14:12
End Time            : 16.11.17 14:24
Total Time Spent    : 00:12
Complexity          : O(n * k) k: count of digits of a number
Answer              : 142857

"""
from itertools import count
import mathematics
import sys


for num in iter(count(2)):
    digits = sorted(mathematics.int_to_list(num))
    if (5 in digits or 0 in digits) and sum(digits) % 3 == 0:
        for i in range(2, 7):
            if digits != sorted(mathematics.int_to_list(num * i)):
                break
        else:
            print num
            sys.exit()
