for k in range(10):
    a=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(2, a-2):
        M=max(arr[i-2], arr[i-1], arr[i+1],arr[i+2])
        if arr[i]>M:
            count+=arr[i]-M
    print(f'#{k+1} {count}')
