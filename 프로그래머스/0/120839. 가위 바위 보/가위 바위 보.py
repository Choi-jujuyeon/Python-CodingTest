def solution(rsp):
    a=["2","0","5"]
    return "".join([a[a.index(i)-2] for i in rsp])