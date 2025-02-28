def solution(n):
    count=0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                count+=1
                break
    return count
            
        