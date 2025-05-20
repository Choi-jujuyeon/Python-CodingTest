n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a+b>=24:
        T=(a+b)%24
    else:
        T=a+b
    print(f'#{i+1} {T}')