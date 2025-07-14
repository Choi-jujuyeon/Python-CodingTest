def solution(price, money, count):
    r=sum([price*i for i in range(1,count+1)])
    return max(0,r-money)