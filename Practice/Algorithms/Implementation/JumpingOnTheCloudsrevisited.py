#!/bin/python3

import math
import os
import random
import re
import sys

#NOTE: THE 1ST PROBLEM DOES NOT COMPLY WITH THE RULES, HENCE THIS PROGRAM
#WILL FAIL ON THAT TEST CASE - 10/July/2019

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    ind = (k)%n
    e -= c[ind]*2+1
    while ind!=0:
        ind= (ind+k)%n
        e -=c[ind]*2+1
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

