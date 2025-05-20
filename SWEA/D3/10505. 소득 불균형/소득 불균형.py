T=int(input())
for k in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    avg=sum(arr)//n
    print(f'#{k+1} {len([i for i in arr if i <= avg])}')