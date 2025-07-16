def solution(n):
    one,two=1,1
    for _ in range(n-1):
        temp=two
        two=one
        one=one+temp
    return one%1234567