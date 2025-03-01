import math
def solution(n):
    if n%6==0:
        return n//6
    else:
        a=math.gcd(n, 6)
        return a*(n//a)*6//a//6
            
            
        