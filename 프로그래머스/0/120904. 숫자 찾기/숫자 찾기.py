def solution(num, k):
    a=[int(i) for i in str(num) ]
    return a.index(k)+1 if k in a else -1
    