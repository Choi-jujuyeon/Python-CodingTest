T=int(input())
for K in range(T):
    N,M,L=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(M):
        a,b=map(int,input().split())
        arr.insert(a,b)
    print(f'#{K+1} {arr[L]}')