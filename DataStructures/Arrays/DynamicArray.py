#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqList=[[] for _ in range(n)]
    lastAnswer=0
    res=[]
    for i in queries:
        ind = (i[1]^lastAnswer)%n
        if i[0]==1:
            seqList[ind].append(i[2])
        else:
            ind2 = i[2] % len(seqList[ind])
            lastAnswer = seqList[ind][ind2]
            res.append(lastAnswer)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

