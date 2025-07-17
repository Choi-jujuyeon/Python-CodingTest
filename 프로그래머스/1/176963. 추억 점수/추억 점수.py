def solution(name, yearning, photo):
    dic={}
    res=[]
    dic=dict(zip(name,yearning))
    for i in photo:
        count=0
        for j in i:
            if j in dic:
                count+=dic[j]
        res.append(count)
    return res