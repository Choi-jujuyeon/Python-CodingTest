T=int(input())
for t in range(1,T+1):
    arr=list(map(int,input().split()))
    arr.sort()
    
    result = sum(arr[1:-1]) /8
    print(f"#{t} {round(result)}")