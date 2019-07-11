# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
v=[*map(int, input().split())]

u=sum(v)*1.0/len(v)
std = pow(sum( [pow(i-u,2) for i in v]) /len(v),0.5)
print('{:.1f}'.format(std))

