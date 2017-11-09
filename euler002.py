"""

Question            : 2
Start Time          : 09.11.17 14:20
End Time            : 09.11.17 14:23
Total Time Spent    : 00:03
Complexity          : O(n)
Answer              : 4613732

"""
a = 0
b = 1
c = a + b
sum = 0
while c < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        sum += c
print sum
