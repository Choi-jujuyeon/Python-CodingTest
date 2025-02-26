def solution(arr):
    row=len(arr) #원소의 개수==행의 수
    col=len(arr[0]) #열의 개수
    diff=abs(row-col)

    if row>col:
        for i in range(row):
            for _ in range(diff):
                arr[i].append(0)
    elif row<col:
        for i in range(diff):
            arr.append([0]*col)
            
    return arr