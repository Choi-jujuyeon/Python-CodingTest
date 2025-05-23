from itertools import combinations
n,m=map(int,input().split())
arr=list(map(int,input().split()))
r=[]
for i in combinations(arr,3):
    if sum(i)<=m:
        r.append(sum(i))
print(max(r))