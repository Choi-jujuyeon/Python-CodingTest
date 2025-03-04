def solution(emergency):
    a=sorted(emergency,reverse=True)
    return [a.index(i)+1 for i in emergency]