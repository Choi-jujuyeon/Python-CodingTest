def solution(i, j, k):
    return sum([str(a).count(str(k)) for a in range(i,j+1)])