import sys,math
from functools import reduce

n=int(sys.stdin.readline())
prev=int(sys.stdin.readline())
arr=[]
for i in range(n-1):
    c=int(sys.stdin.readline())
    arr.append(abs(prev-c))
    prev=c
val = reduce(math.gcd, arr)
print(sum([i//val-1 for i in arr]))