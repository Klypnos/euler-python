"""

Question            : 19
Start Time          : 10.11.17 16:53
End Time            : 10.11.17 17:56
Total Time Spent    : ~01:00
Complexity          : O(y*n) y: number of years n: list generation
Answer              : 171

"""
thirties = [ 4,6,9,11]
thirtyones = [ 1,3,5,7,8,10,12]
start = 0 # 1 jan 1900 monday , 1 jan 1901 tuesday
count = 0
for i in range(1901,2001):
    yearStart = start
    if i % 4 == 0 and i % 400 != 0:
        yearEnd = yearStart + 365
        start += 366
    else:
        yearEnd = yearStart + 364
        start += 365
    sundays = filter(lambda x: x % 7 == 5, range(yearStart,yearEnd+1))
    #print "sundays",sundays
    monthStarts = [yearStart]
    monthStart = yearStart
    for j in range(11):
        if j + 1 in thirties:
            monthStart += 30
        elif j + 1 in thirtyones:
            monthStart += 31
        elif i % 4 == 0 and i % 400 != 0:
            monthStart += 29
        else:
            monthStart += 28
        monthStarts.append(monthStart)
    #print "month",monthStarts
    intersections = list( set(monthStarts) & set(sundays))
    #print "intersect",intersections
    count += len(intersections)
print count
