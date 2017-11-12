"""

Question            : 32
Start Time          : 12.11.17 16:16
End Time            : 12.11.17 16:33
Total Time Spent    : 00:17
Complexity          : O(n!)
Answer              : 45228

"""
from itertools import permutations

totalSum = 0
pandigitals = set()
for perm in permutations(range(1,10)):
    for j in range(1,3):
        firstArr = [(10 ** i) * val for i, val in enumerate(perm[0:j])]
        secondArr = [(10 ** i) * val for i, val in enumerate(perm[j:5])]
        thirdArr = [(10 ** i) * val for i, val in enumerate(perm[5:])]
        first = sum(firstArr)
        second = sum(secondArr)
        third = sum(thirdArr)
        if first * second == third:
            pandigitals.add(third)
print sum(pandigitals)
