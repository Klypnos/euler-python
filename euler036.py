"""

Question            : 36
Start Time          : 12.11.17 18:09
End Time            : 12.11.17 18:20
Total Time Spent    : 00:11
Complexity          : O(n*d) d: average number of digits in binary repr.
Answer              : 872187

"""

def isPalindrome(n):
    binary = bin(n)[2:]
    decimal = str(n)
    binLength = len(binary)
    decimalLength = len(decimal)
    for i in range(binLength/2):
        if binary[i] != binary[binLength - i - 1]:
            return False
    for i in range(decimalLength/2):
        if decimal[i] != decimal[decimalLength - i - 1]:
            return False
    return True

sum = 0
for i in range(1000000):
    if isPalindrome(i):
        sum += i
print sum
