import sys
input=sys.stdin.readline

a,b=map(int,input().split())
arr=[]
count=0
for i in range(a):
    arr.append(input())
for j in range(b):
    a=input()
    if a in arr:
        count+=1
print(count)