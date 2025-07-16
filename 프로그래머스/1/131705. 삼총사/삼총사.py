from itertools import combinations
def solution(number):
    count=0
    for i in combinations(number,3):
        if sum(i)==0:
            count+=1
    return count
        