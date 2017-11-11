"""

Question            : 22
Start Time          : 11.11.17 23:17
End Time            : 11.11.17 23:38
Total Time Spent    : 00:21
Complexity          : O(n*l) l: average number of letters
Answer              : 871198282

"""

with open("p022_names.txt") as file:
    names_ = file.read().replace('"',"")
names = names_.split(",")
sum = 0
for i,value in enumerate(sorted(names)):
    curr_sum = 0
    for x in value:
        curr_sum +=  ord(x) - ord('A') + 1
    sum += curr_sum * (i+1)
print sum
