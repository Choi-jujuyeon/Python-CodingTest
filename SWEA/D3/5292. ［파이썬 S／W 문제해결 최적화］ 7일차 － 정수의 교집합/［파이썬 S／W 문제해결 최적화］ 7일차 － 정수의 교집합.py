T=int(input())
for i in range(T):
    n,m=map(int,input().split())
    A=set(map(int,input().split()))
    B=set(map(int,input().split()))
    print(f'#{i+1} {len(A & B)}')