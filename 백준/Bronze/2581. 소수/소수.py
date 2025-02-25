a=int(input())
b=int(input())
arr=[]
for i in range(a,b+1):
    val=True
    if i==1: val=False
    for j in range(2,i):
        if i%j==0:
            val=False
            break
    if val:
        arr.append(i)
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)