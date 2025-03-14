def solution(participant, completion):
    p=sorted(participant)
    c=sorted(completion)
    for i in range(len(c)):
        if c[i]!= p[i]:
            return p[i]
    return p[-1]