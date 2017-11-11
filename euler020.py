"""

Question            : 20
Start Time          : 10.11.17 18:06
End Time            : 10.11.17 18:08
Total Time Spent    : 00:02
Complexity          : O(n)
Answer              : 648

"""
#digit sums of 100!
fact = reduce(lambda x,y: x*y, range(1,101) )

stringDigits = [i for i in str(fact)]
sumofDigits = sum(map(int,stringDigits))
print sumofDigits
