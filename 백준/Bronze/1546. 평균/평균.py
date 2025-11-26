a=int(input())
arr=list(map(int,input().split()))
M=max(arr)

print(sum(arr)*100/M/a)