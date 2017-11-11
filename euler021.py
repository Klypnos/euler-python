"""

Question            : 21
Start Time          : 10.11.17 18:25
End Time            : 10.11.17 18:30
Total Time Spent    : 00:05
Complexity          : O(n^2)
Answer              : 31626

"""

def sumofDivisors(n):
    divisors = list()
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

summ = 0
for i in range(1,10000):
    divisorSum = sumofDivisors(i)
    if sumofDivisors(divisorSum) == i and i != divisorSum :
        summ += i
print summ
