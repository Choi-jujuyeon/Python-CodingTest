def solution(numLog):
    a=[]
    for i in range(len(numLog)-1):
        if numLog[i+1]==numLog[i]+1:
            a.append('w')
        elif numLog[i+1]==numLog[i]-1:
            a.append('s')
        elif numLog[i+1]==numLog[i]+10:
            a.append('d')
        else:
            a.append('a')
    return ''.join(a)