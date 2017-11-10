"""

Question            : 16
Start Time          : 10.11.17 01:42
End Time            : 10.11.17 01:44
Total Time Spent    : 00:02
Complexity          : O(n)
Answer              : 1366

"""

print reduce(lambda x,y: x+y, map(int, [i for i in str(2**1000)]))
