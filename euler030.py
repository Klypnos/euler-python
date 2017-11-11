"""

Question            : 30
Start Time          : 12.11.17 02:00
End Time            : 12.11.17 02:14
Total Time Spent    : 00:14
Complexity          : O(n*d) d: number of digits
Answer              : 443839

"""
totalSum = 0
for num in range(10, 5 * (9 ** 5)):
    digits = map(int, [i for i in str(num)] )
    poweredDigits = map(lambda x: x**5, digits)
    digitSum = sum(poweredDigits)
    if digitSum == num:
        totalSum += num
print totalSum
