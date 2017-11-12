"""

Question            : 38
Start Time          : 12.11.17 18:45
End Time            : 12.11.17 18:54
Total Time Spent    : 00:09
Complexity          : O(n)
Answer              : 932718654

"""

def isPandigital(n):
    concatenated = ""
    i = 1
    while len(concatenated) < 9:
        concatenated += str(n * i)
        i += 1
    if len(concatenated) != 9 or '0' in concatenated or len(set(concatenated)) != 9:
        return 0
    return int(concatenated)

max = 0
for i in range(1000000):
    res = isPandigital(i)
    if res:
        max = res
print max
