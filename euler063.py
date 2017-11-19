"""

Question            : 63
Start Time          : 19.11.17 16:35
End Time            : 19.11.17 16:36
Total Time Spent    : 00:01
Complexity          : O(n*n)
Answer              : 49

"""

count = 0
for a in range(1,50):
    for b in range(1,50):
        result = a ** b
        if len(str(result)) == b:
            count += 1
print count
