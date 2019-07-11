#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    C=0
    i=0
    while i < len(c)-1:
        try:
            if c[i+2]==0:
                i=i+2
            else:
                i+=1
        except:
            i+=1
        C+=1    
    return C

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

