"""

Question            : 67
Start Time          : 20.11.17 22:14
End Time            : 20.11.17 22:24
Total Time Spent    : 00:10
Complexity          : O(n*n)
Answer              :

"""

import numpy as np
with open("p067_triangle.txt") as file:
    nums = file.read()
line_separated = nums.split("\n")
number_of_lines = len(line_separated) - 1
numbers = list()
for i in range(number_of_lines):
    line = map(int, line_separated[i].split(" "))
    line_width = len(line)
    missing_width = number_of_lines - line_width
    line.extend( missing_width * [0] )
    numbers.append(line)
pyramid = np.array(numbers)

for i in range(number_of_lines - 2, -1, -1): # start from the second line from bottom
    for j in range(i+1):
        pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1]) # sum
print pyramid[0][0]
