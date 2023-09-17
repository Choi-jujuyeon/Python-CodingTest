n=int(input())
b=list(map(int,input().split()[:n]))
print(min(b), end=" ")
print(max(b))