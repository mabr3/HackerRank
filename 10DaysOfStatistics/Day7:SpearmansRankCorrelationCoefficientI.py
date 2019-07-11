# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int(input())
X=[*map(float,input().split())]
Y=[*map(float,input().split())]
di=[((sorted(X).index(X[i])+1)-(sorted(Y).index(Y[i])+1))**2 for i in range(N)]
P=1 - (6.0*sum(di))/(N*(N**2-1))
print('{:.3f}'.format(P))
