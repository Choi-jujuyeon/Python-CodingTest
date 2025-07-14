def solution(price, money, count):
    r=money-sum([price*i for i in range(1,count+1)])
    if r<=0:
        return abs(r)
    else:
        return 0