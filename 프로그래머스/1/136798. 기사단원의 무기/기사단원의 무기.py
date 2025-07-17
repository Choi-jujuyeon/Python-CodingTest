def solution(number, limit, power):
    res = []
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1  # 짝인 약수 추가
        if count > limit:
            res.append(power)
        else:
            res.append(count)
    return sum(res)
