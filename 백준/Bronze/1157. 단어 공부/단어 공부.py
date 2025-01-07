arr={}
for i in input().upper():
    if i in arr:
        arr[i]+=1
    else:
        arr[i]=1

if list(arr.values()).count(max(arr.values())) >=2:
    print('?')
else:
    for k,v in arr.items():
        if v==max(arr.values()):
            print(k)
