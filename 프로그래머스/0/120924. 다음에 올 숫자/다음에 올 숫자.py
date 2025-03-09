def solution(common):
    prev=common[0]
    a=[]
    for i in range(1,len(common)):
        a.append(common[i]-prev)
        prev=common[i]
    if len(set(a))==1: #등차수열임
        return common[-1]+sum(set(a))
    else: #등비수열임
        return common[1]//common[0]*common[-1]
                 