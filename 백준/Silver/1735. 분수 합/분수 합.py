import math,sys
a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())

lcm_val=math.lcm(b,d)
boonja=a*lcm_val//b + c*lcm_val//d
boonmo=lcm_val
gcd_val=math.gcd(boonja,boonmo)
print(boonja//gcd_val, boonmo//gcd_val)