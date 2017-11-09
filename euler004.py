"""

Question            : 4
Start Time          : 09.11.17 14:37
End Time            : 09.11.17 14:55
Total Time Spent    : 00:18
Complexity          : O(n^2*k) ~ O(n^2) # since k is trivial ( count of digits in a number)
Answer              : 906609

"""

def isPalindrome(num): # O(n)
    numStr = str(num)
    half = len(numStr) / 2
    size = len(numStr) - 1
    for i in range(half):
        if numStr[i] != numStr[size - i]:
            return False
    return True

max = 0
for i in range(100,999):
    for j in range(100,999):
        num = i*j
        if isPalindrome(num) and num > max:
            max = num
print max
