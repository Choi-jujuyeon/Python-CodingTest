from collections import Counter
def solution(s):
    a=[k for k,v in Counter(s).items() if v==1 ]
    return "".join(sorted(a)) if a else ""