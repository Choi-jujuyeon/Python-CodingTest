def solution(dots):
    a=list(set(a for a,b in dots))
    b=list(set(b for a,b in dots))
    return (max(a)-min(a))*(max(b)-min(b))
        