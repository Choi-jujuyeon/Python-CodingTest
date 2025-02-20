from collections import Counter
def solution(strArr):
    return max((Counter(len(i) for i in strArr)).values())
