def solution(n):
    one,two=1,1
    count=2
    while count!=n:    
        tmp=two
        two=one
        one=one + tmp
        count+=1
    return one%1234567
    