def solution(array, commands):
    a=[]
    for i,j,k in commands:
        a.append(sorted(array[i-1:j])[k-1])
    return a