# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

N= int(input())
a = np.array([*map(int,input().split())])
print(np.mean(a))
print(np.median(a))
print(stats.mode(a)[0][0])
