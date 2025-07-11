def solution(x):
    re=sum([int(i) for i in str(x)])
    if x%re ==0:
        return True
    else:
        return False