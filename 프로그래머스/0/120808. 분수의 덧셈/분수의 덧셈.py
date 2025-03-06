import math
def solution(numer1, denom1, numer2, denom2):
    dd=denom1*denom2
    uu=numer1*denom2 + numer2*denom1
    return [uu//math.gcd(dd,uu), dd//math.gcd(dd,uu)]
    