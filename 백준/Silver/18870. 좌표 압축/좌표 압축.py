import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
sort_index={v:i for i,v in enumerate((sorted(set(arr))))}
for i in arr:
    print(sort_index[i], end=" ")