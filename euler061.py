"""

Question            : 61
Start Time          : 17.11.19 ~
End Time            : 19.11.19 15:25
Total Time Spent    : 3-4 hours
Complexity          : worst: O(n*k!) best O(nk) #trivial for loops are ignored k: number of figurate types
Answer              : 28684

"""
from collections import defaultdict
import sys

def polygonal(x, r):
    if r == 3: return int(x * (x + 1) / 2)
    if r == 4: return int(x * x)
    if r == 5: return int(x * (3*x - 1) / 2)
    if r == 6: return int(x * (2*x - 1))
    if r == 7: return int(x * (5*x - 3) / 2)
    if r == 8: return int(x * (3*x - 2))

polygonals = defaultdict(list)

for i in range(3,9):
    nth_polygonals = list()
    for n in range(200):
        nth_polygonal = polygonal(n, i)
        if 999 < nth_polygonal < 10000 and (nth_polygonal % 100) > 9 and int(nth_polygonal / 100) > 9 :
            nth_polygonals.append(nth_polygonal)
    polygonals[i] = nth_polygonals

starts = defaultdict(lambda: defaultdict(list))
ends = defaultdict(lambda: defaultdict(list))
for i in range(3,9):
    for num in polygonals[i]:
        starts[i][ int(num / 100) ].append(num)
        ends[i][ num % 100 ].append(num)

def search(found_list, nth_list):
    needed_start = found_list[-1]
    for i in nth_list:
        for num in starts[i][needed_start]:
            nth_list.remove(i)
            last_number = needed_start * 100 + found_list[0]
            if nth_list:
                search(found_list + [num % 100], nth_list)
            elif last_number in polygonals[i]:
                print("Found:", found_list, sum(found_list) * 101)
                sys.exit()
            nth_list.append(i)
    return []

for i in range(3,9):
    list_ = list(range(3,9))
    list_.remove(i)
    for num in polygonals[i]:
        search([int(num / 100), num % 100], list_)
