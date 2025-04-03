import math
a=int(input())
for i in range(a):
    c,d=map(int,input().split())
    gcd_val=math.gcd(c,d)
    if c==1 or d==1:
        print(c*d)
    else:
        print(c//gcd_val * d//gcd_val*gcd_val)