def solution(numbers):
    res=0
    for i in range(1,10):
        if i not in numbers:
            res+=i
    return res