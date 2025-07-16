def solution(n):
    result=""
    while n>0:
        result = str(n%3) + result
        n//=3
    return int(result[::-1],3)