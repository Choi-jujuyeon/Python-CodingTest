def solution(l, r):
    arr=[]
    for i in range(l,r+1):
        if set(str(i))<= {'0','5'}:
            arr.append(i)
    return arr if arr else [-1]