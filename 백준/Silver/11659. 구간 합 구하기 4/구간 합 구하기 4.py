import sys
input= sys.stdin.readline
a,b=map(int,input().split())
arr=list(map(int,input().split()))

arr2=[0]
for i in range(a):
    arr2.append(arr2[-1]+arr[i])

for i in range(b):
    i,j=map(int,input().split())
    print(arr2[j] - arr2[i-1])