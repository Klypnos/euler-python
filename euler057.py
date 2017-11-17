"""

Question            : 57
Start Time          : 16.11.17 20:46
End Time            : 16.11.17 21.15
Total Time Spent    : 00:29
Complexity          : O(n)
Answer              : 153

"""

numerator = 3
denominator = 2
count = 0
for i in range(1000):
    if len(str(numerator)) > len(str(denominator)):
        count += 1
    numerator, denominator = 2*denominator + numerator ,numerator + denominator
print count
