def solution(dot):
    a=list(({1,4} if dot[0]>0 else {2,3}) & ({1,2} if dot[1]>0 else {3,4}))
    return a.pop()