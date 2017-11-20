"""

Question            : 65
Start Time          : 20.11.17 11:55
End Time            : 20.11.17 13:44
Total Time Spent    : 00:15
Complexity          : O(n)
Answer              : 272

"""
import mathematics
sequence = [2]
for k in range(1, 40):
    sequence.extend([1, 2 * k, 1])


def nth_convergent(n):
    needed_sequence = list(sequence[:n])
    #print needed_sequence
    numerator = 1
    denominator = 0
    while needed_sequence:
        numerator, denominator = denominator, numerator
        last = needed_sequence.pop()
        numerator += denominator * last
        #print numerator, denominator
    return sum(mathematics.int_to_list(numerator))

print nth_convergent(100)
