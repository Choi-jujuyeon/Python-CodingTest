def solution(arr):
    arr2=[]
    for i in arr:
        if arr2==[] or arr2[-1]!=i:
            arr2.append(i)
            
    return arr2