"""

Question            : 24
Start Time          : 11.11.17 23:46
End Time            : 11.11.17 23:50
Total Time Spent    : 00:04
Complexity          : O(n!)
Answer              : 2783915460

"""
from itertools import permutations

perms = list(permutations(range(10)))

print perms[999999]
