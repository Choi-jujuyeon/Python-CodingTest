def solution(arr, flag):
    a=[]
    for i in range(len(flag)):
        if flag[i]:
            for _ in range(arr[i]*2):
                a.append(arr[i])
        else:
            a=a[:-arr[i]]
    return a