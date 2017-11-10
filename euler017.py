"""

Question            : 17
Start Time          : 10.11.17 01:46
End Time            : 10.11.17 03:10
Total Time Spent    : 01:24
Complexity          : O(n*d)
Answer              : 21124

"""

readings20 = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
readingstens = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","thousand"]
count = 0
for i in range(1,1001):
    curr = i
    digits = list(reversed(map(int,[a for a in str(i)])))
    #print digits
    if curr > 100 and curr % 100 != 0:
        count += 3
    if len(digits) >= 4:
        if digits[3] > 0:
            count += (len(readings20[digits[3]]) + len(readingstens [11]))
    if len(digits) >= 3:
        if digits[2] > 0:
            count += (len(readings20[digits[2]]) + len(readingstens[10]))
    if len(digits) >= 2 and digits[1] == 1:
        count += len(readings20[10 + digits[0]])
    else:
        if len(digits) >= 2 and digits[1] > 0:
            count += len(readingstens[digits[1]])
        if len(digits) >= 1 and digits[0] > 0:
            count += len(readings20[digits[0]])
print count
