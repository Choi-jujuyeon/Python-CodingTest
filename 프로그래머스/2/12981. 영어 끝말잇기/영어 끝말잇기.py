def solution(n, words):
    p={}    #사람관리
    
    for idx,num in enumerate(words):
        person= idx%n
        
        if person not in p:
            p[person] = 1
        else:
            p[person]+=1
            
        if idx>0:
            if num in words[:idx] or num[0] != words[idx-1][-1]:
                return person+1, p[person]
    return [0,0]
        
    