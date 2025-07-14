def solution(n):
    count=0
    r=""
    while count!= n:
        count+=1
        if count%2!=0:
            r+="수"
        else:
            r+="박"
    return r
            
        