import math
def solution(n, m):
    return [math.gcd(n,m), abs(n*m)//math.gcd(n,m)]
    
        