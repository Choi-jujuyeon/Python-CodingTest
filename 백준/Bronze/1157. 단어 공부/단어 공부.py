from collections import Counter

counter=Counter(input().upper())
arr=[ch for ch,count in counter.items() if count==max(counter.values())]
if len(arr)>1:
    print('?')
else:
    print(*arr)