import sys
input= sys.stdin.readline
T=int(input())
arr=set()
for i in range(T):
    n,s=input().split()
    if s=="enter":
        arr.add(n)
    else:
        arr.discard(n)
for i in sorted(arr, reverse=True):
    print(i)