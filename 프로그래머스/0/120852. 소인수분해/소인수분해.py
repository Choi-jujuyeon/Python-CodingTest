def solution(n):
    a=[]
    num=n
    for i in range(2,n+1):
        while num%i==0:
            a.append(i)
            num//=i
        if num == 1:
            break
    return sorted(list(set(a)))