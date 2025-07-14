def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    r=0
    for i in range(len(A)):
        r+=A[i]*B[i]
    return r