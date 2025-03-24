def solution(lines):
    arr=[0]*200
    for i,j in lines:
        for i in range(100+i,100+j):
            arr[i]+=1
    sum=0
    for i in set(arr):
        print(i)
        if i>1:
            sum+=arr.count(i)
    return (sum)