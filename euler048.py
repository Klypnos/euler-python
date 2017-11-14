"""

Question            : 48
Start Time          : 13.11.17 17:29
End Time            : 13.11.17 17:30
Total Time Spent    : 00:01
Complexity          : O(n)
Answer              : 9110846700

"""

sum = 0
for i in range(1,1001):
    sum += i ** i
print sum % (10 ** 10)
