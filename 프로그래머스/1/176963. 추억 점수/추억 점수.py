def solution(name, yearning, photo):
    dic={}
    res=[]
    for n,y in zip(name,yearning):
        dic[n] = y
    for i in photo:
        count=0
        for j in i:
            if j in dic:
                count+=dic[j]
        res.append(count)
    return res