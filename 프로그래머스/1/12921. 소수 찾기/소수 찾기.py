def solution(n):
    arr=set([i for i in range(1,n+1)])
    
    for i in range(2,int(max(arr)**0.5)+1):
        arr-=set(range(i*2,max(arr)+1,i))
    arr-=set(range(0,2))
    
    return len(arr)