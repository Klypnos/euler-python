"""

Question            : 53
Start Time          : 16.11.17 14:38
End Time            : 16.11.17 15:00
Total Time Spent    : 00:22
Complexity          : O(n*n)
Answer              : 4075

"""
import numpy as np
n = 101
pascal_triangle = np.zeros(shape=(n,n), dtype=np.int64)

pascal_triangle[0][0] = 1
for i in range(1, n):
    for j in range(i + 1):
        result = pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1]
        pascal_triangle[i][j] = 1000001 if result > 1000001 else result

print sum(i > 1000000 for i in pascal_triangle.flatten())
