"""

Question            : 56
Start Time          : 16.11.17 20:32
End Time            : 16.11.17 20:35
Total Time Spent    : 00:03
Complexity          : O(n^2*k) k: average number of digits
Answer              : 972

"""

max_digit_sum = 0
for a in range(100):
    for b in range(100):
        number = a ** b
        digits = map(int, str(number))
        digit_sum = sum(digits)
        #print a, b, number ,digit_sum
        max_digit_sum = digit_sum if digit_sum > max_digit_sum else max_digit_sum
print max_digit_sum
