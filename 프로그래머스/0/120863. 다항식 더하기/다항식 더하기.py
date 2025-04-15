def solution(polynomial):
    a = []  # x항
    b = []  # 상수항

    for i in polynomial.split(' + '):  # ' + '로 정확히 나누기
        if 'x' in i:
            coeff = i.replace('x', '')
            a.append(int(coeff) if coeff else 1)
        else:
            b.append(int(i))

    x_sum = sum(a)
    const_sum = sum(b)

    result = []
    if x_sum > 0:
        result.append(f"{x_sum}x" if x_sum != 1 else "x")
    if const_sum > 0:
        result.append(str(const_sum))

    return ' + '.join(result)
