def solution(s):
    hm={}
    res=[]
    
    for idx,num in enumerate(s):
        if num in hm:
            res.append(idx-hm[num])
        else:
            res.append(-1)
        hm[num] = idx
    return res
            