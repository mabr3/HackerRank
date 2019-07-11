#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    #y = [p.index(p.index(i)+1)+1 for i in sorted(p)]
    # O(n²)

    #O(2n)->O(n)
    p_inv=[0]*(len(p)+1)

    for i,I in enumerate(p):
        p_inv[I]=i+1

    y = [p_inv[p_inv[i]] for i in range(1,len(p)+1)]
    return y
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

