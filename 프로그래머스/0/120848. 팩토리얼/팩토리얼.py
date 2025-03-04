def solution(n):
    result =1
    i=1
    
    while result<=n:
        i+=1
        result*=i
    return i-1