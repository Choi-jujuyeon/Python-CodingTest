from collections import Counter
def solution(array, n):
    for k,v in Counter(array).items():
        if k==n:
            return v
        
    return 0
    
        