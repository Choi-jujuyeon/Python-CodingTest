T=int(input())
for k in range(T):
    a,b=map(int,input().split())
    A=set(input() for i in range(a))
    B=set(input() for i in range(b))
    print(f'#{k+1} {len(A&B)}')