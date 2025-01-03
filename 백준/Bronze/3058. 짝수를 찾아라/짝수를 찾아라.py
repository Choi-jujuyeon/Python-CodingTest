T=int(input())
for _ in range(T):
    arr=list(map(int,input().split()))
    arr2=[num for num in arr if num%2==0]
    print(sum(arr2), min(arr2))