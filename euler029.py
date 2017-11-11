"""

Question            : 29
Start Time          : 12.11.17 01:52
End Time            : 12.11.17 01:56
Total Time Spent    : 00:04
Complexity          : O(a*b)
Answer              : 9183

"""

terms = set()
for a in range(2,101):
    for b in range(2,101):
        terms.add(a**b)
print len(terms)
