# Enter your code here. Read input from STDIN. Print output to STDOUT
def calc_q(V):
    n=len(V)
    if n%2==0:
        q = (V[n//2-1]+V[n//2])/2.0
    else:
        q = V[n//2]
    return q

N = int(input())
values=[*map(int,input().split())]
values = sorted(values)

Q2 = calc_q(values)
L = [i for i in values if i<Q2]
U = [i for i in values if i>Q2]
Q1=calc_q(L)
Q3=calc_q(U)
print('{:.0f}\n{:.0f}\n{:.0f}'.format(Q1,Q2,Q3))

