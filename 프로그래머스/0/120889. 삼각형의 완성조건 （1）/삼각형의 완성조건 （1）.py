def solution(sides):
    s=sorted(sides)
    return 1 if s[2]<s[0]+s[1] else 2