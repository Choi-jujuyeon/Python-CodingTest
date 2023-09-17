n,m=map(int,input().split())
a=[0]*n
for _ in range(m):
    i,j,k=map(int,input().split())
    for b in range(i-1, j):
        a[b]=k
print(*a)