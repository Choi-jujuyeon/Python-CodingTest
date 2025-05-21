T=int(input())
for k in range(T):
    arr=list(map(int,input().split()))
    print(f'#{k+1} {max(arr)}')