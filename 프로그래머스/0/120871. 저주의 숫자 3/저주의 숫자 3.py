def solution(n):
    size=[]
    i=1
    while len(size)<n:
        if i%3==0 or '3' in str(i):
            i+=1
            continue
        size.append(i)
        i+=1
            
    return size[-1]
        
        