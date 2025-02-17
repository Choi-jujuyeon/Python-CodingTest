def solution(arr):
    arr2=[]
    for i in arr:
        if i>=50 and i%2==0:
            arr2.append(i/2)
        elif i<50 and i%2!=0:
            arr2.append(i*2)
        else:
            arr2.append(i)
    return arr2