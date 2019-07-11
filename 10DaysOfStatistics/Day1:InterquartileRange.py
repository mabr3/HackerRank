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

freq= [*map(int,input().split())]
new_vals= []
for i in range(N):
    for _ in range(freq[i]):
        new_vals.append(values[i])
new_vals=sorted(new_vals)
#print(len(new_vals))
Q2 = calc_q(new_vals)
L = new_vals[:len(new_vals)//2]
U = new_vals[len(new_vals)//2+1:]
#print(len(L))
#print(len(U))

Q1=calc_q(L)
Q3=calc_q(U)
#print(Q1, Q2, Q3)
print('{:.1f}'.format(Q3-Q1))

