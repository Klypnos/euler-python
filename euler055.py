"""

Question            : 55
Start Time          : 16.11.17 20:13
End Time            : 16.11.17 20:26
Total Time Spent    : 00:13
Complexity          : O(n*k) k: number of cycles (max:50)
Answer              : 249

"""
import mathematics

count = 0
for num in xrange(10000):
    cycle = 0
    value = num
    while cycle < 50:
        reverse = mathematics.reverse_int(value)
        value += reverse
        #print num, value
        if mathematics.is_palindrome(value):
            break
        cycle += 1
    if cycle == 50:
        count += 1
print count
