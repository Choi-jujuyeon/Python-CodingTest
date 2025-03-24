import math
from functools import reduce
def solution(arrayA, arrayB):
    a=reduce(math.gcd,arrayA)
    b=reduce(math.gcd,arrayB)
    
    ra=[a if a!=1 and all(x%a!=0 for x in arrayB) else 0]  
    rb=[b if b!=1 and all(x%b!=0 for x in arrayA) else 0]
    return max(ra,rb).pop()