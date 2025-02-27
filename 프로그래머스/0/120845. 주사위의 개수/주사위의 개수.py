def solution(box, n):
    a=1
    for i in box:
        a*=i//n
    return a
        