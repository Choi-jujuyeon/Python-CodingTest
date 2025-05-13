from collections import Counter
arr=list(map(int,input().split()))
for k,v in sorted(Counter(arr).items(),reverse=True):
    if v==3:
        print(10000+k*1000)
        break
    elif v==2:
        print(1000+k*100)
        break
else:
    print(max(arr)*100)