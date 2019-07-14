# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
import numpy as np

lm= linear_model.LinearRegression()
lis=[]
m,n = map(int,input().split())
for _ in range(n):
    lis.append([*map(float, input().split())])


x=np.array([i[:m] for i in lis])
y=np.array([i[m:] for i in lis])

lis2=[]
q = int(input())

lm.fit(x,y)

for _ in range(q):
    print(int(lm.predict\
    (np.array(\
    [i for i in map(float,input().split())]).reshape(1,-1))))



