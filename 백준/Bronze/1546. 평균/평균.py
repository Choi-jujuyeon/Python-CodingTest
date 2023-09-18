a=int(input())
s=list(map(int,input().split()))
M=max(s)
for i in range(a):
    s[i]=s[i]/M*100
print(sum(s)/a)