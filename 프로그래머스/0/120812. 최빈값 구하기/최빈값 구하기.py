from collections import Counter
def solution(array):
    mm=Counter(array).most_common(2)
    return -1 if len(mm) > 1 and mm[0][1] == mm[1][1] else mm[0][0]
