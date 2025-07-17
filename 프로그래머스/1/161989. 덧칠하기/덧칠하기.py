def solution(n, m, section):
    start = section[0]
    count=1
    for i in range(len(section)):
        if section[i] in range(start,start+m):
            continue
        else:
            count+=1
            start = section[i]
    return count