#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    p = [5]*n
    if n%3 ==0:
        print(''.join(str(z) for z in p))
        return
    else:
        for i in range(n):
            p[-(i+1)] = 3
            if (p.count(5)%3==0 and p.count(3)%5==0) \
            or (p.count(5)%3==0 and p.count(3)==0) or \
            (p.count(5)==0 and p.count(3)%5==0):
                print(''.join(str(z) for z in p))
                return

    print(-1)
    return

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

