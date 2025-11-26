a=int(input())
arr=list(map(int,input().split()))
M=max(arr)
r=0
for i in arr:
    r+=i/M*100
print(r/a)