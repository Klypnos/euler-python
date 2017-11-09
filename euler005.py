import math
"""

Question            : 5
Start Time          : 09.11.17 15.11
End Time            : 09.11.17 15.52
Total Time Spent    : 00:41
Complexity          : O(n^2*logn)
Answer              : 232792560

"""
# 1 2 3 2 5 7 2 3               >>> until 10
# 1 2 3 2 5 7 2 3 11 13 2 17 19 >>> until 20
#print (2*3*2*5*7*2*3*11*13*2*17*19)
# Result can easily be found by eliminating factors with care but lets do it the code way.

factorDict = {}
def factorize(num): # O(nlogn)
    factors = {}
    for i in range(2, num + 1):
        count = 0
        while num % i == 0:
            num /= i
            count += 1
        factors[i] = count
    return factors # factors[3]=2 factors[2]=1 for number 18

for i in range(2,20):
    factors = factorize(i)
    for key,value in factors.iteritems():
        if key not in factorDict or value > factorDict[key]:
            factorDict[key] = value
#print factorDict
num = 1
for key,value in factorDict.iteritems():
    num *= pow(key,value)
print int(num)
