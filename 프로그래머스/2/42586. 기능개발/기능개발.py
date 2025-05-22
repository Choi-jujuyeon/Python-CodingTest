def solution(progresses, speeds):
    Q=[]
    for p,s in zip(progresses,speeds):
        now=-((p-100)//s)
        if len(Q)==0 or Q[-1][0]<now :
            Q.append([now,1])
        else:
            Q[-1][1]+=1
    return [i[1] for i in Q]
    