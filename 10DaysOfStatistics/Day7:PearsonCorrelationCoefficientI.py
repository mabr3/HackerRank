# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
X=[*map(float,input().split())]
Y=[*map(float,input().split())]
ux= sum(X)/len(X)
uy= sum(Y)/len(Y)
stdx=pow((1.0/N)*sum([(X[i]-ux)**2 for i in range(N)]),0.5)
stdy=pow((1.0/N)*sum([(Y[i]-uy)**2 for i in range(N)]),0.5)
P=sum([(X[i]-ux)*(Y[i]-uy)for i in range(N)])/(N*stdx*stdy)
print('{:.3f}'.format(P))
