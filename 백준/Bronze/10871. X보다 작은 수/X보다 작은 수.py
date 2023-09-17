n,x=map(int,input().split())

a = list(map(int, input().split()[:n]))

for i in range(n):
  if a[i]<x:
    print(a[i],end=" ")