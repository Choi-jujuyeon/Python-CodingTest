import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr2=[0]
for i in arr:
    arr2.append(i+arr2[-1])
for i in range(m):
    i,j=map(int,input().split())
    print(arr2[j]-arr2[i-1])