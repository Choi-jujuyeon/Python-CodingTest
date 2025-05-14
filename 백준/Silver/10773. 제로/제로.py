import sys
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    k=int(input())
    if k==0:
        a.pop()
    else:
        a.append(k)
print(sum(a))