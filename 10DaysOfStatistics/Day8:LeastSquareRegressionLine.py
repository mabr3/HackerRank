# Enter your code here. Read input from STDIN. Print output to STDOUT
x=[]
y=[]
for _ in range(5):
    v=input().split()
    x.append(int(v[0]))
    y.append(int(v[1]))

meanx= sum(x)*1.0/len(x)
meany= sum(y)*1.0/len(y)
n=len(x)
b = (n*sum([x[i]*y[i] for i in range(n)])-sum(x)*sum(y))/(n*sum([i**2 for i in x])-pow(sum(x),2))
a = meany - meanx*b
res = b*80 +a
print('{:.3f}'.format(res))

