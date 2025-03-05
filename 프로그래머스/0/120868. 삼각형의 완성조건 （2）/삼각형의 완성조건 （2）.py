def solution(sides):
    count=0
    for i in range(1,sum(sides)):
        if max(sides)-min(sides)<i<=max(sides):
            count+=1
        elif max(sides)<i<sum(sides):
            count+=1
    return count