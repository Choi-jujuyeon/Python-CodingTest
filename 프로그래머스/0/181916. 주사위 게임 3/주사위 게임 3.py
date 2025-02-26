from collections import Counter
def solution(a, b, c, d):
    items=sorted(Counter([a, b, c, d]).items(),key=lambda x:x[1] )
    if len(items)==1:
        return items[0][0]*1111
    elif len(items)==2:
        if 3 ==items[1][1]:
            return (10*items[1][0]+items[0][0])**2
        else:
            return (items[0][0]+items[1][0])*abs(items[0][0]-items[1][0])
    elif len(items)==3:
        return items[0][0]*items[1][0]
    else:
        return min(items[0][0],items[1][0],items[2][0],items[3][0])