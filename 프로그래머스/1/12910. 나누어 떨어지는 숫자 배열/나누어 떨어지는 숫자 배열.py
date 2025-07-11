def solution(arr, divisor):
    re=[]
    for i in arr:
        if i % divisor==0:
            re.append(i)
    return sorted(re) if re else [-1]