"""

Question            : 31
Start Time          : 12.11.17 02:20
End Time            : 12:11.17 14:06
Total Time Spent    : 01:30
Complexity          : O(n) could be considered O(n*m) if we consider m(number of unique coins) to differ on each question
Answer              : 73682

"""

import numpy as np
def coinCombinations(credit):
    coins = [1,2,5,10,20,50,100,200]
    matrix = np.zeros((len(coins), credit + 1), dtype = int)
    matrix[:,0] = [ 1 for _ in matrix[:,0] ]
    matrix[0,:] = [ 1 for _ in matrix[0,:] ]
    for i in range(1,matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            if j >= coins[i]:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - coins[i]]
            else:
                matrix[i][j] = matrix[i - 1][j]
    #print matrix
    return matrix[-1][-1]

print coinCombinations(200)
