def solution(babbling):
    s=[ "aya", "ye", "woo", "ma"]
    count=0
    
    for i in babbling:
        for j in s:
            if j*2 in i:
                break
            i = i.replace(j," ")
        if i.strip() =="":
            count+=1
    return count
        