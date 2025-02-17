def solution(n):
    a=[]
    while n!=1:
        a.append(n)
        if n%2==0:
            n/=2         
        else:
            n=3*n+1
    a.append(1)
    return a
        