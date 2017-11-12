"""

Question            : 40
Start Time          : 12.11.17 19:24
End Time            : 12.11.17 19:30
Total Time Spent    : 00:06
Complexity          : O(n)
Answer              :

"""

fraction = ""
i = 1
while len(fraction) < 1000000:
    fraction += str(i)
    i += 1
requireds = map(lambda i: fraction[10**i - 1], range(7))
print reduce(lambda a,b: a*b, map(int,requireds))
