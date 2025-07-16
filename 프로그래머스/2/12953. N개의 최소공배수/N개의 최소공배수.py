import math
def solution(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm= lcm*i//math.gcd(lcm,i)
    return lcm