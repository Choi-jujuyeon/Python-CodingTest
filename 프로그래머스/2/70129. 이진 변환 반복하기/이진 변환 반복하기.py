def solution(s):
    d,count=0,0
    while s!='1':
        sc=s.count('1')
        d+=len(s)-sc
        s=bin(sc)[2:]
        count+=1
        
    return count,d