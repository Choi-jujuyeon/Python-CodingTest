def solution(A, B):
    count=-1
    for i in range(1,len(A)+1):
        if A==B:
            count=0
            break
        elif A[-i:]+A[:-i]==B:
            count=i
            break
    return count
    
            
        
        