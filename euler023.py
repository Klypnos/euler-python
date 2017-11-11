"""

Question            : 23
Start Time          : 10.11.17 18:45
End Time            : 10.11.17 19:00
Total Time Spent    : 00:15
Complexity          : O(n^2)
Answer              : 4179871

"""

def sumofDivisors(n):
    divisors = list()
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

totalSum = 0
abundants = list()
sums = set()
for i in range(28123):
    if sumofDivisors(i) > i:
        abundants.append(i)
for i in abundants:
    for j in abundants:
        if i+j < 28123:
            sums.add(i+j)
print 28122*28123/2 - sum(sums)
