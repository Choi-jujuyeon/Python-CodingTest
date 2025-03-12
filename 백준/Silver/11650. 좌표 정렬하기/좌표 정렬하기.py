import sys
a=int(sys.stdin.readline())
arr=sorted([list(map(int,sys.stdin.readline().split())) for i in range(a)],key=lambda x:(x[0],x[1]))
for i,j in arr:
    print(i,j)