from itertools import combinations
def solution(nums):
    count=0
    for i in combinations(nums,3):
        for j in range(2, int(sum(i)**0.5)+1):
            if sum(i)%j==0:
                break
        else:
            count+=1          
    return count
    