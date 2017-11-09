"""

Question            : 6
Start Time          : 09.11.17 22:27
End Time            : 09.11.17 22:29
Total Time Spent    : 00:02
Complexity          : O(1)
Answer              : 25164150

"""
# sum of squares of first n = n(n+1)(2n+1)/6
n = 100
print (n*(n+1)/2)**2 - (n*(n+1)*(2*n+1)/6)
