def solution(answers):
    arr=[[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    res=[]
    for num in arr:
        count=0
        for i in range(0,len(answers)):
            if num[i%len(num)] == answers[i]:       #길이 무한히 체크
                count+=1
        res.append(count)
    m=max(res)
    rr=[]
    for i in range(len(res)):
        if res[i]== m:
            rr.append(i+1)
    return rr
        
    
            