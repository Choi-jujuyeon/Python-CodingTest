def solution(denum1, num1, denum2, num2):
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 * num2

    start = max(boonja, boonmo)
    gcd_value = 1

    for i in range(start, 0, -1):
        if boonmo % i == 0 and boonja % i == 0:
            gcd_value = i
            break

    answer = [boonja // gcd_value, boonmo // gcd_value]
    return answer
