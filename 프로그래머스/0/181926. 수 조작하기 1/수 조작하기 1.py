def solution(n, control):
    a= dict(zip(['w','s','d','a'],[1,-1,10,-10]))
    for i in control:
        n+=a[i]
    return n