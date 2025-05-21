for k in range(10):
    T=int(input())
    arr=list(map(int,input().split()))
    total=0
    for i in range(2,T-2):
        M=max([arr[i-2],arr[i-1],arr[i+1],arr[i+2]])
        if arr[i]>M:
            total+=arr[i]-M
    print(f'#{k+1} {total}')