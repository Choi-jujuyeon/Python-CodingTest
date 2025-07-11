import math
def solution(n):
    root= math.isqrt(n)
    if root*root == n:
        return (root+1)**2
    else:
        return -1