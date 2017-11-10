"""

Question            : 14
Start Time          : 10.11.17 01:17
End Time            : 10.11.17 01:30
Total Time Spent    : 00:13
Complexity          : O(n*m)
Answer              : 837799

"""
longestChainLength = 0
longestStart = 0
for i in range(1,1000000):
    chainLength = 0
    curr = i
    while curr != 1:
        if curr % 2 == 0:
            curr /= 2
            chainLength += 1
        else:
            curr = 3*curr + 1
            chainLength += 1
    longestStart = i if chainLength > longestChainLength else longestStart
    longestChainLength = chainLength if chainLength > longestChainLength else longestChainLength
print longestStart
