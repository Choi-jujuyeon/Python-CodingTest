def solution(k, m, score):

    score.sort(reverse=True)
    res=[]
    for i in range(m-1,len(score),m):
        res.append(score[i]*m)
    return sum(res)
        
    