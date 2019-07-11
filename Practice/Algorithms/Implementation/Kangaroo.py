#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
#COuldve been simplified, by using (x1-x2)%(v2-v1)==0
    if v1<=v2:
        return 'NO'
    else:
        i=1
        while True:
            if v1*i+x1 > v2*i+x2:
                return 'NO'
            elif  v1*i+x1 == v2*i+x2:
                return 'YES'
            else:
                i = i+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

