"""

Question            : 26
Start Time          : 12.11.17 00:41
End Time            : 12.11.17 01:17
Total Time Spent    : 00:36
Complexity          : O(n*m^2) m: average recurring cycle length of divisors
Answer              : 983

"""

maxCycle = 0
maxCycleDivisor = 0
for divisor in range(2,1001):
    dividend = 1
    quotients = list()
    remainders = list()
    cycle = 0
    while dividend:
        if dividend < divisor:
            dividend *= 10
        quotient = dividend / divisor
        dividend = dividend % divisor
        if dividend not in remainders:
            quotients.append(quotient)
            remainders.append(dividend)
        else:
            cycle = len(remainders) - remainders.index(dividend)
            break
    maxCycleDivisor = divisor if cycle > maxCycle else maxCycleDivisor
    maxCycle = cycle if cycle > maxCycle else maxCycle
    #print divisor, quotients, cycle
print maxCycleDivisor
