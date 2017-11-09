"""

Question            : 1
Start Time          : 09.11.17 14:12
End Time            : 09.11.17 14.14
Total Time Spent    : 00:02
Complexity          : O(n)
Answer              : 233168

"""
sum = 0
for i in range(1000):
    if i%5 == 0 or i%3 == 0:
        sum += i
print sum
