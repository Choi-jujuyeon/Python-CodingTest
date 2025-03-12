a=int(input())
arr=sorted([list(map(int,input().split())) for i in range(a)],key=lambda x:(x[0],x[1]))
for i,j in arr:
    print(i,j)