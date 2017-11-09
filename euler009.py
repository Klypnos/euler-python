"""

Question            : 9
Start Time          : 09.11.17 23:08
End Time            : 09.11.17 23:12
Total Time Spent    : 00:04
Complexity          : O(n^2)
Answer              : 31875000

"""
for a in range(1,1000):
    for b in range(a,1000):
        c = 1000 - a - b
        if a+b < 1000 and a*a + b*b == c*c:
            print a*b*c
