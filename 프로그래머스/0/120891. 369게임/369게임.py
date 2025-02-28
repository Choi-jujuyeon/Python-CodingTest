def solution(order):
    count=0
    for i in str(order):
        if int(i) in [3,6,9]:
            count+=1
    return count