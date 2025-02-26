def solution(arr, queries):
    a=[]
    for s,e,k in queries:
        b=[]
        for i in range(s,e+1):
            if arr[i] > k:  
                b.append(arr[i])
        a.append(min(b) if b else -1)
                
    return a