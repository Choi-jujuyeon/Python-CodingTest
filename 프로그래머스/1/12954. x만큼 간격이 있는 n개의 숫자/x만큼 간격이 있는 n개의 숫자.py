def solution(x, n):
    # return list(range(x,x*n+1,x))
    return [x*i for i in range(1,n+1)]