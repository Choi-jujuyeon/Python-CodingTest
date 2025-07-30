def solution(dots):
    def is_parallel(a, b, c, d):
        # 두 벡터의 기울기 비교: (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)
        return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0])

    # 가능한 세 가지 조합만 확인
    if is_parallel(dots[0], dots[1], dots[2], dots[3]):
        return 1
    if is_parallel(dots[0], dots[2], dots[1], dots[3]):
        return 1
    if is_parallel(dots[0], dots[3], dots[1], dots[2]):
        return 1

    return 0