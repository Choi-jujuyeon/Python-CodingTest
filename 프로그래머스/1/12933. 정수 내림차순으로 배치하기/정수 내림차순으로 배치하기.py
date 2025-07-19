def solution(n):
    a="".join((sorted([i for i in str(n)], reverse=True)))
    return int(a)