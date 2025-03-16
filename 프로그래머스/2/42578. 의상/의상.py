from collections import Counter
from functools import reduce
def solution(clothes):
        
    counter=Counter([type for cloth,type in clothes])
    
    result=reduce(lambda k,v:k*(v+1),counter.values(),1)
    return result-1
    
        