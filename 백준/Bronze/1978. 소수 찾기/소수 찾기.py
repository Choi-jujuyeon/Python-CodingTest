a=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    val=True
    if i<2:
        val=False
    for j in range(2,i):
        if i%j==0:
            val=False
            break
    if val:
        count+=1
print(count)