def solution(arr):
    a=[]
    for i in arr:
        if a and a[-1] ==i:
            a.pop()
        else:
            a.append(i)
    return a if a else [-1]
    
        
        

    
    