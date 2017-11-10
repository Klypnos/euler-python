"""

Question            : 15
Start Time          : 10.11.17 01:40
End Time            : 10.11.17 01:40
Total Time Spent    : ~ 00:00
Complexity          :
Answer              :

"""
fortyFact = reduce(lambda x,y:x*y, range(1,41))
twentyFact = reduce(lambda x,y:x*y, range(1,21))

print (fortyFact / twentyFact) / twentyFact
