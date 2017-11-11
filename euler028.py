"""

Question            : 28
Start Time          : 12.11.17 01:46
End Time            : 12.11.17 01:49
Total Time Spent    : 00:03
Complexity          : O(n) : if a diagonal is n*n
Answer              : 669171001

"""

start = 1
increase = 2
sum = 1
while increase <= 1000:
    for i in range(4):
        start += increase
        sum += start
    increase += 2
print sum
