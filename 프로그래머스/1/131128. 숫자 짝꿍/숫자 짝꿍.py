from collections import Counter
def solution(X, Y):
    
    X = {num: count for num, count in Counter(X).items()}
    Y = {num: count for num, count in Counter(Y).items()}
    res=[]
    for k in X:
        if k in Y:
            res.append(k* min(X[k],Y[k]))
    if not res:
        return "-1"
    result="".join(sorted(res,reverse=True))
    if result[0]=="0": return "0"
    return result
    