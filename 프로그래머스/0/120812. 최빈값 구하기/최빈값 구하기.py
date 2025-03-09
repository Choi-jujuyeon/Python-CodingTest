from collections import Counter
def solution(array):
    #return Counter(array)
    v=sorted([v for k,v in Counter(array).items()], reverse=True)
    return -1 if len(v) >= 2 and v[0] in v[1:] else max(Counter(array),key=Counter(array).get)
    

    