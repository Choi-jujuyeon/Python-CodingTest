def solution(num, total):
    a=sorted([x for i in range(1,num//2+1) for x in [total//num+i, total//num-i]]+[total//num])
    return a if num%2!=0 else a[1:]