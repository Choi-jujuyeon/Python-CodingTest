def solution(numbers, n):
    s=0
    for i in range(len(numbers)):
        s+=numbers[i]
        if s>n:
            return s