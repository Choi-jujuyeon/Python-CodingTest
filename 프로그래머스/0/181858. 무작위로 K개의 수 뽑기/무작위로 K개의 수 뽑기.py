def solution(arr, k):
    #a=list(set(arr))
    #return a[:k] if len(a)>=k else a+[-1]*(k-len(a))
    a=[arr[0]]
    for i in arr:
        if i not in a:
            a.append(i)
    return a[:k] if len(a)>=k else a+[-1]*(k-len(a))
    
