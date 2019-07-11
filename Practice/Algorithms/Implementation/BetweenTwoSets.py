#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    nr =[]
    i=1
    while i <= min(b):
        c=0
        for x in a:
            if i%x==0:
                c +=1
        if c == len(a):
            nr.append(i)
        i+=1
    res=[]
    #print(nr)
    for j in nr:
        c=0
        for x in b:
            if x%j ==0:
                c+=1
        if c == len(b):
            res.append(j)
    return len(res)     


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

