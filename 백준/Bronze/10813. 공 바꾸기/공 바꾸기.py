n,m=map(int,input().split())
a=list(i for i in range(n+1))
for _ in range(m):
    i,j=map(int,input().split())
    a[i],a[j]=a[j],a[i]
print(*a[1:])