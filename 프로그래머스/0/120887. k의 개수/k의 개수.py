def solution(i, j, k):
    n="".join([str(a) for a in range(i,j+1)])
    return n.count(str(k))