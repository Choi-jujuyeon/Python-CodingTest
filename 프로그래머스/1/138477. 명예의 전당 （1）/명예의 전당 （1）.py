def solution(k, score):
    q=[]
    res=[]
    for i in score:
        q.append(i)
        if len(q)>k:
            q.remove(min(q))
        res.append(min(q))
    return res