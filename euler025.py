"""

Question            : 25
Start Time          : 12.11.17 00:25
End Time            : 12.11.17 00:30
Total Time Spent    : 00:05
Complexity          : O(n)
Answer              : 4782

"""

a = 0
b = 1
c = a + b
i = 2
while c < 10**999:
    a = b
    b = c
    c = a + b
    i += 1
print i
