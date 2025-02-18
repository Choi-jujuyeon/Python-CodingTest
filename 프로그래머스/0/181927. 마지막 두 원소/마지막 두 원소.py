def solution(l):
    if l[-1] > l[-2]:
        l.append(l[-1] - l[-2])
    else:
        l.append(l[-1] * 2)
    return l
