"""

Question            : 34
Start Time          : 12.11.17 17:35
End Time            : 12.11.17 17:50
Total Time Spent    : 00:15
Complexity          : O(n*d) d: average num of digits
Answer              : 40730

"""
hits = 0
misses = 0
factorial = {}
def fact(k):
    global hits, misses
    if k < 2:
        return 1
    elif k not in factorial:
        factorial[k] = fact(k-1) * k
        misses += 1
        return factorial[k]
    else:
        hits += 1
        return factorial[k]

totalSum = 0
for val in range(10,1000000):
    digitsVal = map(int, [i for i in str(val)])
    factSumofDigits = sum(map(fact,digitsVal))
    if val == factSumofDigits:
        totalSum += val
print totalSum
#print hits, misses
