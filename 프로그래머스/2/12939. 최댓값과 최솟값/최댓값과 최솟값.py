def solution(s):
    arr=[int(i) for i in s.split()]
    return str(min(arr))+" "+str(max(arr))