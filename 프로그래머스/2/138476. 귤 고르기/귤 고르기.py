from collections import Counter
def solution(k, tangerine):
    arr=sorted(Counter(tangerine).values(), reverse=True)
    count=0
    for i in arr:
        k -= i
        count += 1
        if k <= 0:
            break
    return count
    
        