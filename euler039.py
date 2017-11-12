"""

Question            : 39
Start Time          : 12.11.17 18:57
End Time            : 12.11.17 19:01
Total Time Spent    : 00:04
Complexity          : O(n^2)
Answer              : 840

"""

# a^2 + b^2 = c^2 , a+b+c = P  >> c = P - a - b
# b = p*(p-2a)/2(p-a)
def countRightAngleTriangles(perimeter):
    count = 0
    for a in range(perimeter):
        b = perimeter * (perimeter - 2 * a) / (2 * (perimeter - a))
        c = perimeter - a - b
        if a * a + b * b == c * c:
            count += 1
    return count

maxCount = 0
maxCountPerimeter = 0
for perimeter in range(4,1001,2):
    count = countRightAngleTriangles(perimeter)
    maxCountPerimeter = perimeter if count > maxCount else maxCountPerimeter
    maxCount = count if count > maxCount else maxCount
print maxCountPerimeter
