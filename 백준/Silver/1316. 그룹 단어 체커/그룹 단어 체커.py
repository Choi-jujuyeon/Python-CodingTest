from collections import Counter

a=int(input())
arr=[input() for _ in range(a)]
count=0
for i in arr:
    valid=True
    for k,v in Counter(i).items():
        if k*v not in i:
            valid=False
            break
    if valid:
        count+=1
print(count)