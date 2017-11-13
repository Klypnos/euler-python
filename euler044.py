"""

Question            : 44
Start Time          : 12.11.17 22:15
End Time            : 13.11.17 14:51
Total Time Spent    : ~01:00
Complexity          : O(n^2)
Answer              : 5482660

"""
from math import sqrt

def pentagonaltoN(penta): # p(n) = (3*n*n - n)/2
    return int( (sqrt(penta * 24 + 1) + 1 ) / 6 )

def pentagonal(n):
    return n * (3 * n - 1) / 2

min = 10**12
for i in range(1, 5000):
    for j in range(1, i):
        ival = pentagonal(i)
        jval = pentagonal(j)
        ijsum = pentagonal(pentagonaltoN(ival + jval))
        ijdiff = pentagonal(pentagonaltoN(abs(ival - jval)))
        if ijsum == ival + jval and ijdiff == abs(ival - jval) and ijdiff < min :
            min = ijdiff
            print min
