"""

Question            : 42
Start Time          : 12.11.17 21:00
End Time            : 12.11.17 21:09
Total Time Spent    : 00:09
Complexity          : O(n*m) m: length of triangle list
Answer              : 162

"""

with open("p042_words.txt") as file:
    names = file.read().replace('"','').split(",")

triangles = list()
val = 0
i = 1
while val < 1000:
    val = i * (i + 1) / 2
    triangles.append(val)
    i += 1

count = 0
for name in names:
    nameVal = map(ord,name)
    nameVal = [ char - ord('A') + 1 for char in nameVal ]
    if sum(nameVal) in triangles:
        count += 1
print count
