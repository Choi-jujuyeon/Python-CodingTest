def solution(a, b, n):
    binglass,result=0,0
    while n>=a:
        binglass=(n//a)*b
        result+=binglass
        n=binglass+n%a
    return result
    