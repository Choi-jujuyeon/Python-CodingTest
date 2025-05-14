import sys
a,b=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
for i in arr:
    if i<b:
        print(i, end=" ")    