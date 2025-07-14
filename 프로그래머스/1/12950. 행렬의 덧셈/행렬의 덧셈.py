def solution(arr1, arr2):
    return [[c+d for c,d in zip(a1,b1)] for a1,b1 in zip(arr1,arr2)]
