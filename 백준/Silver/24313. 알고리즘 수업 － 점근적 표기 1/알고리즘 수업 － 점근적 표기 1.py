a,b=map(int,input().split())
c=int(input())
n0=int(input())
for n in range(n0, 101):
    if a * n + b > c * n:
        print(0)
        break
else:
    print(1)