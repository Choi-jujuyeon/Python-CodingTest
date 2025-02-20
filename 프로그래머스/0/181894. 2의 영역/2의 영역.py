def solution(arr):
    a=[i for i in range(len(arr)) if 2==arr[i]]
    return arr[a[0]:a[-1]+1] if a else [-1]