def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 * num2

    gcd_value = gcd(boonmo, boonja)

    answer = [boonja // gcd_value, boonmo // gcd_value]
    return answer
