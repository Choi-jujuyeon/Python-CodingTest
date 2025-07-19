def solution(absolutes, signs):
    result=0
    for n,s in zip(absolutes,signs):
        if s:
            result+=n
        else:
            result-=n
    return result