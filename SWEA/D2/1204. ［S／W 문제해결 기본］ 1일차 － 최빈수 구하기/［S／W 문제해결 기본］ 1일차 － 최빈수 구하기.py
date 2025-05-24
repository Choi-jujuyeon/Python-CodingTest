from collections import Counter
T=int(input())
for i in range(T):
    k=int(input())
    arr=list(map(int,input().split()))

    count=Counter(arr)
    # print(count)
    arr2=[k for k,v in count.items() if v==max(count.values())]

    print(f'#{k} {sorted(arr2).pop()}')