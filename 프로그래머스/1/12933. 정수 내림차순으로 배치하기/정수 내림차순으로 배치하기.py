def solution(n):
    result=sorted(str(n), reverse=True)
    return int("".join(result))