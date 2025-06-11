T=int(input())
for i in range(T):
    arr=list(map(int,input().split()))
    avg=sum(arr[1:])//arr[0]
    result=len([i for i in arr[1:] if i>avg])/arr[0] *100
    print(f'{result:.3f}%')
