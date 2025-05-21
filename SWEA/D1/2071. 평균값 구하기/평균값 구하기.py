T=int(input())
for k in range(T):
    arr=list(map(int,input().split()))
    print(f'#{k+1} {int(round(sum(arr)/10,0))}')
