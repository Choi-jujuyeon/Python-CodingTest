import sys
n=int(sys.stdin.readline())
arr=[[i]+sys.stdin.readline().split() for i,v in enumerate(range(n))]
sort_array=sorted(arr,key=lambda x:(int(x[1]),x[0]))
for _,age,name in sort_array:
    print(age,name)