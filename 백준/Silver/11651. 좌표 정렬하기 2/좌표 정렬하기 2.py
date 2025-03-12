import sys
a=int(sys.stdin.readline())
arr=sorted([list(map(int,sys.stdin.readline().split())) for i in range(a)],key=lambda x:(x[1],x[0]))
for i,j in arr:
        print(i,j)