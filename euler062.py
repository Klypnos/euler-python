"""

Question            : 62
Start Time          : 19.11.17 15:56
End Time            : 19.11.17 16:28
Total Time Spent    : 00:34
Complexity          : O(n*k*logk) k= number of digits in a number
Answer              : 127035954683

"""
from itertools import count, permutations
from collections import defaultdict, Counter
import mathematics

n = 10000
cubes = [i * i * i for i in range(n)]

cube_digits = defaultdict(list)
for cube in cubes:
    cube_str = str(sorted(str(cube)))
    cube_digits[cube_str].append(cube)

for k in cube_digits:
    if len(cube_digits[k]) == 5:
        print cube_digits[k]
