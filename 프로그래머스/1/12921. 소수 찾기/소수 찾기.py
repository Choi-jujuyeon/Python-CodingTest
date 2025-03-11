def solution(n):
    arr=set(range(2,n+1))
    
    for i in range(2,int(n**0.5)+1):
        arr-=set(range(i*2,n+1,i))
    
    return len(arr)