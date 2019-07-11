# Enter your code here. Read input from STDIN. Print output to STDOUT


N= int(input())
vals= [*map(int,input().split())]
ws= [*map(int,input().split())]
res = 1.0*sum([vals[i]*ws[i] for i in range(len(vals))])/sum(ws)
print('{:.1f}'.format(res))
