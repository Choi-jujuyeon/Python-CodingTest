import math
a=int(input())
for i in range(a):
    c,d=map(int,input().split())
    print(math.lcm(c,d))